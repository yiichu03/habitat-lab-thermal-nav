#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Optional

import imageio.v2 as imageio
import numpy as np

import habitat
from habitat.config import read_write
from habitat.config.default_structured_configs import (
    ThirdRGBSensorConfig,
    TopDownMapMeasurementConfig,
)
from habitat.sims.habitat_simulator.actions import HabitatSimActions
from habitat.tasks.nav.shortest_path_follower import ShortestPathFollower
from habitat.utils.visualizations import maps


class SimpleRLEnv(habitat.RLEnv):
    def get_reward_range(self):
        return [-1, 1]

    def get_reward(self, observations):
        return 0

    def get_done(self, observations):
        return self.habitat_env.episode_over

    def get_info(self, observations):
        return self.habitat_env.get_metrics()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Record side-by-side stereo RGB rollouts from PointNav episodes "
            "using shortest-path follower."
        )
    )
    parser.add_argument(
        "--config-path",
        type=str,
        default="benchmark/nav/pointnav/pointnav_habitat_test.yaml",
    )
    parser.add_argument(
        "--overrides",
        nargs="*",
        default=[],
        help="Optional Habitat config overrides.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="runs/stereo_debug_rollouts",
    )
    parser.add_argument("--num-episodes", type=int, default=5)
    parser.add_argument("--max-steps", type=int, default=200)
    parser.add_argument("--width", type=int, default=640)
    parser.add_argument("--height", type=int, default=512)
    parser.add_argument("--fx", type=float, default=302.53882)
    parser.add_argument("--baseline-meters", type=float, default=0.12165)
    parser.add_argument(
        "--right-x-sign",
        type=int,
        choices=[-1, 1],
        default=1,
        help=(
            "If 1, right camera is placed at +x and left at -x. "
            "If -1, right camera is placed at -x and left at +x."
        ),
    )
    parser.add_argument(
        "--left-obs-key",
        type=str,
        default="rgb",
        help="Preferred observation key for left RGB image.",
    )
    parser.add_argument(
        "--right-obs-key",
        type=str,
        default="right_rgb",
        help="Preferred observation key for right RGB image.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
    )
    return parser.parse_args()


def fx_to_hfov_deg(width: int, fx: float) -> float:
    return math.degrees(2.0 * math.atan(width / (2.0 * fx)))


def hfov_deg_to_fx(width: int, hfov_deg: float) -> float:
    return width / (2.0 * math.tan(math.radians(hfov_deg / 2.0)))


def _action_id_to_name(action_id: Optional[int]) -> str:
    if action_id is None:
        return "none"
    for action_name in HabitatSimActions:
        if HabitatSimActions[action_name] == action_id:
            return action_name
    return f"unknown_{action_id}"


def _find_rgb_key(
    obs: Dict[str, np.ndarray],
    preferred_key: str,
    excluded_keys: Optional[List[str]] = None,
) -> str:
    excluded = set(excluded_keys or [])
    if preferred_key in obs:
        return preferred_key

    fallback_candidates = ["rgb", "third_rgb", "right_rgb", "right_rgb_sensor"]
    for key in fallback_candidates:
        if key in obs and key not in excluded:
            return key

    for key, value in obs.items():
        if key in excluded:
            continue
        if (
            isinstance(value, np.ndarray)
            and value.ndim == 3
            and value.shape[2] in (3, 4)
        ):
            return key

    raise RuntimeError(
        f"Could not find RGB observation key. Available keys: {list(obs.keys())}"
    )


def _to_uint8_rgb(image: np.ndarray) -> np.ndarray:
    if image.ndim != 3:
        raise ValueError(f"Expected HxWxC image, got shape {image.shape}")
    if image.shape[2] == 4:
        image = image[:, :, :3]
    if image.shape[2] != 3:
        raise ValueError(f"Expected 3 or 4 channels, got shape {image.shape}")

    if image.dtype == np.uint8:
        return image

    image_float = image.astype(np.float32)
    if image_float.max() <= 1.0:
        image_float = image_float * 255.0
    image_float = np.clip(image_float, 0.0, 255.0)
    return image_float.astype(np.uint8)


