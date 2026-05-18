# Spatiotemporal Evidence Fusion of SAR Ship Detections and AIS Tracks for Dark Vessel Discovery in Maritime Emergency Awareness: A Taiwan Strait Case Study

**Target journal:** *Remote Sensing* (MDPI, ISSN 2072-4292)
**Article type:** Article
**Draft version:** v3 author-profile and style update, 2026-05-18
**Authors:** Banghui Yang^1,2, Wei Tian^1\*, Junna Yuan^1, [Jimei University collaborator]^3
**Affiliations:** ^1 National Engineering Research Center for Geomatics, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing 100101, China; ^2 University of Chinese Academy of Sciences, Beijing 100049, China; ^3 Navigation College, Jimei University, Xiamen, China
**Contact:** \*Wei Tian, tianwei@aircas.ac.cn, ORCID: https://orcid.org/0000-0002-2024-4200

**Authorship note for final confirmation:** This v3 file implements the working decision that Banghui Yang is the first author and Wei Tian is the corresponding author. If Banghui Yang should also be listed as co-corresponding author, add `\*Banghui Yang, yangbh@aircas.ac.cn` before final MDPI submission.

---

## Highlights

- A six-stage spatiotemporal evidence-fusion framework converts independent SAR ship detections and cooperative AIS tracks into a five-class emergency evidence chain (matched, dark-vessel candidate, AIS-only, identity mismatch, geofence violation).
- A dedicated scene-time AIS reconstruction module aligns cleaned per-MMSI tracks to the satellite acquisition instant within a ±5 min temporal window, with bounded constant-velocity extrapolation.
- An adaptive-gate matching cost combines geolocation distance, AIS time-offset speed budget, track quality, and SAR–AIS size consistency, solved as a globally-optimal Hungarian assignment with explicit ambiguity rules.
- Over 50 controlled Taiwan-Strait scenes, the framework attains mean F1 = 0.857 for SAR detection, dark-vessel recall = 0.93, identity-mismatch recall = 0.69, and 3.5 s per 15 km × 15 km patch on a single CPU core (well within the 60 min/scene operational budget).
- An operational validation layer is grounded in 202 third-party functional test cases (100 % requirement coverage, all detected issues regression-passed) on a deployed maritime emergency platform with 232 GF-3 and 6044 Sentinel-1 SAR scenes archived over the Fujian–Taiwan corridor.

## Abstract

Non-cooperative vessel activity is a persistent challenge for maritime search-and-rescue, emergency response, environmental protection and law-enforcement awareness. Synthetic Aperture Radar (SAR) provides day-night, all-weather independent observations of sea-surface targets, while the Automatic Identification System (AIS) offers high-frequency cooperative identity and trajectory information. Neither source alone is sufficient: SAR detections lack identity context and AIS misses non-reporting vessels. Following the applied SAR system style used in recent marine-emergency work by the author team, we propose an operational spatiotemporal evidence-fusion framework that converts independent SAR detections and cooperative AIS tracks into a five-class emergency evidence chain comprising **matched cooperative vessels**, **dark-vessel candidates**, **AIS-only targets**, **identity-mismatch warnings**, and **geofence violations**. The framework consists of six modules: SAR preprocessing and sea-land masking; Cell-Averaging Constant False-Alarm-Rate (CA-CFAR) detection with connected-component analysis; AIS decoding and per-MMSI track reconstruction; AIS scene-time interpolation with a ±5 min window and bounded extrapolation; adaptive-gate SAR–AIS association solved as a global Hungarian assignment with explicit one-to-many ambiguity rules; and rule-based emergency evidence generation. A controlled simulation over 50 Taiwan-Strait scenes calibrated against a deployed maritime emergency platform demonstrates a mean SAR ship-detection F1 of 0.857 (P = 0.819, R = 0.911), dark-vessel recall of 0.93, identity-mismatch recall of 0.69, and a mean processing time of 3.5 ± 0.3 s per 15 km × 15 km patch on a single CPU core. The proposed framework is independently grounded in a 232-scene GF-3 / 6044-scene Sentinel-1 / 1300-scene Sentinel-2 maritime data inventory and validated by a 202-case third-party functional evaluation with 100 % requirement coverage and full regression closure. To our knowledge, this is the first published SAR–AIS fusion study that simultaneously (i) treats matched, dark, AIS-only, identity-inconsistent and geofence-violating vessels as one rule-transparent evidence taxonomy; (ii) couples physical adaptive gating with global Hungarian assignment and explicit ambiguity tagging; and (iii) co-positions itself for both research reproducibility (open simulation pipeline) and operational deployment (third-party functional evidence). The framework is directly transferable to other regional maritime emergency systems.

**Keywords:** SAR; AIS; dark vessel; ship detection; identity mismatch; geofence; maritime emergency; evidence fusion; data assimilation; Taiwan Strait; GF-3; Sentinel-1

---

## 1. Introduction

Maritime emergency awareness — search and rescue (SAR), oil-spill response, illegal-activity monitoring and regional maritime security — depends on the ability to integrate independent remote-sensing observations, cooperative vessel self-reporting, and geospatial decision overlays into a single, defensible operational picture [@Farthing2023; @Farias2024; @Morando2023]. Decision-makers need to know not only where a vessel is, but also whether its identity, behaviour and reported trajectory are consistent with independent observations; and they need this knowledge fast enough for the result to influence an actionable response.

The Automatic Identification System (AIS) is the most widely used operational source of vessel identity and trajectory information, providing MMSI, ship name, type, dimensions, position, speed-over-ground, course-over-ground, heading and timestamps under ITU-R M.1371 [@imo_ais]. Yet AIS is a cooperative system. Vessels may be absent from AIS through equipment failure, reception gaps, deliberate deactivation, identity spoofing, late or out-of-order messages, or non-carriage by smaller vessels [@dAfflisio2021; @Xie2023]. These limitations are most consequential precisely when situational awareness matters most.

Spaceborne SAR provides an independent, day-night, weather-resilient observation of sea-surface targets [@Alexandre2024_CbandReview; @Li2022_DLSARReview]. Sentinel-1, GF-3 and similar C-band SARs deliver repeated wide-area coverage of busy maritime corridors. However, raw SAR detections lack identity context. They report position, backscatter, geometry and approximate size; they cannot directly distinguish a cooperatively-broadcasting vessel from a non-cooperative one. Cross-comparison with AIS is therefore required before SAR detections can support emergency reasoning [@Pelich2019_Sentinel1AIS; @Rodger2021_ClassAidedFusion; @Galdelli2021_SynergicAIS].

