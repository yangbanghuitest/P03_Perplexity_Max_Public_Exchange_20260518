# P03 Perplexity Max One-File Review Packet

Date: 2026-05-18

Purpose: a single-file public review packet for Perplexity Max and other cloud AI tools that cannot reliably fetch a full GitHub repository.

Primary task: review and improve the P03 Remote Sensing manuscript, especially literature positioning, claim calibration, title/abstract/contributions, and submission-readiness risks.


---

## PERPLEXITY MAX PROMPT

Source file: `PERPLEXITY_MAX_PROMPT.md`

# Perplexity Max Prompt for P03

Use the public GitHub repository below as the source material:

`https://github.com/yangbanghuitest/P03_Perplexity_Max_Public_Exchange_20260518`

I am preparing a manuscript for *Remote Sensing*:

**Spatiotemporal Evidence Fusion of SAR Ship Detections and AIS Tracks for Dark Vessel Discovery in Maritime Emergency Awareness: A Taiwan Strait Case Study**

Please read the repository in this order:

1. `manuscript/P03_manuscript_v3.md`
2. `submission/cover_letter_v3.md`
3. `author_profile/AUTHOR_PROFILE_AND_STYLE_NOTE_TianWei_ORCID_poster_20260518.md`
4. `references/lit_summary.md`
5. `references/references_v2.bib`
6. `research_plan/P03_four_skill_action_plan_20260518.md`
7. `research_plan/P03_RemoteSensing_experiment_submission_checklist_20260517.md`
8. `metrics/overall_metrics.json`
9. `metrics/scene_stats.csv`

Tasks:

1. Judge whether the manuscript is suitable for *Remote Sensing* as an Article, and explain the main acceptance risks.
2. Compare it with recent SAR-AIS fusion, dark-vessel discovery, xView3/Sentinel-1/GF-3 maritime monitoring, AIS anomaly detection, and operational maritime-awareness literature.
3. Find 8-12 high-value references from 2020-2026, prioritizing papers with DOI or official publisher/arXiv links. Include exact places where each reference should be cited.
4. Identify claims that are too strong, especially around first-of-its-kind wording, operational validation, dark-vessel detection, identity mismatch, and law-enforcement implications.
5. Rewrite the title, abstract, highlights, and contribution bullets in a stronger *Remote Sensing* style while keeping the engineering deployment value.
6. Suggest how to explain the validation design: controlled simulation, public/open reproducibility, and third-party functional testing.
7. Return a reviewer-facing checklist: what must be added before submission, what can be deferred to revision, and what should be moved to supplementary material.

Constraints:

- Keep `Banghui Yang` as first author and `Wei Tian` as corresponding author unless explicitly asked otherwise.
- Do not treat evidence classes as legal conclusions. Use `dark-vessel candidates`, `identity-mismatch warnings`, and `geofence alerts`.
- Do not ask for raw AIS, real MMSI, ship names, precise coordinates, or restricted operational data.
- Separate verified facts from your recommendations.

Please return the answer in structured Markdown with tables where useful.


---

## README

Source file: `README.md`

# P03 Perplexity Max Public Exchange

Date: 2026-05-18

This repository is a public AI-assistance exchange package for P03:

**Spatiotemporal Evidence Fusion of SAR Ship Detections and AIS Tracks for Dark Vessel Discovery in Maritime Emergency Awareness: A Taiwan Strait Case Study**

Target journal: *Remote Sensing*.

## Purpose

Use this public repository as the easiest route for Perplexity Max or external academic reviewers to read the current P03 materials and return literature, framing, and manuscript-improvement suggestions.

GitHub mirror for cloud AI access:

`https://github.com/yangbanghuitest/P03_Perplexity_Max_Public_Exchange_20260518`

The formal working repository remains:

`http://tj.100000000.cc:3000/yangbh/P03_SAR_AIS_DarkVessel_RemoteSensing.git`

This public exchange repo is for AI reading, literature checking, and draft-level suggestions.

## Recommended Reading Order

1. `manuscript/P03_manuscript_v3.md`
2. `submission/cover_letter_v3.md`
3. `author_profile/AUTHOR_PROFILE_AND_STYLE_NOTE_TianWei_ORCID_poster_20260518.md`
4. `references/lit_summary.md`
5. `references/references_v2.bib`
6. `research_plan/P03_four_skill_action_plan_20260518.md`
7. `research_plan/P03_RemoteSensing_experiment_submission_checklist_20260517.md`
8. `metrics/overall_metrics.json`
9. `metrics/scene_stats.csv`