def _episode_dir_name(episode_idx: int, scene_id: str, episode_id: str) -> str:
    scene_stem = Path(scene_id).stem if scene_id else "unknown_scene"
    return f"ep_{episode_idx:03d}_{scene_stem}_{episode_id}"


def _quat_to_wxyz(rotation) -> List[float]:
    if hasattr(rotation, "w"):
        return [
            float(rotation.w),
            float(rotation.x),
            float(rotation.y),
            float(rotation.z),
        ]
    if hasattr(rotation, "real") and hasattr(rotation, "imag"):
        imag = rotation.imag
        return [
            float(rotation.real),
            float(imag[0]),
            float(imag[1]),
            float(imag[2]),
        ]
    return [float("nan"), float("nan"), float("nan"), float("nan")]


def _build_stereo_side_by_side(
    left_rgb: np.ndarray,
    right_rgb: np.ndarray,
) -> np.ndarray:
    left = _to_uint8_rgb(left_rgb)
    right = _to_uint8_rgb(right_rgb)
    if left.shape[0] != right.shape[0]:
        raise ValueError(
            f"Left/Right heights differ: {left.shape[0]} vs {right.shape[0]}"
        )
    return np.concatenate([left, right], axis=1)


def _draw_top_down_map(
    info: Dict[str, np.ndarray], output_size: int
) -> Optional[np.ndarray]:
    if "top_down_map" not in info:
        return None
    return maps.colorize_draw_agent_and_fit_to_height(
        info["top_down_map"], output_size
    )


