# 文献雷达补充摘要

**论文主题**：Spatiotemporal Evidence Fusion of SAR Ship Detections and AIS Tracks for Dark Vessel Discovery in Maritime Emergency Awareness: A Taiwan Strait Case Study

**期刊目标**：*Remote Sensing* (MDPI, ISSN 2072-4292)

**搜集区间**：2020-2026（经典CFAR文献可更早）

**文献总数**：54 篇（含6篇核实重点文献；各主题6-8篇，台湾海峡/中国近海专题6篇）

---

## 主题 1：SAR 船舶检测（CFAR + 深度学习）

### `Li2022_DLSARReview`
**Li J. et al., Remote Sensing, 2022, 14(11):2712**  
综述177篇SAR船舶检测论文，系统对比CFAR与深度学习（单阶段、双阶段、Anchor-free等）方法的精度与速度，揭示AP50从2017年78.8%提升至2022年97.8%。  
**预期论文位置**：Introduction 综述引言 + Related Work 概述

### `Li2023_RealtimeSARReview`
**Li J. et al., IEEE JSTARS, 2023**  
系统综述70篇实时SAR船舶检测论文，聚焦剪枝、量化、知识蒸馏、轻量网络等模型加速策略。  
**预期论文位置**：Related Work

### `ElDarymli2024_DeepvsKCFAR`
**El-Darymli K. et al., IGARSS 2024**  
首次直接定量比较K-CFAR/SUMO与xView3冠军深度学习模型在Sentinel-1 Gulf of Guinea图像上的性能，1stDLM/xView3优于K-CFAR。  
**预期论文位置**：Method（CFAR vs 深度学习基准对比）

### `Zeng2024_CFARDPFusion`
**Zeng T. et al., IEEE JSTARS, 2024**  
提出CFAR引导双极化融合框架CFAR-DP-FW，在大场景SAR数据集上近岸小船mAP提升3.28%。  
**预期论文位置**：Method（SAR检测模块参考）

### `Wang2024_CFARRangeCompressed`
**Wang C. et al., IEEE TGRS, 2024**  
首次针对距离压缩SAR数据设计广义Gamma分布海杂波模型及CFAR检测器，在Sentinel-1和ERS-2上验证。  
**预期论文位置**：Method（CFAR实现细节）

### `Xu2021_OnboardHISEA`
**Xu P. et al., Remote Sensing, 2021, 13(10):1995**  
HISEA-1卫星在轨CFAR+YOLOv4联合检测方案，精度85.9%，处理时间约为传统方法一半。  
**预期论文位置**：Related Work

### `WangYOLOSD2022`
**Wang S. et al., Remote Sensing, 2022, 14(20):5268**  
YOLO-SD模型在HRSID和LS-SSDD-v1.0上优于YOLOX基线，多尺度卷积+特征变换模块提升小船检测。  
**预期论文位置**：Related Work

### `Alexandre2024_CbandReview`
**Alexandre C. et al., IEEE JSTARS, 2024**  
系统综述2015-2022年C波段SAR船舶检测，分析CFAR极化法向深度学习迁移趋势及计算资源局限性。  
**预期论文位置**：Introduction + Related Work

### `Zhang2020_LSSSDD`
**Zhang T. et al., Remote Sensing, 2020, 12(18):2997**  
发布大场景Sentinel-1 SAR小船检测基准数据集LS-SSDD-v1.0，专门应对大场景小目标挑战。  
**预期论文位置**：Related Work（数据集参考）

---

## 主题 2：SAR-AIS 数据融合 / 关联

### `Pelich2019_Sentinel1AIS` ⭐ 必须验证核心文献
**Pelich R. et al., Remote Sensing, 2019, 11(9):1078 — DOI: 10.3390/RS11091078 ✓已核实**  
提出基于Sentinel-1双极化复相干性的大规模自动船舶监测算法，与AIS交叉对比评估检测率（>60m船舶>80%），首次大规模量化SAR暗船现象。  
**预期论文位置**：Introduction + Method（核心基准）

### `Rodger2021_ClassAidedFusion`
**Rodger M. & Guida R., Remote Sensing, 2021, 13(1):104**  
分类辅助SAR-AIS数据融合框架，解决密集航运环境中数据关联错误问题，结合CNN识别提升关联正确率。  
**预期论文位置**：Method（融合算法设计参考）

