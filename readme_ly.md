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

## 跑通记录：预训练评估 + 导出视频

### 1) 下载官方预训练权重（DDPPO depth encoder）
```bash
cd ~/projects/habitat-lab
mkdir -p data/ddppo-models
wget -c \
  https://dl.fbaipublicfiles.com/habitat/data/baselines/v1/ddppo/ddppo-models/gibson-2plus-resnet50.pth \
  -O data/ddppo-models/gibson-2plus-resnet50.pth
```
- 这个文件是“视觉编码器的预训练权重”（DDPPO 论文/基线常用），不是一个完整 RL policy ckpt。
- 所以评估时用的是“未加载 RL ckpt（`eval.should_load_ckpt=False`）+ 用预训练 encoder 初始化策略网络”。

### 2) 下载/补齐数据与场景（统一到 DATA_ROOT）
```bash
cd ~/projects/habitat-lab
export DATA_ROOT=/home/liuyi/datasets/habitat

# Rearrange 相关：examples/example.py / interactive_play.py 会用到
python -m habitat_sim.utils.datasets_download \
  --uids rearrange_task_assets \
  --data-path "$DATA_ROOT" \
  --replace

# PointNav 测试：场景 + test pointnav episodes
python -m habitat_sim.utils.datasets_download \
  --uids habitat_test_scenes habitat_test_pointnav_dataset \
  --data-path "$DATA_ROOT" \
  --replace
```

### 3) 评估逻辑做了什么（从命令到代码）
- 入口命令：`python -u -m habitat_baselines.run ...`
- 主要调用链（建议你读代码时按这个顺序）：
  - `habitat-baselines/habitat_baselines/run.py`：Hydra 读取 config，分支到 train/eval
  - `habitat-baselines/habitat_baselines/common/base_trainer.py`：`eval()`，处理 resume-state（`.habitat-resume-state*`）
  - `habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`：`_eval_checkpoint()`，建 env、建 policy、跑 evaluator
  - `habitat-baselines/habitat_baselines/rl/ppo/habitat_evaluator.py`：循环跑 episode，收集 metrics 与视频帧
  - `habitat-lab/habitat/utils/visualizations/utils.py`：`observations_to_image()`/`images_to_video()` 写 mp4
- 我们这次“跑通预训练评估”的关键配置是：
  - `habitat_baselines.evaluate=True`
  - `habitat_baselines.eval.should_load_ckpt=False`（不加载 RL checkpoint）
  - `habitat_baselines.rl.ddppo.pretrained=True`
  - `habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth`
  - `habitat_baselines.eval.video_option=[disk]` + `habitat_baselines.video_dir=...`
  - `habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]`（使观测通道与预训练权重匹配）

### 4) 高级可视化我们开了什么
- `top_down_map`：来自 Habitat task measurement `TopDownMap`（会画轨迹、可选 shortest path、fog of war）
- `third_rgb`：作为 eval 的“额外渲染相机”，不参与 policy 输入（policy 会从 observation_space 里过滤掉这类相机）

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

## 概念澄清：数据集、场景与 PointGoal

### 1) “我们下载的数据集就是可交互环境场景”对吗？
- 大方向是对的，但更准确的拆法是：
  - **场景/资产（scene assets）**：`*.glb`、纹理、navmesh 等，决定“可交互的 3D 世界长什么样”。
  - **episode 数据集（episodes json.gz）**：每条 episode 给出 `scene_id + start_pose + goal(s)`，决定“在这个世界里从哪到哪做任务”。
- Habitat 的 `PointNav-v1` 评估/训练基本是“按 episodes 列表驱动”，不是每次在线随机采样起点/终点（除非你用生成器/自建 dataset）。

### 2) PointGoal 是怎么设定的？训练集随机、评估集固定吗？
- 对 `PointNav-v1` 来说，**goal 的绝对位置**在 episode 里是固定字段（例如 `goals[0].position`）。
- `pointgoal_with_gps_compass` 这个观测不是数据集直接存好的“监督标签”，而是任务传感器在仿真里根据：
  - agent 当前位姿（GPS/Compass）
  - goal 的绝对位置（来自 episode）
  即时计算出来的“相对目标向量/极坐标”。
- 训练集/评估集是否“随机”，取决于你用的 episodes：
  - 常见做法：train split episodes 很多，训练时会 shuffle/cycle；但每条 episode 本身仍是固定的起点与目标点。
  - eval split（val/test）通常就是固定一组 episodes，用来做可重复对比。

### 3) 把 DDPPO 改成双目 RGB，会不会影响数据集使用？能对比吗？
- **不会像监督学习那样要求数据集里“预先存好双目 RGB 图像”。**  
  在 Habitat 里，RGB/Depth 图像是仿真器根据场景实时渲染出来的 observation；episode 只需要提供“在哪个 scene + 起点 + 目标”。
- 所以你完全可以：
  - 用同一份 episodes（同样起点/目标/场景）
  - 换一套传感器配置（比如双目 RGB）
  - 训练一个新 policy
  - 在同一 eval episodes 上用同一套指标（SPL/success/distance_to_goal）对比
- 需要注意的“对比公平性”：
  - 传感器变了，输入信息量变了，所以不是“同一个模型的消融”，而是“不同观测模态的策略对比”，这在 RL 里是合理的对比方式。