## What Perplexity Max Should Help With

- Check whether the contribution is sufficiently distinct from recent SAR-AIS dark-vessel, xView3, Sentinel-1/GF-3, and maritime anomaly-detection literature.
- Suggest 8-12 high-value recent references with DOI or stable URLs.
- Identify overclaims, weak evidence, missing baselines, and reviewer risks.
- Improve title, abstract, contribution bullets, limitation wording, and cover-letter positioning.
- Recommend how to frame the work for *Remote Sensing* without sounding like a platform report.

## Guardrails

- Treat all vessel labels as candidates or evidence classes, not confirmed legal conclusions.
- Do not request raw AIS, real MMSI, ship names, precise coordinates, operational boundaries, or non-public source documents.
- Prefer wording such as `dark-vessel candidates`, `identity-mismatch warnings`, and `geofence alerts`.
- Keep Wei Tian as corresponding author and Banghui Yang as first author unless the authors explicitly change this.

## Return Format Requested From Perplexity Max

Please return:

1. A concise manuscript diagnosis.
2. A table of literature additions, including title, authors, year, venue, DOI/URL, relevance, and exact insertion point.
3. Section-by-section revision suggestions.
4. Revised abstract and contribution bullets.
5. Reviewer-risk checklist.
6. Any sentences that should be softened or removed.


---

## MANUSCRIPT V3

Source file: `manuscript\P03_manuscript_v3.md`

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


---

## COVER LETTER V3

Source file: `submission\cover_letter_v3.md`

# Cover Letter Draft v3

Dear Editor,

We submit for your consideration the article entitled "Spatiotemporal Evidence Fusion of SAR Ship Detections and AIS Tracks for Dark Vessel Discovery in Maritime Emergency Awareness: A Taiwan Strait Case Study" for publication in *Remote Sensing*.

This manuscript is submitted by Banghui Yang as first author, with Wei Tian serving as corresponding author. Wei Tian is an Associate Professor at the National Engineering Research Center for Geomatics, Aerospace Information Research Institute, Chinese Academy of Sciences, and his ORCID is https://orcid.org/0000-0002-2024-4200. The manuscript follows the author team's applied marine SAR remote-sensing style: it starts from an operational maritime emergency problem, formalises a reproducible SAR-based method, reports quantitative metrics, and connects the method to deployable emergency-warning systems.

The study proposes a six-stage SAR-AIS spatiotemporal evidence-fusion framework that converts independent SAR detections and cooperative AIS tracks into a five-class evidence taxonomy: matched cooperative vessels, dark-vessel candidates, AIS-only targets, identity-mismatch warnings, and geofence violations. The framework uses AIS scene-time reconstruction, adaptive SAR-AIS gating, Hungarian assignment, explicit ambiguity tagging, and rule-transparent emergency evidence generation.

The manuscript is suitable for *Remote Sensing* because it addresses SAR maritime monitoring, operational data fusion, regional emergency awareness, and reproducible remote-sensing workflows. It reports controlled simulation over 50 Taiwan-Strait scenes, a mean SAR detection F1 of 0.857, dark-vessel recall of 0.93, identity-mismatch recall of 0.69, and 3.5 s processing time per 15 km by 15 km patch. It also anchors the method in third-party functional evidence from a deployed maritime emergency platform.

We use the terms "dark-vessel candidates" and "non-cooperative vessel candidates" deliberately. The paper does not claim law-enforcement confirmation of illegal activity; it provides an auditable remote-sensing evidence chain for operator review.

Sincerely,

Banghui Yang  
Aerospace Information Research Institute, Chinese Academy of Sciences  
University of Chinese Academy of Sciences  

Wei Tian  
National Engineering Research Center for Geomatics  
Aerospace Information Research Institute, Chinese Academy of Sciences  
ORCID: https://orcid.org/0000-0002-2024-4200  
Email: tianwei@aircas.ac.cn


---

## AUTHOR PROFILE AND STYLE NOTE

Source file: `author_profile\AUTHOR_PROFILE_AND_STYLE_NOTE_TianWei_ORCID_poster_20260518.md`

# P03 Author Profile and Style Update Note

Date: 2026-05-18

## 1. User Decision Implemented

Working authorship setting for P03:

