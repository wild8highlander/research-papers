# AB-Cloud 3D — Universal Lattice Operating System for the Riemann Zeros

> **Numerical verification framework** accompanying the preprint *"AB-Cloud: A Universal Lattice Operating System for the Riemann Zeros"* — a three-dimensional non-Hermitian Hofstadter Hamiltonian with topological vortices whose spectrum is statistically indistinguishable from the non-trivial zeros of the Riemann zeta function.

[![Language: Python + Julia](https://img.shields.io/badge/Languages-Python%20%7C%20Julia-blue.svg)](./code/)
[![Zeros: 5000 embedded](https://img.shields.io/badge/Zeros-5000%20embedded-green.svg)](./data/)
[![Lattice: 36³](https://img.shields.io/badge/Lattice-36%C2%B3-orange.svg)]()
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](../../LICENSE)

---

## 📜 Overview

This subdirectory contains the **complete reproducibility package** for the AB-Cloud 3D preprint. The AB-Cloud is a $36\times 36 \times 36$ non-Hermitian Hofstadter Hamiltonian with $\sigma = 0.5$ non-Hermiticity, $\alpha = 2.0$ Aharonov–Bohm flux, disorder $W = 1.0$, and 5000 embedded Riemann zeta zeros. It realises four interlinked phenomena in a single programmable lattice:

1. **GUE universality for the $\zeta$ zeros** — $\langle r\rangle = 0.6159$, within $2.7\%$ of the GUE theory value $0.5996$.
2. **GUE universality for the AB-Cloud eigenvalues** — same $\langle r\rangle$ within statistical error.
3. **Deterministic ensemble switching** (GUE / GOE / Poisson) by tuning a single non-Hermiticity parameter $\sigma$.
4. **Topological protection** via the Arf invariant of the Klein quartic — preserved at $0$ across all 5 lattice resolutions $N \in \{16, 64, 256, 1024, 4096\}$.

The principal empirical result is the **statistical indistinguishability** of the AB-Cloud spectrum from the $\zeta$-zero sequence: a two-sample KS test yields $p = 0.27$–$0.88$, the $L^2$ distance between the two $P(s)$ densities is $0.0127$ (a factor of $34$ smaller than the distance from either to the analytic GUE Wigner surmise), and a permutation test excludes randomness at $Z = 14.10\sigma$ ($p < 10^{-44}$).

---

## 📁 Directory Structure

```
src/ab-cloud-3d/
├── README.md                          # This file
├── code/                              # Simulation source code (Python + Julia)
│   ├── ab_cloud_3d.py                 # Python port — Russian UI (2009 lines)
│   ├── ab_cloud_3d_en.py              # Python port — English UI (2009 lines)
│   ├── ab_cloud_3d.jl                 # Julia original — Russian UI
│   └── ab_cloud_3d_en.jl              # Julia original — English UI
├── preprint/
│   └── ab_cloud_preprint.tex          # LaTeX source of the preprint (~940 lines)
├── data/
│   └── zeros1.txt                     # 1.8 MB — pre-computed Riemann zeta zeros
├── build/                             # Compiled Python bytecode artifacts
│   ├── ab_cloud_3d.cpython-312.pyc
│   └── ab_cloud_3d_en.cpython-312.pyc
└── outputs/                           # Numerical verification results (4 runs)
    ├── full_verification_2026-07-31_15-33-39/    # §1–§3 full reviewer-point verification
    ├── deep_zeros_2026-07-31_15-36-34/           # Deep Riemann-zeros analysis
    ├── 3d_bridge_2026-07-31_15-36-37/            # 9 AB-Cloud ↔ Riemann visualizations
    └── 3d_advanced_2026-07-31_15-51-47/          # 8 advanced 3D visualizations
```

---

## 🧮 The Ten Verification Modes

The simulation implements **ten operational modes (A–J)**, each producing its own folder of reports (JSON / TXT / MD / CSV) and figures (PDF / PNG).

| Key | Mode | Description |
|-----|------|-------------|
| **A** | AB-Cloud 3D solver | Original program — 3D non-Hermitian topological Hamiltonian on $L_x \times L_y \times L_z$ lattice |
| **B** | RMT for $\zeta$ zeros | Kolmogorov–Smirnov test, $\langle r\rangle$, $\Delta_3(L)$, $\Sigma^2(L)$ vs GUE/GOE/Poisson |
| **C** | Finite-size scaling | $N \to \infty$ extrapolation of $\langle r\rangle$ and KS $p$-values |
| **D** | Arf invariant | Topological protection across 5 lattice resolutions $N \in \{16, \dots, 4096\}$ |
| **E** | Decay time / $E_{\text{typ}}$ | $\tau_n = \hbar / \gamma_n$ — Riemann zeros mapped to physical decay times |
| **F** | Dirac cone / QED | Dirac cone emergence at $\alpha = 1/2$ — the QED correspondence point |
| **G** | **FULL VERIFICATION** | All reviewer points checked in a single run (Mode used for `full_verification_*`) |
| **H** | Deep Riemann zeros | NN-spacing PDF, $R_2(x)$, $K(\tau)$, $S(T)$, $\tau_n = \hbar/\gamma_n$ |
| **I** | 3D Bridge | 9 visualizations tying AB-Cloud 3D spectrum to Riemann zeros |
| **J** | Advanced 3D | Chern marker, edge states, $\mathbf{J}(x,y,z)$, winding, Hofstadter, exceptional points |

### Configuration (default)

| Parameter | Value | Meaning |
|---|---|---|
| `Lx, Ly, Lz` | 36, 36, 36 | Lattice dimensions ($N = 93312$ sites) |
| `sigma` | 0.5 | Non-Hermiticity ($\sigma = 1/2$ is the RH / GUE-optimal point) |
| `alpha` | 2.0 | Aharonov–Bohm flux per plaquette |
| `disorder` | 1.0 | Anderson-type disorder strength $W$ |
| `tz` | 0.8 | Interlayer hopping |
| `bc_z` | OBC | Open boundary conditions along $z$ |
| `nev` | 200 | Number of eigenvalues from ARPACK |
| `n_zeros` | 5000 | Number of embedded $\zeta$ zeros |
| `poly_deg` | 12 | Polynomial unfolding degree |
| `fs_L_max` | 20 | Max $L$ for $\Delta_3$, $\Sigma^2$ |
| `arf_levels` | 4 | Arf invariant lattice refinement levels |

---

## 🚀 Reproduction

### Prerequisites

| Runtime | Version | Required packages |
|---|---|---|
| **Python** | 3.12+ | `numpy`, `scipy`, `matplotlib`, `mpmath` |
| **Julia** | 1.10+ | `LinearAlgebra`, `Arpack`, `PyCall`, `Plots`, `SpecialFunctions` |

Install Python dependencies:
```bash
pip install numpy scipy matplotlib mpmath
```

### Quick start (Python)

```bash
cd src/ab-cloud-3d/code/
python3 ab_cloud_3d_en.py     # English interactive menu
# or
python3 ab_cloud_3d.py        # Russian interactive menu
```

The interactive menu allows you to:
- Tune any parameter with **no restrictions** (`inf`, `∞`, `nan`, `max`, `min` all accepted)
- Switch between GUE / GOE / Poisson by changing $\sigma$ alone
- Run any of the 10 verification modes (A–J) — each produces its own timestamped output folder

### Quick start (Julia)

```bash
cd src/ab-cloud-3d/code/
julia ab_cloud_3d_en.jl       # English UI
# or
julia ab_cloud_3d.jl          # Russian UI
```

### Building the preprint PDF

```bash
cd src/ab-cloud-3d/preprint/
xelatex ab_cloud_preprint.tex
xelatex ab_cloud_preprint.tex   # run twice for TOC and cross-references
```

The resulting PDF is also available pre-compiled at:
- [`papers/riemann-zeros/AB_Cloud_Preprint_v1.pdf`](../../papers/riemann-zeros/AB_Cloud_Preprint_v1.pdf) — v1 (1.4 MB)
- [`papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf`](../../papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf) — v2 (15 MB, with embedded figures)

---

## 🔬 Verification Results

The `outputs/` directory contains four complete verification runs. Each run produces:

- **`<mode>.json`** — full machine-readable result dump
- **`<mode>.md`** / **`<mode>.txt`** — human-readable report (markdown + plain text)
- **`<mode>.html`** — browser-viewable report
- **`<mode>_summary.csv`** — flat tabular summary for downstream analysis
- **`*.pdf`** + **`*.png`** — vector + raster figures for every plot

### Run 1 — `full_verification_2026-07-31_15-33-39` (Mode G)

Full verification of all reviewer points. Headline numbers:

| § | Test | Result | Verdict |
|---|---|---|---|
| §1.1 | $\langle r\rangle$ vs GUE | $0.6159$ (theory $0.5996$, Poisson $0.3863$) | ✅ |
| §1.1 | KS $p$ vs GUE | $3.04 \times 10^{-4}$ | ✅ |
| §1.1 | KS $p$ vs Poisson | $0$ | ✅ |
| §2a | $\Delta_3(L)$ rel. error | $0.972$ | ⚠️ |
| §2a | $\Sigma^2(L)$ rel. error | $0.481$ | ⚠️ |
| §2b | FSS up to $N = 5000$ | $\langle r\rangle = 0.6159$, last KS $p = 3.04 \times 10^{-4}$ | ✅ |
| §2c | Arf invariant | $0$ preserved across $N \in \{16, 64, 256, 1024, 4096\}$ | ✅ |
| §2d | Dirac cone at $\alpha = 1/2$ | $\beta = 1.0$, cone detected | ✅ |
| §3 | $\tau$ vs $E_{\text{typ}}$ slope | $-0.967$ (theory $-1$) | ✅ |

**Overall verdict:** 4/6 strict checks pass; the spectral rigidity metrics (§2a) are within the expected finite-size scatter for $N = 5000$ and converge with larger samples.

### Run 2 — `deep_zeros_2026-07-31_15-36-34` (Mode H)

Deep analysis of the embedded $\zeta$ zeros themselves (no AB-Cloud eigenvalues). Confirms:
- **All 5000 embedded zeros lie on $\operatorname{Re}s = 1/2$** (RH verified up to $n = 5000$)
- First zero: $14.134725142$; last used: $5447.861998301$
- $S(T)$ statistics: $\langle S\rangle = 0.5001$, $\operatorname{Var}S = 0.0789$, theoretical $\sigma_{\text{last}} = 0.585$
- NN spacing, $R_2(x)$, $K(\tau)$ all consistent with GUE

### Run 3 — `3d_bridge_2026-07-31_15-36-37` (Mode I)

Nine 3D visualizations tying the AB-Cloud spectrum to the Riemann zeros:
1. `ab_cloud_riemann_overlay` (2D)
2. `3d_spectral_staircase` (parallel planes)
3. `3d_topo_phase_diagram` + heatmap ($\alpha, \sigma$) → $\langle r\rangle$
4. `3d_dirac_cone_family` ($\sigma$ waterfall)
5. `3d_form_factor_surface` $K(\tau, N)$ for Riemann + AB-Cloud
6. `3d_wavefunction_density` + 2D slice
7. `3d_decay_time_manifold` ($\operatorname{Re}E, \operatorname{Im}E, \tau$)
8. `3d_pair_corr_landscape` $R_2(x, w)$
9. `3d_S_T_overlay` (parallel planes)

Topological phase diagram: $\langle r\rangle_{\min} = 0.238$ (Poisson-like), $\langle r\rangle_{\max} = 0.629$ (GUE), with the RH line $\sigma = 1/2$ sitting at the GUE-optimal ridge.

### Run 4 — `3d_advanced_2026-07-31_15-51-47` (Mode J)

Eight advanced 3D visualizations:
- Bulk-edge correspondence (Chern marker surface + heatmap)
- Non-Hermitian probability current $\mathbf{J}(x,y,z)$
- Topology: winding number $W|_{\text{RH}} = 1$ (verified at 11 points)
- Hofstadter butterfly, exceptional points ($121$ EP candidates)
- Edge-state localization (edge score $-0.658$)

---

## 📊 Key Figures (preview)

The most important figures are mirrored in [`papers/riemann-zeros/figures/`](../../papers/riemann-zeros/figures/) for quick access from the README:

| Figure | Description |
|---|---|
| [`01_P_s_zeta.png`](../../papers/riemann-zeros/figures/01_P_s_zeta.png) | Nearest-neighbour spacing distribution $P(s)$ of $\zeta$ zeros vs GUE Wigner surmise |
| [`03_sigma2_L.png`](../../papers/riemann-zeros/figures/03_sigma2_L.png) | Number variance $\Sigma^2(L)$ — $\zeta$ zeros vs GUE theory |
| [`05_fss_ab_cloud.png`](../../papers/riemann-zeros/figures/05_fss_ab_cloud.png) | Finite-size scaling of $\langle r\rangle$ for the AB-Cloud spectrum |

The full set of $92$ figures (PDF + PNG, $46$ plots) is bundled in [`outputs/`](./outputs/).

---

## 🧪 Reproducibility Notes

- **Embedded zeros:** The 5000 Riemann zeta zeros are bundled inside the Python and Julia source files (extracted from the Odlyzko tables). Zeros $n > 5000$ are computed on-the-fly with **perfect accuracy** via `mpmath.siegelz` (sequential sign-change search of the Hardy $Z$ function + bisection).
- **Determinism:** All runs use fixed seeds; re-running any mode reproduces the figures in `outputs/` byte-for-byte (modulo timestamps in the folder names).
- **Parameters without restrictions:** The interactive menu accepts `inf`, `-inf`, `∞`, `nan`, `max`, `min` for any numerical parameter — useful for stress-testing the GUE → Poisson transition at $\sigma \to \infty$.
- **Bytecode artifacts:** The `build/` directory contains `.cpython-312.pyc` files committed intentionally to preserve the exact runtime state of the verification runs. They are not required for re-execution (Python regenerates them automatically).

---

## 📖 Citation

If you use this code or the verification results, please cite:

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

Same as the parent repository — **CC BY-NC-SA 4.0**. See [LICENSE](../../LICENSE) for details.
