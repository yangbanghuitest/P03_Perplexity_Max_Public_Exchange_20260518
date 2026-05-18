# P03 四 skill 联合推进作战书

项目：P03 集美大学 SAR-AIS 暗船识别 Remote Sensing 论文  
工作区：`D:/学术科研工作空间_2026/02_论文项目/P03_集美大学_SAR-AIS暗船识别_RemoteSensing_20260517`  
参考区：`D:/学术科研工作空间_2026/02_论文项目/P03_低空经济与无人机遥感`  
日期：2026-05-18  
目标：把现有 v2 送审稿从“可投稿初稿”推进到“证据链可审、实验可复现、投稿包可交付”的 Remote Sensing Article。

---

## 0. 当前材料判断

### 0.1 已形成的稿件骨架

主稿件在 `08_v2_送审稿/manuscript_v2.md`，题目为：

> Spatiotemporal Evidence Fusion of SAR Ship Detections and AIS Tracks for Dark Vessel Discovery in Maritime Emergency Awareness: A Taiwan Strait Case Study

稿件已经具备 Remote Sensing Article 的基本形态：

| 维度 | 当前状态 | 判断 |
|---|---|---|
| 论文定位 | SAR 船舶检测 + AIS 轨迹重建 + SAR-AIS 时空证据融合 + 暗船候选/身份不符/电子围栏告警 | 主线正确，不应写成平台建设报告 |
| 核心贡献 | 六阶段融合框架、五类证据 taxonomy、AIS 过境时刻重建、自适应门限 + Hungarian、身份/围栏层 | 有可审稿的“方法贡献”雏形 |
| 实验结果 | 50 个 Taiwan-Strait 控制仿真场景；mean F1 = 0.857；dark recall = 0.93；identity mismatch recall = 0.69；3.5 s/patch | 可支撑初投，但真实数据补强仍是关键 |
| 运行材料 | `08_v2_送审稿/code/` 已有 SAR 检测、AIS 处理、融合与绘图脚本 | 需要补 run ledger 和参数核查表 |
| 图件 | Fig.1-Fig.7 PNG/PDF 已生成 | 需要替换/补充若干真实脱敏产品图 |
| 文献 | `refs/references_v2.bib` 与 `refs/lit_summary.md` 已有 54 条 | 需做 2025-2026 最新查新和 DOI/元数据复核 |
| 证据台账 | `08_v2_送审稿/EVIDENCE_LEDGER.md` 已列支撑材料和缺口 | 需要把缺口转成学生任务和 Go/No-Go |

### 0.2 08 续推进包的核心结论

`08_科研智能体续推进包_20260517/P03_RemoteSensing补实验与投稿清单_20260517.md` 已给出正确方向：

1. 不要先做语言润色，先补 Remote Sensing 最容易审查的数据、方法、实验和图件证据链。
2. 术语统一为 `dark-vessel candidates`、`non-cooperative vessel candidates`、`SAR-AIS unmatched detections`、`identity-inconsistent vessel events`、`geofence-related anomaly candidates`。
3. 避免使用 `confirmed illegal vessels`、`smuggling vessels`、`hostile vessels` 等法律定性词。
4. 本周最小补实验为 E1 SAR-AIS 匹配统计、E2 门限敏感性、E3 误差来源分析、E4 可视化案例。
5. 投稿前关键风险：稿件仍可能被审稿人质疑“仿真多、真实产品少”和“工程平台报告味道重”。

### 0.3 当前最大缺口

| 缺口 | 影响 | 优先级 |
|---|---|---|
| 平台实际参数未完全核实：CFAR 窗口/Pfa、SAR-AIS 匹配距离、AIS 漂移阈值、最小/最大目标面积、极化通道 | Methods 可复现性与审稿可信度 | P0 |
| 缺少 5-10 个真实脱敏 SAR-AIS 联合产品案例 | 容易被质疑“全是仿真” | P0 |
| 缺少 K-sweep / 门限敏感性曲线 | 自适应门限与工作点选择证据不足 | P1 |
| 真实 AIS 数据规模、船舶数、报文数未补齐 | Data section 不够硬 | P1 |
| 文献中若干 2025-2026 新工作和 DOI 尚需最终核查 | Related Work 时效性 | P1 |
| 投稿包的 cover letter、highlights、CRediT、MDPI 模板转换未完成 | 投稿交付 | P2 |

---

## 1. 四 skill 联合作战框架

