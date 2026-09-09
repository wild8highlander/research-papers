# Ⓜ️ Haskell — Formal/Numerical Verification Layer

> **Navigation:** [`verification`](../README.md) › **`haskell`**

![Haskell](https://img.shields.io/badge/Haskell-9.4-informational?style=flat-square&logo=haskell&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Sections](https://img.shields.io/badge/Sections-6-blue?style=flat-square)

This directory carries the **Haskell (GHC 9.4) numerical-verification layer**: a Cabal project with one module per research section under `SectionN_*/src/`, registered in `cabal.project`. The ports mirror the framework contract — `Text.Printf`-formatted output at 15-digit precision, per-assertion PASS/FAIL lines and the final JSON verdict — while keeping the implementations idiomatic and short.

Section 1 (`Section1_CorrectionB/src`) defines `bCorrection = pi / (4·pi² + 2·pi·√3)` as a top-level `Double` binding and prints it with `printf "b = %.15e"`, exactly matching the values the other languages assert; later sections exercise the functional style on the spectral and dynamical scaffolding. GHC's purity makes these ports particularly readable as *executable specifications* of the claims.

Build with `cabal build` and run per-section executables with `cabal run`. CI builds the project in `ci-extended-languages.yml`.

Each section folder carries its own `src/` with the executable's `Main.hs`.

## 🗂 The Six Section Ports

- [`Section1_CorrectionB/`](Section1_CorrectionB/README.md) — Correction b — the Universal Polarization Constant
- [`Section2_PreprintNSE/`](Section2_PreprintNSE/README.md) — Preprint NSE — the Regularity Argument Chain
- [`Section3_ABCloud/`](Section3_ABCloud/README.md) — AB-Cloud — the Non-Hermitian Hofstadter Hamiltonian
- [`Section4_KdV/`](Section4_KdV/README.md) — KdV — Soliton Interactions under the b-Correction
- [`Section5_KleinAttractor/`](Section5_KleinAttractor/README.md) — Klein Attractor — Ergodic Dynamics and the NSE Bridge
- [`Section6_RiemannZeros/`](Section6_RiemannZeros/README.md) — Riemann Zeros — the Hilbert–Pólya Programme

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`Section1_CorrectionB/`](Section1_CorrectionB/) | — | Section 1 port — Correction b — the Universal Polarization Constant |
| [`Section2_PreprintNSE/`](Section2_PreprintNSE/) | — | Section 2 port — Preprint NSE — the Regularity Argument Chain |
| [`Section3_ABCloud/`](Section3_ABCloud/) | — | Section 3 port — AB-Cloud — the Non-Hermitian Hofstadter Hamiltonian |
| [`Section4_KdV/`](Section4_KdV/) | — | Section 4 port — KdV — Soliton Interactions under the b-Correction |
| [`Section5_KleinAttractor/`](Section5_KleinAttractor/) | — | Section 5 port — Klein Attractor — Ergodic Dynamics and the NSE Bridge |
| [`Section6_RiemannZeros/`](Section6_RiemannZeros/) | — | Section 6 port — Riemann Zeros — the Hilbert–Pólya Programme |
| [`cabal.project`](cabal.project) | 128 B | Cabal project file — registers all section packages |

## 🗂 Directory Layout

```
haskell/
├── Section1_CorrectionB/   # 4 files
│   ├── src/   # 2 files
│   │   ├── Main.hs
│   │   └── README.md  (this file)
│   ├── README.md  (this file)
│   └── Section1_CorrectionB.cabal
├── Section2_PreprintNSE/   # 4 files
│   ├── src/   # 2 files
│   │   ├── Main.hs
│   │   └── README.md  (this file)
│   ├── README.md  (this file)
│   └── Section2_PreprintNSE.cabal
├── Section3_ABCloud/   # 4 files
│   ├── src/   # 2 files
│   │   ├── Main.hs
│   │   └── README.md  (this file)
│   ├── README.md  (this file)
│   └── Section3_ABCloud.cabal
├── Section4_KdV/   # 4 files
│   ├── src/   # 2 files
│   │   ├── Main.hs
│   │   └── README.md  (this file)
│   ├── README.md  (this file)
│   └── Section4_KdV.cabal
├── Section5_KleinAttractor/   # 4 files
│   ├── src/   # 2 files
│   │   ├── Main.hs
│   │   └── README.md  (this file)
│   ├── README.md  (this file)
│   └── Section5_KleinAttractor.cabal
├── Section6_RiemannZeros/   # 4 files
│   ├── src/   # 2 files
│   │   ├── Main.hs
│   │   └── README.md  (this file)
│   ├── README.md  (this file)
│   └── Section6_RiemannZeros.cabal
├── cabal.project
└── README.md  (this file)
```

## ▶️ How to Run

```bash
cd verification/haskell
cabal build && cabal run <section>
```
Build step: `cabal build`.

## 🇷🇺 Краткое резюме (Russian Summary)

**verification/haskell/** — слой верификации на Haskell (9.4): GHC-реализация на Double с выводом через Text.Printf по общему контракту. Шесть портов по разделам (1: Correction b, 2: Preprint NSE, 3: AB-Cloud, 4: KdV, 5: Klein Attractor, 6: Riemann Zeros); единый контракт PASS/JSON; команды сборки — в разделе How to Run.

---

<div align="center">

**[⬆ Back to top](#-haskell--formalnumerical-verification-layer)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>