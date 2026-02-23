# Habitat + DDPPO 学习手册（个人版）
conda activate habitat
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
# 本机：把数据放进仓库的 data/（避免多处路径混用）
export DATA_ROOT=$(pwd)/data

# 远程服务器：通常放在共享盘（示例）
# export DATA_ROOT=/data/habitat

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
- 你的历史问题核心是：数据曾经分散在“仓库 `data/`”和“外部 `$DATA_ROOT`”两套路径里。
- 2026-02-23 已把 `/home/liuyi/datasets/habitat` 下现有数据复制进仓库 `data/`，并把 `data/datasets` 等外部软链替换为本地目录/仓库内相对软链。
- 本机推荐以仓库 `data/` 作为唯一数据根目录；如果要用下载器，`DATA_ROOT=$(pwd)/data` 即可。
- 每次开新终端先做：
```bash
cd ~/projects/habitat-lab
conda activate habitat
export TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1
export DATA_ROOT=$(pwd)/data
```

### 1) 预训练权重和观测必须匹配
- `gibson-2plus-resnet50.pth` 是 depth 风格权重，不是 RGBD 通吃。
- 如果直接用默认 RGBD，会报参数 shape mismatch（例如 `conv1` 输入通道不一致）。
- 评估预训练权重时要用：
  - `habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]`

### 2) `data/` 目录是软链接混合结构
- 目前仓库 `data/` 里只保留“指向仓库内 `data/versioned_data` 的相对软链接”，不再指向 `/home/liuyi/datasets/habitat`。
- 历史外部软链已备份在 `data/_external_links_backup/`（仅用于回滚，不参与正常运行）。

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