| Skill | 在 P03 中的角色 | 交付物 |
|---|---|---|
| `ai4s-literature-radar` | 最新文献/工具查新、引用筛选、对比表补强 | 查新路线、must-read 列表、引用动作 |
| `ai4s-experiment-pipeline` | 可复现实验矩阵、run ledger、Go/No-Go | 实验矩阵、指标、验收标准 |
| `ai4s-manuscript-factory` | 稿件结构、图表清单、投稿包和审稿风险 | 投稿包清单、图表清单、证据台账 |
| `ai4s-gaussian-splatting-workflow` | 谨慎迁移“空间证据链核查/可视化审计”思想 | 多源空间证据链核查表、可视化质检方案 |

注意：P03 不是 3DGS 论文，不引入 Gaussian Splatting 方法，不写 novel-view synthesis、point-line-plane Gaussian、3D 重建指标。这里只迁移 3DGS 工作流里“多源空间几何一致性、可视化核查、视角/尺度/证据可追溯”的工程思想。

---

## 2. Literature Radar：最新文献/工具查新路线

### 2.1 搜索 lanes

| Lane | 查询式 | 目标 | 动作 |
|---|---|---|---|
| L1 SAR-AIS fusion | `SAR AIS association ship detection data fusion Sentinel-1`, `SAR AIS matching dark vessel` | 支撑 adaptive gate、Hungarian、AIS scene-time interpolation | 补 Table 6 与 Related Work 2.3 |
| L2 dark vessel / non-cooperative vessel | `dark vessel detection SAR AIS 2024 2025`, `non-cooperative vessel detection SAR maritime surveillance` | 确认问题背景、最新 SOTA 与术语边界 | Introduction + Discussion |
| L3 SAR ship detection | `SAR ship detection CFAR deep learning review 2024`, `GF-3 SAR ship detection maritime` | 说明 CFAR 可替换、本文不是 detector paper | Related Work 2.1 + Limitation |
| L4 AIS anomaly / spoofing | `AIS spoofing identity mismatch trajectory anomaly 2024 2025`, `AIS intentional disabling detection` | 支撑 identity mismatch 与 AIS gap/error taxonomy | Related Work 2.2 + Error taxonomy |
| L5 operational maritime awareness | `operational maritime domain awareness SAR AIS`, `ESA dark vessel detection SAR AIS` | 支撑 emergency awareness 与服务化落地 | Introduction + Discussion |
| L6 datasets/tools | `xView3 SAR dataset`, `HRSID LS-SSDD SAR-Ship-Dataset`, `Copernicus Sentinel-1 maritime surveillance` | 审稿人要求 benchmark/SOTA 时的备选 | Methods/Discussion 备份 |

### 2.2 Must-read / must-verify

| 文献/工具 | 年份 | 作用 | 当前动作 |
|---|---:|---|---|
| Paolo et al., *Nature*, “Satellite mapping reveals extensive industrial activity at sea” | 2024 | 全球“非公开追踪活动/暗船”背景，高影响力引文 | 保留 Introduction，不把全球比例硬套到台海 |
| xView3-SAR / NeurIPS Datasets and Benchmarks | 2022 | 暗渔船 SAR benchmark 与公开数据集 | Related Work 中说明本文不是 benchmark，而是 evidence fusion |
| Pelich et al., *Remote Sensing*, Sentinel-1 + AIS large-scale monitoring | 2019 | 与目标期刊高度贴合的 SAR-AIS 基准论文 | Table 6 必列 |
| Rodger & Guida, classification-aided Sentinel-1 SAR and AIS fusion | 2021 | 密集海域数据关联参考 | 支撑 association section |
| Galdelli et al., synergic SAR-AIS | 2021 | Sentinel-1 + AIS 点/线关联与异常案例 | 支撑 AIS gap/dark candidate |
| Li et al., *Remote Sensing*, “Dark Ship Detection via Optical and SAR Collaboration” | 2025 | 近期 Remote Sensing 暗船工作 | Related Work 最新直接对比 |
| Li et al., SAR ship detection deep learning review | 2022 | detector 综述 | 说明 CA-CFAR 与 DL 关系 |
| El-Darymli et al., deep model vs K-CFAR / SUMO on xView3 | 2024 | 审稿人要求 detector 对比时的防线 | Discussion 中承认 detector 可替换 |
| AIS spoofing / intentional AIS disabling work | 2021-2025 | 支撑身份不符和 AIS 关机语义 | 补 error taxonomy |
| ESA / Copernicus maritime surveillance / dark vessel services | 2024-2026 | 服务化背景，不一定作为学术引文 | cover letter 与 Discussion 背景 |