- 不能直接加载当前 depth-only 预训练权重（输入通道会变）；要么随机初始化，要么找 ImageNet/自监督权重，要么自己做通道适配。

## 代码阅读路线（针对“要改 encoder/加辅助头/改传感器与动作”）

### 0) PPO vs DDPPO（别被名字误导）
- 你这次跑通的“算法核心”是 **PPO**：loss/advantage/clip/optimizer step 都在 `ppo.py`。
- **DDPPO 不是另一套算法**，而是 Habitat Baselines 里“PPO + 分布式/多进程采样与同步”的训练形态。
- 简单记法：
  - `habitat-baselines/habitat_baselines/rl/ppo/ppo.py`：PPO 更新公式（你必须看）
  - `habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`：rollout 收集 + returns + 调 `updater.update`
  - `habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py`：分布式初始化、rank0 保存/恢复、同步工具（多 GPU/多进程才重点）
  - `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet_policy.py`：DDPPO baseline 常用的 PointNav policy 网络（encoder/RNN/heads）

### 1) 从入口到梯度更新（训练主链路）
- 实验入口（Hydra + train/eval 分支）  
  `habitat-baselines/habitat_baselines/run.py`
- Trainer 主循环（rollout 收集、更新、存 ckpt）  
  `habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`
  - rollout：`_compute_actions_and_step_envs()` / `_collect_environment_result()`
  - 更新：`_update_agent()`（算 returns + 调 updater.update）
- Agent / policy / updater 的组装与加载权重逻辑  
  `habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py`
  - `SingleAgentAccessMgr._create_policy()`：policy.from_config + (可选)加载 `ddppo.pretrained*`
  - `SingleAgentAccessMgr._create_updater()`：构造 PPO/DDPPO updater
- PPO 算法实现（loss、entropy、value、梯度裁剪、优化器）  
  `habitat-baselines/habitat_baselines/rl/ppo/ppo.py`

### 2) Baseline 模型结构（你要改 encoder 的位置）
- PointNav policy（ResNet encoder + RNN + actor/critic heads）  
  `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet_policy.py`
  - `ResNetEncoder`：视觉编码器入口（改 backbone/输入通道/融合都在这里落地）
  - `PointNavResNetNet.forward()`：把 visual + goal 传感器特征拼接后送入 RNN

### 3) 辅助监督头/辅助 loss（你要“加辅助头”的正确挂载点）
- auxiliary loss 框架（NetPolicy 会收集 `aux_loss_state` 并调用 aux modules）  
  `habitat-baselines/habitat_baselines/rl/ppo/policy.py`
  - `get_aux_modules()`：从 config 里实例化 auxiliary losses
  - `aux_loss_state["perception_embed"]` / `aux_loss_state["rnn_output"]`：你最常用的挂点
- PPO update 会把 `aux_loss_res` 合并进总 loss 并对 aux 模块参数做梯度裁剪  
  `habitat-baselines/habitat_baselines/rl/ppo/ppo.py`
- 配置入口：  
  `habitat-baselines/habitat_baselines/config/default_structured_configs.py`（`habitat_baselines.rl.auxiliary_losses`）

### 4) 推理/评估与视频（理解“policy 如何和 env 交互”）
- evaluator 循环（env.step -> obs->action->metrics/video）  
  `habitat-baselines/habitat_baselines/rl/ppo/habitat_evaluator.py`
- 视频帧合成与写 mp4  
  `habitat-lab/habitat/utils/visualizations/utils.py`

### 5) Habitat 环境与交互边界（你要熟悉 habitat-lab 的重点）
- gym wrapper（Habitat env -> gym API）  
  `habitat-lab/habitat/core/environments.py`  
  `habitat-lab/habitat/gym/gym_wrapper.py`  
  `habitat-lab/habitat/gym/gym_definitions.py`
- 仿真器核心（reset/step/渲染 observation）  
  `habitat-lab/habitat/sims/habitat_simulator/habitat_simulator.py`
- PointNav 任务逻辑（StopAction、Success/SPL、TopDownMap）  
  `habitat-lab/habitat/tasks/nav/nav.py`

### 6) 传感器配置（你提到双目/更多传感器）
- sensor setup yaml（决定 agent 开哪些传感器）  
  `habitat-lab/habitat/config/habitat/simulator/sensor_setups/`
  - 例如：`rgbd_agent.yaml` / `depth_agent.yaml` / `spot_agent.yaml`（里面有 stereo depth 示例）
- simulator sensor schema（第三视角相机等也在这里注册）  
  `habitat-lab/habitat/config/default_structured_configs.py`
  - 例如：`ThirdRGBSensorConfig`、`HeadStereoLeftDepthSensorConfig`

### 7) 动作空间：离散 vs 连续（你提到“从离散改连续”）
- trainer 层面已经兼容连续动作（Box space 会走 clip）  
  `habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`（`is_continuous_action_space` 分支）
- action space 的判定与分发网络（categorical vs gaussian）  
  `habitat-baselines/habitat_baselines/utils/common.py`（`CategoricalNet` / `GaussianNet`）
- Habitat action config（Navigation/Rearrrange 的连续 action 配置不同）  
  `habitat-lab/habitat/config/default_structured_configs.py`（例如 `VelocityControlActionConfig` / `BaseVelocityActionConfig`）