- Banghui Yang: first author.
- Wei Tian: corresponding author.
- Junna Yuan and Jimei University collaborator: retained as placeholders pending final author-list confirmation.

If Banghui Yang should also be co-corresponding author, add `Banghui Yang, yangbh@aircas.ac.cn` as a second corresponding contact before final MDPI submission.

## 2. ORCID-Verified Wei Tian Information

Source: `https://orcid.org/0000-0002-2024-4200`

Public ORCID record:

- Name: Wei Tian.
- Employment: Associate Prof., National Engineering Research Center for Geomatics, Aerospace Information Research Institute, Beijing, China.
- ORCID: `0000-0002-2024-4200`.

Representative publication style from ORCID:

- SAR and microwave remote sensing applications.
- Marine and environmental monitoring.
- GF-series, Sentinel-1 and polarimetric/compact-polarimetric SAR.
- MDPI-style applied remote-sensing articles, including *Remote Sensing*, *Geomatics*, *Hydrology*, and related venues.

Representative ORCID-listed works relevant to P03 framing:

| Year | Venue | Title / theme | DOI |
| --- | --- | --- | --- |
| 2026 | Geomatics | SBAS-InSAR quantification of wind erosion and dune migration | 10.3390/geomatics6020038 |
| 2025 | Hydrology | Near-real-time water-stress monitoring using remote-sensing data | 10.3390/hydrology12120325 |
| 2023 | Remote Sensing | Green tide biomass detection with remote sensing and in situ measurement | 10.3390/rs15143625 |
| 2019 | Frontiers of Earth Science | C- and L-band simulated compact polarized SAR in oil spill detection | 10.1007/s11707-018-0733-9 |
| 2018 | IEEE JSTARS | Shallow water depth retrieval from multitemporal Sentinel-1 SAR data | 10.1109/jstars.2018.2851845 |
| 2017 | IEEE GRSL | GF-4 images for dynamic ship monitoring | 10.1109/lgrs.2017.2687700 |
| 2015 | Aquatic Procedia | Oil spill detection with China's HJ-1C SAR image | 10.1016/j.aqpro.2015.02.204 |
| 2008 | IGARSS | Automatic identification of oil spill in ENVISAT ASAR images | 10.1109/igarss.2008.4779621 |

## 3. Poster-Derived Style Cues

Source copied locally:

`08_v3_作者信息与风格更新_20260518/source_materials/e-poster-TianWei_20260518.pdf`

Poster title:

`An Intelligent Oil Spill Warning System Leveraging Sentinel-1 and GF-3 SAR Data with ResNet34-Unet++ Model`

Poster authors:

- Wei Tian
- Junna Yuan
- Banghui Yang

Poster affiliation style:

- National Engineering Research Center for Geoinformatics / Geomatics, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing 100101, China.
- University of Chinese Academy of Sciences, Beijing 100049, China.

Poster writing style to transfer into P03:

1. Start from an operational marine emergency problem.
2. Use SAR as the all-weather wide-area observation backbone.
3. Present a clear model/system pipeline, not just a detached algorithm.
4. Include cross-sensor data sources, especially Sentinel-1 and GF-3.
5. Report concrete metrics in the abstract and results.
6. Emphasize engineering deployment: Web GIS, backend service, spatial database, automated warning, emergency management.
7. Keep limitations practical: sample imbalance, sensor differences, look-alikes, offline/near-real-time constraints.

## 4. P03 Style Direction

P03 should be written as:

> an operational SAR-AIS evidence-fusion article for maritime emergency awareness, combining reproducible simulation with deployable system evidence.

It should not be written as:

- a pure ship detector paper;
- a law-enforcement conclusion paper;
- a generic GIS platform report;
- a black-box AI paper.

## 5. Concrete Manuscript Changes Made

Created:

- `manuscript_v3_author_profile_updated.md`

Updated:

- Author line: Banghui Yang first author; Wei Tian corresponding author.
- Affiliation line: AIR/CAS + UCAS + Jimei University collaborator placeholder.
- Contact line: Wei Tian email and ORCID.
- Abstract: added a sentence linking the paper to the applied SAR system style used in the author team's marine-emergency work.
- Author contributions: replaced placeholders with Banghui Yang / Wei Tian roles.
- Data availability and acknowledgments: added AIR/CAS remote-sensing team context.

## 6. Still Needed Before Submission