A growing literature exploits SAR–AIS pairing for global mapping of non-publicly-tracked activity [@paolo2024satellite; @xview3sar2022]. These studies have established the *scientific value* of dark-vessel discovery from satellites. The remaining challenge — and the one this paper targets — is the *operational engineering* of dark-vessel evidence into a decision product: an evidence chain that an emergency operator can audit, calibrate, and act on in a regional theatre, integrating geofences and identity checks alongside SAR–AIS matching.

The central scientific and operational problem is therefore not ship detection or AIS visualisation in isolation. It is *spatiotemporal evidence fusion under uncertainty*: aligning the satellite acquisition instant, SAR target geometry, AIS interpolated tracks, vessel static attributes and emergency geofences into a coherent decision chain. This problem is particularly acute in high-traffic, complex-coast settings such as the Taiwan Strait, where vessel density, coastline geometry, island clutter, variable sea state and multi-source data quality all compound association uncertainty [@Pu2023_TaiwanStrait; @Chang_SARAIS_Taiwan].

### 1.1 Problem statement

Given (i) a set of SAR ship detections \(D = \{d_i = (p_i, t_s, f_i, c_i)\}_{i=1}^{N_D}\) at the satellite acquisition time \(t_s\); (ii) a set of cooperative AIS message streams \(A_v = \{a_{v,k}\}\) per vessel; (iii) a vessel static-attribute database; and (iv) one or more emergency geofence polygons \(G\); we wish to produce an *evidence chain* assigning each detection \(d_i\) and each AIS-derived candidate \(\hat{a}_j\) to exactly one of five operational classes:

1. **Matched cooperative vessel** — SAR detection and AIS candidate consistent in space, time, and (where available) static attributes;
2. **Dark-vessel candidate** — SAR detection without a plausible AIS counterpart at \(t_s\);
3. **AIS-only target** — AIS candidate inside the SAR footprint with no matching detection;
4. **Identity mismatch** — matched pair whose attributes (e.g. length) are inconsistent;
5. **Geofence violation** — any of the above within a defined emergency area of interest.

Each class must be accompanied by a calibrated uncertainty (an *ambiguity flag* when the second-best match is too close to the best) so that an operator can prioritise manual review.

### 1.2 Contributions

This paper makes four contributions.

1. **A six-stage spatiotemporal evidence-fusion framework (Sections 3–4).** Building on the operational vessel-monitoring service of a Jimei-University-led maritime emergency platform, we formalise an end-to-end procedure from SAR/AIS inputs to a five-class evidence taxonomy. The framework couples physically-grounded matching (adaptive search radius driven by AIS time offset, geolocation uncertainty and SAR localisation uncertainty) with globally-optimal assignment (Hungarian) and explicit one-to-many ambiguity rules.

2. **An AIS scene-time reconstruction module (Section 3.5).** We formalise the AIS branch: ITU-R M.1371-compliant decoding, MMSI / coordinate / speed sanity checks, per-MMSI track building, anomalous-jump removal, scene-time linear interpolation inside a configurable \(\pm 5\) min window, and bounded constant-velocity extrapolation (\(\le 60\) s). This addresses the inevitable AIS–SAR temporal mis-registration in operational settings.

3. **An identity-and-geofence layer (Section 3.7).** Beyond classical SAR–AIS matching, we add (a) a SAR-length-vs-AIS-length consistency test that flags identity-mismatch even on successfully-matched pairs (Type-V spoofing or transposed MMSI), and (b) a polygon-based geofence overlay that elevates *any* target — matched, dark, or AIS-only — to a geofence-violation alert when inside a defined emergency area of interest. This positions the framework as an emergency *evidence* product, not just a detector.

4. **A reproducible validation pathway with operational anchoring (Sections 5–6).** We propose a two-layer validation strategy that is realistic for engineering-derived manuscripts: a *controlled simulation* (50 scenes, ground-truth-labelled, fully reproducible from this repository) gives detection/association metrics; and an *independent third-party functional test* (202 test cases, 100 % requirement coverage, all detected issues regression-closed) anchors operational deployability. The associated data inventory comprises 232 GF-3 SAR scenes, 6044 Sentinel-1 SAR scenes, 1300 Sentinel-2 and 1067 Landsat-8/9 optical scenes, and 653 GF-1/2/6/7 high-resolution optical scenes archived over the Fujian–Taiwan corridor.

### 1.3 Why *Remote Sensing*?

The work is positioned for *Remote Sensing* (MDPI) because it sits squarely at the intersection of the journal's published interests in (a) ocean remote sensing and SAR maritime applications, (b) operational data-fusion methods, and (c) regional case studies that demonstrate transferability. Compared to dark-vessel benchmarks [@xview3sar2022; @Li2025_OpticalSARDark] and global activity mapping [@paolo2024satellite], the present work prioritises rule-transparent operational evidence over headline detection accuracy, and explicitly addresses identity and geofence reasoning that downstream emergency systems require.

The rest of the paper is organised as follows. Section 2 reviews related work in SAR ship detection, AIS analytics, SAR–AIS fusion and operational maritime awareness. Section 3 details the proposed framework. Section 4 describes the validation strategy. Section 5 presents quantitative results from 50 simulated Taiwan-Strait scenes and the third-party functional evaluation. Section 6 discusses limitations, identity and geofence semantics, and operational implications. Section 7 concludes.

---

## 2. Related Work

### 2.1 SAR ship detection

SAR ship detection has progressed from classical CFAR detectors [@rohling1983cfar; @Wang2024_CFARRangeCompressed] through CFAR-with-polarimetry hybrids [@Zeng2024_CFARDPFusion] to modern deep learning [@Li2022_DLSARReview; @Li2023_RealtimeSARReview; @WangYOLOSD2022]. Cell-Averaging CFAR (CA-CFAR) remains attractive in operational systems because it is interpretable, requires no large labelled training set, adapts to local clutter, and is straightforward to certify. Recent comparative work confirms that deep-learning detectors outperform classical CFAR/SUMO baselines on free-data benchmarks such as xView3, but with substantially higher computational and data-curation cost [@ElDarymli2024_DeepvsKCFAR]. On-board CFAR + YOLO hybrids [@Xu2021_OnboardHISEA] have demonstrated near-real-time satellite detection. Dataset benchmarks (HRSID, LS-SSDD-v1.0, SAR-Ship-Dataset) [@Zhang2020_LSSSDD] have accelerated the field by exposing the small-target and dense-traffic problems that dominate operational deployment.

In the present work we deliberately use CA-CFAR. Our innovation does not aim to advance the detector itself; rather, our contribution is to make CFAR detections *interpretable* in an evidence chain. This positions the work parallel to the deep-learning literature: a more accurate detector could be substituted for the CFAR stage without altering the rest of the framework.

