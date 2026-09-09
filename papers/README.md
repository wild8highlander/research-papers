# 📄 Papers — Published PDF Research Papers

> **Navigation:** **`papers`**

![Papers](https://img.shields.io/badge/Content-Research%20Papers-blue?style=flat-square&logo=adobeacrobatreader&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Repo](https://img.shields.io/badge/Repo-wild8highlander%2Fresearch--papers-181717?style=flat-square&logo=github&logoColor=white)

This directory is the **journal-facing face of the repository**: the finished, typeset PDF papers that present the research programs to the scientific community. Each subfolder bundles one paper (or one paper in two language editions), stored as final PDFs exactly as they circulate — with LaTeX sources available separately in [`src/`](../src/README.md) and Word-form monographs in [`docs/`](../docs/README.md).

Three collections are hosted here. The **correction-b** pair (`main.pdf`, `main_v2.pdf`) is the full-length paper on the universal polarization correction *b* = π/(4π² + 2π√3) ≈ 0.0785 and the analytical proof of 3D Navier–Stokes regularity without dissipation. The **KdV chapter** (EN and RU editions of `KdV_b_correction_Chapter16`) extends the same constant to soliton interactions of the Korteweg–de Vries equation. The **NSE preprint** (`preprint_v1/v2`) is the compact statement of the regularity argument — the fastest complete read for a newcomer, with the title *"Correction b as Polarization Twisting: Analytical Proof of 3D Navier–Stokes Regularity without Dissipation"*.

All numbers quoted in these papers are cross-verified in this very repository: the [verification framework](../verification/README.md) re-derives each headline constant in eleven languages, and the AB-Cloud companion suite does the same in ten more. Citing these papers is always welcome — see the [citation block](../README.md#-citation) in the root README (BibTeX, APA, and [`CITATION.cff`](../CITATION.cff)).

## 📑 The Collections at a Glance

| Collection | Editions | Volume | Research program |
|---|---|---|---|
| **correction-b** | `main.pdf`, `main_v2.pdf` (identical 2.3 MB typeset editions) | ~2.3 MB each | NSE regularity via polarization correction *b* |
| **kdv** | `KdV_b_correction_Chapter16_EN.pdf` (7.2 MB), `..._RU.pdf` (7.4 MB) | ~14.6 MB total | KdV soliton interactions under the b-correction |
| **preprint** | `preprint_v1.pdf`, `preprint_v2.pdf` (identical 120 KB) | ~0.24 MB total | Compact NSE preprint — best first read |

The two PDFs inside each of `correction-b/` and `preprint/` are byte-identical twins kept under two filenames for convenience (`main` vs `main_v2`, `v1` vs `v2`) — they represent the same final revision, so either may be cited. The KdV chapter ships as two genuinely separate language editions produced from the same source.

## 🧭 Which Paper Should You Read First?

1. **`preprint/preprint_v2.pdf`** — ~100 KB, the shortest complete statement of the NSE result: the correction *b*, the rotation angle θ_b ≈ 7.07°, and the 3.5× BKM-criterion reduction. Read this if you have fifteen minutes.
2. **`correction-b/main_v2.pdf`** — the full paper: derivation of *b* from the Kirchhoff point-vortex system, the regularity proof, and the numerical stress-tests.
3. **`kdv/KdV_b_correction_Chapter16_EN.pdf`** — the integrable-systems continuation: how the same constant shows up in soliton interactions; read the RU edition instead if you prefer Russian.

After the papers, the natural next steps are the formal/computational verification in [`verification/`](../verification/README.md) and the AB-Cloud complex in [`ab-cloud/`](../ab-cloud/README.md).

## 🔬 Verification Backing

Every quantitative claim in these papers maps onto a section of the multi-language verification framework:

- **Section 1** — the value and bounds of *b* (asserted in all 8 language ports, proved in all 4 proof assistants);
- **Section 2** — the preprint's regularity argument chain;
- **Section 4** — the KdV soliton results (pseudospectral port in C++);
- **Sections 3 & 6** — the AB-Cloud ↔ ζ-zero correspondence for the spectral claims referenced by the correction-b paper.

The Word monographs backing these papers (with figure-rich layouts) live in [`docs/correction-b/`](../docs/correction-b/README.md) and [`docs/kdv/`](../docs/kdv/README.md).

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`correction-b/`](correction-b/) | — | the correction-b paper — two identical typeset editions (main / main_v2) |
| [`kdv/`](kdv/) | — | the KdV book chapter — English and Russian editions |
| [`preprint/`](preprint/) | — | the compact NSE preprint — v1 and v2 (same revision) |

## 🗂 Directory Layout

```
papers/
├── correction-b/   # 3 files
│   ├── main.pdf
│   ├── main_v2.pdf
│   └── README.md  (this file)
├── kdv/   # 3 files
│   ├── KdV_b_correction_Chapter16_EN.pdf
│   ├── KdV_b_correction_Chapter16_RU.pdf
│   └── README.md  (this file)
├── preprint/   # 3 files
│   ├── preprint_v1.pdf
│   ├── preprint_v2.pdf
│   └── README.md  (this file)
└── README.md  (this file)
```

## 🇷🇺 Краткое резюме (Russian Summary)

**papers/** — готовые PDF-статьи репозитория. Три подборки: **correction-b/** — полная статья о поправке *b* ≈ 0.0785 и доказательстве регулярности 3D Navier–Stokes без диссипации (два идентичных издания main/main_v2); **kdv/** — глава о солитонах КдФ с той же поправкой (английское и русское издания, ~7 МБ каждый); **preprint/** — компактный препринт о регулярности NSE — лучшая первая статья для знакомства. LaTeX-исходники — в `src/`, вёрстки Word — в `docs/`. Все числа из статей воспроизводятся верификацией в 11 языках (см. `verification/`).

---

<div align="center">

**[⬆ Back to top](#-papers--published-pdf-research-papers)** · 
**[Repository root](README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>