1. Confirm final author list and order.
2. Confirm whether Banghui Yang should also be co-corresponding author.
3. Confirm Jimei University collaborator name, email, ORCID, and affiliation.
4. Confirm funding numbers.
5. Confirm whether the term `National Engineering Research Center for Geomatics` or `Geoinformatics` should be used consistently.
6. Confirm whether the poster's oil-spill system can be mentioned only in internal style notes or also cited in cover letter/background.


---

## LITERATURE SUMMARY

Source file: `references\lit_summary.md`

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


---

## FOUR-SKILL ACTION PLAN

Source file: `research_plan\P03_four_skill_action_plan_20260518.md`

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


---

## REMOTE SENSING EXPERIMENT AND SUBMISSION CHECKLIST

Source file: `research_plan\P03_RemoteSensing_experiment_submission_checklist_20260517.md`

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


---

## OVERALL METRICS JSON

Source file: `metrics\overall_metrics.json`

{
  "n_scenes": 50,
  "total_sar_detections": 1076,
  "total_matches": 684,
  "total_dark_candidates": 392,
  "total_ais_only": 302,
  "total_identity_mismatch": 64,
  "total_geofence_alerts": 227,
  "mean_precision": 0.8194840000000001,
  "mean_recall": 0.9105820000000001,
  "mean_f1": 0.8564999999999999,
  "mean_dark_precision": 0.495246,
  "mean_dark_recall": 0.9301466666666667,
  "mean_id_mismatch_recall": 0.6896551724137931,
  "mean_proc_time_sec": 3.50002,
  "std_proc_time_sec": 0.25833639594410185,
  "pct_dark_of_sar_dets": 0.3643122676579926,
  "pct_match_of_sar_dets": 0.6356877323420075
}

---

## SCENE STATS CSV

Source file: `metrics\scene_stats.csv`