### 2.2 AIS analytics and dark-vessel awareness

AIS analytics range from per-vessel track reconstruction to anomaly and intent inference [@Riveiro2018_review; @Xie2023]. AIS spoofing and identity manipulation are now documented operationally [@dAfflisio2021; @Singh_AIS_spoofing]. Trajectory cleaning techniques [@Guo2021] address the AIS data-quality problem that any operational SAR–AIS pipeline must solve. Recent dark-vessel work [@paolo2024satellite] uses SAR detections relative to broadcast AIS to map non-publicly-tracked activity at global scale; complementary work [@Li2025_OpticalSARDark] uses optical–SAR collaboration for dark-ship identification. Our framework draws on this AIS-anomaly literature by treating identity-mismatch and AIS gap-related dark-vessel candidates as *first-class evidence types* rather than as derivatives of a detection.

### 2.3 SAR–AIS association

SAR–AIS association is the bridge between independent remote-sensing detections and self-reported maritime traffic. Pelich et al. demonstrated large-scale automated vessel monitoring with dual-polarisation Sentinel-1 cross-checked against AIS at >80 % detection for vessels >60 m [@Pelich2019_Sentinel1AIS]. Classification-aided fusion has improved data-association in dense traffic [@Rodger2021_ClassAidedFusion]; synergic Sentinel-1+AIS point-to-track strategies have been demonstrated in the Adriatic [@Galdelli2021_SynergicAIS]; AIS scene-time interpolation correction has been investigated specifically against Sentinel-1 [@Song2020_AISInterpolation]. We extend this literature in three ways: (i) we make the search radius adaptive to AIS time offset, vessel speed, and explicit geolocation/SAR uncertainty terms; (ii) we replace nearest-neighbour assignment with globally-optimal Hungarian assignment and explicit ambiguity tagging; and (iii) we extend the output beyond a binary "matched / dark" decision to a five-class evidence taxonomy.

### 2.4 Operational maritime awareness

Operational SAR-based maritime services such as Copernicus Marine Service ship-detection products and various national maritime-domain-awareness platforms have demonstrated the feasibility of routine SAR-AIS-fused vessel monitoring [@Farthing2023; @Morando2023]. Our framework is designed to fit this operational class: low-latency, interpretable, with explicit data-quality and ambiguity tags, and instrumented with a geofence layer that links remote-sensing observations to user-defined emergency areas of interest.

---

## 3. Materials and Methods

### 3.1 Study area and existing data assets

The study area is the Taiwan Strait and adjacent coastal waters of Fujian Province (China) and Taiwan Island (Figure 2). This region is appropriate for SAR–AIS evidence fusion research because it combines dense shipping activity, complex coastlines, island and nearshore clutter, and strategic maritime-emergency relevance.

The project has assembled a multi-source maritime remote-sensing archive that anchors this paper's data layer. The most relevant data assets are summarised in Table 1.

**Table 1.** Existing data assets supporting the SAR-AIS spatiotemporal evidence fusion framework over the Fujian–Taiwan corridor. Numbers from the project data-delivery inventory.

| Data type | Sensor / source | Time range | Delivered or archived volume | Role in this paper |
|---|---|---|---:|---|
| SAR | GF-3 (L2 GEC/GTC) | 2021–2023 | 232 scenes | Primary domestic SAR observation source |
| SAR | Sentinel-1 (IW GRD / SLC) | 2021– | 6 044 scenes | Public-source SAR supplement; repeat coverage |
| Optical | Sentinel-2 (MSI) | 2021– | 1 300 scenes | Background, optional optical cross-check |
| Optical | Landsat-8 / 9 (OLI/TIRS) | 2021– | 1 067 scenes | Background, context |
| Optical | GF-1 / 2 / 6 / 7 | 2021–2023 | 653 scenes (combined) | High-resolution context, qualitative |
| AIS dynamic | AIS receivers / files | Project-dependent | Existing platform inputs | Per-MMSI track reconstruction; \(t_s\) interpolation |
| AIS static | AIS Type-5 + vessel DB | Project-dependent | Static records keyed by MMSI | Identity-consistency check |
| Ship chips | SAR / optical chips DB | Generated by system | Existing chip library | Visual target review |
| GIS products | GeoTIFF / Shapefile / JPEG | Generated by system | Thematic products | Final emergency maps |

The relevance of each asset to the present manuscript is two-tier: GF-3 and Sentinel-1 SAR scenes form the *core observational layer*; optical imagery and ship-chip libraries form the *contextual layer*. AIS data provide the cooperative track layer; the static-attribute database provides the identity-consistency layer.

### 3.2 Overall framework

The proposed framework (Figure 1) contains six modules processed in three parallel branches that are merged in stage 5:

1. Multi-source data ingestion and quality control;
2. SAR preprocessing, sea-land masking, CA-CFAR detection, connected-component analysis (Section 3.3);
3. AIS decoding, MMSI / coordinate / speed sanity, per-MMSI track reconstruction (Section 3.4);
4. AIS scene-time interpolation with \(\pm 5\) min window and bounded extrapolation (Section 3.5);
5. SAR-AIS adaptive-gate association via Hungarian assignment with explicit ambiguity rules (Section 3.6);
6. Emergency evidence generation: matched / dark / AIS-only / identity-mismatch / geofence-violation tagging and product output (Section 3.7).

The framework is designed for *interpretability at every stage*: each module emits a structured intermediate product that an operator can inspect.

### 3.3 SAR preprocessing and ship detection

Input SAR data are *Level-2 geocoded* products (GEC/GTC) derived from L1 single-look complex (SLC) data through multi-look processing, adaptive Lee speckle filtering [@Lee_filter_classic], geometric correction and geocoding. The platform supports GF-3 multi-polarisation modes (single / dual / quad) and Sentinel-1 IW/EW (HH or VV single-pol; HH+HV or VV+VH dual-pol) [@esa_sentinel1]. In the present implementation, SAR scenes are processed in VV polarisation by default, which is best suited to ship detection over open water.

The processing pipeline is:

1. Read SAR image and metadata, including acquisition time, footprint, projection, resolution and polarisation.
2. Apply adaptive Lee speckle filtering based on the multiplicative noise model and MMSE criterion.
3. Apply a sea-land mask file to exclude land and nearshore non-water objects, with an 8-pixel (≈ 80 m at 10 m GSD) inward erosion to suppress the bright nearshore clutter band.
4. Detect ship candidates using a cell-averaging CFAR detector (Equations 1–3 below).
5. Apply connected-component analysis and target attribute extraction (centroid, area, bounding box, major/minor axis, orientation, approximate length and width proxies). Components outside plausible vessel size ranges (e.g. 4 ≤ pixels ≤ 5000 at 10 m GSD) are removed.
6. Generate scene-level satellite ship monitoring products and ship chips.

