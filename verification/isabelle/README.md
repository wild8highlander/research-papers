# Ⓜ️ Isabelle-HOL — Formal/Numerical Verification Layer

> **Navigation:** [`verification`](../README.md) › **`isabelle`**

![Isabelle-HOL](https://img.shields.io/badge/Isabelle-HOL-2024-informational?style=flat-square&logo=isamars&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Sections](https://img.shields.io/badge/Sections-6-blue?style=flat-square)

This directory carries the **Isabelle-HOL (2024) formal-verification layer**: one theory file per research section, each stated over `Complex_Main` and registered in the session `ROOT`. Isabelle's role in the framework is independence — the statements are written afresh in Isar style, not translated from the Coq or Lean sources, so agreement between systems is evidence, not tautology.

The theories define `b_correction` as a real constant (`pi / (4 * pi^2 + 2 * pi * sqrt 3)`), prove `b_pos` from `pi_gt_zero` with `divide_pos_pos`, exercise `value "b_correction"` so the numeric value prints during session build, and chain the trigonometric identities (`sin_theta_eq_b` via `theta_b` = `arcsin b_correction`). Admitted branches use explicit `sorry` and are itemised in the framework's gap ledger.

Build the session with `isabelle build -D .`, or open any theory with `isabelle jedit -l HOL`. CI builds the session in `ci-extended-languages.yml`.

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
| [`ROOT`](ROOT) | 290 B | Isabelle session ROOT — registers the theories for isabelle build |
| [`Section1_CorrectionB/`](Section1_CorrectionB/) | — | Section 1 port — Correction b — the Universal Polarization Constant |
| [`Section2_PreprintNSE/`](Section2_PreprintNSE/) | — | Section 2 port — Preprint NSE — the Regularity Argument Chain |
| [`Section3_ABCloud/`](Section3_ABCloud/) | — | Section 3 port — AB-Cloud — the Non-Hermitian Hofstadter Hamiltonian |
| [`Section4_KdV/`](Section4_KdV/) | — | Section 4 port — KdV — Soliton Interactions under the b-Correction |
| [`Section5_KleinAttractor/`](Section5_KleinAttractor/) | — | Section 5 port — Klein Attractor — Ergodic Dynamics and the NSE Bridge |
| [`Section6_RiemannZeros/`](Section6_RiemannZeros/) | — | Section 6 port — Riemann Zeros — the Hilbert–Pólya Programme |

## 🗂 Directory Layout

```
isabelle/
├── Section1_CorrectionB/   # 2 files
│   ├── CorrectionB.thy
│   └── README.md  (this file)
├── Section2_PreprintNSE/   # 2 files
│   ├── ProofChain.thy
│   └── README.md  (this file)
├── Section3_ABCloud/   # 2 files
│   ├── Hofstadter.thy
│   └── README.md  (this file)
├── Section4_KdV/   # 2 files
│   ├── KdV.thy
│   └── README.md  (this file)
├── Section5_KleinAttractor/   # 2 files
│   ├── Klein.thy
│   └── README.md  (this file)
├── Section6_RiemannZeros/   # 2 files
│   ├── README.md  (this file)
│   └── RiemannZeros.thy
├── README.md  (this file)
└── ROOT
```

## ▶️ How to Run

```bash
cd verification/isabelle
isabelle jedit -l HOL <Theory>.thy  (or isabelle build)
```
Build step: `isabelle build -D .`.

## 🇷🇺 Краткое резюме (Russian Summary)

**verification/isabelle/** — слой верификации на Isabelle-HOL (2024): теоремы над Complex_Main, каждый раздел — отдельная теория. Шесть портов по разделам (1: Correction b, 2: Preprint NSE, 3: AB-Cloud, 4: KdV, 5: Klein Attractor, 6: Riemann Zeros); единый контракт PASS/JSON; команды сборки — в разделе How to Run.

---

<div align="center">

**[⬆ Back to top](#-isabelle-hol--formalnumerical-verification-layer)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>