### 2.3 引用筛选规则

1. 必须优先保留：Remote Sensing、TGRS、JSTARS、Sensors、Nature、Science Advances、NeurIPS Datasets。
2. 会议论文只用于最新趋势或无期刊替代时；不要让会议文献撑起核心创新。
3. 任何带 “illegal / smuggling” 的文献只作为背景，不在本文结果中做法律定性迁移。
4. 所有 DOI、卷期、页码、作者名在投稿前统一从 publisher/arXiv/DOI 官网复核。
5. 参考文献最终分层：核心必引 15-20 篇、方法支撑 15-20 篇、背景与区域应用 10-15 篇。

### 2.4 工具查新路线

| 工具/源 | 用途 | 输出 |
|---|---|---|
| Web of Science / Scopus | 终稿引用元数据复核 | `references_checked_20260524.bib` |
| Google Scholar | 追踪 2025-2026 新文献和被引关系 | `literature_screening_20260524.xlsx` |
| MDPI Remote Sensing 官网 | 目标期刊 scope、模板、AI disclosure | 投稿包 checklist |
| arXiv / Papers with Code | xView3 与 detector 代码状态 | 审稿应答备份 |
| GitHub | xView3、SAR ship detector、AIS cleaning 工具代码状态 | 不直接引入主实验，作为替换 detector 备选 |
| Zotero | 统一 BibTeX 和 citekey | `references_v3.bib` |

---

## 3. Experiment Pipeline：实验矩阵与复现账本

### 3.1 可证伪主张

主张 A：SAR-AIS 时空证据融合比单独 SAR 检测或单独 AIS 轨迹分析更适合生成可审计的暗船候选、身份不符和电子围栏告警。  
主张 B：自适应门限 + Hungarian assignment 在密集海域场景中比固定半径/最近邻匹配更稳定。  
主张 C：该框架可以在受限真实数据条件下通过“控制仿真 + 脱敏真实产品 + 第三方功能测试”形成可投稿的双层验证。

### 3.2 数据分层

| Tier | 数据 | 当前状态 | 用途 |
|---|---|---|---|
| T0 公开数据 | Sentinel-1、Sentinel-2、xView3、HRSID/LS-SSDD/SAR-Ship-Dataset | 可查证，不一定进入主实验 | 文献对比、审稿备选 |
| T1 控制仿真 | 50 个 Taiwan-Strait 15 km x 15 km 场景 | 已完成，见 `scene_stats.csv` | 主结果和可复现指标 |
| T2 内部脱敏产品 | GF-3/Sentinel-1 + AIS 联合产品 5-10 景 | 待导出 | 初投前最关键补强 |
| T3 工程证据 | 202 第三方测试用例、232 GF-3、6044 Sentinel-1、1300 Sentinel-2 等资产 | 已有台账 | operational anchoring |
| T4 敏感原始数据 | 原始 AIS、精确坐标、船名/MMSI、涉管控区边界 | 不公开 | 只用于内部核查，不进公共仓库 |

### 3.3 实验矩阵