def main() -> None:
    args = parse_args()

    if args.num_episodes <= 0:
        raise ValueError("--num-episodes must be > 0")
    if args.max_steps <= 0:
        raise ValueError("--max-steps must be > 0")
    if args.width <= 0 or args.height <= 0:
        raise ValueError("--width and --height must be > 0")
    if args.fx <= 0:
        raise ValueError("--fx must be > 0")
    if args.baseline_meters <= 0:
        raise ValueError("--baseline-meters must be > 0")

    output_root = Path(args.output_dir)
    output_root.mkdir(parents=True, exist_ok=True)

    hfov_float = fx_to_hfov_deg(args.width, args.fx)
    hfov_int = int(round(hfov_float))
    effective_fx = hfov_deg_to_fx(args.width, hfov_int)
    fx_rel_error_pct = abs(effective_fx - args.fx) / args.fx * 100.0
    print(
        f"Stereo setup: width={args.width}, height={args.height}, "
        f"target_fx={args.fx:.5f}, hfov_float={hfov_float:.5f} deg, "
        f"hfov_used={hfov_int} deg, effective_fx={effective_fx:.5f}, "
        f"fx_error={fx_rel_error_pct:.4f}%, baseline={args.baseline_meters:.5f} m"
    )

    config = habitat.get_config(
        config_path=args.config_path,
        overrides=args.overrides,
    )

    with read_write(config):
        config.habitat.seed = args.seed
        config.habitat.environment.iterator_options.shuffle = False
        if "top_down_map" not in config.habitat.task.measurements:
            config.habitat.task.measurements["top_down_map"] = (
                TopDownMapMeasurementConfig()
            )
        sim_sensors = config.habitat.simulator.agents.main_agent.sim_sensors

        left_sensor = sim_sensors.rgb_sensor
        left_sensor.width = args.width
        left_sensor.height = args.height
        left_sensor.hfov = hfov_int

        original_pos = list(left_sensor.position)
        original_ori = list(left_sensor.orientation)
        x_offset = args.right_x_sign * (args.baseline_meters / 2.0)
        left_pos = [
            original_pos[0] - x_offset,
            original_pos[1],
            original_pos[2],
        ]
        right_pos = [
            original_pos[0] + x_offset,
            original_pos[1],
            original_pos[2],
        ]
        left_sensor.position = left_pos
        left_sensor.orientation = original_ori

        right_sensor = ThirdRGBSensorConfig()
        right_sensor.width = args.width
        right_sensor.height = args.height
        right_sensor.hfov = hfov_int
        right_sensor.position = right_pos
        right_sensor.orientation = original_ori
        right_sensor.uuid = args.right_obs_key
        sim_sensors["right_rgb_sensor"] = right_sensor

    print("Creating environment...")
    with SimpleRLEnv(config=config) as env:
        print(f"Total available episodes: {len(env.episodes)}")
        if len(env.episodes) == 0:
            raise RuntimeError("No episodes found in dataset/config.")

        written_episodes = 0
        for episode_idx in range(args.num_episodes):
            obs = env.reset()
            episode = env.habitat_env.current_episode

            goal_radius = episode.goals[0].radius
            if goal_radius is None:
                goal_radius = config.habitat.simulator.forward_step_size
            follower = ShortestPathFollower(
                env.habitat_env.sim,
                goal_radius=goal_radius,
                return_one_hot=False,
            )

            episode_dir = output_root / _episode_dir_name(
                episode_idx=episode_idx,
                scene_id=episode.scene_id,
                episode_id=episode.episode_id,
            )
            episode_dir.mkdir(parents=True, exist_ok=True)
            metadata_path = episode_dir / "metadata.jsonl"

            left_key = _find_rgb_key(obs, args.left_obs_key)
            right_key = _find_rgb_key(
                obs, args.right_obs_key, excluded_keys=[left_key]
            )
            print(
                f"[Episode {episode_idx}] id={episode.episode_id}, scene={episode.scene_id}"
            )
            print(f"  using left key='{left_key}', right key='{right_key}'")

            with metadata_path.open("w", encoding="utf-8") as meta_f:
                step_idx = 0
                latest_topdown_map: Optional[np.ndarray] = None

                def write_frame(
                    observations: Dict[str, np.ndarray],
                    action_id: Optional[int],
                    done: bool,
                ) -> None:
                    nonlocal step_idx

                    side_by_side = _build_stereo_side_by_side(
                        observations[left_key],
                        observations[right_key],
                    )
                    image_path = episode_dir / f"frame_{step_idx:05d}.png"
                    imageio.imwrite(image_path, side_by_side)

                    agent_state = env.habitat_env.sim.get_agent_state()
                    record = {
                        "step": step_idx,
                        "frame_path": str(image_path),
                        "action_id": action_id,
                        "action_name": _action_id_to_name(action_id),
                        "done": done,
                        "episode_id": episode.episode_id,
                        "scene_id": episode.scene_id,
                        "goal_position": [float(v) for v in episode.goals[0].position],
                        "agent_position": [float(v) for v in agent_state.position],
                        "agent_rotation_wxyz": _quat_to_wxyz(agent_state.rotation),
                    }
                    meta_f.write(json.dumps(record) + "\n")

                latest_topdown_map = _draw_top_down_map(
                    env.habitat_env.get_metrics(), args.height
                )
                write_frame(obs, action_id=None, done=False)

                steps_taken = 0
                while (
                    not env.habitat_env.episode_over
                    and steps_taken < args.max_steps
                ):
                    next_action = follower.get_next_action(
                        episode.goals[0].position
                    )
                    if (
                        next_action is None
                        or next_action == HabitatSimActions.stop
                    ):
                        break

                    obs, _, done, info = env.step(next_action)
                    steps_taken += 1
                    step_idx += 1
                    current_topdown_map = _draw_top_down_map(info, args.height)
                    if current_topdown_map is not None:
                        latest_topdown_map = current_topdown_map
                    write_frame(obs, action_id=int(next_action), done=done)
                    if done:
                        break

            if latest_topdown_map is not None:
                topdown_path = episode_dir / "topdown_trajectory.png"
                imageio.imwrite(topdown_path, latest_topdown_map)

            print(
                f"  saved {step_idx + 1} side-by-side frame(s) to {episode_dir}"
            )
            written_episodes += 1

        print(
            f"Finished. Recorded {written_episodes} episode(s) under {output_root}"
        )


if __name__ == "__main__":
    main()