### D. 高级可视化（第三视角 + top-down map）#################################
```bash
TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1 python -u -m habitat_baselines.run --config-name=pointnav/ddppo_pointnav_pretrained_tdm.yaml benchmark/nav/pointnav=pointnav_habitat_test

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

### 0.1) `habitat_baselines/rl/ppo` vs `habitat_baselines/rl/ddppo`（目录职责怎么理解）
- **`rl/ppo/` 更像“通用 RL 框架层”**：rollout、PPO 更新、评估循环、视频导出都在这里，既服务 `trainer_name=ppo` 也服务 `trainer_name=ddppo`。
  - 关键文件：
    - `habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`：训练/评估主循环（注意 `@register_trainer(name="ddppo")` 也挂在这个类上）
    - `habitat-baselines/habitat_baselines/rl/ppo/ppo.py`：PPO loss 与优化器更新（算法核心）
    - `habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py`：组装 policy/updater，并负责加载 `ddppo.pretrained*` 权重
    - `habitat-baselines/habitat_baselines/rl/ppo/habitat_evaluator.py`：评估 loop（env.step -> action -> metrics/video）
- **`rl/ddppo/` 更像“PPO 的分布式实现 + DDPPO baseline 的模型库”**：把“分布式同步/工具 + 常用 policy 网络（ResNet）”单独放在这里。
  - 分布式部分（你用多 GPU/多进程时才是重点）：
    - `habitat-baselines/habitat_baselines/rl/ddppo/algo/ddppo.py`：`class DDPPO(..., PPO)`，在 PPO 基础上加分布式/去中心化同步逻辑
    - `habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py`：rank/world 初始化、广播、保存/恢复 resume state 等
  - 模型/网络部分（即使单机也常用）：
    - `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet.py`：ResNet backbone 定义（供 policy encoder 用）
    - `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet_policy.py`：PointNavResNetPolicy / encoder / RNN / heads（你改 encoder 通常从这里入手）
    - `habitat-baselines/habitat_baselines/rl/ddppo/policy/running_mean_and_var.py`：输入归一化统计（预训练权重/视觉输入常用）
- **为什么“DDPPO 文件夹里也有 resnet/resnet_policy”**：因为 Habitat Baselines 的历史实现里，“DDPPO baseline 最常用的 PointNav 网络结构”就是 ResNet+RNN，这套网络被复用到了 PPO 和 DDPPO 两种 trainer 上，所以网络文件不在 `rl/ppo/` 也很正常。
- **一个实用记法**：
  - 想懂 “PPO 更新怎么做”：先看 `habitat-baselines/habitat_baselines/rl/ppo/ppo.py`
  - 想懂 “rollout 怎么收集 + 何时 update + 怎么保存 ckpt”：看 `habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`
  - 想改 “视觉 encoder / 融合 / RNN 输入”：看 `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet_policy.py`
  - 想跑 “多 GPU/多机 DDPPO”：看 `habitat-baselines/habitat_baselines/rl/ddppo/algo/ddppo.py` + `habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py`

### 1) 从入口到梯度更新（训练主链路）
- 实验入口（Hydra + train/eval 分支）  
  `habitat-baselines/habitat_baselines/run.py`
  - `@hydra.main(config_path="config")`：`--config-name=pointnav/ddppo_pointnav.yaml` 会去 `habitat-baselines/habitat_baselines/config/pointnav/ddppo_pointnav.yaml` 找配置
  - `patch_config(cfg)`：主要做 Habitat config 的一致性修补（比如单智能体时补全 `habitat.simulator.agents_order`）
  - `execute_exp(cfg, ...)`：通过 `habitat_baselines.evaluate` 决定走 `trainer.train()` 还是 `trainer.eval()`
  - `baseline_registry.get_trainer(habitat_baselines.trainer_name)`：按字符串找 trainer 构造函数（例如 `trainer_name=ddppo` 也会构造 `PPOTrainer`，因为它被注册成了 `ddppo` trainer）
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

### 1.1) Baseline DDPPO 训练时 reward 是怎么来的？
- **reward 不是在 baselines 里“手写”出来的**，而是 Habitat-Lab 的 `RLEnv` 负责定义 reward；baselines 只是拿到 `env.step()` 返回的 reward 存进 rollout buffer。
- 对 PointNav/Navigation 来说，关键配置都在 `habitat-lab/habitat/config/habitat/task/pointnav.yaml`：
  - `reward_measure: "distance_to_goal_reward"`
  - `slack_reward` / `success_reward`（在训练/benchmark 配置里通常会覆盖默认值）
  - `success_measure: "spl"`（用于判定“episode 是否成功”，成功时额外加 `success_reward`）
  - `end_on_success: True`（成功后可以提前 done）
- **reward 的组合逻辑**在 `habitat-lab/habitat/core/environments.py`：
  - `RLTaskEnv.get_reward()`：`reward = slack_reward + metrics[reward_measure] + (success ? success_reward : 0)`
  - `RLTaskEnv.get_done()`：episode_over 或（end_on_success 且 success）即 done
- **`distance_to_goal_reward` 的数学定义**在 `habitat-lab/habitat/tasks/nav/nav.py`：
  - `DistanceToGoalReward`：`reward = -(new_distance - previous_distance)`（即“距离减少”为正奖励）
- **`success_measure="spl"` 为什么也能当 success**：`spl` 在 `habitat-lab/habitat/tasks/nav/nav.py` 里是 `SPL` measure（依赖 `Success`），失败时为 0，成功时在 (0,1]，所以在 `if spl:` 的判断里等价于 “是否成功”。

### 1.2) DDPPO 是怎么计算 loss/目标函数并更新参数的？
- **DDPPO 的 loss 本质就是 PPO loss**，核心实现都在 `habitat-baselines/habitat_baselines/rl/ppo/ppo.py`（`class PPO`）。
- 训练时“从 reward 到 optimizer.step”的调用链（建议你按这个顺序读）：
  1) rollout 收集（env.step 返回 reward）：`habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`  
     `_collect_rollout_step()` -> `_compute_actions_and_step_envs()` / `_collect_environment_result()`
  2) 计算 returns/GAE：`habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py:_update_agent()`  
     `rollouts.compute_returns(next_value, use_gae, gamma, tau)`（实现见 `habitat-baselines/habitat_baselines/common/rollout_storage.py:compute_returns`）
  3) PPO 更新：`habitat-baselines/habitat_baselines/rl/ppo/ppo.py:update()`  
     生成 minibatch -> `_update_from_batch(...)` -> `total_loss.backward()` -> `clip_grad_norm_` -> `optimizer.step()`
- **PPO 的总 loss 组成**（都能在 `habitat-baselines/habitat_baselines/rl/ppo/ppo.py:_update_from_batch()` 对上号）：
  - `ratio = exp(new_logp - old_logp)`
  - `action_loss = -min(adv * ratio, adv * clamp(ratio, 1-eps, 1+eps))`
  - `value_loss = 0.5 * mse(V(s), returns)`（可选 value clipping）
  - `entropy bonus`：`-entropy_coef * dist_entropy`（鼓励探索）
  - `aux losses`：如果你配置了 `habitat_baselines.rl.auxiliary_losses.*`，会 `all_losses.extend(...)` 加到 `total_loss`
  - `total_loss = value_loss_coef * value_loss + action_loss - entropy_coef * entropy + aux`
- **DDPPO 和 PPO 的区别点在哪里**（不改 loss，只改“如何分布式算它”）：
  - `habitat-baselines/habitat_baselines/rl/ddppo/algo/ddppo.py`：`class DDPPO(DecentralizedDistributedMixin, PPO)`  
    主要是把 `evaluate_actions` 包一层 `DistributedDataParallel`，并把 `advantages` 的 var/mean 统计做成 distributed 版本（`distributed_var_mean`）。

### 2) Baseline 模型结构（你要改 encoder 的位置）
- PointNav policy（ResNet encoder + RNN + actor/critic heads）  
  `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet_policy.py`
  - `ResNetEncoder`：视觉编码器入口（改 backbone/输入通道/融合都在这里落地）
  - `PointNavResNetNet.forward()`：把 visual + goal 传感器特征拼接后送入 RNN

### 2.1) 我怎么确认 “模型输入/输出” 到底是什么（推理视角）
- **模型输入来自 env observation（由 config 决定）**，核心入口在：
  - `habitat-lab/habitat/gym/gym_wrapper.py`：`HabGymWrapper` 会按 `habitat.gym.obs_keys` 过滤 observation keys
    - `obs_keys=None` 时默认包含 env 提供的所有 observation keys
    - 这就是为什么“同一套 policy 代码”有时吃 RGBD，有时只吃 depth: 取决于 `obs_keys` 和 sim_sensors 是否开启
  - `habitat-baselines/habitat_baselines/rl/ddppo/policy/resnet_policy.py`：`ResNetEncoder.visual_keys` 会把所有“图像类输入（shape>1）”找出来，然后把它们在 channel 维 concat
    - 如果 observation 里同时有 `rgb(H,W,3)` + `depth(H,W,1)`，那 encoder 的输入通道数就是 4（RGBD）
    - 如果你只保留 `depth(H,W,1)`，那输入通道数就是 1（depth-only）
- **PointNav 默认的 “GPS+Compass” 在哪**：
  - 配置启用传感器：`habitat-lab/habitat/config/habitat/task/pointnav.yaml` 里默认启用 `pointgoal_with_gps_compass_sensor`
  - 传感器实现代码：`habitat-lab/habitat/tasks/nav/nav.py` 的 `IntegratedPointGoalGPSAndCompassSensor`（uuid=`pointgoal_with_gps_compass`）
    - 它不是直接把 `(gps, compass)` 两个 raw 传感器值拼给你，而是用 episode goal + agent state 在线计算 “pointgoal” 观测
    - 如果你同时在 task 里启用 `GPSSensor`/`CompassSensor`，policy 里也有对应 embedding（见 `PointNavResNetNet` 对 `EpisodicGPSSensor`/`EpisodicCompassSensor` 的分支）
- **模型输出是什么（离散/连续）**：
  - 输出动作张量在 `habitat-baselines/habitat_baselines/rl/ppo/policy.py`：`NetPolicy.act()` 返回 `PolicyActionData.actions`
  - `action_distribution_type` 决定离散/连续：
    - 默认 `PolicyConfig.action_distribution_type="categorical"`（离散动作 id），由 `habitat-baselines/habitat_baselines/config/default_structured_configs.py` 定义
    - 如果设成 `gaussian` 才是连续动作（mean/std），同一个 `act()` 会输出连续向量
  - 对 PointNav 任务来说，默认动作集合在 `habitat-lab/habitat/config/habitat/task/pointnav.yaml`：
    - `stop` / `move_forward` / `turn_left` / `turn_right`
    - 因此 “离散动作 id” 本质是在这个 action set 上做分类
- **项目里有没有“加载权重的推理代码”**：有，两条主路径（你现在已经用过）
  - `python -m habitat_baselines.run habitat_baselines.evaluate=True ...`：走 `PPOTrainer._eval_checkpoint()`（`habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py`）
  - 权重加载位置：
    - 加载 RL ckpt：`PPOTrainer._eval_checkpoint()` -> `self.load_checkpoint(...)` -> `self._agent.load_state_dict(...)`
    - 加载 DDPPO 预训练 encoder：`SingleAgentAccessMgr._create_policy()`（`habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py`）里读 `habitat_baselines.rl.ddppo.pretrained*`

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

## 本机数据盘点（2026-02-23）

> 说明：
> - 空间占用来自 `du -sh`（会受文件系统 block size 影响，属于近似值）。
> - `data/` 内存在少量“仓库内相对软链接”（例如 `data/scene_datasets/habitat-test-scenes -> ../versioned_data/habitat_test_scenes`），`du` 看到的 `0` 只是链接本身大小。
> - 本节只统计 Habitat 相关数据/权重/产物，不包含 conda env、pip cache 等。

### 1) 仓库目录：`/home/liuyi/projects/habitat-lab`

- 压缩包/历史文件
  - `habitat-test-scenes.zip`：91M
- 训练/评估产物（仓库根目录）
  - `videos/`：11M
  - `tb/`：9.7M
  - `outputs/`：752K
- `data/`（仓库内数据根目录）总计：2.7G
  - 预训练权重
    - `data/ddppo-models/`：48M（`gibson-2plus-resnet50.pth`）
  - 训练/评估产物（checkpoint）
    - `data/new_checkpoints/`：290M（`ckpt.*.pth` + `latest.pth` + `.habitat-resume-state*.pth`）
    - `data/new_checkpoints_ddppo_demo/`：848M（你的 demo 训练产物）
  - 数据集（episodes）
    - `data/datasets/`：386M（含 `pointnav/gibson`）
  - 场景/资源（versioned_data）
    - `data/versioned_data/`：1.2G（`habitat_test_*` + `replica_cad_dataset` + `ycb` + `hab_fetch` + `rearrange_*`）
  - 自定义数据
    - `data/custom_datasets/`：20K（`val_long10.json.gz`）
  - 旧外部软链备份（不参与运行）
    - `data/_external_links_backup/`：8K

树结构（简化）：
```text
/home/liuyi/projects/habitat-lab
|-- habitat-test-scenes.zip (91M)
|-- data (2.7G)
|   |-- datasets (386M)
|   |-- scene_datasets (dir + internal symlinks)
|   |-- objects (dir + internal symlinks)
|   |-- robots (dir + internal symlinks)
|   |-- replica_cad -> versioned_data/replica_cad_dataset
|   |-- new_checkpoints (290M)
|   |-- ddppo-models (48M)
|   |-- new_checkpoints_ddppo_demo (848M)
|   |-- versioned_data (1.2G)
|   |-- custom_datasets (20K)
|   `-- _external_links_backup (8K)
|-- videos (11M)
|-- tb (9.7M)
`-- outputs (752K)
```

### 2) 旧数据根目录（未删除）：`/home/liuyi/datasets/habitat`（2.0G）

该目录已不再被仓库内 `data/` 依赖（仅作为迁移前数据来源保留）。确认你本地运行无误后，可以再讨论是否删除以释放空间。

### 3) 迁移状态（总结）

- 仓库 `data/` 现在是本机唯一数据根目录；`data/` 内不再指向 `/home/liuyi/datasets/habitat`。
- `/home/liuyi/datasets/habitat` 仍存在（冗余副本）；后续如果你确认不再依赖，可以删除。

## 数据整理建议（按你当前“本地全放 data/”的规则）

1) 本机 canonical root：仓库内 `data/`（仅放静态数据：scene assets / datasets / pretrained weights）。  
2) 训练与评估产物统一放 `runs/<task>/<exp>/<timestamp>/...`（不再写入 `data/`）。  
3) 远程服务器 canonical root：建议放到共享盘（示例 `/data/habitat`），每个 repo 的 `data/` 软链到共享盘路径，避免多份拷贝。  
4) 需要 rearrange demo 时再补齐 `example_objects`（当前不创建坏链接，避免踩坑）。  
5) 确认无回滚需求后，可删除 `/home/liuyi/datasets/habitat` 冗余副本与 `data/_external_links_backup/`。

## 运行产物重整（2026-02-23）

为避免 `data/` 与运行输出混放，已完成重整：

- 历史运行产物已迁移到 `runs/legacy/`：
  - `runs/legacy/checkpoints/new_checkpoints`
  - `runs/legacy/checkpoints/new_checkpoints_ddppo_demo`
  - `runs/legacy/hydra_outputs/all_outputs`
  - `runs/legacy/tensorboard/tb`
  - `runs/legacy/videos/videos`
  - `runs/legacy/logs/train.log`
- 过渡软链接已删除，不再保留（避免目录混乱）：
  - `outputs` / `tb` / `videos` / `train.log`
  - `data/new_checkpoints` / `data/new_checkpoints_ddppo_demo` / `data/videos`

后续新实验统一写入 `runs/...`，不再默认写入仓库根目录或 `data/`。

## 双目轨迹录制脚本（2026-02-23）

脚本路径：`examples/pointnav_stereo_rollout_recorder.py`

### 1) 脚本用途

- 从 PointNav episodes 中取样并 `reset`。
- 用 `ShortestPathFollower` 生成近似最短路动作序列并执行 rollout。
- 每一步保存一张 `left|right` side-by-side PNG。
- 每个 episode 结束后额外保存一张 topdown 地图+轨迹图（`topdown_trajectory.png`）。
- 同步写 `metadata.jsonl`（step、action、goal、agent pose）。
- 该脚本独立运行，不改训练/评估主链路。

### 2) 实现逻辑（当前版本）

- 左目使用主 agent 的 `rgb_sensor`；右目运行时注入 `ThirdRGBSensorConfig`。
- 两目分辨率与 `hfov` 相同，`hfov` 由 `fx` 和 `width` 反算：
  - `hfov = 2 * atan(width / (2 * fx))`
  - 注意：当前 Habitat 结构化配置里 `hfov` 字段是 `int`，脚本会对反算出的浮点 `hfov` 做 `round` 后写入，并打印等效 `fx` 与误差百分比。
- 基线按对称方式放置在原相机中心两侧：
  - left: `center - sign * baseline / 2`
  - right: `center + sign * baseline / 2`
- `right-x-sign` 用于切换左右在 x 轴上的方向定义（便于快速检查视差方向）。
- 脚本会自动启用 `top_down_map` measurement（若配置里未开启），并在 rollout 过程中更新 topdown 轨迹图。
- rollout 在以下条件之一停止：
  - episode 结束
  - follower 返回 `stop/None`
  - 达到 `max_steps`

### 3) 主要参数说明

- `--config-path`：PointNav 配置，默认 `benchmark/nav/pointnav/pointnav_habitat_test.yaml`
- `--overrides`：可选 Habitat config 覆盖项
- `--output-dir`：输出目录，默认 `runs/stereo_debug_rollouts`
- `--num-episodes`：录制 episode 数量，默认 `5`
- `--max-steps`：每条 episode 最多步数，默认 `200`
- `--width --height`：图像分辨率，默认 `640x512`
- `--fx`：用于反算 `hfov` 的焦距（像素），默认 `302.53882`
- `--baseline-meters`：双目基线（米），默认 `0.12165`
- `--right-x-sign`：右目 x 轴方向，`1` 或 `-1`，默认 `1`
- `--left-obs-key`：左目观测键名，默认 `rgb`
- `--right-obs-key`：右目观测键名，默认 `right_rgb`
- `--seed`：随机种子，默认 `0`

### 4) 推荐运行命令（最新）

```bash
cd ~/projects/habitat-lab
conda activate habitat
export DATA_ROOT=$(pwd)/data
python -u examples/pointnav_stereo_rollout_recorder.py \
  --config-path benchmark/nav/pointnav/pointnav_habitat_test.yaml \
  --num-episodes 5 \
  --max-steps 80 \
  --output-dir runs/stereo_debug_rollouts/habitat_test \
  --width 640 --height 512 \
  --fx 302.53882 \
  --baseline-meters 0.12165 \
  --right-x-sign 1