| Exp | 数据 | 方法/对比 | 指标 | 输出 | Go 标准 |
|---|---|---|---|---|---|
| E1 最小场景统计 | T1 + T2 | 五类 evidence taxonomy | matched、dark、AIS-only、id-mismatch、geofence 数量 | `P03_RS_minimal_experiment_filled_20260524.csv` | 至少 50 仿真 + 5 真实脱敏场景 |
| E2 门限敏感性 | T1 | 时间窗 `{±2, ±5, ±10 min}` x 半径 `{200, 500, 1000 m}` x K `{4,5,6,6.5,7,8}` | P/R/F1、dark recall/precision、ambiguous rate | `P03_threshold_sensitivity_v0.1.csv` + PR 曲线 | 当前工作点不是孤立最优或任意选择 |
| E3 匹配消融 | T1 | nearest neighbor、fixed gate、adaptive gate、adaptive+Hungarian、adaptive+Hungarian+ambiguity | association F1、dense-scene F1、false match | 消融表 | adaptive+Hungarian 至少在密集场景明显优于 nearest/fixed |
| E4 Detector 可替换性 | T1 + 小样本 T2 | CA-CFAR vs 可获得 DL detector 或 xView3 公开模型备选 | raw detection F1、processing time | 审稿备份表 | 不要求初投完成；若审稿强问则启动 |
| E5 误差来源分析 | T1 + T2 | AIS 关机/延迟/漂移、SAR 虚警、近岸混叠、海况、重复 MMSI | error taxonomy | `P03_error_taxonomy_v0.1.md` | 每类误差有 mitigation 和图例 |
| E6 真实脱敏案例 | T2 | 5 类证据链逐例核查 | evidence completeness、可脱敏性 | 5-10 张案例图 + GeoJSON/shp 元数据 | 至少覆盖 dark、matched、AIS-only、id-mismatch、geofence 中 4 类 |
| E7 运行效率 | T1 + T2 | 单核/多核；15 km patch 与整景估算 | s/patch、memory、scene budget | `runtime_ledger.csv` | 解释 3.5 s/patch 与 60 min/scene 工程指标关系 |
| E8 第三方测试复核 | T3 | 202 case 功能映射 | requirement coverage、issue closure | `third_party_validation_mapping.md` | 三个问题等级和回归闭环说清楚 |

### 3.4 Run ledger 模板

建议新增 `04_数据与实验表/P03_run_ledger_20260524.csv`：

| run_id | date | git_commit | data_tier | data_version | config | command | output_path | metrics_path | operator | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| R001 | 2026-05-24 | 待填 | T1 | sim_v2_seeded | `K=6.5, window=±5min` | `python simulate_scene.py` | 待填 | 待填 | 学生A | 复现实验 |

### 3.5 Go/No-Go

| 决策点 | Go | No-Go / 降级路线 |
|---|---|---|
| 参数核查 | CFAR、匹配半径、AIS 漂移阈值、极化/产品级别至少 80% 有真实系统值 | 无法确认的参数统一写为 configurable engineering setting，并放入 limitation |
| 真实脱敏案例 | 至少 5 个可公开/可论文展示案例 | 若不能公开，改为 derived vector/statistical summaries + 内部审查说明 |
| 门限敏感性 | 至少 3 组时间窗 x 3 组空间半径；结果能解释工作点 | 若结果不稳，降低贡献表述为“framework demonstration”，不声称最佳 |
| 检测器质疑 | 能解释本文不是 detector paper，并给出可替换接口 | 若审稿强制要求 SOTA，补 xView3/DL detector 小样本替换实验 |
| 投稿时机 | v2 + 参数表 + 真实脱敏案例 + cover letter + references checked | 缺 T2 真实案例时不建议投 Remote Sensing，先内部送审 |

---

## 4. Manuscript Factory：投稿包、图表清单与证据台账

### 4.1 推荐投稿版本结构

| 部分 | 当前动作 |
|---|---|
| Title | 保留现题；备选题可弱化 Taiwan Strait，如 “Operational SAR-AIS Evidence Fusion for Dark-Vessel Candidate Discovery” |
| Abstract | 保留五类证据链和双层验证，但真实数据补强后更新数字 |
| Introduction | 用 Nature 2024 / xView3 / Pelich 2019 引出问题，强调 emergency awareness |
| Related Work | 分成 SAR detection、AIS anomaly、SAR-AIS association、operational MDA |
| Methods | 参数表必须补齐；所有 configurable 参数标明默认值和来源 |
| Validation | 区分 controlled simulation、desensitized operational samples、third-party functional evaluation |
| Results | 加入门限敏感性/消融/真实案例 |
| Discussion | 正面承认 dark precision、simulation-derived metrics、AIS data restrictions |
| Conclusion | 不宣称确认非法船，只说 dark-vessel/non-cooperative candidates |

### 4.2 投稿包清单

| 文件 | 状态 | 负责人 | 截止 |
|---|---|---|---|
| `manuscript_v3_RS_template.docx` 或 `.tex` | 待生成 | 写作负责人 | 2026-05-27 |
| `references_checked_20260524.bib` | 待核查 | 文献负责人 | 2026-05-24 |
| `cover_letter_RemoteSensing_v1.md` | 待写 | 通讯作者/智能体 | 2026-05-26 |
| `highlights_v3.md` | 已有雏形，待压缩 | 写作负责人 | 2026-05-25 |
| `graphical_abstract_or_toc.png` | 可选 | 图件负责人 | 2026-05-28 |
| `supplementary_material.zip` | 待整理 | 实验负责人 | 2026-05-28 |
| `data_availability_statement_v2.md` | 待按实际数据改写 | 数据负责人 | 2026-05-25 |
| `ai_use_disclosure_v2.md` | 已有雏形 | 写作负责人 | 2026-05-25 |
| `CRediT_author_statement.md` | 待作者确认 | 通讯作者 | 2026-05-25 |
| `conflict_of_interest.md` | 已有雏形 | 通讯作者 | 2026-05-25 |
| `ethics_sensitive_data_checklist.md` | 待补 | 数据负责人 | 2026-05-25 |