### `Galdelli2021_SynergicAIS`
**Galdelli A. et al., Sensors, 2021, 21(8):2756**  
Sentinel-1+AIS点对点与点对线两种关联策略，识别管理区附近AIS数据缺口疑似行为，亚得里亚海案例研究。  
**预期论文位置**：Method（AIS缺口识别逻辑）

### `Song2020_AISInterpolation`
**Song J. & Kim D.J., IGARSS 2020**  
针对SAR获取时刻对AIS离散数据内插并校正多普勒频移，显著提升自动标注训练数据质量。  
**预期论文位置**：Method（AIS内插校正模块）

### `Chen2025_SVIADF`
**Chen L. et al., Remote Sensing, 2025, 17(5):868**  
YOLOv8x+CA-CFAR双阶段多源信息融合框架（SVIADF），结合SAR-AIS融合数据，解决小目标检测与SAR-光学跨域迁移。  
**预期论文位置**：Method

### `Wong2022_GlobalLongline`
**Wong B. et al., Scientific Reports, 2022, 12:21004**  
全球大洋SAR-AIS匹配揭示约35%延绳钓渔船为非广播型暗船，提供SAR检测与AIS匹配的大尺度方法论。  
**预期论文位置**：Introduction + Discussion

### `Lv2021_AISOffset`
**Lv Y. et al., IET Conference 2021**  
利用AIS连续轨迹计算径向速度，校正运动舰船在SAR图像中的方位偏移，提升SAR-AIS空间对准精度。  
**预期论文位置**：Method（时空对准模块）

---

## 主题 3：暗船 / 非合作船舶检测

### `Paolo2024_Nature` ⭐ 必须验证核心文献
**Paolo F.S. et al., Nature, 2024, 625(7993):85-91 — DOI: 10.1038/s41586-023-06825-8 ✓已核实**  
完整作者：Fernando S. Paolo, David Kroodsma, Jennifer Raynor, Timothy Hochberg, Pete Davis, Jesse Cleary, Luca Marsaglia, Sara Orofino, Christian Thomas, Patrick N. Halpin。分析2 PB卫星图像+530亿条船舶GPS，揭示72-76%工业渔船不在公开追踪系统内。  
**预期论文位置**：Introduction（暗船问题核心引文）+ Discussion

### `Li2025_DarkShipOSAR` ⭐ 必须验证核心文献
**Li F. et al., Remote Sensing, 2025, 17(13):2201 — DOI: 10.3390/rs17132201 ✓已核实**  
作者：Fan Li, Kun Yu, Chao Yuan, Yichen Tian, Guang Yang, Kai Yin, Youguang Li。高分六号（光学）+高分三号B（SAR）协同，YOLOv11n-OBB+JVC全局优化，关联精度91.74%（光学）、91.33%（SAR）。  
**预期论文位置**：Introduction + Related Work（高度相关方法）

### `Paolo2022_xView3` ⭐ 必须验证核心文献
**Paolo F. et al., NeurIPS 2022 Datasets and Benchmarks Track — DOI: 10.48550/arXiv.2206.00897 ✓已核实**  
完整作者：Fernando Paolo, Tsu-ting Tim Lin, Ritwik Gupta, Bryce Goodman, Nirav Patel, Daniel Kuster, David Kroodsma, Jared Dunnmon。发布近1000景Sentinel-1标注数据集及xView3挑战赛，专注暗渔船检测。  
**预期论文位置**：Related Work（数据集基准）

### `Caricchio2024_YOLOv8Noncoop`
**Caricchio C. et al., IEEE GRSL, 2024**  
YOLOv8+SAHI非合作船舶检测，mAP@0.5: 94.3%，recall: 95.6%，演示暗船检测作战辅助决策应用。  
**预期论文位置**：Related Work

### `Rodger2023_MauritiusDark`
**Rodger M. & Guida R., IGARSS 2023**  
毛里求斯EEZ多时相SAR+AIS识别暗船，AI辅助决策支持渔业监管，Nereus项目案例研究。  
**预期论文位置**：Related Work（暗船应用场景对比）