For the CA-CFAR detector, let \(x\) denote the intensity of a test cell and \(R\) the set of reference cells around it after excluding guard cells. The local clutter mean is

\[
\mu_R = \frac{1}{|R|}\sum_{r \in R} x_r, \tag{1}
\]

and the adaptive threshold is

\[
T = K\,\mu_R, \tag{2}
\]

where \(K\) is a threshold multiplier controlling the false-alarm rate. A cell is marked as a candidate if

\[
x > T. \tag{3}
\]

In this study we use a square 31×31-pixel reference window with a 7×7-pixel guard window and \(K = 6.5\) (Rayleigh-clutter Pfa ≈ 10\(^{-6}\) for the ≈ 660-cell reference). These parameters are reproducible defaults; the values originate from the platform software design specification, which mandates CA-CFAR but leaves \(L\) and \(K\) configurable.

The output of this branch is

\[
D = \{d_i = (p_i, t_s, f_i, c_i)\}_{i=1}^{N_D}, \tag{4}
\]

where \(p_i\) is the geospatial position, \(t_s\) is the satellite acquisition time, \(f_i\) is the extracted target feature vector (area, bbox, length-proxy, orientation), and \(c_i\) is the corresponding image chip record.

### 3.4 AIS decoding, cleaning, and per-MMSI track reconstruction

The AIS branch follows ITU-R M.1371. The platform AIS module decodes raw ASCII payloads, performs checksum verification, applies ASCII-to-6-bit conversion, and extracts static and dynamic attributes:

- **Dynamic** (Type 1/2/3): position (lat, lon), SOG, COG, heading, navigation status, rate-of-turn, UTC timestamp;
- **Static / voyage-related** (Type 5): MMSI, IMO, call sign, ship name, ship type, cargo type, ship dimensions.

Quality control consists of (i) MMSI validity (nine-digit numeric, leading digit non-zero); (ii) coordinate sanity (\(-90 \le \mathrm{lat} \le 90\), \(-180 \le \mathrm{lon} \le 180\)); (iii) drift-point removal via instantaneous-speed thresholding (samples implying \(v > 60\) kn are flagged as anomalous); (iv) sparse-track removal (vessels with fewer than three retained samples within the working window are discarded); (v) duplicate-timestamp removal.

For each surviving MMSI, the cleaned dynamic and static records are joined into a per-vessel track:

\[
A_v = \{ a_{v,k} = (p_{v,k}, t_{v,k}, s_{v,k}, \theta_{v,k}, m_v) \}_{k=1}^{N_v}, \tag{5}
\]

with \(m_v\) the static attribute record (only the most recent Type-5 record per MMSI is retained, as mandated by the platform design specification).

### 3.5 Scene-time interpolation

To make AIS and SAR comparable, each per-MMSI track is reconstructed at the SAR acquisition epoch \(t_s\). The platform design specifies a \(\pm 5\) min interpolation window; we adopt this as the bracketing window and add an explicit bounded extrapolation rule for tracks that almost-bracket \(t_s\) but miss by ≤ 60 s.

For a vessel \(v\) with \(t_{v,k} \le t_s \le t_{v,k+1}\):

\[
\hat{p}_v(t_s) = p_{v,k} + \frac{t_s - t_{v,k}}{t_{v,k+1} - t_{v,k}}\, (p_{v,k+1} - p_{v,k}). \tag{6}
\]

If no AIS sample brackets \(t_s\) but the nearest sample's \(\Delta t = t_s - t_{v,k}\) satisfies \(|\Delta t| \le 60\) s, we apply constant-velocity extrapolation:

\[
\hat{p}_v(t_s) = p_{v,k} + \Delta t \cdot \hat{u}(s_{v,k}, \theta_{v,k}), \tag{7}
\]

where \(\hat{u}\) is the local east–north displacement vector implied by SOG and COG. Beyond \(\pm 60\) s the candidate is dropped: AIS uncertainty grows non-linearly with time separation [@Song2020_AISInterpolation].

A *track-quality score* \(q_j \in [0, 1]\) is assigned to every interpolated candidate, computed as \(q_j = 1 - \delta t_j / 300\) for bracketed samples and \(q_j = 0.6 \cdot (1 - \delta t_j / 60)\) for extrapolated ones, where \(\delta t_j\) is the time gap to the nearest original AIS sample.

After interpolation, candidates are filtered by the SAR scene footprint, yielding the scene-time AIS candidate set

\[
A(t_s) = \{ \hat{a}_j = (\hat{p}_j(t_s), m_j, \delta t_j, q_j) \}_{j=1}^{N_A}. \tag{8}
\]

### 3.6 Adaptive-gate SAR–AIS association

For each candidate pair \((d_i, \hat{a}_j)\) we first compute an *adaptive search radius* that explicitly accounts for AIS time-offset speed budget and geolocation/SAR uncertainties:

\[
r_j = r_0 + \alpha\, |\delta t_j|\, s_j + \beta\, \sigma_{\text{geo}} + \gamma\, \sigma_{\text{SAR}}, \tag{9}
\]

with default \(r_0 = 200\) m, \(\alpha = 0.6\), \(\beta = 50\) m, \(\gamma = 80\) m and uncertainty units \(\sigma_{\text{geo}}\) and \(\sigma_{\text{SAR}}\) set to 1 by convention so that \(\beta, \gamma\) directly express the geolocation and SAR target localisation uncertainty budgets in metres. The pair is admissible iff \(\mathrm{dist}(p_i, \hat{p}_j(t_s)) \le r_j\).

For each admissible pair we compute a matching cost in [0, ≈2]:

\[
C_{ij} = w_d \frac{d(p_i,\hat{p}_j)}{r_j}
       + w_l\, \Delta_l(f_i, m_j)
       + w_q\, (1 - q_j), \tag{10}
\]

with default weights \(w_d = 1.0\), \(w_l = 0.5\), \(w_q = 0.3\), and \(\Delta_l = |\,L_{\text{SAR}} - L_{\text{AIS}}\,| / \max(L_{\text{AIS}}, 1)\) clipped to [0, 1]. When AIS length is missing, \(\Delta_l = 0.5\) by convention.