### 4.3 图表清单

| 编号 | 图表 | 当前状态 | 下一步 |
|---|---|---|---|
| Fig.1 | Overall SAR-AIS Evidence Fusion Framework | 已有 v2 图 | 核查是否突出五类证据链和六阶段模块 |
| Fig.2 | Study Area and Data Coverage | 已有 v2 图 | 加入数据资产规模和脱敏说明 |
| Fig.3 | SAR Ship Detection Example | 已有 v2 图 | 尽量替换为真实脱敏 SAR 产品局部图 |
| Fig.4 | AIS Scene-Time Reconstruction | 已有 v2 图 | 标清 ±5 min、bounded extrapolation、quality score |
| Fig.5 | SAR-AIS Fusion Result | 核心图已存在 | 增加 matched/dark/AIS-only/id-mismatch/geofence 统一图例 |
| Fig.6 | Scene Composition / Confusion Matrix | 已有 v2 图 | 保留，用于 50 场景统计 |
| Fig.7 | Aggregate Metrics | 已有 v2 图 | 加门限敏感性或 PR 曲线，必要时拆成 Fig.7a/7b |
| Fig.8 | Desensitized Operational Case Chain | 待新增 | 真实脱敏案例证据链图，强烈建议初投前补 |
| Fig.S1 | Run pipeline / product chain | 可作为补充材料 | 对应第三方测试和工程流程 |
| Table 1 | Data Assets | 已有雏形 | 补 AIS 报文量/船舶数/时间范围 |
| Table 2 | Evidence Classes | 已有 | 补每类误差来源和操作含义 |
| Table 3 | Method Modules and Parameters | 待强化 | 列所有参数、来源、默认值、是否核实 |
| Table 4 | Third-Party Validation Evidence | 已有 | 补 3 个问题具体描述或说明未公开 |
| Table 5 | Per-Scene Statistics | 已有 `scene_stats.csv` | 生成论文压缩版 |
| Table 6 | Literature Comparison | 已有雏形 | 加 2025 dark ship paper 和 detector 可替换列 |
| Table S1 | Threshold Sensitivity | 待新增 | E2 输出 |
| Table S2 | Error Taxonomy | 待新增 | E5 输出 |

### 4.4 证据台账升级

建议在 `08_v2_送审稿/EVIDENCE_LEDGER.md` 基础上新增一张 “claim-to-evidence” 表：

| Claim | Evidence | File | Risk |
|---|---|---|---|
| 五类证据 taxonomy 可生成 matched/dark/AIS-only/id/geofence | Fig.5, Table 2, scene_stats | v2 figures + csv | 类定义需避免法律定性 |
| ±5 min AIS interpolation 来自系统文档 | Evidence Ledger B3 | EVIDENCE_LEDGER.md | 需确认实际平台可配置项 |
| 202 第三方测试支撑 operational anchoring | Evidence Ledger E1-E4 | EVIDENCE_LEDGER.md | 不是精度验证，必须说清 |
| 232 GF-3 / 6044 Sentinel-1 数据资产存在 | Evidence Ledger F1-F2 | EVIDENCE_LEDGER.md | 原始数据不可公开，需脱敏策略 |
| 3.5 s/patch 满足 60 min/scene 预算 | overall_metrics + technical report | json + ledger | patch-to-scene 推算需解释 |

---

## 5. 3DGS Skill 谨慎迁移：可视化/空间证据链核查

### 5.1 迁移原则

只迁移以下思想：

1. 多源空间数据必须有共同坐标、时间戳、尺度和不确定性预算。
2. 每一个可视化点、框、轨迹、围栏都要能回溯到原始/中间数据记录。
3. 图件不能只“好看”，必须能审计：图例、阈值、坐标脱敏、证据分类一致。
4. 空间证据链要检查遮挡/近岸混叠/密集目标/尺度误差等几何问题。