```

Gibson 版本：

```bash
python -u examples/pointnav_stereo_rollout_recorder.py \
  --config-path benchmark/nav/pointnav/pointnav_gibson.yaml \
  --num-episodes 5 \
  --max-steps 80 \
  --output-dir runs/stereo_debug_rollouts/gibson \
  --width 640 --height 512 \
  --fx 302.53882 \
  --baseline-meters 0.12165 \
  --right-x-sign 1
```

### 5) 输出结构

- `runs/stereo_debug_rollouts/<split>/ep_xxx_<scene>_<episode_id>/frame_00000.png`
- `runs/stereo_debug_rollouts/<split>/ep_xxx_<scene>_<episode_id>/metadata.jsonl`
- `runs/stereo_debug_rollouts/<split>/ep_xxx_<scene>_<episode_id>/topdown_trajectory.png`
绿线：shortest path（从起点到目标的最短路参考线）
代码在 nav.py (line 832) 到 nav.py (line 836)，颜色常量是绿色 MAP_SHORTEST_PATH_COLOR，定义在 maps.py (line 50)。

蓝线：通常是 agent 实际走过轨迹的“早期颜色段”
轨迹在 nav.py (line 904) 到 nav.py (line 915) 用随步数变化的 colormap 画，开始偏蓝，后面会逐渐变绿/黄/红。
另外起点本身也是蓝色标记，定义在 maps.py (line 48)。

### 6) 常见检查项

- 如果视差方向和预期相反：改 `--right-x-sign -1` 重跑。
- 如果左右图键名不一致：显式指定 `--left-obs-key` 与 `--right-obs-key`。
- 如果没有生成 topdown 图：检查配置是否是导航任务并确认 episode 至少执行了一步。
