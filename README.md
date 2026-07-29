# 🔬 Research Papers: Correction *b* & 3D Navier–Stokes Regularity

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Papers](https://img.shields.io/badge/Papers-12-blue.svg)](./papers/)
[![Documents](https://img.shields.io/badge/Documents-14-green.svg)](./docs/)
[![LaTeX Sources](https://img.shields.io/badge/LaTeX%20Sources-3-orange.svg)](./src/)
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
│   └── monographs/                 # Full monographs (EN/RU)
├── papers/                         # Published papers & preprints (PDF)
│   ├── correction-b/
│   ├── preprint/
│   ├── ab-cloud/
│   ├── kdv/
│   └── monographs/
├── src/                            # LaTeX source files
│   ├── main/
│   └── preprint/
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

**Build instructions:**
```bash
cd src/main/
xelatex main.tex
xelatex main.tex   # run twice for TOC and cross-references
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/research-papers.git
cd research-papers
```

### Browse by topic

- **Quick start**: Read the [preprint](./papers/preprint/preprint_v2.pdf) for a concise overview
- **Deep dive**: Read the [full monograph](./papers/monographs/Monograph_full_EN.pdf) for the complete treatment
- **Build from source**: See [LaTeX Sources](#-latex-sources) for compilation instructions

### Recommended reading order

1. `papers/preprint/preprint_v2.pdf` — concise overview of the main result
2. `papers/correction-b/main_v2.pdf` — detailed analytical proof
3. `papers/monographs/Monograph_full_EN.pdf` — complete monograph with all chapters
4. `docs/kdv/` — KdV extension of the *b*-correction
5. `docs/klein-attractor/` — Klein attractor connection

---

## 📖 Citation

If you use this work, please cite:

```bibtex
@article{z-ai-research-2026,
  title   = {Correction $b$ as Polarization Twisting: Analytical Proof of 3D {Navier--Stokes} Regularity without Dissipation},
  author  = {Z.ai Research},
  year    = {2026},
  journal = {Preprint},
  url     = {https://github.com/your-username/research-papers}
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
  <sub>Built with ❤️ by <a href="https://github.com/your-username">Z.ai Research</a></sub>
</p>