### `Kroodsma2022_HotSpots`
**Kroodsma D. et al., Science Advances, 2022, 8(44):eabq2109**  
全球AIS关闭热点数据集，渔业中约6%（>490万小时）活动被主动隐匿，高密度区位于亚洲及西非。  
**预期论文位置**：Introduction + Discussion

### `Wong2020_NorthKorea`
**Wong B. et al., Science Advances, 2020, 6(30):eabb1197**  
四星多源（SAR+AIS+光学+夜光）揭示朝鲜水域中国暗渔船非法作业，>900艘（2017年），具有台湾海峡/东北亚对比研究价值。  
**预期论文位置**：Introduction + Discussion

---

## 主题 4：AIS 轨迹清洗与异常检测

### `dAfflisio2021_Spoofing`
**d'Afflisio E. et al., IEEE TAES, 2021, 57(4):2406-2422**  
分段均值回归过程建模AIS轨迹，基于GLRT与模型阶次选择检测AIS欺骗与隐身偏差，多假设检验框架。  
**预期论文位置**：Related Work（AIS欺骗检测背景）

### `Nurfalah2023_AISAR_Assoc`
**Nurfalah A. et al., ICISS 2023**  
AIS/雷达轨迹关联实时异常检测，可识别位置欺骗、AIS会合行为、MMSI重复、AIS开关等多类异常。  
**预期论文位置**：Method（AIS数据校验模块）

### `Guo2021_KinematicInterp`
**Guo S. et al., Journal of Marine Science and Engineering, 2021, 9(6):609**  
三步骤AIS轨迹异常检测法（预处理→运动学估计→误差聚类），迭代识别异常数据，真实AIS案例验证。  
**预期论文位置**：Method（AIS数据清洗流程）

### `Xie2023_GMVAE`
**Xie L. et al., IEEE TVT, 2023, 72(11):14858-14870**  
GMVAE高维隐空间学习多类别船舶轨迹特征，DTW度量重建误差判断异常，检测率91.26%，误报率0.68%。  
**预期论文位置**：Related Work（轨迹异常检测参考）

### `Zheng2020_TrajectoryRecon`
**Zheng H. et al., Mathematical Problems in Engineering, 2020:7191296**  
集成方法从含噪声AIS数据重建高精度船舶轨迹，多传感器数据质量控制与预测结合。  
**预期论文位置**：Method（AIS数据预处理参考）

### `Song2024_AISIdentity`
**Song X. et al., Sensors, 2024, 24(8):2443**  
AIS与吉林一号遥感图像融合，基于位置特征点集匹配与属性特征模糊综合决策的异常目标识别与定位校正。  
**预期论文位置**：Method（SAR-AIS时空对准参考）

### `Bernabe2023_IntentionalAIS`
**Bernabé P. et al., IEEE TITS, 2023**  
自监督深度学习在1年挪威卫星AIS实测数据（>6万艘船）上检测故意关闭AIS行为，精度验证。  
**预期论文位置**：Related Work（AIS意图关闭检测背景）

---

## 主题 5：海上态势感知 / 应急遥感

### `Morando2023_MultiSensorFusion`
**Morando E. et al., IGARSS 2023**  
多星SAR+光学+AIS+RF电磁信号融合工具，提升对海上目标位置和行为的综合感知能力。  
**预期论文位置**：Introduction（MDA框架背景）

### `Nereus2023_FisheriesAnom`
**Guida R. et al., IGARSS 2023**  
Nereus卫星系统（SAR+AIS+VMS）毛里求斯EEZ应用，AI辅助渔业监控与暗船检测决策。  
**预期论文位置**：Related Work（系统参考架构）

### `Farias2024_HybridSurveillance`
**Farias C.M. et al., Sensors, 2024, 24(17):5623**  
基于JDL分级框架，融合AIS行为模型与专家规则的五级四类别违法活动分类检测系统。  
**预期论文位置**：Discussion（综合预警框架参考）

### `Mdakane2022_SentinelAfrica`
**Mdakane L., ISPRS Archives, 2022, XLIII-B3:301-308**  
Sentinel-1在OCIMS南非运营海洋监控服务中的应用，探讨商业与开放数据混合获取方案。  
**预期论文位置**：Related Work

