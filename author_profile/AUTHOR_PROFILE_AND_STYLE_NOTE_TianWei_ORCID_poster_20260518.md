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
