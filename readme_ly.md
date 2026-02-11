# Habitat + DDPPO 学习手册（个人版）

## 目标
- 在 Habitat 里先跑通 `DDPPO baseline` 的训练与评估。
- 用可复现命令导出视频，确认策略行为。
- 之后重点阅读 DDPPO 训练/推理代码，理解 Habitat 仿真与导航任务流程，为后续导航项目做准备。

## 当前已跑通（到 2026-02-10）
- 小步数训练流程：`pointnav/ppo_pointnav_example.yaml` 可以正常跑。
- 评估并导出视频：可以产出 `mp4`。
- 官方预训练权重已下载：`data/ddppo-models/gibson-2plus-resnet50.pth`。
- 预训练评估成功（depth-only 观测），指标明显更好（`success/spl` 高）。
- 已支持更高级可视化（`top_down_map` + `third_rgb`）的专用配置文件：
  `habitat-baselines/habitat_baselines/config/pointnav/ddppo_pointnav_pretrained_tdm.yaml`。

## 你必须记住的关键点

### 0) 先统一数据根目录（最容易忘）
- 你的历史问题核心是：`data/` 里混用了两套来源。
- 一套是软链到 `/home/liuyi/datasets/habitat/*`，另一套是直接下到仓库内 `data/versioned_data/*`。
- 这会触发：`FileExistsError` / `IsADirectoryError` / `Requested ... not downloaded locally`。
- 推荐固定使用：`DATA_ROOT=/home/liuyi/datasets/habitat`。
- 每次开新终端先做：
```bash
cd ~/projects/habitat-lab
conda activate habitat
export TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1
export DATA_ROOT=/home/liuyi/datasets/habitat
```

### 1) 预训练权重和观测必须匹配
- `gibson-2plus-resnet50.pth` 是 depth 风格权重，不是 RGBD 通吃。
- 如果直接用默认 RGBD，会报参数 shape mismatch（例如 `conv1` 输入通道不一致）。
- 评估预训练权重时要用：
  - `habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]`

### 2) `data/` 目录是软链接混合结构
- 你的 `data/datasets`、`data/scene_datasets` 等有软链接到 `/home/liuyi/datasets/habitat/...`。
- 下载器报错（`FileExistsError` / `IsADirectoryError`）很多是因为目标路径已经存在且类型（目录/链接）不一致。
- 结论：后续统一用同一个 `DATA_ROOT`，不要反复混用 `/data`、仓库内 `data/versioned_data` 和其他绝对路径。

### 3) `interactive_play.py` 的 GLX 报错
- 报 `X_GLXMakeCurrent BadAccess` 属于图形上下文/显示环境问题，不是 DDPPO 主流程错误。
- 学习 DDPPO 先走 baselines 的 train/eval + 视频导出路线，不要被 interactive demo 卡住。

### 4) 评估视频默认不一定输出
- 需要显式开启：`habitat_baselines.eval.video_option=[disk]`
- 视频目录看：`habitat_baselines.video_dir=...`

### 5) Resume state 可能“污染”新评估
- 建议评估时加：
  - `habitat_baselines.load_resume_state_config=False`
  - 并用独立 `checkpoint_folder`（避免读到旧 `.habitat-resume-state*`）

## 最小可复现命令（建议直接用）

### 0.5) 首次/换环境时，先补齐数据（统一到 DATA_ROOT）
```bash
python -m habitat_sim.utils.datasets_download \
  --uids rearrange_task_assets \
  --data-path "$DATA_ROOT" \
  --replace
```
- 如果要把 PointNav 测试数据也统一到同一个根目录，再执行：
```bash
python -m habitat_sim.utils.datasets_download \
  --uids habitat_test_scenes habitat_test_pointnav_dataset \
  --data-path "$DATA_ROOT" \
  --replace
```