### `Kim2025_DarkVesselRT`
**Kim D.J. et al., OCEANS 2025**  
SAR卫星+AI实时暗船检测系统，面向海上安全态势感知运营场景验证。  
**预期论文位置**：Related Work

### `Farthing2023_ShiftingIdentities`
**Farthing C.M. et al., Science Advances, 2023, 9(3):eabp8200**  
十年GPS数据追踪全球渔船换旗与身份切换模式，约17%公海捕鱼为外国所有船，身份伪装与暗船问题关联分析。  
**预期论文位置**：Discussion

---

## 主题 6：方法基础与领域综述

### `Rohling1983_CFAR` ⭐ 必须验证核心文献（经典）
**Rohling H., IEEE TAES, 1983, 19(4):608-621 — DOI: 10.1109/TAES.1983.309350 ✓已核实**  
经典OS-CFAR（排序统计CFAR）算法论文，在杂波与多目标情况下自适应设定雷达检测门限，SAR船舶检测CFAR方法的必引奠基之作。  
**预期论文位置**：Method（CFAR算法依据）

### `Graziano2019_WakeHeading` ⭐ 需要进一步核实
**Graziano M.D. et al., Remote Sensing, 2019, 11(18):2196 — DOI: 10.3390/rs11182196**  
⚠️ DOI解析暂时失败（页面返回404）。基于Radon变换和尾迹分量检测的船舶航向与速度估计算法，用于辅助暗船运动状态估计。2016年Acta Astronautica DOI: 10.1016/J.ACTAASTRO.2016.07.001已验证（同组研究早期版本）。  
**预期论文位置**：Method  
`note = {Unverified - skip if cannot confirm}`

### `Santamaria2017_MassProcessing`
**Santamaria C. et al., Remote Sensing, 2017, 9(7):678**  
处理11500景Sentinel-1图像实现地中海大规模海上监控，建立SAR与AIS交叉验证系统化框架。  
**预期论文位置**：Related Work（大规模处理参考）

### `DelPrete2021_WakeDL`
**Del Prete R. et al., Remote Sensing, 2021, 13(22):4573**  
首次CNN纯数据驱动船舶尾迹检测（无先验船位信息），发布250+尾迹芯片数据集，Sentinel-1高流量区验证。  
**预期论文位置**：Related Work

### `Yasir2022_SARReview`
**Yasir M. et al., Soft Computing, 2022**  
深度学习SAR船舶检测系统性综述，覆盖数据集构建、算法对比、性能评估的全链路分析。  
**预期论文位置**：Related Work

### `Heiselberg2023_ShipVelocity`
**Heiselberg H. et al., Remote Sensing of Environment, 2023, 290:113492**  
多任务深度学习同时估计SAR图像中船舶速度矢量，辅助运动学信息提取用于暗船轨迹重建。  
**预期论文位置**：Method（运动参数辅助参考）

### `Yasir2023_YOLOv5SAR`
**Yasir M. et al., Frontiers in Marine Science, 2023, 9:1086140**  
改进YOLOv5实现GF-3 SAR图像多尺度船舶检测，提供中国国产SAR数据深度学习检测参考。  
**预期论文位置**：Related Work

---

## 台湾海峡 / 中国近海地域相关文献

### `Pu2023_TaiwanStraitAIS` ⭐ 核心地域文献
**Pu T., Int. J. Data Warehousing and Mining, 2023 — DOI: 10.4018/ijdwm.332864**  
利用2020年南海卫星AIS数据挖掘与可视化分析，明确指出台湾海峡南部过往船舶数量显著增加，是与本文研究区域最直接相关的参考文献。  
**预期论文位置**：Introduction（台湾海峡地域背景）+ Discussion

### `Cao2021_SCS_Fishing` ⭐ 核心地域文献
**Cao C. et al., Remote Sensing, 2021, 13(10):1952**  
1.5亿AIS轨迹点识别南海北部渔船类型（拖网/流刺网/围网），分析2018年不同季节空间分布特征。  
**预期论文位置**：Discussion（南海渔船监管背景）

### `Wang2025_SCS_VIIRS` ⭐ 核心地域文献
**Wang D. et al., Remote Sensing, 2025, 17(17):2967**  
改进2D-CFAR+形态学分析检测VIIRS夜光渔船（2013-2022），揭示南海禁渔期及非法捕鱼规律，涵盖海南至广东沿岸热点区域。  
**预期论文位置**：Introduction（南海渔船监管现状）+ Discussion

