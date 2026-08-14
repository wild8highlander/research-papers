<div align="center">

# Research Papers

### Correction *b* & 3D Navier–Stokes Regularity · AB-Cloud · Riemann Zeros

</div>

<div align="center">

[![License: All Rights Reserved](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg?style=flat-square)](./LICENSE)
[![Languages](https://img.shields.io/badge/Languages-11-blue.svg?style=flat-square)]()
[![Papers](https://img.shields.io/badge/Papers-14-blue.svg?style=flat-square)](./papers/)
[![Documents](https://img.shields.io/badge/Documents-15-green.svg?style=flat-square)](./docs/)
[![Code](https://img.shields.io/badge/Code-Python%20%7C%20Julia%20%7C%20Rust%20%7C%20C%2B%2B%20%7C%20Haskell%20%7C%20Lean%204-purple.svg?style=flat-square)](./verification/)
[![Last Commit](https://img.shields.io/github/last-commit/wild8highlander/research-papers?style=flat-square)](https://github.com/wild8highlander/research-papers/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/wild8highlander/research-papers?style=flat-square)](https://github.com/wild8highlander/research-papers)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB.svg?logo=python&logoColor=white&style=flat-square)](https://www.python.org/)
[![Rust](https://img.shields.io/badge/Rust-1.75%2B-CE422B.svg?logo=rust&logoColor=white&style=flat-square)](https://www.rust-lang.org/)
[![C++](https://img.shields.io/badge/C%2B%2B-17-00599C.svg?logo=c%2B%2B&logoColor=white&style=flat-square)](https://isocpp.org/)
[![Haskell](https://img.shields.io/badge/Haskell-9.4-5D4F85.svg?logo=haskell&logoColor=white&style=flat-square)](https://www.haskell.org/)
[![Lean 4](https://img.shields.io/badge/Lean%204-v4.14-FFD700.svg?style=flat-square)](https://leanprover.github.io/)
[![Coq](https://img.shields.io/badge/Coq-8.18-DFA524.svg?style=flat-square)](https://coq.inria.fr/)
[![Isabelle](https://img.shields.io/badge/Isabelle-HOL-FF0000.svg?style=flat-square)](https://isabelle.in.tum.de/)

</div>

---

> **Analytical proof of 3D Navier–Stokes regularity without artificial dissipation**, grounded in the universal polarization correction *b* ≈ 0.0785 from Kirchhoff point-vortex equations, together with the **AB-Cloud** — a 36³ non-Hermitian Hofstadter Hamiltonian whose spectrum is statistically indistinguishable from the Riemann ζ-zeros, realising the Hilbert–Pólya conjecture, Montgomery–Dyson GUE correspondence, and a concrete bridge to the Langlands programme.

---

## Multi-Language Verification Framework

This project implements **11 programming languages** for cross-validation of all mathematical results:

### Numerical Languages (Tier 1)

| Language | Role | Sections |
|----------|------|----------|
| **Python** | Full-featured numerical verification | 1–6 |
| **Julia** | High-performance BLAS/LAPACK | 1–6 |
| **Java** | Enterprise-grade, Apache Commons Math | 1–6 |
| **Rust** | Memory-safe numerical verification | 1–6 |
| **C++** | Maximum-performance STL | 1–6 |
| **Haskell** | Pure functional numerical + symbolic | 1–6 |

### Formal Proof Languages (Tier 2)

| Language | Role | Theorems |
|----------|------|----------|
| **Lean 4** | Machine-checked proofs with Mathlib4 | 222 |
| **Coq** | Formal proofs with Reals library | 129 |
| **Isabelle/HOL** | Higher-order logic proofs | 51 |
| **Agda** | Dependent-type proofs | 50+ |

### Dashboard & API

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Dashboard** | Next.js + React + Zustand | Real-time visualization |
| **REST API** | FastAPI + WebSocket | Programmatic access |
| **Notebooks** | Jupyter | Interactive analysis |
| **Demos** | Streamlit + Gradio | Quick exploration |

---

## Key Results

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

## Repository Structure

```
research-papers/
├── papers/                          Research papers (PDF)
├── docs/                            Documentation (DOCX)
├── src/                             LaTeX sources + AB-Cloud code
├── verification/                    Multi-language verification framework
│   ├── common/python/               Shared Python framework
│   ├── section1_correction_b/       §1: Correction b (Py/Jl/Jv)
│   ├── section2_preprint/           §2: Preprint NSE
│   ├── section3_ab_cloud/           §3: AB-Cloud
│   ├── section4_kdv/                §4: KdV
│   ├── section5_klein_attractor/    §5: Klein Attractor
│   ├── section6_riemann_zeros/      §6: Riemann Zeros
│   ├── lean4/                       Lean 4 formal proofs (222 theorems)
│   ├── coq/                         Coq formal proofs
│   ├── isabelle/                    Isabelle/HOL proofs
│   ├── agda/                        Agda dependent-type proofs
│   ├── rust/                        Rust numerical verification
│   ├── cpp/                         C++ numerical verification
│   ├── haskell/                     Haskell verification
│   ├── docker/                      Dockerfiles for all languages
│   ├── web-dashboard/               Next.js dashboard
│   ├── api/                         FastAPI REST server
│   ├── demo/                        Streamlit + Gradio demos
│   ├── notebooks/                   Jupyter notebooks
│   ├── tests/                       pytest + cross-language validator
│   └── docs/                        Verification documentation
├── .github/workflows/               CI/CD (10+ workflows)
├── LICENSE                          All Rights Reserved
├── CODE_OF_CONDUCT.md               Community standards
├── CONTRIBUTING.md                  Contribution guide
├── SECURITY.md                      Security policy
├── CHANGELOG.md                     Version history
├── AUTHORS.md                       Author information
├── CITATION.cff                     Citation metadata
├── Makefile                         Build automation
├── pyproject.toml                   Python project config
├── environment.yml                  Conda environment
├── mkdocs.yml                       Documentation config
└── .pre-commit-config.yaml          Pre-commit hooks
```

---

## Quick Start

### Option 1: Python only

```bash
pip install numpy scipy matplotlib mpmath
python verification/common/python/main.py --section 1 --preset default
```

### Option 2: All languages

```bash
make install
make verify-all       # Python, Julia, Java
make verify-extended  # Lean 4, Coq, Rust, C++, Haskell
```

### Option 3: Docker

```bash
make docker-up
# Dashboard: http://localhost:3000
# API:       http://localhost:8000/docs
```

---

## Citation

```bibtex
@misc{isaev2026research,
  author    = {Isaev, Iskhak Hamzatovich},
  title     = {Research Papers: NSE Regularity, AB-Cloud, and Riemann Zeros},
  year      = {2026},
  url       = {https://github.com/wild8highlander/research-papers}
}
```

---

## License

**All Rights Reserved.** Copyright © 2026 Isaev Iskhak Khamzatovich (Исаев Исхак Хамзатович).

No part of this project may be reproduced, distributed, or used in any form
without the written permission of the author. See [LICENSE](./LICENSE) for details.

---

## Author

**Isaev Iskhak Khamzatovich** (Исаев Исхак Хамзатович)
- GitHub: [@wild8highlander](https://github.com/wild8highlander)
- Email: aslan08_05@mail.ru