### A. 小步数训练（先熟悉流程）
```bash
python -u -m habitat_baselines.run \
  --config-name=pointnav/ppo_pointnav_example.yaml \
  habitat_baselines.checkpoint_folder=data/new_checkpoints_ddppo_demo \
  habitat_baselines.total_num_steps=2e5 \
  habitat_baselines.num_environments=1
```

### B. 用自己训练出的 ckpt 评估并导视频
```bash
python -u -m habitat_baselines.run \
  --config-name=pointnav/ppo_pointnav_example.yaml \
  habitat_baselines.trainer_name=ddppo \
  habitat_baselines.evaluate=True \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.eval_ckpt_path_dir=data/new_checkpoints_ddppo_demo/latest.pth \
  habitat_baselines.eval.video_option=[disk] \
  habitat_baselines.video_dir=videos/ddppo_demo_eval
```

### C. 用官方预训练权重评估（推荐基线）
```bash
python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.eval.video_option=[disk] \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  'habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]' \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.checkpoint_folder=data/new_checkpoints_pretrained_eval_tmp \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval
```

### D. 高级可视化（第三视角 + top-down map）
```bash
python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav_pretrained_tdm.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test
```
- 默认输出目录：`videos/ddppo_pretrained_eval_tdm/`

## 让视频更长（更容易观察策略）

### 方法 1：选更长起终点距离的 episode（推荐）
- 先生成过滤后的数据集（例如 geodesic distance >= 10m）：
```bash
python scripts/filter_pointnav_dataset.py \
  --input data/datasets/pointnav/habitat-test-scenes/v1/val/val.json.gz \
  --output data/custom_datasets/pointnav/habitat-test-scenes/v1/val_long10.json.gz \
  --min-geodesic-distance 10
```

- 再评估：
```bash
python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav_pretrained_tdm.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat.dataset.data_path=data/custom_datasets/pointnav/habitat-test-scenes/v1/val_long10.json.gz \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval_tdm_long10
```

### 方法 2：只让视频“播放变慢”
- 加：`habitat_baselines.video_fps=5`
- 注意：这只改变播放速度，不改变策略实际步数。

## 常见报错速查

### `Missing key(s) ... size mismatch conv1`
- 原因：预训练权重与观测通道不匹配（RGBD vs depth-only）。
- 处理：改 `obs_keys` 为 `[depth,pointgoal_with_gps_compass]`。

### `Could not override ... top_down_map`
- 原因：Hydra struct config 下 CLI 临时拼接复杂 dict/group 容易失败。
- 处理：使用独立 yaml（已提供 `ddppo_pointnav_pretrained_tdm.yaml`）。

### `TypeError: unsupported format string passed to numpy.ndarray.__format__`
- 原因：video overlay 里对 ndarray 指标强制 `:.2f`。
- 处理：已在本地代码修复（仅格式化 scalar/size=1 array）。

### `ValueError: All images in a movie should have same size`
- 原因：含 top-down-map 时帧尺寸在 episode 边界可能不一致。
- 处理：已在本地代码修复（视频写入前统一帧尺寸 + evaluator 边界帧逻辑调整）。

## 接下来建议的源码阅读顺序（DDPPO）

1. 入口与实验调度  
   - `habitat-baselines/habitat_baselines/run.py`
2. Trainer 主循环（train/eval）  
   - `habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`
3. DDP 辅助/断点状态  
   - `habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py`
4. 策略网络（PointNavResNetPolicy）  
   - `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet_policy.py`
5. 评估器与视频逻辑  
   - `habitat-baselines/habitat_baselines/rl/ppo/habitat_evaluator.py`
   - `habitat-lab/habitat/utils/visualizations/utils.py`
6. Habitat 任务与测量（success/spl/top_down_map）  
   - `habitat-lab/habitat/tasks/nav/nav.py`

---

如果后面要进入“改算法”阶段，先从 `ppo_trainer.py` 里把一次 rollout 的 `obs -> action -> env.step -> storage -> update` 路径完整画出来，再看 DDP 同步细节，会快很多。