### `Lee2024_SAR_AIS_Korea` ⭐ 核心地域文献
**Lee Y.K. et al., Ocean Science Journal, 2024 — DOI: 10.1007/s12601-024-00153-2**  
SAR图像+AIS/V-Pass数据整合的东亚近岸海域船舶检测与跟踪评估，地理上覆盖东亚（含黄海/东海）。  
**预期论文位置**：Method + Discussion（东亚邻近案例）

### `WangFen2025_BeiDou_ECS` ⭐ 核心地域文献
**Wang F. et al., Journal of Marine Science and Engineering, 2025, 13(5):905**  
北斗VMS大数据+CNN-BiLSTM东海黄海渔船捕鱼热点分析，与夏季禁渔政策效果关联，揭示近岸违规捕鱼集中于浙江海域。  
**预期论文位置**：Discussion（中国近海监管政策背景）

### `ChangSARAIS2024_OilTrack` ⭐ 台湾研究团队
**Chang L. et al., SPIE RS 2024 — DOI: 10.1117/12.3027230**  
台湾团队研究，SAR+AIS追踪疑似排油船舶，改进U-Net检测油膜并通过AIS数据关联违规船只，是与本文研究区域与方法最接近的台湾本地研究。  
**预期论文位置**：Related Work + Discussion（地域最相关）

---

## 补充核心文献（方法辅助）

### `MaGF32018_CNN`
**Ma M. et al., Remote Sensing, 2018, 10(12):2043**  
首次系统利用GF-3 SAR图像开展CNN船舶分类与检测（8类），发布GF-3专有数据集，中国SAR船舶检测开山之作。  
**预期论文位置**：Related Work

### `An2018_GF3CFAR`
**An Q. et al., Sensors, 2018, 18(2):334**  
FCN海陆分割+CFAR+CNN三阶段GF-3暗船检测流水线，可与本文Sentinel-1 CFAR方法形成对比参考。  
**预期论文位置**：Method（CFAR实现对比参考）

### `Belenguer2025_YOLOv8AIS`
**Belenguer-Plomer M.A. et al., SPIE RS 2025**  
Embed2Scale项目Sentinel-1+AIS大规模数据集（2020-2024年美国12主要港口2008景图像）及YOLOv8评估。  
**预期论文位置**：Method（数据集构建参考）

### `Kerekes2024_CircleNet`
**Kerekes D. & Nascetti A., IGARSS 2024**  
xView3 CircleNet多时相扩展，有效过滤静止目标误检，暗渔船检测精度提升。  
**预期论文位置**：Related Work

### `Zhao2023_STYOLOA`
**Zhao K. et al., Frontiers in Neurorobotics, 2023, 17:1170163**  
Swin Transformer+坐标注意力ST-YOLOA，复杂背景下SAR检测精度超越YOLOX。  
**预期论文位置**：Related Work

---

## 核实状态总结

| 文献编号 | 核实结果 |
|---------|---------|
| Paolo F.S. et al., Nature 625:85-91 (2024) | ✅ 已核实，完整作者：Paolo, Kroodsma, Raynor, Hochberg, Davis, Cleary, Marsaglia, Orofino, Thomas, Halpin |
| xView3-SAR, NeurIPS 2022 | ✅ 已核实，DOI: 10.48550/arXiv.2206.00897，作者：Paolo, Lin, Gupta, Goodman, Patel, Kuster, Kroodsma, Dunnmon |
| Pelich R. et al., RS 11:1078 (2019) | ✅ 已核实，DOI: 10.3390/RS11091078 |
| Remote Sensing 2025, 17(13):2201 | ✅ 已核实，作者：Fan Li et al.，完整标题：Dark Ship Detection via Optical and SAR Collaboration... |
| Rohling H., IEEE TAES AES-19(4):608-621 (1983) | ✅ 已核实，DOI: 10.1109/TAES.1983.309350 |
| Graziano M.D. et al., RS 11:2196 (2019) | ⚠️ DOI 10.3390/rs11182196 解析失败；2016年早期版本（Acta Astronautica）已核实 |
