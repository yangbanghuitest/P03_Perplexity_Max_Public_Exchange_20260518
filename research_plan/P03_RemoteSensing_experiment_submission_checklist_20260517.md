# P03 Remote Sensing 补实验与投稿清单

项目：集美大学 SAR-AIS 暗船识别 Remote Sensing 论文  
日期：2026-05-17

## 当前判断

P03 已经有英文初稿和支撑材料包。下一步不要先追求语言润色，而是补齐 Remote Sensing 初投稿最容易被检查的证据链：

1. 数据来源、时间范围、空间范围、样本量。
2. SAR 船舶检测与 AIS 轨迹关联流程。
3. dark-vessel candidates 的判定规则与误差来源。
4. 最小统计实验和消融表。
5. 数据可用性、代码可用性、AI 使用声明、利益冲突声明。

## 术语边界

全文统一使用：

- dark-vessel candidates
- non-cooperative vessel candidates
- SAR-AIS unmatched detections
- identity-inconsistent vessel events
- geofence-related anomaly candidates

避免使用：

- confirmed illegal vessels
- smuggling vessels
- hostile vessels
- law-enforcement confirmed targets

除非有权威执法确认材料，否则不做法律定性。

## 本周最小补实验

| 实验 | 目的 | 输出 | 验收标准 |
|---|---|---|---|
| E1 SAR-AIS 匹配统计 | 证明不是个例描述 | `P03_RS_minimal_experiment_filled_20260524.csv` | 至少 20-50 景或事件，含 matched/unmatched/uncertain |
| E2 时空门限敏感性 | 证明阈值选择合理 | `P03_threshold_sensitivity_v0.1.csv` | 至少 3 组时间窗、3 组空间半径 |
| E3 误差来源分析 | 控制误报风险 | `P03_error_taxonomy_v0.1.md` | 包含 AIS 关机、延迟、漂移、SAR 虚警、近岸混叠 |
| E4 可视化案例 | 支撑方法可读性 | 5-7 张脱敏图 | 每张图有图注、来源、脱敏说明 |

## 建议图表

| 编号 | 图表 | 内容 | 状态 |
|---|---|---|---|
| Fig.1 | 研究区与数据流程 | SAR、AIS、时间窗、证据融合流程 | 需要绘制 |
| Fig.2 | SAR 船舶检测示例 | SAR 图像、候选框、置信度 | 需要脱敏图 |
| Fig.3 | AIS 轨迹重建与插值 | 原始 AIS 点、插值轨迹、时间间隔 | 需要平台导出 |
| Fig.4 | SAR-AIS 匹配/不匹配案例 | matched、unmatched、uncertain 三类 | 需要案例 |
| Fig.5 | dark-vessel candidate 判定流程 | 阈值、规则、证据等级 | 可先画流程图 |
| Fig.6 | 阈值敏感性结果 | 时间窗/空间半径对候选数量影响 | 需统计表 |
| Table 1 | 数据资产表 | 数据源、时间、空间、分辨率、样本量 | 需要填写 |
| Table 2 | 方法对比表 | 仅 SAR、仅 AIS、SAR-AIS fusion | 需要实验 |
| Table 3 | 误差与限制 | 误差来源、影响、缓解方法 | 可先写 |

## 投稿声明草稿

### Data Availability Statement

可先使用如下口径，后续按实际数据调整：

The data used in this study include remote-sensing images and AIS-derived vessel trajectories. Due to maritime safety, privacy, and data-licensing constraints, the raw operational data cannot be publicly released. Desensitized statistical summaries, processing protocols, and selected non-sensitive examples are provided in the article and supplementary material. Additional access may be considered by the corresponding author under appropriate permission and data-use agreements.

### AI Assistance Disclosure

可先使用如下口径，后续按实际使用工具调整：

During the preparation of this manuscript, the authors used AI-assisted tools for language polishing, literature organization, figure planning, and internal checklist generation. The authors reviewed, edited, and verified all AI-assisted outputs and take full responsibility for the content of the manuscript.

### Conflict of Interest

若无冲突：

The authors declare no conflicts of interest.

## 给学生的执行任务

1. 填写 `04_数据与实验表/02_最小统计实验_填写模板.csv`，至少 20-50 行。
2. 导出 5-7 张脱敏图，命名为 `P03_Fig1` 至 `P03_Fig7`。
3. 补 15-25 篇参考文献，优先 SAR ship detection、SAR-AIS fusion、AIS anomaly detection、dark vessel detection。
4. 把所有文献写进 `05_文献与参考/references_checked_20260524.bib`。
5. 将 Methods 中所有工程系统描述改成可复现实验流程。

## 审稿风险

Remote Sensing 会重视数据、方法复现和图件质量。当前最大风险是：初稿看起来像系统应用报告，而不是方法论文。解决方式是把贡献重新压成一句话：

本文提出一种 SAR 船舶检测与 AIS 轨迹重建的时空证据融合框架，用于在海上应急态势感知中发现 non-cooperative vessel candidates，并通过脱敏案例和最小统计实验验证其可用性。