Two competing implementations were considered. (a) Nearest-neighbour with per-detection ambiguity, as in earlier SAR–AIS work; (b) globally-optimal bipartite assignment via the Hungarian algorithm [@Kuhn1955]. Hungarian assignment is optimal in dense-traffic scenes where a greedy choice produces locally-good but globally sub-optimal matches; we therefore adopt it. The cost matrix is padded with a large value where the gate fails so that the assignment naturally produces a partial matching. After assignment, we annotate every accepted pair with an *ambiguity flag* if the second-best admissible candidate is within margin \(\eta = 0.15\) of the best.

The result is summarised in five operational classes (Table 2).

**Table 2.** SAR-AIS evidence classes and their operational interpretation.

| Class | SAR detection | AIS candidate | Interpretation | Emergency product |
|---|---|---|---|---|
| Matched cooperative vessel | Present | Present, consistent | Normal cooperative target | Joint SAR-AIS vessel record |
| Dark-vessel candidate | Present | Absent within \(r_j\) | Non-cooperative vessel, AIS gap, or false SAR detection | Suspicious-threat layer + review list |
| AIS-only vessel | Absent | Present in footprint | Missed SAR detection, small vessel, timing gap, low backscatter | AIS-only review layer |
| Identity mismatch | Present | Present, inconsistent attributes (e.g. \(\Delta_l > 0.6\)) | Incorrect AIS identity, spoofing, transposed MMSI, association ambiguity | Identity-mismatch warning |
| Geofence violation | Present and/or AIS present | Inside defined emergency zone | Vessel within restricted or accident-related area | Electronic-fence alert |

### 3.7 Emergency evidence and product generation

The product layer assembles the assignment outputs and class labels into operator-facing products. We define a graded emergency-evidence score:

\[
R_i = w_1 I_{\text{dark}} + w_2 I_{\text{mismatch}} + w_3 I_{\text{geofence}} + w_4 I_{\text{lowAISq}} + w_5 I_{\text{ambig}}, \tag{11}
\]

with binary indicators and default weights \(w = (0.40, 0.25, 0.20, 0.10, 0.05)\). \(R_i\) is intended as a ranking score for review prioritisation, not as a calibrated risk metric; weights are configurable per deployment.

The framework emits the following GIS-ready products:

- *AIS-and-satellite joint monitoring product* (GeoJSON / Shapefile);
- *Satellite ship chip database* (PNG + attribute table per detection);
- *Suspicious-threat thematic map* (SAR base + matched/unmatched markers);
- *Identity-mismatch warning table*;
- *Electronic-fence abnormal-vessel layer*;
- *Operator-display GeoTIFF / Shapefile / JPEG bundle*.

---

## 4. Validation strategy

Validation is organised in three layers, designed to be defensible to *Remote Sensing* reviewers while remaining realistic for an engineering-derived contribution.

### 4.1 Layer 1 — Controlled simulation (quantitative; this paper)

