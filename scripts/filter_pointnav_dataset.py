#!/usr/bin/env python3
"""
Filter a Habitat PointNav-v1 dataset (.json.gz) by geodesic distance and/or scene.

This is useful for making longer PointNav episodes so videos are longer and
policy behavior is easier to see.
"""

import argparse
import gzip
import json
import os
from typing import Any, Dict, List, Optional


def _load_json_gz(path: str) -> Dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def _dump_json_gz(obj: Dict[str, Any], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        json.dump(obj, f)


def _maybe_get_geodesic_distance(ep: Dict[str, Any]) -> Optional[float]:
    info = ep.get("info", {})
    if not isinstance(info, dict):
        return None
    gd = info.get("geodesic_distance", None)
    if gd is None:
        return None
    try:
        return float(gd)
    except (TypeError, ValueError):
        return None


def _scene_matches(scene_id: str, contains: Optional[str]) -> bool:
    if contains is None:
        return True
    return contains in scene_id


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Filter a PointNav dataset (.json.gz) by geodesic distance."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input dataset, e.g. data/datasets/pointnav/.../val.json.gz",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output dataset, e.g. data/datasets/pointnav/.../val_long.json.gz",
    )
    parser.add_argument(
        "--min-geodesic-distance",
        type=float,
        default=0.0,
        help="Keep episodes with geodesic_distance >= this value.",
    )
    parser.add_argument(
        "--max-geodesic-distance",
        type=float,
        default=None,
        help="Optional. Keep episodes with geodesic_distance <= this value.",
    )
    parser.add_argument(
        "--scene-contains",
        default=None,
        help="Optional. Keep episodes whose scene_id contains this substring.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional. Keep at most N episodes (after filtering).",
    )
    args = parser.parse_args()

    data = _load_json_gz(args.input)
    episodes: List[Dict[str, Any]] = list(data.get("episodes", []))

    kept: List[Dict[str, Any]] = []
    kept_dists: List[float] = []
    for ep in episodes:
        scene_id = str(ep.get("scene_id", ""))
        if not _scene_matches(scene_id, args.scene_contains):
            continue

        gd = _maybe_get_geodesic_distance(ep)
        if gd is None:
            continue
        if gd < args.min_geodesic_distance:
            continue
        if args.max_geodesic_distance is not None and gd > args.max_geodesic_distance:
            continue

        kept.append(ep)
        kept_dists.append(gd)
        if args.limit is not None and len(kept) >= args.limit:
            break

    out = dict(data)
    out["episodes"] = kept
    _dump_json_gz(out, args.output)

    if kept_dists:
        kept_dists.sort()
        print(
            "Filtered episodes: %d -> %d | geodesic_distance min=%.3f max=%.3f"
            % (len(episodes), len(kept), kept_dists[0], kept_dists[-1])
        )
    else:
        print("Filtered episodes: %d -> %d" % (len(episodes), len(kept)))


if __name__ == "__main__":
    main()