明确不迁移：

1. 不写 3D Gaussian Splatting。
2. 不引入 PSNR、SSIM、LPIPS、Chamfer 等 3DGS 指标。
3. 不把电子沙盘或三维推演写成本文贡献。
4. 不让可视化喧宾夺主，主线仍是 SAR-AIS evidence fusion。

### 5.2 空间证据链核查表

| 核查项 | 问题 | 通过标准 |
|---|---|---|
| 时间一致性 | SAR acquisition time 与 AIS interpolation time 是否一致 | 每个 scene 有 UTC 时间，AIS 点有 `delta_t` |
| 坐标一致性 | SAR 检测点、AIS 点、电子围栏是否同一 CRS | 图件和表格记录 CRS/投影或 WGS84 |
| 空间门限 | 匹配半径是否按速度/时间差/定位误差调整 | 每个 match 输出 gate radius 和 distance |
| 一对多歧义 | 第二候选是否接近第一候选 | ambiguity flag 有规则和数量统计 |
| 尺度一致性 | SAR length proxy 与 AIS length 是否可比 | 记录 SAR 分辨率、像素尺度、长度误差带 |
| 近岸混叠 | 陆地/养殖/港区强散射是否影响 dark candidate | 有 coast_fraction 或 land-sea mask 标记 |
| 围栏叠加 | geofence 是否后分类 overlay，而不是新类别爆炸 | Base class + AOI state 分开显示 |
| 脱敏 | MMSI/船名/精确坐标是否暴露 | Hash MMSI、降精度坐标、局部相对坐标 |
| 可追溯 | 图中每个目标能否追溯到 scene_stats 或中间 GeoJSON | 每图附 source scene_id 和 layer id |

### 5.3 推荐可视化核查产物

| 产物 | 内容 | 用途 |
|---|---|---|
| `P03_visual_evidence_checklist_20260524.md` | 每张图逐项核查：坐标、时间、图例、脱敏、来源 | 图件质检 |
| `P03_operational_case_manifest.csv` | 真实脱敏案例清单：scene_id、sensor、time、evidence classes、source layers | 审稿与补充材料 |
| `P03_case_001_evidence_chain.geojson` | 一个脱敏案例的 SAR 点、AIS 点、匹配线、围栏 | 可选补充材料 |
| `P03_case_001_evidence_chain.png` | 同一案例的论文图 | Fig.8 候选 |

### 5.4 多源证据链图设计

一张合格的 Fig.8 应包含：

1. SAR detections：统一圆点或框，颜色表示 detection confidence。
2. AIS interpolated positions：三角点，标注 `delta_t` 或质量等级。
3. Match lines：细线连接 matched pairs，线型表示确定/歧义。
4. Dark candidates：高亮但不写 “illegal”。
5. AIS-only：用空心符号，说明可能是 AIS 覆盖/检测漏检/非船散射。
6. Identity mismatch：单独外圈或标记，不覆盖 base class。
7. Geofence：半透明边界，明确为 post-classification overlay。
8. 脱敏说明：图注写 “coordinates and vessel identifiers are desensitized”。

---

## 6. 学生任务分工

| 角色 | 任务 | 输入 | 输出 | 验收 |
|---|---|---|---|---|
| 学生 A：参数核查 | 向平台/开发同事核实 CFAR、匹配、AIS 清洗、极化、目标面积参数 | EVIDENCE_LEDGER 缺口表 | `P03_platform_parameter_check_20260524.md` | P0 参数至少 80% 有真实值 |
| 学生 B：真实案例导出 | 从平台导出 5-10 个脱敏 SAR-AIS 联合产品 | 平台产品/日志 | PNG/PDF + GeoJSON/shp 属性表 | 覆盖至少 4 类证据 |
| 学生 C：门限敏感性 | 跑 K/window/radius sweep | v2 code + scene_stats | sensitivity csv + PR/heatmap 图 | 可解释当前工作点 |
| 学生 D：文献核查 | 补 2025-2026 文献，核查 DOI/BibTeX | lit_summary + Web of Science/Scholar | `references_checked_20260524.bib` | 无 “to verify” 条目进入终稿 |
| 学生 E：误差 taxonomy | 写 AIS/SAR/匹配/近岸/围栏误差来源 | scene cases + ledger | `P03_error_taxonomy_v0.1.md` | 每类误差有影响与缓解 |
| 学生 F：投稿包 | MDPI 模板、cover letter、CRediT、data availability | manuscript_v2 | 投稿包文件 | 可以进行内部预审 |

