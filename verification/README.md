# 🔬 Verification — the 11-Language Verification Framework

> **Navigation:** **`verification`**

![Languages](https://img.shields.io/badge/Languages-11-blue?style=flat-square) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![CI](https://img.shields.io/badge/CI-ci--cross--language-2088FF?style=flat-square&logo=githubactions&logoColor=white)

This directory is the **independent verification framework** of the repository: every headline claim of the research programs is re-derived here, in **eleven programming languages**, from a single shared contract — run a verifier, it prints per-assertion `[PASS]`/`[FAIL]` lines plus a final `JSON: {...}` verdict, and exits non-zero on any failure. Four proof assistants machine-check the structural facts; seven computational languages re-derive the numbers from first principles with no hidden dependencies.

**Tier 1 — proof assistants (formal verification):**
- [`lean4/`](lean4/README.md) — Lean 4 (v4.14, Mathlib4): machine-checked proofs of the correction-b bounds, NSE stability scaffolding and AB-Cloud structural theorems;
- [`coq/`](coq/README.md) — Coq/Rocq (8.18): classical `Reals`-based proofs with `lra` automation;
- [`isabelle/`](isabelle/README.md) — Isabelle-HOL (2024): independent statement over `Complex_Main`;
- [`agda/`](agda/README.md) — Agda (2.6): dependently-typed constructive development with an explicit, minimal trust base.

**Tier 2 — computational languages (numerical verification):**
- [`section1_correction_b/` … `section6_riemann_zeros/`](section1_correction_b/README.md) — pure-Python reference implementations of the six research sections;
- [`cpp/`](cpp/README.md) — C++17 ports with a uniform `check()` harness (CMake build);
- [`rust/`](rust/README.md) — memory-safe Rust ports (std-only, Cargo);
- [`haskell/`](haskell/README.md) — GHC 9.4 ports (Cabal).

**Infrastructure:**
- [`common/`](common/README.md) — shared Python utilities (verifier base class, config);
- [`api/`](api/README.md) — REST API exposing the verifiers over HTTP;
- [`demo/`](demo/README.md) — interactive Gradio and Streamlit front-ends;
- [`docker/`](docker/README.md) — one pinned container per formal/extended toolchain;
- [`tests/`](tests/README.md) — cross-language validator and extended-language integration tests;
- [`scripts/`](scripts/README.md) — cross-validation and API bootstrap shell scripts;
- [`notebooks/`](notebooks/README.md) — Jupyter entry point;
- [`docs/extended-languages/`](docs/README.md) — notes on the extended toolchains;
- [`web-dashboard/`](web-dashboard/README.md) — dashboard package manifest.

The six research sections map 1-to-1 onto the research programs described in the root README: **1** — the polarization correction *b*; **2** — the NSE regularity chain of the preprint; **3** — the AB-Cloud Hamiltonian; **4** — the KdV soliton interactions; **5** — the Klein attractor; **6** — the Riemann-zeros correspondence. The root README carries the full [Section × Language matrix](../README.md#-section--language-verification-matrix) with direct links into every port.

Historical note: [`README_VERIFICATION.md`](README_VERIFICATION.md) is the original (short) framework description kept for provenance; this README supersedes it. Admitted gaps in the formal systems are tracked openly — see [`lean4/TODO_sorry.md`](lean4/TODO_sorry.md).

## 📜 The Verification Contract

Every computational port in this framework follows one output contract, which is what makes cross-language comparison mechanical:

1. print a banner line identifying section and language;
2. compute the section's quantities from closed-form inputs (no data files needed at this tier);
3. assert each expected property, printing `[PASS] name: expected=…, actual=…` or `[FAIL] …`;
4. print a final line `JSON: {"section": N, "language": "<lang>", "values": {…}, "all_passed": true|false}`;
5. exit with status 0 only if every assertion passed.

The formal tier mirrors the same assertions as lemmas (`b_pos`, `b_lt_one`, `sin_θ_b_eq_b`, …) so that a reviewer can diff the *mathematical content* across systems rather than the code style.

## 🚀 Running the Framework

```bash
# From the repository root:
make install          # Python environment
make verify-all       # Python reference implementations (sections 1–6)
make verify-extended  # extended toolchains (requires those installed)

# Or directly, per language:
python3  verification/section1_correction_b/python/verify.py
cargo run --release --manifest-path verification/rust/Cargo.toml
cmake -S verification/cpp -B /tmp/cppbuild && cmake --build /tmp/cppbuild

# Formal tier:
cd verification/lean4 && lake build && lake exe check
cd verification/isabelle && isabelle build -D .
```

Docker images pin every formal toolchain — see [`docker/`](docker/README.md). The REST API (`api/server.py`) runs the same verifiers over HTTP for scripted audits.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`CODEOWNERS`](CODEOWNERS) | 278 B | review routing — code owners per path |
| [`Makefile`](Makefile) | 1.1 KB | build automation — the verification targets of this layer |
| [`agda/`](agda/) | — | subdirectory with 14 files (see its own README) |
| [`api/`](api/) | — | subdirectory with 3 files (see its own README) |
| [`common/`](common/) | — | subdirectory with 6 files (see its own README) |
| [`coq/`](coq/) | — | subdirectory with 14 files (see its own README) |
| [`cpp/`](cpp/) | — | subdirectory with 14 files (see its own README) |
| [`demo/`](demo/) | — | subdirectory with 4 files (see its own README) |
| [`docker/`](docker/) | — | subdirectory with 15 files (see its own README) |
| [`docs/`](docs/) | — | subdirectory with 2 files (see its own README) |
| [`haskell/`](haskell/) | — | subdirectory with 26 files (see its own README) |
| [`isabelle/`](isabelle/) | — | subdirectory with 14 files (see its own README) |
| [`lean4/`](lean4/) | — | subdirectory with 22 files (see its own README) |
| [`notebooks/`](notebooks/) | — | subdirectory with 2 files (see its own README) |
| [`rust/`](rust/) | — | subdirectory with 26 files (see its own README) |
| [`scripts/`](scripts/) | — | subdirectory with 3 files (see its own README) |
| [`section1_correction_b/`](section1_correction_b/) | — | subdirectory with 3 files (see its own README) |
| [`section2_preprint/`](section2_preprint/) | — | subdirectory with 3 files (see its own README) |
| [`section3_ab_cloud/`](section3_ab_cloud/) | — | subdirectory with 3 files (see its own README) |
| [`section4_kdv/`](section4_kdv/) | — | subdirectory with 3 files (see its own README) |
| [`section5_klein_attractor/`](section5_klein_attractor/) | — | subdirectory with 3 files (see its own README) |
| [`section6_riemann_zeros/`](section6_riemann_zeros/) | — | subdirectory with 3 files (see its own README) |
| [`tests/`](tests/) | — | subdirectory with 3 files (see its own README) |
| [`web-dashboard/`](web-dashboard/) | — | subdirectory with 2 files (see its own README) |

## 🗂 Directory Layout

```
verification/
├── agda/   # 14 files
│   ├── Section1_CorrectionB/   # 2 files
│   │   ├── CorrectionB.agda
│   │   └── README.md  (this file)
│   ├── Section2_PreprintNSE/   # 2 files
│   │   ├── ProofChain.agda
│   │   └── README.md  (this file)
│   ├── Section3_ABCloud/   # 2 files
│   │   ├── Hofstadter.agda
│   │   └── README.md  (this file)
│   ├── Section4_KdV/   # 2 files
│   │   ├── KdV.agda
│   │   └── README.md  (this file)
│   ├── Section5_KleinAttractor/   # 2 files
│   │   ├── Klein.agda
│   │   └── README.md  (this file)
│   ├── Section6_RiemannZeros/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── RiemannZeros.agda
│   ├── agda.agda-lib
│   └── README.md  (this file)
├── api/   # 3 files
│   ├── README.md  (this file)
│   ├── requirements.txt
│   └── server.py
├── common/   # 6 files
│   ├── python/   # 5 files
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── README.md  (this file)
│   │   └── verifier_base.py
│   └── README.md  (this file)
├── coq/   # 14 files
│   ├── section1_correction_b/   # 2 files
│   │   ├── CorrectionB.v
│   │   └── README.md  (this file)
│   ├── section2_preprint/   # 2 files
│   │   ├── ProofChain.v
│   │   └── README.md  (this file)
│   ├── section3_ab_cloud/   # 2 files
│   │   ├── Hofstadter.v
│   │   └── README.md  (this file)
│   ├── section4_kdv/   # 2 files
│   │   ├── KdV.v
│   │   └── README.md  (this file)
│   ├── section5_klein_attractor/   # 2 files
│   │   ├── Klein.v
│   │   └── README.md  (this file)
│   ├── section6_riemann_zeros/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── RiemannZeros.v
│   ├── _CoqProject
│   └── README.md  (this file)
├── cpp/   # 14 files
│   ├── section1_correction_b/   # 2 files
│   │   ├── main.cpp
│   │   └── README.md  (this file)
│   ├── section2_preprint/   # 2 files
│   │   ├── main.cpp
│   │   └── README.md  (this file)
│   ├── section3_ab_cloud/   # 2 files
│   │   ├── main.cpp
│   │   └── README.md  (this file)
│   ├── section4_kdv/   # 2 files
│   │   ├── main.cpp
│   │   └── README.md  (this file)
│   ├── section5_klein_attractor/   # 2 files
│   │   ├── main.cpp
│   │   └── README.md  (this file)
│   ├── section6_riemann_zeros/   # 2 files
│   │   ├── main.cpp
│   │   └── README.md  (this file)
│   ├── CMakeLists.txt
│   └── README.md  (this file)
├── demo/   # 4 files
│   ├── gradio_app.py
│   ├── README.md  (this file)
│   ├── requirements.txt
│   └── streamlit_app.py
├── docker/   # 15 files
│   ├── agda/   # 2 files
│   │   ├── Dockerfile
│   │   └── README.md  (this file)
│   ├── coq/   # 2 files
│   │   ├── Dockerfile
│   │   └── README.md  (this file)
│   ├── cpp/   # 2 files
│   │   ├── Dockerfile
│   │   └── README.md  (this file)
│   ├── haskell/   # 2 files
│   │   ├── Dockerfile
│   │   └── README.md  (this file)
│   ├── isabelle/   # 2 files
│   │   ├── Dockerfile
│   │   └── README.md  (this file)
│   ├── lean4/   # 2 files
│   │   ├── Dockerfile
│   │   └── README.md  (this file)
│   ├── rust/   # 2 files
│   │   ├── Dockerfile
│   │   └── README.md  (this file)
│   └── README.md  (this file)
├── docs/   # 2 files
│   ├── extended-languages/   # 1 files
│   │   └── README.md  (this file)
│   └── README.md  (this file)
├── haskell/   # 26 files
│   ├── Section1_CorrectionB/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── Section1_CorrectionB.cabal
│   ├── Section2_PreprintNSE/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── Section2_PreprintNSE.cabal
│   ├── Section3_ABCloud/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── Section3_ABCloud.cabal
│   ├── Section4_KdV/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── Section4_KdV.cabal
│   ├── Section5_KleinAttractor/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── Section5_KleinAttractor.cabal
│   ├── Section6_RiemannZeros/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── Section6_RiemannZeros.cabal
│   ├── cabal.project
│   └── README.md  (this file)
├── isabelle/   # 14 files
│   ├── Section1_CorrectionB/   # 2 files
│   │   ├── CorrectionB.thy
│   │   └── README.md  (this file)
│   ├── Section2_PreprintNSE/   # 2 files
│   │   ├── ProofChain.thy
│   │   └── README.md  (this file)
│   ├── Section3_ABCloud/   # 2 files
│   │   ├── Hofstadter.thy
│   │   └── README.md  (this file)
│   ├── Section4_KdV/   # 2 files
│   │   ├── KdV.thy
│   │   └── README.md  (this file)
│   ├── Section5_KleinAttractor/   # 2 files
│   │   ├── Klein.thy
│   │   └── README.md  (this file)
│   ├── Section6_RiemannZeros/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── RiemannZeros.thy
│   ├── README.md  (this file)
│   └── ROOT
├── lean4/   # 22 files
│   ├── ResearchPapersVerification/   # 16 files
│   │   ├── Common/   # 2 files
│   │   ├── Section1_CorrectionB/   # 2 files
│   │   ├── Section2_PreprintNSE/   # 2 files
│   │   ├── Section3_ABCloud/   # 2 files
│   │   ├── Section4_KdV/   # 2 files
│   │   ├── Section5_KleinAttractor/   # 2 files
│   │   ├── Section6_RiemannZeros/   # 2 files
│   │   ├── Basic.lean
│   │   └── README.md  (this file)
│   ├── lakefile.lean
│   ├── lean-toolchain
│   ├── Main.lean
│   ├── README.md  (this file)
│   ├── Test.lean
│   └── TODO_sorry.md
├── notebooks/   # 2 files
│   ├── README.md  (this file)
│   └── requirements.txt
├── rust/   # 26 files
│   ├── section1_correction_b/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── Cargo.toml
│   │   └── README.md  (this file)
│   ├── section2_preprint/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── Cargo.toml
│   │   └── README.md  (this file)
│   ├── section3_ab_cloud/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── Cargo.toml
│   │   └── README.md  (this file)
│   ├── section4_kdv/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── Cargo.toml
│   │   └── README.md  (this file)
│   ├── section5_klein_attractor/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── Cargo.toml
│   │   └── README.md  (this file)
│   ├── section6_riemann_zeros/   # 4 files
│   │   ├── src/   # 2 files
│   │   ├── Cargo.toml
│   │   └── README.md  (this file)
│   ├── Cargo.toml
│   └── README.md  (this file)
├── scripts/   # 3 files
│   ├── README.md  (this file)
│   ├── run_cross_validation.sh
│   └── start_api.sh
├── section1_correction_b/   # 3 files
│   ├── python/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── verify.py
│   └── README.md  (this file)
├── section2_preprint/   # 3 files
│   ├── python/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── verify.py
│   └── README.md  (this file)
├── section3_ab_cloud/   # 3 files
│   ├── python/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── verify.py
│   └── README.md  (this file)
├── section4_kdv/   # 3 files
│   ├── python/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── verify.py
│   └── README.md  (this file)
├── section5_klein_attractor/   # 3 files
│   ├── python/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── verify.py
│   └── README.md  (this file)
├── section6_riemann_zeros/   # 3 files
│   ├── python/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── verify.py
│   └── README.md  (this file)
├── tests/   # 3 files
│   ├── extended_cross_language_validator.py
│   ├── README.md  (this file)
│   └── test_extended_languages.py
├── web-dashboard/   # 2 files
│   ├── package.json
│   └── README.md  (this file)
├── CODEOWNERS
├── Makefile
├── README.md  (this file)
└── README_VERIFICATION.md  (this file)
```

## 🇷🇺 Краткое резюме (Russian Summary)

**verification/** — независимый фреймворк верификации на 11 языках: 4 пруф-ассистента (Lean 4, Coq, Isabelle, Agda) машинно проверяют структурные факты, 7 вычислительных языков пересчитывают числа по единому контракту (строки PASS + JSON-вердикт). Шесть разделов соответствуют программам исследований; инфраструктура — common/, api/, demo/, docker/, tests/, scripts/, notebooks/. Исторический короткий README сохранён рядом.

---

<div align="center">

**[⬆ Back to top](#-verification--the-11-language-verification-framework)** · 
**[Repository root](README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>