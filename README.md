<div align="center">

# 🔬 Research Papers

### Correction *b* & 3D Navier–Stokes Regularity · AB-Cloud · Riemann Zeros

</div>

<div align="center">

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?style=flat-square)](./LICENSE)
[![Papers](https://img.shields.io/badge/Papers-14-blue.svg?style=flat-square)](./papers/)
[![Documents](https://img.shields.io/badge/Documents-15-green.svg?style=flat-square)](./docs/)
[![Code](https://img.shields.io/badge/Code-Python%20%7C%20Julia-purple.svg?style=flat-square)](./src/ab-cloud-3d/)
[![Languages](https://img.shields.io/badge/Languages-EN%20%2F%20RU-yellow.svg?style=flat-square)]()
[![Last Commit](https://img.shields.io/github/last-commit/wild8highlander/research-papers?label=Last%20commit&style=flat-square)](https://github.com/wild8highlander/research-papers/commits/main)
[![Repo Size](https://img.shields.io/github/languages/code-size/wild8highlander/research-papers?label=Repo%20size&style=flat-square)](https://github.com/wild8highlander/research-papers)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB.svg?logo=python&logoColor=white&style=flat-square)](https://www.python.org/)

</div>

---

> **Analytical proof of 3D Navier–Stokes regularity without artificial dissipation**, grounded in the universal polarization correction *b* ≈ 0.0785 from Kirchhoff point-vortex equations, together with the **AB-Cloud** — a 36³ non-Hermitian Hofstadter Hamiltonian whose spectrum is statistically indistinguishable from the Riemann ζ-zeros, realising the Hilbert–Pólya conjecture, Montgomery–Dyson GUE correspondence, and a concrete bridge to the Langlands programme.

---

## 🏆 Key Results

### 3D Navier–Stokes Regularity

| Property | Value | Significance |
|:---------|:------|:-------------|
| Polarization correction *b* | ≈ 0.0785 | Universal constant from Kirchhoff vortex equations |
| Rotation angle θ_b | ≈ 7.07° | Phase rotation of velocity **u** around vortex axis **ω** |
| Stabilization factor | **3.5×** (133.15 → 38.05) | Without adding dissipation |
| Energy preservation | RᵀR = I | Rotation, not damping — no energy lost |
| BKM criterion satisfied | ∫‖**ω**‖_∞ dt < ∞ | ⟹ global-in-time smoothness |

### AB-Cloud & Riemann Zeros

| Property | Value | Significance |
|:---------|:------|:-------------|
| KS test *p*-value | **0.27–0.88** | AB-Cloud spectrum indistinguishable from ζ-zeros |
| L² distance P(s) | 0.0127 | 34× closer than either to GUE Wigner surmise |
| Permutation test | **Z = 14.10σ** (p < 10⁻⁴⁴) | Excludes randomness at extraordinary significance |
| ⟨r⟩ value | 0.6159 (GUE: 0.5996) | Within 2.7% of GUE theory |
| Arf invariant | 0 | Preserved across all 5 lattice resolutions |
| Lattice size | 36³ = 46,656 sites | Non-Hermitian Hofstadter Hamiltonian |

---

## 📑 Table of Contents

- [🔍 Overview](#-overview)
- [🧪 Research Topics](#-research-topics)
- [📁 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
- [💻 Usage](#-usage)
- [📊 Verification Results](#-verification-results)
- [📄 Papers & Documents](#-papers--documents)
- [📖 Citation](#-citation)
- [🤝 Contributing](#-contributing)
- [⚖️ License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🔍 Overview

This repository presents a unified research program spanning **fluid dynamics, spectral theory, and number theory**, with two deeply interlocked threads:

**Thread 1 — 3D Navier–Stokes Regularity.** The Clay Millennium Problem for the three-dimensional Navier–Stokes equations asks whether smooth initial data remain smooth for all time. We introduce the **polarization correction *b* ≈ 0.0785**, an analytically derived constant arising from the Kirchhoff equations for point vortices as a −90° rotation. Applied as a phase rotation of the velocity field **u** by angle θ_b = *b*·π/2 ≈ 7.07° around the vortex axis **ω**, this correction:

1. **Preserves energy** — the transformation R satisfies RᵀR = I, so no artificial dissipation is introduced.
2. **Bounds the vorticity supremum** — ‖**ω**‖_∞ is controlled by C(*b*, ν)·‖**ω**‖_∞(0).
3. **Satisfies the Beale–Kato–Majda criterion** — ∫‖**ω**‖_∞ dt < ∞, which implies global smoothness.
4. **Stabilizes by 3.5×** numerically (133.15 → 38.05), confirming the analytical prediction.

**Thread 2 — AB-Cloud & Riemann Zeros.** The **AB-Cloud** is a universal lattice operating system running on the non-trivial zeros of the Riemann zeta function. It is constructed as a 36³ non-Hermitian Hofstadter Hamiltonian with topological vortices whose unfolded eigenvalue spectrum is **statistically indistinguishable** from the ζ-zero sequence. This single object simultaneously realises:

- The **Hilbert–Pólya conjecture** — a self-adjoint (after symmetrisation) operator whose eigenvalues encode the Riemann zeros.
- The **Montgomery–Dyson GUE correspondence** — pair correlation of the AB-Cloud spectrum matches the Gaussian Unitary Ensemble prediction.
- A concrete bridge to the **Langlands programme** — the automorphic–spectral duality is instantiated in the lattice's topological structure.

The complete numerical reproducibility package — 92 Python files, 3 Julia files, 5,000 embedded ζ-zeros, and 4 full verification runs with 92 figures — is included in [`src/ab-cloud-3d/`](./src/ab-cloud-3d/).

---

## 🧪 Research Topics

### 1. Correction *b* & 3D NSE Regularity

The core research thread. The universal polarization correction *b* ≈ 0.0785 is derived analytically from the Kirchhoff point-vortex equations as a −90° rotation. When applied to the 3D Navier–Stokes velocity field, it yields an energy-preserving transformation that satisfies the Beale–Kato–Majda regularity criterion without any artificial dissipation — directly addressing the Clay Millennium Problem. The numerical verification confirms a **3.5× stabilization** of the vorticity supremum.

### 2. Klein Attractor & Navier–Stokes Bridge

Investigation of the **Klein fractal attractor** and its structural connection to the Navier–Stokes equations. The φ-attractor, Fibonacci self-similarity, and Euler's number *e* emerge as geometric signatures linking the chaotic dynamics of the NSE to a universal fractal skeleton. This bridge provides a geometric lens through which the *b*-correction's stabilizing action can be interpreted as a constraint on the attractor's fractal dimension.

### 3. AB-Cloud Monograph

A comprehensive monograph on the **AB-Cloud model**, covering the full analytical framework, detailed numerical verification, and cross-topic connections. The AB-Cloud is presented as a programmable lattice operating system whose spectral properties encode deep arithmetic information — the non-trivial zeros of the Riemann zeta function.

### 4. KdV & *b*-Correction

Application of the *b*-correction framework to the **Korteweg–de Vries (KdV) equation**. Just as in the NSE case, the polarization rotation induces a stabilization of the KdV soliton dynamics without altering the Hamiltonian structure. This chapter (Chapter 16 of the broader research program) demonstrates the universality of *b* across integrable and near-integrable PDE systems.

### 5. Choptuik–Riemann Monograph

Study of the **Choptuik critical collapse** and its unexpected connection to the Riemann problem within the *b*-correction framework. The critical exponent in Type II gravitational collapse mirrors the scaling exponents arising in the spectral analysis of the AB-Cloud, suggesting a universality class shared between gravitational criticality and zeta-zero statistics.

### 6. AB-Cloud & Riemann Zeros

The AB-Cloud as a **universal lattice operating system** running on the non-trivial zeros of the Riemann zeta function. A three-dimensional 36³ non-Hermitian Hofstadter Hamiltonian with topological vortices whose spectrum is **statistically indistinguishable** from the ζ-zero sequence (KS *p* = 0.27–0.88; permutation test Z = 14.10σ, *p* < 10⁻⁴⁴). This construction realises the Hilbert–Pólya conjecture, the Montgomery–Dyson GUE correspondence, and provides a spectral-theoretic bridge to the Langlands programme. The full Python + Julia reproducibility package, LaTeX preprint source, and 4 complete numerical verification runs with 92 figures are included. See [`src/ab-cloud-3d/`](./src/ab-cloud-3d/) for the code and [`papers/riemann-zeros/`](./papers/riemann-zeros/) for the preprint PDFs.

---

## 📁 Repository Structure

```
research-papers/
├── .github/
│   ├── FUNDING.yml                        # GitHub Sponsors configuration
│   └── workflows/
│       └── ci.yml                         # CI: syntax check on Python 3.10/3.11/3.12
│
├── papers/                                # 📄 Published papers & preprints (PDF)
│   ├── correction-b/                      #   Main b-correction papers (v1, v2)
│   ├── preprint/                          #   NSE regularity preprints (v1, v2)
│   ├── ab-cloud/                          #   AB Cloud monographs (EN, RU, v23)
│   ├── kdv/                               #   KdV b-correction Chapter 16 (EN, RU)
│   ├── monographs/                        #   Full monographs (EN, RU)
│   └── riemann-zeros/                     #   AB-Cloud / Riemann zeros preprints
│       └── figures/                       #     PNG previews of headline plots
│
├── docs/                                  # 📝 Research documents (Word .docx)
│   ├── correction-b/                      #   b-correction monographs (EN + RU)
│   │   ├── en/
│   │   └── ru/
│   ├── klein-attractor/                   #   Klein attractor & NS bridge
│   ├── ab-cloud/                          #   AB Cloud monographs (EN + RU)
│   │   ├── en/
│   │   └── ru/
│   ├── kdv/                               #   KdV b-correction (EN + RU)
│   │   ├── en/
│   │   └── ru/
│   ├── choptuik-riemann/                  #   Choptuik–Riemann monograph (RU)
│   ├── riemann-zeros/                     #   AB-Cloud Riemann zeros (EN v2)
│   │   └── en/
│   └── monographs/                        #   Full monographs (EN + RU)
│
├── src/                                   # 💻 LaTeX sources + numerical code
│   ├── main/                              #   Main paper LaTeX (v1, v2)
│   ├── preprint/                          #   Preprint LaTeX (English)
│   └── ab-cloud-3d/                       #   Full reproducibility package
│       ├── code/                          #     92 Python + 3 Julia files (EN + RU)
│       ├── preprint/                      #     AB-Cloud preprint LaTeX source
│       ├── data/                          #     5,000 embedded Riemann zeta zeros
│       ├── build/                         #     Compiled .pyc artifacts (CPython 3.12)
│       ├── outputs/                       #     4 verification runs (92 figures + reports)
│       ├── requirements.txt               #     Python dependencies
│       ├── pyproject.toml                 #     Package configuration
│       └── README.md                      #     Detailed code & reproduction guide
│
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                                # CC BY-NC-SA 4.0
└── README.md                              # ← You are here
```

---

## 🚀 Getting Started

### Prerequisites

| Dependency | Version | Purpose |
|:-----------|:--------|:--------|
| Python | 3.10, 3.11, or 3.12 | Numerical verification, figure generation |
| Julia | ≥ 1.8 | Alternative solver implementation |
| XeLaTeX | ≥ 2020 | Compiling LaTeX paper sources |

### Clone the Repository

```bash
git clone https://github.com/wild8highlander/research-papers.git
cd research-papers
```

### Install Python Dependencies

```bash
cd src/ab-cloud-3d/
pip install -r requirements.txt
```

Or install as an editable package:

```bash
cd src/ab-cloud-3d/
pip install -e .
```

### Quick Start — Browse by Topic

| Goal | Resource |
|:-----|:---------|
| **Concise NSE overview** | [`papers/preprint/preprint_v2.pdf`](./papers/preprint/preprint_v2.pdf) |
| **Full NSE treatment** | [`papers/monographs/Monograph_full_EN.pdf`](./papers/monographs/Monograph_full_EN.pdf) |
| **AB-Cloud / Riemann zeros** | [`papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf`](./papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf) |
| **Run verification** | [`src/ab-cloud-3d/`](./src/ab-cloud-3d/) |

### Recommended Reading Order

1. `papers/preprint/preprint_v2.pdf` — concise overview of the main NSE result
2. `papers/correction-b/main_v2.pdf` — detailed analytical proof
3. `papers/monographs/Monograph_full_EN.pdf` — complete monograph with all chapters
4. `docs/kdv/` — KdV extension of the *b*-correction
5. `docs/klein-attractor/` — Klein attractor connection
6. `papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf` — AB-Cloud as a lattice OS for Riemann zeros
7. `src/ab-cloud-3d/` — full numerical reproducibility package

---

## 💻 Usage

### Run the Interactive AB-Cloud Simulation

The main entry point provides an interactive menu with **10 verification modes (A–J)**:

```bash
cd src/ab-cloud-3d/
python code/ab_cloud_3d_en.py
```

| Mode | Label | Description |
|:-----|:------|:------------|
| A | 3D Solver | Full 3D AB-Cloud lattice simulation |
| B | RMT Analysis | Random Matrix Theory analysis of ζ-zeros |
| C | Finite-Size Scaling | ⟨r⟩ scaling across lattice resolutions |
| D | Arf Invariant | Topological Arf invariant computation |
| E | Decay-Time | Decay-time correspondence mapping |
| F | Dirac/QED Cone | Dirac cone and QED spectral structure |
| G | Reviewer Points | Full reviewer-point-by-point verification |
| H | Deep Riemann Zeros | Deep ζ-zero spectral analysis |
| I | 3D Bridge | 3D AB-Cloud ↔ Riemann bridge verification |
| J | Advanced 3D Topology | Chern marker, edge states, probability current, winding number, Hofstadter butterfly, exceptional points |

### Run Individual Verification Modes (Non-Interactive)

```bash
# Full verification (modes A–G)
python code/run_verification.py

# Extended verification (all modes)
python code/run_verification_extended.py

# Generate reports
python code/generate_report_en.py
python code/generate_report_v4_en.py
```

### Build LaTeX Papers from Source

```bash
# Main paper
cd src/main/
xelatex main.tex && xelatex main.tex

# Preprint
cd src/preprint/
xelatex preprint.tex && xelatex preprint.tex

# AB-Cloud preprint (~940 lines)
cd src/ab-cloud-3d/preprint/
xelatex ab_cloud_preprint.tex && xelatex ab_cloud_preprint.tex
```

> **Note:** Always run XeLaTeX twice to resolve cross-references and table of contents.

### Reproduce All Figures

The 92 figures across 4 verification runs are fully reproducible:

```bash
cd src/ab-cloud-3d/
python code/ab_cloud_3d_en.py   # Select mode G for full verification
# Output saved to outputs/ with PDF + PNG + JSON + CSV + MD + TXT + HTML
```

---

## 📊 Verification Results

Four complete numerical verification runs are stored in [`src/ab-cloud-3d/outputs/`](./src/ab-cloud-3d/outputs/), producing **92 figures** in total:

### Run 1 — Full Verification

| | |
|:--|:--|
| **Directory** | `outputs/full_verification_2026-07-31_15-33-39/` |
| **Figures** | 11 (PDF + PNG) |
| **Reports** | JSON, CSV, MD, TXT, HTML |

| Figure | Description |
|:-------|:------------|
| `01_P_s_zeta` | Nearest-neighbour spacing P(s) of ζ-zeros vs GUE Wigner surmise |
| `02_delta3_L` | Three-point correlation Δ₃(L) |
| `03_sigma2_L` | Number variance Σ²(L) — ζ-zeros vs GUE theory |
| `04_fss_zeta` | Finite-size scaling of ⟨r⟩ for ζ-zeros |
| `05_fss_ab_cloud` | Finite-size scaling of ⟨r⟩ for AB-Cloud spectrum |
| `06_arf_invariant` | Arf invariant across lattice resolutions |
| `07_decay_time` | Decay-time correspondence |
| `08_dirac_cone` | Dirac cone spectral structure |
| `09_3d_complex_spectrum` | 3D AB-Cloud complex spectrum |
| `10_3d_P_s` | 3D AB-Cloud spacing distribution |
| `11_3d_skin_effect` | 3D skin effect visualization |

### Run 2 — Deep Riemann Zeros Analysis

| | |
|:--|:--|
| **Directory** | `outputs/deep_zeros_2026-07-31_15-36-34/` |
| **Figures** | 6 (PDF + PNG) |
| **Reports** | JSON, CSV, MD, TXT, HTML |

| Figure | Description |
|:-------|:------------|
| `nn_spacing_pdf` | Nearest-neighbour spacing PDF |
| `pair_correlation_R2` | Pair correlation R₂ |
| `form_factor_K` | Spectral form factor K(τ) |
| `S_T_fluctuation` | S(T) fluctuation analysis |
| `decay_time_from_zeros` | Decay-time from deep zeros |

### Run 3 — 3D AB-Cloud ↔ Riemann Bridge

| | |
|:--|:--|
| **Directory** | `outputs/3d_bridge_2026-07-31_15-36-37/` |
| **Figures** | 16 (PDF + PNG) |
| **Reports** | JSON, CSV, MD, TXT, HTML |

| Figure | Description |
|:-------|:------------|
| `3d_pair_corr_landscape` | 3D pair correlation landscape |
| `3d_form_factor_surface_ab` | Form factor surface (AB-Cloud) |
| `3d_form_factor_surface_ri` | Form factor surface (Riemann) |
| `3d_spectral_staircase` | Spectral staircase N(E) |
| `3d_decay_time_manifold` | Decay-time manifold |
| `3d_dirac_cone_family` | Dirac cone family |
| `3d_wavefunction_density` | Wavefunction density |
| `3d_topo_phase_diagram` | Topological phase diagram |
| `ab_cloud_riemann_overlay` | AB-Cloud ↔ Riemann spectral overlay |
| `3d_S_T_overlay` | S(T) overlay comparison |

### Run 4 — Advanced 3D Topology

| | |
|:--|:--|
| **Directory** | `outputs/3d_advanced_2026-07-31_15-51-47/` |
| **Figures** | 7 (PDF + PNG) |
| **Reports** | JSON, CSV, MD, TXT, HTML |

| Figure | Description |
|:-------|:------------|
| `local_chern_marker_surface` | Local Chern marker (3D surface) |
| `local_chern_marker_heatmap` | Local Chern marker (heatmap) |
| `edge_state_localization` | Edge-state localization profile |
| `3d_hofstadter_butterfly` | 3D Hofstadter butterfly |
| `3d_exceptional_points` | Exceptional points of the non-Hermitian Hamiltonian |
| `3d_spectral_flow` | Spectral flow under parameter deformation |
| `3d_winding_number` | Winding number computation |
| `3d_probability_current` | Probability current field |

> Each run produces multi-format output: **PDF** (publication quality), **PNG** (preview), **JSON** (structured data), **CSV** (tabular summary), **Markdown** (readable report), **TXT** (plain text), and **HTML** (interactive report).

---

## 📄 Papers & Documents

### Papers (PDF)

#### Correction *b* & 3D NSE

| File | Description |
|:-----|:------------|
| [`papers/correction-b/main.pdf`](./papers/correction-b/main.pdf) | Main paper — *b* as polarization twisting (v1) |
| [`papers/correction-b/main_v2.pdf`](./papers/correction-b/main_v2.pdf) | Main paper — revised version (v2) |

#### Preprint

| File | Description |
|:-----|:------------|
| [`papers/preprint/preprint_v1.pdf`](./papers/preprint/preprint_v1.pdf) | Preprint — analytical proof of 3D NSE regularity (v1) |
| [`papers/preprint/preprint_v2.pdf`](./papers/preprint/preprint_v2.pdf) | Preprint — updated version (v2) |

#### AB Cloud

| File | Description |
|:-----|:------------|
| [`papers/ab-cloud/AB_Cloud_Monograph_EN.pdf`](./papers/ab-cloud/AB_Cloud_Monograph_EN.pdf) | AB Cloud monograph (English) |
| [`papers/ab-cloud/AB_Cloud_Monograph_v23_EN.pdf`](./papers/ab-cloud/AB_Cloud_Monograph_v23_EN.pdf) | AB Cloud monograph v23 (English) |
| [`papers/ab-cloud/AB_Cloud_Monograph_v23_RU.pdf`](./papers/ab-cloud/AB_Cloud_Monograph_v23_RU.pdf) | Монография AB Cloud v23 (Русский) |

#### KdV & *b*-Correction

| File | Description |
|:-----|:------------|
| [`papers/kdv/KdV_b_correction_Chapter16_EN.pdf`](./papers/kdv/KdV_b_correction_Chapter16_EN.pdf) | KdV *b*-correction Chapter 16 (English) |
| [`papers/kdv/KdV_b_correction_Chapter16_RU.pdf`](./papers/kdv/KdV_b_correction_Chapter16_RU.pdf) | КдВ *b*-поправка Глава 16 (Русский) |

#### AB-Cloud & Riemann Zeros

| File | Description |
|:-----|:------------|
| [`papers/riemann-zeros/AB_Cloud_Preprint_v1.pdf`](./papers/riemann-zeros/AB_Cloud_Preprint_v1.pdf) | AB-Cloud preprint v1 (1.4 MB) |
| [`papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf`](./papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf) | AB-Cloud preprint v2 — revised with embedded figures (15 MB) |

**Key figures** (mirrored in [`papers/riemann-zeros/figures/`](./papers/riemann-zeros/figures/)):

| Figure | Description |
|:-------|:------------|
| [`01_P_s_zeta.png`](./papers/riemann-zeros/figures/01_P_s_zeta.png) | Spacing P(s) of ζ-zeros vs GUE Wigner surmise |
| [`03_sigma2_L.png`](./papers/riemann-zeros/figures/03_sigma2_L.png) | Number variance Σ²(L) — ζ-zeros vs GUE |
| [`05_fss_ab_cloud.png`](./papers/riemann-zeros/figures/05_fss_ab_cloud.png) | Finite-size scaling of ⟨r⟩ for AB-Cloud |

#### Full Monographs

| File | Description |
|:-----|:------------|
| [`papers/monographs/Monograph_full_EN.pdf`](./papers/monographs/Monograph_full_EN.pdf) | Complete monograph (English) |
| [`papers/monographs/Monograph_full_RU.pdf`](./papers/monographs/Monograph_full_RU.pdf) | Полная монография (Русский) |

### Documents (Word .docx)

#### Correction *b*

| File | Language | Description |
|:-----|:---------|:------------|
| [`docs/correction-b/en/monograph_with_figures.docx`](./docs/correction-b/en/monograph_with_figures.docx) | English | Monograph with figures |
| [`docs/correction-b/ru/monograph_with_figures.docx`](./docs/correction-b/ru/monograph_with_figures.docx) | Русский | Монография с иллюстрациями |

#### Klein Attractor

| File | Description |
|:-----|:------------|
| [`docs/klein-attractor/Klein_FAttractor_NS_Research.docx`](./docs/klein-attractor/Klein_FAttractor_NS_Research.docx) | Klein fractal attractor & NS research |
| [`docs/klein-attractor/Klein_NS_Bridge_Research.docx`](./docs/klein-attractor/Klein_NS_Bridge_Research.docx) | Klein NS bridge research |

#### AB Cloud

| File | Language | Description |
|:-----|:---------|:------------|
| [`docs/ab-cloud/en/AB_Cloud_Monograph.docx`](./docs/ab-cloud/en/AB_Cloud_Monograph.docx) | English | AB Cloud monograph |
| [`docs/ab-cloud/en/AB_Cloud_Monograph_v1.docx`](./docs/ab-cloud/en/AB_Cloud_Monograph_v1.docx) | English | AB Cloud monograph v1 |
| [`docs/ab-cloud/en/AB_Cloud_Monograph_v23.docx`](./docs/ab-cloud/en/AB_Cloud_Monograph_v23.docx) | English | AB Cloud monograph v23 |
| [`docs/ab-cloud/ru/AB_Cloud_Monograph.docx`](./docs/ab-cloud/ru/AB_Cloud_Monograph.docx) | Русский | Монография AB Cloud |
| [`docs/ab-cloud/ru/AB_Cloud_Monograph_v1.docx`](./docs/ab-cloud/ru/AB_Cloud_Monograph_v1.docx) | Русский | Монография AB Cloud v1 |
| [`docs/ab-cloud/ru/AB_Cloud_Monograph_v23.docx`](./docs/ab-cloud/ru/AB_Cloud_Monograph_v23.docx) | Русский | Монография AB Cloud v23 |

#### AB-Cloud & Riemann Zeros

| File | Language | Description |
|:-----|:---------|:------------|
| [`docs/riemann-zeros/en/AB_Cloud_Monograph_EN_v2.docx`](./docs/riemann-zeros/en/AB_Cloud_Monograph_EN_v2.docx) | English | AB-Cloud monograph v2 — companion to the preprint |

#### KdV & *b*-Correction

| File | Language | Description |
|:-----|:---------|:------------|
| [`docs/kdv/en/KdV_b_correction_Chapter16.docx`](./docs/kdv/en/KdV_b_correction_Chapter16.docx) | English | KdV *b*-correction (Chapter 16) |
| [`docs/kdv/ru/KdV_b_correction_Chapter16.docx`](./docs/kdv/ru/KdV_b_correction_Chapter16.docx) | Русский | КдВ *b*-поправка (Глава 16) |

#### Choptuik–Riemann

| File | Description |
|:-----|:------------|
| [`docs/choptuik-riemann/Choptuik_Riemann_Monograph_RU.docx`](./docs/choptuik-riemann/Choptuik_Riemann_Monograph_RU.docx) | Монография Choptuik–Riemann (Русский) |

#### Full Monographs

| File | Language | Description |
|:-----|:---------|:------------|
| [`docs/monographs/Monograph_full_EN.docx`](./docs/monographs/Monograph_full_EN.docx) | English | Complete monograph |
| [`docs/monographs/Monograph_full_RU.docx`](./docs/monographs/Monograph_full_RU.docx) | Русский | Полная монография |

### LaTeX Sources

| File | Description |
|:-----|:------------|
| [`src/main/main.tex`](./src/main/main.tex) | Main paper source (v1, Russian) |
| [`src/main/main_v2.tex`](./src/main/main_v2.tex) | Main paper source (v2, Russian) |
| [`src/preprint/preprint.tex`](./src/preprint/preprint.tex) | Preprint source (English) |
| [`src/ab-cloud-3d/preprint/ab_cloud_preprint.tex`](./src/ab-cloud-3d/preprint/ab_cloud_preprint.tex) | AB-Cloud preprint source (English, ~940 lines) |

---

## 📖 Citation

If you use this work in your research, please cite the relevant papers:

**Correction *b* & 3D NSE Regularity:**

```bibtex
@article{isaev2026bcorrection,
  title     = {Correction {$b$} as Polarization Twisting: Analytical Proof of
               3D {Navier--Stokes} Regularity without Dissipation},
  author    = {Isaev, Ishak Hamzatovich},
  year      = {2026},
  journal   = {Preprint},
  url       = {https://github.com/wild8highlander/research-papers}
}
```

**AB-Cloud & Riemann Zeros:**

```bibtex
@misc{isaev2026abcloud3d,
  title     = {{AB-Cloud}: A Universal Lattice Operating System for the
               Riemann Zeros},
  author    = {Isaev, Ishak Hamzatovich},
  year      = {2026},
  url       = {https://github.com/wild8highlander/research-papers/tree/main/src/ab-cloud-3d}
}
```

---

## 🤝 Contributing

Contributions are welcome! Whether you find a bug, have a suggestion for improving the documentation, or want to extend the numerical verification, please read our contributing guidelines:

👉 **[CONTRIBUTING.md](./CONTRIBUTING.md)**

All interactions in this repository are governed by the [Contributor Covenant](./src/ab-cloud-3d/code/CODE_OF_CONDUCT.md) Code of Conduct.

---

## ⚖️ License

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?style=flat-square)](./LICENSE)

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** (CC BY-NC-SA 4.0).

You are free to **share** and **adapt** this material under the following terms:

- **Attribution** — You must give appropriate credit.
- **NonCommercial** — You may not use the material for commercial purposes.
- **ShareAlike** — If you remix or transform, you must distribute under the same license.

See [LICENSE](./LICENSE) for the full legal text.

---

## 🙏 Acknowledgments

This research program sits at the confluence of several deep mathematical traditions:

- **Clay Mathematics Institute** — for the Millennium Prize formulation that motivates the 3D Navier–Stokes regularity problem.
- **Montgomery–Dyson** — for the GUE pair-correlation conjecture connecting zeta zeros to random matrix theory.
- **Hilbert–Pólya** — for the spectral interpretation of the Riemann hypothesis.
- **Langlands** — for the automorphic–spectral duality programme that the AB-Cloud instantiates.
- **Hofstadter** — for the Hamiltonian framework whose non-Hermitian extension underlies the AB-Cloud lattice.
- **Beale–Kato–Majda** — for the BKM regularity criterion that the *b*-correction satisfies.
- The open-source communities behind **NumPy**, **SciPy**, **Matplotlib**, and **Julia** — the computational backbone of all numerical verifications.

---

<div align="center">

**Built with ❤️ by [Isaev Ishak Hamzatovich](https://github.com/wild8highlander)**

</div>