---

## 7. 一周推进节奏

| 日期 | 里程碑 | 产物 |
|---|---|---|
| 2026-05-18 | 联合作战书落地 | 本文件 |
| 2026-05-19 | 参数核查启动、真实案例清单确定 | 参数问题清单、案例候选表 |
| 2026-05-20 | E2/E3 sweep 跑通 | sensitivity 初表、消融初表 |
| 2026-05-21 | 真实脱敏图件第一版 | Fig.8 draft、case manifest |
| 2026-05-22 | 文献 DOI/BibTeX 核查 | references_checked draft |
| 2026-05-23 | v3 稿件整合 | manuscript_v3 draft |
| 2026-05-24 | Go/No-Go 评审 | 投稿/延后/降级决定 |

---

## 8. 最终 Go/No-Go 会议议程

1. 数据：真实脱敏案例是否足以抵消“全仿真”质疑。
2. 方法：核心参数是否可复现；不能公开的参数是否有合理 statement。
3. 实验：门限敏感性和消融是否支撑 adaptive gate + Hungarian。
4. 图件：是否存在敏感信息、图例不一致、坐标/时间不清。
5. 文献：是否覆盖 2024-2026 最新 dark vessel / SAR-AIS / AIS anomaly。
6. 投稿包：MDPI 声明、AI disclosure、data availability、CRediT 是否齐全。
7. 风险：是否仍像平台报告；是否过度声明“非法船”。

### Go

满足以下条件可进入 Remote Sensing 初投：

1. v3 中加入至少 5 个真实脱敏 operational samples 或等价 derived vector evidence。
2. 参数表 P0 项目核实或明确声明为 configurable/default。
3. E2 门限敏感性和 E3 消融至少完成一个。
4. references 无明显 metadata 错误。
5. 图件完成脱敏核查。

### Conditional Go

若真实案例只能放统计和局部图，仍可投稿，但需在 cover letter 与 Data Availability 中主动说明数据限制；贡献表述从“validated by operational samples”降为“anchored by operational evidence and desensitized examples”。

### No-Go

若无法提供真实脱敏案例、参数无法核实、文献仍有大量待核查，则不建议投 Remote Sensing。降级路线：

1. 先投国内/行业会议或内部技术报告；
2. 或转为 “framework and protocol paper”，降低性能主张；
3. 或等待真实数据导出后再投 Remote Sensing。

---

## 9. 立即可执行清单

1. 新建 `04_数据与实验表/P03_platform_parameter_check_20260524.md`，逐项核实 CFAR、匹配半径、AIS 规则、极化通道。
2. 新建 `04_数据与实验表/P03_run_ledger_20260524.csv`，记录所有仿真/补实验运行。
3. 跑 E2：`K x time window x radius` sweep，并生成 Fig.7b 或 Table S1。
4. 从平台导出 5-10 个真实脱敏 SAR-AIS 联合产品，优先覆盖 dark、matched、id-mismatch、geofence。
5. 新建 `06_图表规划/P03_visual_evidence_checklist_20260524.md`，逐图检查可视化证据链。
6. 更新 `08_v2_送审稿/refs/references_v2.bib` 的派生版本，不直接覆盖原文件，命名为 `references_checked_20260524.bib`。
7. 起草 `07_投稿与风险检查/cover_letter_RemoteSensing_v1.md` 和 `data_availability_statement_v2.md`。

---

## 10. 结论

P03 当前不是从零开始，而是已经有一版可送审的 v2 稿件、可复现实验代码、7 张期刊级图、54 条文献、第三方测试证据和数据资产台账。下一步的关键不是“再写更多文字”，而是把审稿人最可能追问的四件事钉牢：

1. 参数和数据来源是否可信；
2. 仿真指标是否有真实脱敏案例支撑；
3. SAR-AIS 匹配规则是否经得起门限敏感性检查；
4. 图件和术语是否避免法律定性与敏感信息泄露。

四个 skill 的合流策略是：文献雷达保证时效和对比坐标，实验流水线保证可复现和可证伪，稿件工厂保证投稿包完整，3DGS 工作流仅作为空间证据链核查的可视化纪律。按此推进，P03 最现实的目标是在一周内完成 v3 内部预审，并在 Go 条件满足后进入 Remote Sensing 初投。