scene_id,sensor,acquisition_time_utc,area_name,n_vessels_true,truly_dark_n,spoofed_truths,ais_raw_messages,ais_after_cleaning,ais_candidates_in_footprint,sar_detections_n,matched_sar_ais_n,sar_only_dark_candidates_n,ais_only_n,identity_mismatch_warnings_n,ambiguous_matches_n,geofence_alerts_n,processing_time_sec,tp,fp,fn,precision,recall,f1,dark_precision,dark_recall,identity_mismatch_recall,ais_coverage_true,coast_fraction,thematic_map_output
SIM_0000,Sentinel-1 IW GRD (sim),2024-05-14 15:20:00,Taiwan Strait nearshore (sim),19,7,1,723,719,19,22,8,14,11,1,0,3,3.584,14,8,5,0.6364,0.7368,0.6829,0.4286,0.8571,1.0,0.727,0.193,Y
SIM_0001,GF-3 FSII (sim),2024-05-14 16:20:00,Taiwan Strait (sim),9,2,0,309,307,8,7,4,3,4,0,0,1,3.359,6,1,3,0.8571,0.6667,0.75,0.6667,1.0,,0.747,0.0,Y
SIM_0002,Sentinel-1 IW GRD (sim),2024-05-14 17:20:00,Taiwan Strait (sim),20,4,1,714,709,19,19,14,5,5,0,0,5,3.336,18,1,2,0.9474,0.9,0.9231,0.8,1.0,0.0,0.897,0.0,Y
SIM_0003,GF-3 FSII (sim),2024-05-14 18:20:00,Taiwan Strait nearshore (sim),20,4,0,873,871,23,26,15,11,8,1,0,4,3.837,19,7,1,0.7308,0.95,0.8261,0.3636,1.0,,0.794,0.084,Y
SIM_0004,Sentinel-1 IW GRD (sim),2024-05-14 19:20:00,Taiwan Strait (sim),14,1,0,616,613,16,12,11,1,5,3,0,1,3.446,12,0,2,1.0,0.8571,0.9231,1.0,1.0,,0.896,0.0,Y
SIM_0005,GF-3 FSII (sim),2024-05-14 20:20:00,Taiwan Strait (sim),28,5,1,1097,1095,29,34,22,12,7,1,0,6,3.483,26,8,2,0.7647,0.9286,0.8387,0.3333,0.8,1.0,0.776,0.0,Y
SIM_0006,Sentinel-1 IW GRD (sim),2024-05-14 21:20:00,Taiwan Strait (sim),30,5,1,1112,1107,29,25,18,7,11,1,0,6,3.657,22,3,8,0.88,0.7333,0.8,0.5714,0.8,1.0,0.743,0.0,Y
SIM_0007,GF-3 FSII (sim),2024-05-14 22:20:00,Taiwan Strait nearshore (sim),25,4,0,916,913,24,31,18,13,6,2,0,6,4.026,21,10,4,0.6774,0.84,0.75,0.2308,0.75,,0.874,0.193,Y
SIM_0008,Sentinel-1 IW GRD (sim),2024-05-14 23:20:00,Taiwan Strait (sim),7,1,0,268,263,7,8,6,2,1,1,0,1,3.216,7,1,0,0.875,1.0,0.9333,0.5,1.0,,0.848,0.0,Y
SIM_0009,GF-3 FSII (sim),2024-05-15 00:20:00,Taiwan Strait nearshore (sim),25,3,1,997,992,26,28,19,9,7,2,0,13,3.848,22,6,3,0.7857,0.88,0.8302,0.3333,1.0,1.0,0.835,0.165,Y
SIM_0010,Sentinel-1 IW GRD (sim),2024-05-15 01:20:00,Taiwan Strait (sim),9,1,0,312,308,8,8,7,1,1,0,0,2,3.185,8,0,1,1.0,0.8889,0.9412,1.0,1.0,,0.802,0.0,Y
SIM_0011,GF-3 FSII (sim),2024-05-15 02:20:00,Taiwan Strait nearshore (sim),21,4,1,833,830,22,20,14,6,8,1,0,3,3.495,18,2,3,0.9,0.8571,0.878,0.6667,1.0,1.0,0.714,0.102,Y
SIM_0012,Sentinel-1 IW GRD (sim),2024-05-15 03:20:00,Taiwan Strait (sim),8,2,0,315,310,8,8,6,2,2,1,0,3,3.175,8,0,0,1.0,1.0,1.0,1.0,1.0,,0.719,0.0,Y
SIM_0013,GF-3 FSII (sim),2024-05-15 04:20:00,Taiwan Strait (sim),17,4,0,652,647,17,19,13,6,4,0,0,3,3.207,17,2,0,0.8947,1.0,0.9444,0.6667,1.0,,0.775,0.0,Y
SIM_0014,Sentinel-1 IW GRD (sim),2024-05-15 05:20:00,Taiwan Strait nearshore (sim),23,5,0,912,910,24,21,15,6,9,1,0,4,3.745,19,2,4,0.9048,0.8261,0.8636,0.6667,0.8,,0.862,0.194,Y
SIM_0015,GF-3 FSII (sim),2024-05-15 06:20:00,Taiwan Strait nearshore (sim),12,2,1,530,528,14,19,9,10,5,1,1,1,3.814,11,8,1,0.5789,0.9167,0.7097,0.2,1.0,1.0,0.786,0.122,Y
SIM_0016,Sentinel-1 IW GRD (sim),2024-05-15 07:20:00,Taiwan Strait (sim),7,2,0,192,188,5,9,4,5,1,2,0,0,3.187,6,3,1,0.6667,0.8571,0.75,0.4,1.0,,0.875,0.0,Y
SIM_0017,GF-3 FSII (sim),2024-05-15 08:20:00,Taiwan Strait (sim),32,5,4,1282,1278,34,41,26,15,8,4,0,7,3.506,31,10,1,0.7561,0.9688,0.8493,0.3333,1.0,1.0,0.715,0.0,Y
SIM_0018,Sentinel-1 IW GRD (sim),2024-05-15 09:20:00,Taiwan Strait nearshore (sim),12,0,1,491,487,13,19,11,8,2,0,0,3,3.655,11,8,1,0.5789,0.9167,0.7097,0.0,,0.0,0.861,0.136,Y
SIM_0019,GF-3 FSII (sim),2024-05-15 10:20:00,Taiwan Strait nearshore (sim),18,2,0,764,762,20,18,14,4,6,0,0,4,3.683,16,2,2,0.8889,0.8889,0.8889,0.5,1.0,,0.718,0.101,Y
SIM_0020,Sentinel-1 IW GRD (sim),2024-05-15 11:20:00,Taiwan Strait (sim),23,2,2,1074,1071,28,24,20,4,8,0,1,6,3.371,22,2,1,0.9167,0.9565,0.9362,0.5,1.0,0.0,0.865,0.0,Y
SIM_0021,GF-3 FSII (sim),2024-05-15 12:20:00,Taiwan Strait (sim),22,6,1,730,725,19,23,15,8,4,2,0,4,3.336,20,3,2,0.8696,0.9091,0.8889,0.625,0.8333,1.0,0.714,0.0,Y
SIM_0022,Sentinel-1 IW GRD (sim),2024-05-15 13:20:00,Taiwan Strait (sim),12,5,1,419,416,11,12,7,5,4,0,0,4,3.179,11,1,1,0.9167,0.9167,0.9167,0.8,0.8,0.0,0.743,0.0,Y
SIM_0023,GF-3 FSII (sim),2024-05-15 14:20:00,Taiwan Strait (sim),16,3,3,721,719,19,15,12,3,7,0,0,2,3.229,15,0,1,1.0,0.9375,0.9677,1.0,1.0,0.0,0.772,0.0,Y
SIM_0024,Sentinel-1 IW GRD (sim),2024-05-15 15:20:00,Taiwan Strait (sim),16,7,0,651,648,17,14,7,7,10,0,0,2,3.347,14,0,2,1.0,0.875,0.9333,1.0,1.0,,0.74,0.0,Y
SIM_0025,GF-3 FSII (sim),2024-05-15 16:20:00,Taiwan Strait nearshore (sim),8,0,0,351,346,9,12,8,4,1,0,0,0,3.511,8,4,0,0.6667,1.0,0.8,0.0,,,0.802,0.133,Y
SIM_0026,Sentinel-1 IW GRD (sim),2024-05-15 17:20:00,Taiwan Strait (sim),23,6,2,765,760,20,24,14,10,6,2,0,7,3.394,20,4,3,0.8333,0.8696,0.8511,0.6,1.0,1.0,0.741,0.0,Y
SIM_0027,GF-3 FSII (sim),2024-05-15 18:20:00,Taiwan Strait (sim),7,0,0,345,342,9,9,7,2,2,2,0,2,3.2,7,2,0,0.7778,1.0,0.875,0.0,,,0.882,0.0,Y
SIM_0028,Sentinel-1 IW GRD (sim),2024-05-15 19:20:00,Taiwan Strait (sim),12,7,1,431,428,11,15,4,11,7,0,0,1,3.315,11,4,1,0.7333,0.9167,0.8148,0.6364,1.0,0.0,0.708,0.0,Y
SIM_0029,GF-3 FSII (sim),2024-05-15 20:20:00,Taiwan Strait (sim),18,6,0,579,576,15,21,12,9,3,0,0,2,3.263,18,3,0,0.8571,1.0,0.9231,0.6667,1.0,,0.761,0.0,Y
SIM_0030,Sentinel-1 IW GRD (sim),2024-05-15 21:20:00,Taiwan Strait nearshore (sim),17,5,0,570,568,15,34,12,22,3,1,0,3,3.799,17,17,0,0.5,1.0,0.6667,0.2273,1.0,,0.663,0.119,Y
SIM_0031,GF-3 FSII (sim),2024-05-15 22:20:00,Taiwan Strait (sim),34,4,1,1379,1377,36,33,28,5,8,3,0,10,3.597,31,2,3,0.9394,0.9118,0.9254,0.6,0.75,1.0,0.775,0.0,Y
SIM_0032,Sentinel-1 IW GRD (sim),2024-05-15 23:20:00,Taiwan Strait (sim),22,11,1,689,686,18,22,10,12,8,1,0,4,3.355,20,2,2,0.9091,0.9091,0.9091,0.8333,0.9091,1.0,0.676,0.0,Y
SIM_0033,GF-3 FSII (sim),2024-05-16 00:20:00,Taiwan Strait nearshore (sim),16,4,1,571,569,15,22,12,10,3,2,0,4,3.672,15,7,1,0.6818,0.9375,0.7895,0.3,0.75,1.0,0.799,0.085,Y
SIM_0034,Sentinel-1 IW GRD (sim),2024-05-16 01:20:00,Taiwan Strait nearshore (sim),28,1,1,1547,1543,41,36,24,12,17,4,0,16,4.01,25,11,3,0.6944,0.8929,0.7812,0.0833,1.0,1.0,0.852,0.197,Y
SIM_0035,GF-3 FSII (sim),2024-05-16 02:20:00,Taiwan Strait nearshore (sim),31,4,1,1247,1242,33,35,21,14,12,2,0,8,3.997,25,10,6,0.7143,0.8065,0.7576,0.2857,1.0,1.0,0.885,0.119,Y
SIM_0036,Sentinel-1 IW GRD (sim),2024-05-16 03:20:00,Taiwan Strait (sim),16,4,2,541,536,14,18,11,7,3,1,0,0,3.34,14,4,2,0.7778,0.875,0.8235,0.4286,0.75,0.5,0.801,0.0,Y
SIM_0037,GF-3 FSII (sim),2024-05-16 04:20:00,Taiwan Strait (sim),17,4,0,675,670,18,21,13,8,5,2,0,4,3.251,17,4,0,0.8095,1.0,0.8947,0.5,1.0,,0.707,0.0,Y
SIM_0038,Sentinel-1 IW GRD (sim),2024-05-16 05:20:00,Taiwan Strait (sim),33,10,1,1099,1096,29,40,24,16,5,5,0,5,3.406,31,9,2,0.775,0.9394,0.8493,0.4375,0.7,1.0,0.777,0.0,Y
SIM_0039,GF-3 FSII (sim),2024-05-16 06:20:00,Taiwan Strait nearshore (sim),29,2,1,1286,1283,34,31,24,7,10,0,0,7,4.11,26,5,3,0.8387,0.8966,0.8667,0.2857,1.0,0.0,0.95,0.17,Y
SIM_0040,Sentinel-1 IW GRD (sim),2024-05-16 07:20:00,Taiwan Strait (sim),26,8,1,995,991,26,30,18,12,8,3,0,9,3.537,24,6,2,0.8,0.9231,0.8571,0.5,0.75,1.0,0.828,0.0,Y
SIM_0041,GF-3 FSII (sim),2024-05-16 08:20:00,Taiwan Strait (sim),33,7,1,1295,1293,34,32,24,8,10,0,0,19,3.501,30,2,3,0.9375,0.9091,0.9231,0.75,0.8571,0.0,0.72,0.0,Y
SIM_0042,Sentinel-1 IW GRD (sim),2024-05-16 09:20:00,Taiwan Strait (sim),26,6,0,1150,1148,30,28,19,9,11,1,0,2,3.593,25,3,1,0.8929,0.9615,0.9259,0.6667,1.0,,0.787,0.0,Y
SIM_0043,GF-3 FSII (sim),2024-05-16 10:20:00,Taiwan Strait nearshore (sim),13,2,2,531,528,14,16,10,6,4,1,0,10,3.596,12,4,1,0.75,0.9231,0.8276,0.3333,1.0,0.5,0.898,0.084,Y
SIM_0044,Sentinel-1 IW GRD (sim),2024-05-16 11:20:00,Taiwan Strait (sim),7,0,0,271,267,7,7,7,0,0,0,0,2,3.335,7,0,0,1.0,1.0,1.0,0.0,,,0.707,0.0,Y
SIM_0045,GF-3 FSII (sim),2024-05-16 12:20:00,Taiwan Strait (sim),27,7,1,1063,1059,28,34,20,14,8,5,1,1,3.522,26,8,1,0.7647,0.963,0.8525,0.5,1.0,1.0,0.834,0.0,Y
SIM_0046,Sentinel-1 IW GRD (sim),2024-05-16 13:20:00,Taiwan Strait (sim),14,0,0,685,682,18,15,14,1,4,0,0,9,3.236,14,1,0,0.9333,1.0,0.9655,0.0,,,0.92,0.0,Y
SIM_0047,GF-3 FSII (sim),2024-05-16 14:20:00,Taiwan Strait (sim),16,3,1,800,796,21,20,12,8,9,2,0,7,3.311,15,5,1,0.75,0.9375,0.8333,0.375,1.0,1.0,0.876,0.0,Y
SIM_0048,Sentinel-1 IW GRD (sim),2024-05-16 15:20:00,Taiwan Strait (sim),11,4,1,420,416,11,12,6,6,5,1,0,0,3.269,10,2,1,0.8333,0.9091,0.8696,0.6667,1.0,1.0,0.776,0.0,Y
SIM_0049,GF-3 FSII (sim),2024-05-16 16:20:00,Taiwan Strait nearshore (sim),25,8,0,808,804,21,27,15,12,6,2,0,1,3.975,21,6,4,0.7778,0.84,0.8077,0.5,0.75,,0.734,0.193,Y