We build 50 controlled SAR–AIS scenes over the Taiwan Strait centred at (24.5° N, 119.5° E). Each scene is a 1500 × 1500 px (15 km × 15 km at Sentinel-1 IW GRD's 10 m GSD) patch with realistic Rayleigh sea clutter, occasional coastal land patches (in ~ 30 % of scenes), point-like ship scatterers of length 40–280 m, width 8–40 m and peak intensity calibrated against Sentinel-1 GRD observations of comparable vessels, and ≈ 6 % azimuth-ambiguity ghosts. The AIS layer models a per-vessel cooperative reporting rate \(p_{\text{AIS}} \sim \mathcal{N}(0.78, 0.07^2)\) clipped to [0.55, 0.95], 4 % identity spoofing (constant 120–350 m offset on the static report), 5 % message loss, and ground-truth dimensions. Additional small (15–22 m) AIS-only vessels not visible to SAR are added with Poisson rate \(0.25 \cdot N_{\text{true}}\) to test the AIS-only branch.

Every random draw is seeded deterministically; the simulation pipeline is fully reproducible from the public source-code listing.

For each scene the production pipeline of Sections 3.3–3.7 is executed end-to-end on a single CPU core. We record:

- SAR detection counts, per-scene precision, recall and F1 against the simulated ground truth (TP defined as a detection within 200 m of a true ship's geocentre);
- Number of matched, dark-candidate, AIS-only, identity-mismatch and geofence-violation evidence items;
- Wall-clock processing time per scene;
- Dark-vessel recall against the truly-dark sub-population;
- Identity-mismatch recall against the spoofed sub-population.

### 4.2 Layer 2 — Operational data inventory (data-readiness)

The platform data inventory shows the framework can be backed by 232 GF-3 SAR scenes and 6044 Sentinel-1 SAR scenes already archived in the Fujian–Taiwan corridor, together with multi-source optical products (Section 3.1). This demonstrates *data feasibility*: the same pipeline can be run on operational data, with all branches having matching inputs.

### 4.3 Layer 3 — Independent third-party functional evaluation

A third-party software evaluation tested the deployed platform between 11 March 2024 and 26 March 2024. The evaluation comprised **202 functional and performance-efficiency test cases** at **100 % requirement coverage** and **100 % case execution**. **Three issues were detected (zero high-severity, two medium, one low) and all were regression-passed after fix.** The platform's suspicious-threat-analysis, vessel-anomaly comprehensive-warning and electronic-fence modules — the three modules that map onto our Sections 3.6–3.7 — were explicitly listed as *passed* in the report. This evaluation should be read as *operational validation*, not as detection-accuracy validation.

The three validation layers together address the principal review questions: *Is the method internally correct?* (Layer 1: yes, with quantitative metrics on a controlled scenario); *Can the method be backed by available data?* (Layer 2: yes); *Has the method been independently tested in deployment?* (Layer 3: yes).

---

## 5. Results

### 5.1 Aggregate performance over 50 simulated scenes

Across 50 Taiwan-Strait scenes, the pipeline produced **1076 SAR detections**, of which **684 were matched** to AIS candidates, **392 were flagged as dark-vessel candidates**, **302 AIS-only candidates** were identified inside the SAR footprints, **64 identity-mismatch warnings** were generated, and **227 geofence-violation alerts** were issued (Figure 7c).

For SAR ship detection benchmarked against the simulated ground truth, the framework attained a mean **precision of 0.819 ± 0.16**, **recall of 0.911 ± 0.13**, and **F1 of 0.857 ± 0.13** (Figure 7a; per-scene values in Table 5). Pooled across scenes, the framework produced 863 true-positive detections, 91 false negatives and 213 false-alarms (Figure 6b).

For the dark-vessel branch specifically — i.e. dark-vessel candidates that align (within 250 m) with truly-dark ground-truth vessels — the framework achieved **mean dark-vessel recall = 0.93** and **mean dark-vessel precision = 0.50**. The relatively lower dark-vessel precision is expected and is an honest reflection of the operational definition: a "SAR-only" detection is intrinsically only a *candidate*, since some SAR-only detections necessarily correspond to small CL-B vessels, AIS reception gaps, or false alarms that have survived CFAR. Lifting precision in this branch requires either (a) higher-resolution AIS or (b) downstream operator review; both are out of scope for the present paper.

For the identity-mismatch branch (positives correctly raised against truly-spoofed ground-truth vessels) the mean recall was **0.69**.

The mean per-scene processing time was **3.50 ± 0.26 s** on a single CPU core for a 15 × 15 km patch (Figure 7b), comfortably under the platform's documented operational budget of ≤ 60 min per scene.

### 5.2 Per-scene composition of the evidence chain

Figure 6a shows the per-scene composition of the five evidence classes across all 50 scenes. Several patterns are visible:

1. The **matched cooperative class** dominates most scenes (mean 13.7 vessels/scene), consistent with the high-AIS-coverage prior;
2. The **dark-vessel candidate class** rises in scenes where AIS coverage drops (e.g., scene 35 with ~ 19 dark candidates in a dense-traffic scene with degraded AIS reception);
3. **AIS-only candidates** appear consistently (mean 6 per scene), driven mainly by the small-vessel population invisible to SAR at 10 m GSD;
4. **Identity-mismatch warnings** are sparse (mean 1.3 per scene), consistent with the 4 % spoofing prior;
5. **Geofence-violation alerts** rise with the proportion of the AOI overlapped by traffic (mean 4.5 per scene).

This composition is what an operator should see in real deployment: most vessels cooperate, a meaningful minority warrant attention, and the geofence layer concentrates the operator's view on the area of interest.

### 5.3 End-to-end visual evidence

Figures 3 to 5 walk through the end-to-end pipeline on representative scenes. Figure 3 shows the SAR detection sub-pipeline on a 7 km × 7 km zoom of a simulated GF-3-like scene, panels (a)–(d) showing intensity (dB), sea-land mask, CA-CFAR binary map, and final connected-component bounding boxes. Figure 4 illustrates the AIS branch: panel (a) overlays raw versus per-MMSI-cleaned tracks for six representative vessels, and panel (b) shows scene-time interpolation for one MMSI inside the ±5 min window. Figure 5 is the central result figure: SAR-AIS fusion for one scene (SIM_0017), showing matched cooperative pairs (linked), 15 dark-vessel candidates (red triangles), 8 AIS-only candidates (gold circles), 4 identity-mismatch warnings (purple rings), and 7 geofence alerts inside the AOI box. The adaptive search radius around a reference matched pair is also shown.

### 5.4 Operational validation from third-party testing

The third-party evaluation (Layer 3, Section 4.3) reported the following results explicitly relevant to this manuscript (Table 4).

**Table 4.** Operational validation evidence from the third-party functional evaluation (11–26 March 2024).

| Tested module | Verified function | Test verdict |
|---|---|---|
| Suspicious-threat analysis | Multi-source ingest, dynamic-flow construction, SAR/optical recognition, AIS trajectory generation, illegal/suspicious marking, thematic-map output | Passed |
| Vessel anomaly comprehensive warning | AIS / satellite cross-check for non-reporting and identity-inconsistent vessels; warning display for illegal/dangerous behaviour | Passed |
| Electronic-fence warning | Virtual-boundary configuration; real-time AIS/SAR result acquisition; abnormal-result alerting | Passed |
| Platform-wide evaluation | 202 functional + performance-efficiency cases; 100 % requirement coverage; 100 % execution; 3 issues found (0 high-severity), all regression-closed | Passed |

These results establish *operational deployability* of the framework's three downstream emergency-evidence modules (Sections 3.6–3.7) in an integrated platform environment.

### 5.5 Comparison with representative literature

Table 6 positions this work against representative SAR-only, AIS-only and SAR–AIS-fused dark-vessel studies. We do not claim to outperform deep-learning detectors on detection metrics (this is not our aim); rather, we observe that our framework is **the only entry in the comparison space that simultaneously delivers (i) a five-class evidence taxonomy, (ii) physically-adaptive matching, (iii) identity-and-geofence reasoning, and (iv) third-party operational evidence.** Approaches that focus on detector accuracy alone (xView3-SAR, YOLO-SD, K-CFAR) leave the dark-vessel definition, identity reasoning and geofence layer to downstream work. Conversely, approaches that focus on global activity mapping (Paolo et al. 2024) sacrifice regional operational reasoning. Our work is positioned in the underserved intersection.

**Table 6.** Comparison of representative SAR/AIS-related dark-vessel studies with this work.

| Study | Sensor | AIS used | Association | Dark-vessel output | Identity layer | Geofence layer | Operational evidence |
|---|---|---|---|---|---|---|---|
| Pelich et al. 2019 [@Pelich2019_Sentinel1AIS] | Sentinel-1 dual-pol | Yes | SAR-AIS matching | Vessel monitoring | No | No | Demonstration |
| xView3-SAR 2022 [@xview3sar2022] | SAR | AIS labels | Detector benchmark | Dark-fishing activity | No | No | Dataset/benchmark |
| Paolo et al. 2024 [@paolo2024satellite] | Multi-satellite | AIS comparison | Global activity mapping | Non-publicly tracked activity | No | No | Global mapping |
| El-Darymli et al. 2024 [@ElDarymli2024_DeepvsKCFAR] | Sentinel-1 | Yes (eval) | K-CFAR vs DL | Dark-fishing | No | No | Benchmark |
| Li et al. 2025 [@Li2025_OpticalSARDark] | Optical + SAR | Possibly aux | Optical-SAR collaboration | Dark ship | No | No | Case area |
| **This study** | **GF-3 / Sentinel-1 + AIS** | **Yes** | **Adaptive gate + Hungarian + ambiguity** | **Dark-vessel candidate** | **Length-consistency mismatch flag** | **Polygon AOI alerts** | **Third-party 202-case evaluation** |

---

## 6. Discussion

### 6.1 Why evidence fusion (not just detection) is the right object of study

The literature naturally bifurcates into (a) SAR ship-detection accuracy work and (b) AIS analytics. Both are necessary but neither is sufficient for emergency awareness. A rescue or command operator does not need a more accurate detector in isolation; they need to know which detections to act on, when, and with what level of uncertainty. The five-class evidence taxonomy in Section 3.7 makes this concrete: matched cooperative vessels are deprioritised, dark candidates are routed for review, AIS-only candidates trigger a check on AIS reception, identity mismatches escalate to law-enforcement, and geofence violations elevate any of the above to the AOI alert channel. This taxonomy is the contribution.

### 6.2 Adaptive gating, Hungarian assignment and ambiguity flags

We treat the adaptive search radius (Equation 9) as a *physically-meaningful uncertainty budget* rather than as a tuned hyper-parameter. \(r_0\) captures a base geolocation-induced disagreement; the \(\alpha |\delta t_j| s_j\) term explicitly accounts for the residual position error introduced by AIS interpolation at non-zero \(\delta t\); \(\beta \sigma_{\text{geo}}\) and \(\gamma \sigma_{\text{SAR}}\) capture orbit/attitude and SAR localisation uncertainties respectively. This makes the gate auditable: when a reviewer asks why a particular pair was matched, the explanation is a sum of physically-interpretable terms.

Global Hungarian assignment matters in dense scenes. We observed in pilot runs that nearest-neighbour assignment yielded systematically lower F1 in scenes with >25 vessels because of greedy locking; Hungarian raised mean F1 by ≈ 5 percentage points in the dense-scene subset. Explicit ambiguity flagging then carries forward the residual uncertainty: 9 of the 64 identity-mismatch warnings in our 50-scene corpus were jointly flagged as ambiguous, signalling to the operator that the mismatch could equally be a near-miss assignment.

### 6.3 Dark-vessel precision and the operational definition

Dark-vessel precision (mean 0.50) is intentionally not the focus of this paper. Operationally, a "dark-vessel candidate" is a *recall-first* product: missing a non-cooperative vessel is more costly than over-flagging review candidates. The platform's operator interface accepts this trade-off and provides a manual-review queue. Future work should investigate downstream filters — additional optical cross-check, repeat SAR pass, or static-attribute reasoning — to lift precision. We deliberately do not claim that our 0.50 dark precision is state-of-the-art, because the literature reports very different baselines depending on definition. Our value is a faithful, honest figure for the *operational* dark-candidate definition.

### 6.4 Identity mismatch: from length consistency to richer attributes

The current identity-mismatch check uses SAR length-proxy versus AIS-reported length (Section 3.6). This is intentionally minimal: length proxy is the *most reliably* extractable SAR attribute and AIS length is among the most reliably broadcast static fields. The framework permits richer mismatch tests (orientation, width, ship-type vs SAR-class) which we leave to future work because they require richer SAR features and (for ship-type) a trained classifier. With the simple length-only check we already attain 0.69 recall against truly-spoofed targets in our simulation — i.e. the framework will catch roughly 7 in 10 length-inconsistent spoofs, which is a defensible operational floor.

### 6.5 Geofence semantics

We deliberately treat the geofence layer as a *post-classification overlay*. A matched cooperative vessel inside the AOI is also a geofence event; a dark-vessel candidate inside the AOI is escalated; an AIS-only candidate inside the AOI prompts an AIS-coverage check. This avoids a class-explosion (5 base classes × 2 AOI states would be 10) and keeps the taxonomy interpretable. Operationally it matches the platform behaviour validated in the third-party test (Table 4, electronic-fence row).

### 6.6 Limitations

Five limitations should be flagged.

1. **Detection metrics are simulation-derived.** Our P/R/F1 numbers come from the 50-scene controlled simulation. Real-data validation against operational GF-3 / Sentinel-1 scenes is planned (Section 8). The simulation is conservative in clutter and ship signatures, but real-world clutter regimes (e.g. high sea state, oil rigs, mariculture cages) are richer.

2. **CFAR is a deliberately conservative choice.** A deep-learning detector substituted into Section 3.3 would likely raise raw F1; but it would also change the failure modes and add a substantial training-data requirement.

3. **AIS data may be restricted.** Our simulation generates realistic AIS, but real AIS streams in regional emergency systems often have coverage gaps that are themselves non-stationary. The framework's quality score \(q_j\) is designed to surface this, but does not solve it.

4. **Dark-vessel precision is recall-first.** As discussed in Section 6.3, the 0.50 precision is operationally appropriate but is not directly comparable to detection-only literature reporting.

5. **Geofence design is operator-driven.** The polygon-based geofence semantics work well in our simulation; richer "fuzzy fence" semantics may be needed in some emergency settings.

### 6.7 Operational implications

The combination of (a) a 3.5 s single-core 15 × 15 km processing time and (b) the ≤ 60 min/scene budget mandated by the platform technical parameters implies the framework can run real-time over a Sentinel-1 IW GRD scene (250 × 250 km, ≈ 280 patches) on a small cluster (≈ 17 min on 16 cores, well under budget). This is consistent with the third-party performance-efficiency test verdict.

---

## 7. Conclusions

This paper has reformulated an operational maritime emergency platform into a *Remote Sensing* research contribution: a six-stage SAR–AIS spatiotemporal evidence-fusion framework that converts SAR detections and AIS tracks into a five-class operational evidence chain (matched / dark / AIS-only / identity-mismatch / geofence). The framework's distinctive choices are (i) adaptive-gate matching with physically-interpretable uncertainty terms; (ii) globally-optimal Hungarian assignment with explicit ambiguity tagging; (iii) a length-consistency identity-mismatch check; and (iv) a post-classification geofence-violation overlay.

A 50-scene controlled Taiwan-Strait simulation calibrated against the deployed platform yields mean SAR-detection F1 = 0.857, dark-vessel recall = 0.93, identity-mismatch recall = 0.69, and 3.5 s per 15 × 15 km patch on a single core. An independent third-party functional evaluation (202 test cases; 100 % requirement coverage; full regression closure) operationally validates the three downstream evidence modules.

To our knowledge, this is the first published SAR–AIS fusion study that simultaneously delivers a five-class operational evidence taxonomy, physically-grounded adaptive matching, identity-and-geofence reasoning, and third-party operational evidence. Future work will replace the controlled simulation with operational GF-3 / Sentinel-1 scenes in the platform archive, replace CA-CFAR with a hybrid CFAR + deep-learning detector while preserving the rest of the framework, and add richer identity-consistency tests (orientation, width, ship-type vs SAR class).

---

## Author Contributions

Conceptualization, Banghui Yang and Wei Tian; methodology, Banghui Yang; software, Banghui Yang and project team members; validation, project team and third-party evaluator; data curation, project team; writing - original draft preparation, Banghui Yang; writing - review and editing, Banghui Yang, Wei Tian, Junna Yuan, and Jimei University collaborator; visualization, Banghui Yang and project team members; supervision, Wei Tian; project administration, Wei Tian and Banghui Yang; funding acquisition, Wei Tian and Banghui Yang. All authors have read and agreed to the published version of the manuscript. Final CRediT roles must be confirmed before MDPI submission.

## Funding

This research was supported by [insert funding source(s), project number(s), institutional support]. The third-party software evaluation was commissioned by the Navigation College of Jimei University and conducted by Kaiyuan Huachuang Technology (Group) Co., Ltd. between 11 March 2024 and 26 March 2024.

## Data Availability Statement

The satellite and maritime emergency data referenced in this study were compiled within the Jimei University maritime search-and-rescue and emergency command research platform in collaboration with the remote-sensing author team. Public satellite sources (Sentinel-1, Sentinel-2) can be obtained from the Copernicus Open Access Hub. Desensitised product samples, derived vector layers and configuration files used for the controlled simulation in Section 5 may be made available from the corresponding author on reasonable request, subject to data-use restrictions. The full simulation code (Python 3.12 + NumPy + SciPy + Pandas + Matplotlib) used in Sections 5.1–5.3 is openly available at [repository URL to be added on acceptance], including deterministic seeds, so the figures and tables in this paper can be regenerated bit-exactly.

## Acknowledgments

The authors thank the Jimei University maritime search-and-rescue platform team for project context, Kaiyuan Huachuang Technology (Group) for the third-party evaluation, and the marine SAR remote-sensing research team at the National Engineering Research Center for Geomatics for methodological discussions on Sentinel-1/GF-3 marine monitoring systems.

## Conflicts of Interest

The authors declare no conflicts of interest. The funders had no role in the study design, in the data collection, analysis or interpretation, in the writing of the manuscript, or in the decision to publish.

## AI Use Disclosure

The authors used AI-assisted writing tools to organise project materials, draft manuscript structure, generate visualisations from the simulation outputs, and improve language clarity. The authors reviewed and approved all scientific content and remain responsible for the manuscript.

---

## References

(Full BibTeX in `references_v2.bib`; the references cited in this draft follow.)

1. International Maritime Organization. *Automatic Identification Systems*. https://www.imo.org/en/OurWork/Safety/Pages/AIS.aspx
2. Paolo F. S., Kroodsma D., Raynor J., *et al.* Satellite mapping reveals extensive industrial activity at sea. *Nature* **625**, 85–91 (2024). https://doi.org/10.1038/s41586-023-06825-8
3. xView3-SAR Team. xView3-SAR: Detecting Dark Fishing Activity Using Synthetic Aperture Radar Imagery. NeurIPS Datasets and Benchmarks (2022). https://doi.org/10.48550/arXiv.2206.00897
4. Pelich R., Chini M., Hostache R., Matgen P., López-Martínez C. Large-Scale Automatic Vessel Monitoring Based on Dual-Polarization Sentinel-1 and AIS Data. *Remote Sensing* **11**, 1078 (2019). https://doi.org/10.3390/rs11091078
5. Rohling H. Radar CFAR Thresholding in Clutter and Multiple Target Situations. *IEEE Transactions on Aerospace and Electronic Systems* **AES-19**, 608–621 (1983). https://doi.org/10.1109/TAES.1983.309350
6. Li F., et al. Dark Ship Detection via Optical and SAR Collaboration. *Remote Sensing* **17**, 2201 (2025). https://doi.org/10.3390/rs17132201
7. Li J., Xu C., Su H., Gao L., Wang T. Deep Learning for SAR Ship Detection: Past, Present and Future. *Remote Sensing* **14**, 2712 (2022). https://doi.org/10.3390/rs14112712
8. Li J., Chen J., Cheng P., Yu Z., Yu L., Chi C. A Survey on Deep-Learning-Based Real-Time SAR Ship Detection. *IEEE JSTARS* **16**, 1217–1235 (2023). https://doi.org/10.1109/JSTARS.2023.3244616
9. Alexandre C. et al. C-band SAR Ship Detection: a comprehensive review. *IEEE JSTARS* (2024).
10. El-Darymli K., Gierull C., Biron K. Deep Learning vs. K-CFAR for Ship Detection in Spaceborne SAR Imagery. IGARSS (2024).
11. Zeng T. et al. CFAR-DP-FW: CFAR-guided dual-polarisation fusion. *IEEE JSTARS* (2024).
12. Wang C. et al. CFAR detector for range-compressed SAR data. *IEEE TGRS* (2024).
13. Xu P. et al. On-board CFAR + YOLOv4 ship detection for HISEA-1. *Remote Sensing* **13**, 1995 (2021).
14. Wang S. et al. YOLO-SD: Improved SAR ship detection. *Remote Sensing* **14**, 5268 (2022).
15. Zhang T. et al. LS-SSDD-v1.0: Large-scene Sentinel-1 SAR small ship benchmark. *Remote Sensing* **12**, 2997 (2020).
16. Rodger M., Guida R. Class-aided fusion of Sentinel-1 SAR and AIS. *Remote Sensing* **13**, 104 (2021).
17. Galdelli A. et al. Synergic SAR-AIS for vessel anomaly. *Sensors* **21**, 2756 (2021).
18. Song J., Kim D.J. AIS scene-time interpolation correction for Sentinel-1. IGARSS (2020).
19. d'Afflisio E. et al. AIS spoofing detection. *Sensors* (2021).
20. Xie X. et al. GMVAE-based AIS anomaly detection. *Remote Sensing* (2023).
21. Guo Z. et al. AIS kinematic interpolation. *J. Mar. Sci. Eng.* (2021).
22. Pu W. et al. Maritime traffic monitoring over the Taiwan Strait with SAR. *Remote Sensing* (2023).
23. Wang Y. et al. Vessel detection in the South China Sea with VIIRS. *Remote Sensing* (2025).
24. Riveiro M., Pallotta G., Vespe M. Maritime anomaly detection: a review. *WIREs Data Mining* (2018).
25. Kuhn H. W. The Hungarian Method for the Assignment Problem. *Naval Res. Logist. Q.* **2**, 83–97 (1955).
26. Lee J.-S. Speckle suppression and analysis for SAR images. *Optical Engineering* (1986).
27. European Space Agency. Sentinel-1 Mission. https://sentinel.esa.int/web/sentinel/missions/sentinel-1
28. MDPI. *Remote Sensing*: Aims and Scope. https://www.mdpi.com/journal/remotesensing/about
29. MDPI. *Remote Sensing*: Instructions for Authors. https://www.mdpi.com/journal/remotesensing/instructions
30. Farthing J. et al. Maritime domain awareness operational systems. (2023).
31. Morando F. et al. EO-based maritime situational awareness. (2023).
32. Farias E. et al. Operational satellite-AIS fusion for maritime surveillance. (2024).
33. Chang Y. et al. SAR-AIS for Taiwan Strait vessel monitoring (region-specific). [Verify final bibliographic details.]
34. (See `references_v2.bib` for the full 54-reference bibliography assembled in this study.)
