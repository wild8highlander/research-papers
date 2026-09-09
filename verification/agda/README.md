# Ⓜ️ Agda — Formal/Numerical Verification Layer

> **Navigation:** [`verification`](../README.md) › **`agda`**

![Agda](https://img.shields.io/badge/Agda-2.6-informational?style=flat-square&logo=agda&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Sections](https://img.shields.io/badge/Sections-6-blue?style=flat-square)

This directory carries the **Agda (2.6) formal-verification layer**: a dependently-typed, constructive development with one module per research section, compiled with `--safe`. Agda's contribution to the framework is the **minimal trust base**: π and √3 are explicit `postulate`s rather than library imports, so the axioms a reader must accept are visible in the first lines of each file.

The modules define `b-correction` as a rational-expression division over `Data.Rational`, carry postulated positivity/bound lemmas (`b-pos`, `b-lt-one`), and develop the per-section constructions (PSL(2,7) proof chain in Section 2, Hofstadter scaffolding in Section 3, and so on). The `agda.agda-lib` file registers the include roots so `agda` resolves `SectionN_*` modules from anywhere.

Check any module with `agda Section1_CorrectionB/CorrectionB.agda` (or `--safe` for the CI configuration). CI type-checks the modules in `ci-extended-languages.yml`.

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
| [`agda.agda-lib`](agda.agda-lib) | 60 B | Agda library file — include roots and module list |

## 🗂 Directory Layout

```
agda/
├── Section1_CorrectionB/   # 2 files
│   ├── CorrectionB.agda
│   └── README.md  (this file)
├── Section2_PreprintNSE/   # 2 files
│   ├── ProofChain.agda
│   └── README.md  (this file)
├── Section3_ABCloud/   # 2 files
│   ├── Hofstadter.agda
│   └── README.md  (this file)
├── Section4_KdV/   # 2 files
│   ├── KdV.agda
│   └── README.md  (this file)
├── Section5_KleinAttractor/   # 2 files
│   ├── Klein.agda
│   └── README.md  (this file)
├── Section6_RiemannZeros/   # 2 files
│   ├── README.md  (this file)
│   └── RiemannZeros.agda
├── agda.agda-lib
└── README.md  (this file)
```

## ▶️ How to Run

```bash
cd verification/agda
agda <Module>.agda
```
Build step: `agda --safe <Module>.agda`.

## 🇷🇺 Краткое резюме (Russian Summary)

**verification/agda/** — слой верификации на Agda (2.6): конструктивная разработка с зависимыми типами; π и √3 — явные постулаты. Шесть портов по разделам (1: Correction b, 2: Preprint NSE, 3: AB-Cloud, 4: KdV, 5: Klein Attractor, 6: Riemann Zeros); единый контракт PASS/JSON; команды сборки — в разделе How to Run.

---

<div align="center">

**[⬆ Back to top](#-agda--formalnumerical-verification-layer)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>