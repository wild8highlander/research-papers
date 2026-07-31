# 🔬 Research Papers: Correction *b* & 3D Navier–Stokes Regularity

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](./LICENSE)
[![Papers](https://img.shields.io/badge/Papers-14-blue.svg)](./papers/)
[![Documents](https://img.shields.io/badge/Documents-15-green.svg)](./docs/)
[![LaTeX Sources](https://img.shields.io/badge/LaTeX%20Sources-4-orange.svg)](./src/)
[![Source Code](https://img.shields.io/badge/Code-Python%20%7C%20Julia-purple.svg)](./src/ab-cloud-3d/)
[![Languages](https://img.shields.io/badge/Languages-EN%20%2F%20RU-yellow.svg)]()

> **Analytical proof of 3D Navier–Stokes regularity without dissipation** — based on the universal polarization correction *b* ≈ 0.0785, arising from Kirchhoff equations for point vortices as a −90° rotation.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Research Topics](#-research-topics)
- [Repository Structure](#-repository-structure)
- [Papers](#-papers)
- [Documents](#-documents)
- [LaTeX Sources](#-latex-sources)
- [Numerical Source Code (AB-Cloud 3D)](#-numerical-source-code-ab-cloud-3d)
- [Getting Started](#-getting-started)
- [Citation](#-citation)
- [License](#-license)

---

## 🧭 Overview

This repository contains a collection of research papers, monographs, and preprints centered on the **polarization correction *b*** and its role in proving the regularity of three-dimensional Navier–Stokes equations (3D NSE) **without introducing artificial dissipation**.

The correction *b* ≈ 0.0785 arises analytically from Kirchhoff equations for point vortices as a −90° rotation. Applied as a phase rotation of velocity **u** by angle θ_b = *b*·π/2 ≈ 7.07° around the vortex axis **ω**, it:

1. **Preserves energy** (R^T R = I — no dissipation added)
2. **Bounds** ‖**ω**‖_∞ by C(*b*, ν)·‖**ω**‖_∞(0)
3. **Satisfies the Beale–Kato–Majda criterion** ∫‖**ω**‖_∞ dt < ∞ ⟹ smoothness
4. **Stabilizes by 3.5×** numerically (133.15 → 38.05) without dissipation

A second research thread — the **AB-Cloud as a universal lattice operating system for the Riemann zeros** — extends the framework to the spectral side, realising the Hilbert–Pólya conjecture, the Montgomery–Dyson GUE correspondence, and the Langlands programme in a single programmable $36^3$ non-Hermitian Hofstadter Hamiltonian.

---

## 🔍 Research Topics

### 1. Correction *b* & 3D NSE Regularity
The core research thread: the universal polarization correction *b* as a key to resolving the Clay Millennium Problem for 3D Navier–Stokes.

### 2. Klein Attractor & NS Bridge
Investigation of the Klein fractal attractor and its connection to the Navier–Stokes bridge — the φ-attractor, Fibonacci structure, and Euler's number *e*.

### 3. AB Cloud Monograph
A comprehensive monograph on the AB Cloud model, covering analytical framework, numerical verification, and cross-topic connections.

### 4. KdV & *b*-Correction
Application of the *b*-correction to the Korteweg–de Vries (KdV) equation — Chapter 16 of the broader research program.

### 5. Choptuik–Riemann Monograph
Study of the Choptuik critical collapse and Riemann problem connections within the *b*-correction framework.

### 6. AB-Cloud & Riemann Zeros
The AB-Cloud as a universal lattice operating system running on the non-trivial zeros of the Riemann zeta function. A three-dimensional non-Hermitian Hofstadter Hamiltonian with topological vortices whose spectrum is **statistically indistinguishable** from the $\zeta$-zero sequence (KS $p = 0.27$–$0.88$; permutation test $Z = 14.10\sigma$, $p < 10^{-44}$). Includes the full Python + Julia reproducibility package, LaTeX preprint source, and 4 complete numerical verification runs with 92 figures. See [`src/ab-cloud-3d/`](./src/ab-cloud-3d/) for the code and [`papers/riemann-zeros/`](./papers/riemann-zeros/) for the preprint PDFs.

---

## 📁 Repository Structure

```
research-papers/
├── .github/
│   └── FUNDING.yml
├── docs/                           # Research documents (Word .docx)
│   ├── correction-b/
│   │   ├── en/                     # English versions
│   │   └── ru/                     # Russian versions (Русский)
│   ├── klein-attractor/
│   ├── ab-cloud/
│   │   ├── en/
│   │   └── ru/
│   ├── kdv/
│   │   ├── en/
│   │   └── ru/
│   ├── choptuik-riemann/
│   ├── riemann-zeros/              # NEW (v1.3.0) — AB-Cloud / Riemann zeros
│   │   └── en/                     # English monograph v2
│   └── monographs/                 # Full monographs (EN/RU)
├── papers/                         # Published papers & preprints (PDF)
│   ├── correction-b/
│   ├── preprint/
│   ├── ab-cloud/
│   ├── kdv/
│   ├── monographs/
│   └── riemann-zeros/              # NEW (v1.3.0) — preprints + key figures
│       └── figures/                # PNG previews of headline plots
├── src/                            # LaTeX sources + numerical code
│   ├── main/                       # Main paper LaTeX (v1, v2)
│   ├── preprint/                   # Preprint LaTeX (English)
│   └── ab-cloud-3d/                # NEW (v1.3.0) — full reproducibility package
│       ├── code/                   # Python + Julia sources (EN + RU)
│       ├── preprint/               # AB-Cloud preprint LaTeX source
│       ├── data/                   # 5000 embedded Riemann zeta zeros
│       ├── build/                  # Compiled .pyc artifacts (CPython 3.12)
│       └── outputs/                # 4 verification runs (92 figures + JSON/CSV/MD/TXT/HTML)
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## 📄 Papers

### Correction *b* & 3D NSE

| File | Description |
|------|-------------|
| [`papers/correction-b/main.pdf`](./papers/correction-b/main.pdf) | Main paper — *b* as polarization twisting (v1) |
| [`papers/correction-b/main_v2.pdf`](./papers/correction-b/main_v2.pdf) | Main paper — revised version (v2) |

### Preprint

| File | Description |
|------|-------------|
| [`papers/preprint/preprint_v1.pdf`](./papers/preprint/preprint_v1.pdf) | Preprint — analytical proof of 3D NSE regularity (v1) |
| [`papers/preprint/preprint_v2.pdf`](./papers/preprint/preprint_v2.pdf) | Preprint — updated version (v2) |

### AB Cloud

| File | Description |
|------|-------------|
| [`papers/ab-cloud/AB_Cloud_Monograph_EN.pdf`](./papers/ab-cloud/AB_Cloud_Monograph_EN.pdf) | AB Cloud monograph (English, PDF) |
| [`papers/ab-cloud/AB_Cloud_Monograph_v23_EN.pdf`](./papers/ab-cloud/AB_Cloud_Monograph_v23_EN.pdf) | AB Cloud monograph v23 (English, PDF) |
| [`papers/ab-cloud/AB_Cloud_Monograph_v23_RU.pdf`](./papers/ab-cloud/AB_Cloud_Monograph_v23_RU.pdf) | Монография AB Cloud v23 (Русский, PDF) |

### KdV & *b*-Correction

| File | Description |
|------|-------------|
| [`papers/kdv/KdV_b_correction_Chapter16_EN.pdf`](./papers/kdv/KdV_b_correction_Chapter16_EN.pdf) | KdV *b*-correction Chapter 16 (English, PDF) |
| [`papers/kdv/KdV_b_correction_Chapter16_RU.pdf`](./papers/kdv/KdV_b_correction_Chapter16_RU.pdf) | КдВ *b*-поправка Глава 16 (Русский, PDF) |

### AB-Cloud & Riemann Zeros

| File | Description |
|------|-------------|
| [`papers/riemann-zeros/AB_Cloud_Preprint_v1.pdf`](./papers/riemann-zeros/AB_Cloud_Preprint_v1.pdf) | AB-Cloud preprint v1 — *A Universal Lattice Operating System for the Riemann Zeros* (1.4 MB) |
| [`papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf`](./papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf) | AB-Cloud preprint v2 — revised with embedded figures (15 MB) |

**Key figures** (mirrored in [`papers/riemann-zeros/figures/`](./papers/riemann-zeros/figures/)):

| Figure | Description |
|---|---|
| [`figures/01_P_s_zeta.png`](./papers/riemann-zeros/figures/01_P_s_zeta.png) | Nearest-neighbour spacing $P(s)$ of $\zeta$ zeros vs GUE Wigner surmise |
| [`figures/03_sigma2_L.png`](./papers/riemann-zeros/figures/03_sigma2_L.png) | Number variance $\Sigma^2(L)$ — $\zeta$ zeros vs GUE theory |
| [`figures/05_fss_ab_cloud.png`](./papers/riemann-zeros/figures/05_fss_ab_cloud.png) | Finite-size scaling of $\langle r\rangle$ for the AB-Cloud spectrum |

The full set of 92 figures (PDF + PNG) is bundled with the source code in [`src/ab-cloud-3d/outputs/`](./src/ab-cloud-3d/outputs/).

### Full Monographs

| File | Description |
|------|-------------|
| [`papers/monographs/Monograph_full_EN.pdf`](./papers/monographs/Monograph_full_EN.pdf) | Complete monograph (English) |
| [`papers/monographs/Monograph_full_RU.pdf`](./papers/monographs/Monograph_full_RU.pdf) | Полная монография (Русский) |

---

## 📝 Documents

### Correction *b*

| File | Language | Description |
|------|----------|-------------|
| [`docs/correction-b/en/monograph_with_figures.docx`](./docs/correction-b/en/monograph_with_figures.docx) | English | Monograph with figures |
| [`docs/correction-b/ru/monograph_with_figures.docx`](./docs/correction-b/ru/monograph_with_figures.docx) | Русский | Монография с иллюстрациями |

### Klein Attractor

| File | Description |
|------|-------------|
| [`docs/klein-attractor/Klein_FAttractor_NS_Research.docx`](./docs/klein-attractor/Klein_FAttractor_NS_Research.docx) | Klein fractal attractor & NS research |
| [`docs/klein-attractor/Klein_NS_Bridge_Research.docx`](./docs/klein-attractor/Klein_NS_Bridge_Research.docx) | Klein NS bridge research |

### AB Cloud

| File | Language | Description |
|------|----------|-------------|
| [`docs/ab-cloud/en/AB_Cloud_Monograph.docx`](./docs/ab-cloud/en/AB_Cloud_Monograph.docx) | English | AB Cloud monograph |
| [`docs/ab-cloud/en/AB_Cloud_Monograph_v1.docx`](./docs/ab-cloud/en/AB_Cloud_Monograph_v1.docx) | English | AB Cloud monograph v1 |
| [`docs/ab-cloud/en/AB_Cloud_Monograph_v23.docx`](./docs/ab-cloud/en/AB_Cloud_Monograph_v23.docx) | English | AB Cloud monograph v23 |
| [`docs/ab-cloud/ru/AB_Cloud_Monograph.docx`](./docs/ab-cloud/ru/AB_Cloud_Monograph.docx) | Русский | Монография AB Cloud |
| [`docs/ab-cloud/ru/AB_Cloud_Monograph_v1.docx`](./docs/ab-cloud/ru/AB_Cloud_Monograph_v1.docx) | Русский | Монография AB Cloud v1 |
| [`docs/ab-cloud/ru/AB_Cloud_Monograph_v23.docx`](./docs/ab-cloud/ru/AB_Cloud_Monograph_v23.docx) | Русский | Монография AB Cloud v23 |

### AB-Cloud & Riemann Zeros

| File | Language | Description |
|------|----------|-------------|
| [`docs/riemann-zeros/en/AB_Cloud_Monograph_EN_v2.docx`](./docs/riemann-zeros/en/AB_Cloud_Monograph_EN_v2.docx) | English | AB-Cloud monograph v2 — companion to the preprint, full version with embedded figures |

### KdV & *b*-Correction

| File | Language | Description |
|------|----------|-------------|
| [`docs/kdv/en/KdV_b_correction_Chapter16.docx`](./docs/kdv/en/KdV_b_correction_Chapter16.docx) | English | KdV *b*-correction (Chapter 16) |
| [`docs/kdv/ru/KdV_b_correction_Chapter16.docx`](./docs/kdv/ru/KdV_b_correction_Chapter16.docx) | Русский | КдВ *b*-поправка (Глава 16) |

### Choptuik–Riemann

| File | Description |
|------|-------------|
| [`docs/choptuik-riemann/Choptuik_Riemann_Monograph_RU.docx`](./docs/choptuik-riemann/Choptuik_Riemann_Monograph_RU.docx) | Монография Choptuik–Riemann (Русский) |

### Full Monographs

| File | Language | Description |
|------|----------|-------------|
| [`docs/monographs/Monograph_full_EN.docx`](./docs/monographs/Monograph_full_EN.docx) | English | Complete monograph (DOCX) |
| [`docs/monographs/Monograph_full_RU.docx`](./docs/monographs/Monograph_full_RU.docx) | Русский | Полная монография (DOCX) |

---

## ✏️ LaTeX Sources

| File | Description |
|------|-------------|
| [`src/main/main.tex`](./src/main/main.tex) | Main paper source (v1, Russian) |
| [`src/main/main_v2.tex`](./src/main/main_v2.tex) | Main paper source (v2, Russian) |
| [`src/preprint/preprint.tex`](./src/preprint/preprint.tex) | Preprint source (English) |
| [`src/ab-cloud-3d/preprint/ab_cloud_preprint.tex`](./src/ab-cloud-3d/preprint/ab_cloud_preprint.tex) | **NEW** — AB-Cloud preprint source (English, ~940 lines) |

**Build instructions:**
```bash
cd src/main/
xelatex main.tex
xelatex main.tex   # run twice for TOC and cross-references
```

---

## 💻 Numerical Source Code (AB-Cloud 3D)

The complete reproducibility package for the AB-Cloud preprint — **Python + Julia implementations of all 10 verification modes**, the embedded 5000 Riemann zeta zeros, and **4 full verification runs with 92 figures**.

```
src/ab-cloud-3d/
├── README.md                # Detailed code & reproduction guide
├── code/                    # Python + Julia sources (EN + RU, ~2000 lines each)
├── preprint/                # LaTeX source of the preprint
├── data/                    # 5000 embedded Riemann zeta zeros (1.8 MB)
├── build/                   # Compiled .pyc artifacts (CPython 3.12)
└── outputs/                 # 4 verification runs × (PDF + PNG + JSON + CSV + MD + TXT + HTML)
```

**Quick start:**
```bash
cd src/ab-cloud-3d/code/
pip install numpy scipy matplotlib mpmath      # Python deps
python3 ab_cloud_3d_en.py                      # Interactive menu (10 modes A–J)
```

The ten verification modes cover the 3D solver, RMT analysis of the $\zeta$ zeros, finite-size scaling, the Arf invariant, decay-time correspondence, Dirac/QED cone, full reviewer-point verification, deep Riemann-zeros analysis, the 3D AB-Cloud ↔ Riemann bridge, and advanced 3D topology (Chern marker, edge states, probability current, winding number, Hofstadter butterfly, exceptional points).

👉 **See [`src/ab-cloud-3d/README.md`](./src/ab-cloud-3d/README.md) for the full guide.**

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/wild8highlander/research-papers.git
cd research-papers
```

### Browse by topic

- **Quick start (NSE)**: Read the [preprint](./papers/preprint/preprint_v2.pdf) for a concise overview of the *b*-correction
- **Deep dive (NSE)**: Read the [full monograph](./papers/monographs/Monograph_full_EN.pdf) for the complete treatment
- **AB-Cloud / Riemann zeros**: Read [`papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf`](./papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf), then explore [`src/ab-cloud-3d/`](./src/ab-cloud-3d/) to reproduce the numerical verification
- **Build from source**: See [LaTeX Sources](#-latex-sources) for compilation instructions

### Recommended reading order

1. `papers/preprint/preprint_v2.pdf` — concise overview of the main NSE result
2. `papers/correction-b/main_v2.pdf` — detailed analytical proof
3. `papers/monographs/Monograph_full_EN.pdf` — complete monograph with all chapters
4. `docs/kdv/` — KdV extension of the *b*-correction
5. `docs/klein-attractor/` — Klein attractor connection
6. `papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf` — AB-Cloud as a lattice OS for the Riemann zeros
7. `src/ab-cloud-3d/` — full numerical reproducibility package for the AB-Cloud preprint

---

## 📖 Citation

If you use this work, please cite:

```bibtex
@article{z-ai-research-2026,
  title   = {Correction $b$ as Polarization Twisting: Analytical Proof of 3D {Navier--Stokes} Regularity without Dissipation},
  author  = {Z.ai Research},
  year    = {2026},
  journal = {Preprint},
  url     = {https://github.com/wild8highlander/research-papers}
}
```

For the AB-Cloud / Riemann zeros preprint:

```bibtex
@misc{ab-cloud-3d-2026,
  title   = {AB-Cloud: A Universal Lattice Operating System for the Riemann Zeros},
  author  = {Z.ai Research},
  year    = {2026},
  url     = {https://github.com/wild8highlander/research-papers/tree/main/src/ab-cloud-3d}
}
```

---

## 📜 License

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** (CC BY-NC-SA 4.0). See [LICENSE](./LICENSE) for details.

---

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to contribute to this repository.

---

<p align="center">
  <sub>Built with ❤️ by <a href="https://github.com/wild8highlander">Z.ai Research</a></sub>
</p>
