# Ⓜ️ Lean 4 — Formal/Numerical Verification Layer

> **Navigation:** [`verification`](../README.md) › **`lean4`**

![Lean 4](https://img.shields.io/badge/Lean%204-v4.14-informational?style=flat-square&logo=leanpub&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Sections](https://img.shields.io/badge/Sections-6-blue?style=flat-square)

This directory carries the **Lean 4 (v4.14) formal-verification layer** of the framework: machine-checked proofs built on the **Mathlib4** foundation, with the research objects defined in a custom `ResearchPapersVerification` library. The development is the largest formal artifact in the repository — six research sections of lemmas, an aggregator module, a numerical-bridge executable and an honest, itemised list of the admitted gaps.

The hybrid strategy is deliberate: Mathlib supplies the standard mathematical infrastructure (real analysis, matrices, normed spaces), while `Common/Foundation.lean` introduces the research-specific objects — the polarization correction *b* as a closed-form real constant, the rotation angle θ_b, the cross-product matrix construction, the Hofstadter-type spectral scaffolding — so each section file can state and prove exactly the lemmas that matter.

**The checked core includes:** positivity and upper-boundedness of `bCorrection` (`bCorrection_pos`, `bCorrection_lt_one`), the trigonometric identity `sin θ_b = b` via `Real.sin_arcsin`, the unit-norm axis vector `eZ`, the skew-symmetric cross matrix, and the per-section structures listed in the module tree below. **The admitted gaps** — every remaining `sorry` — are enumerated with commentary in [`TODO_sorry.md`](TODO_sorry.md); nothing is hidden behind unconditional axioms.

Build with `lake build`; run the type-check executable with `lake exe check` and the numerical bridge with `lake exe test`. CI builds this directory in `ci-extended-languages.yml` with the toolchain pinned by `lean-toolchain`.

| [`ResearchPapersVerification/`](ResearchPapersVerification/README.md) | the proof library — aggregator, common foundation and the six section modules |
| [`Main.lean`](Main.lean) / [`Test.lean`](Test.lean) | type-check entry point and the numerical-bridge executable |
| [`TODO_sorry.md`](TODO_sorry.md) | the honest, itemised ledger of all admitted gaps |

## 🗂 The Six Section Ports

- [`ResearchPapersVerification/Section1_CorrectionB/`](ResearchPapersVerification/Section1_CorrectionB/README.md) — Correction b — the Universal Polarization Constant
- [`ResearchPapersVerification/Section2_PreprintNSE/`](ResearchPapersVerification/Section2_PreprintNSE/README.md) — Preprint NSE — the Regularity Argument Chain
- [`ResearchPapersVerification/Section3_ABCloud/`](ResearchPapersVerification/Section3_ABCloud/README.md) — AB-Cloud — the Non-Hermitian Hofstadter Hamiltonian
- [`ResearchPapersVerification/Section4_KdV/`](ResearchPapersVerification/Section4_KdV/README.md) — KdV — Soliton Interactions under the b-Correction
- [`ResearchPapersVerification/Section5_KleinAttractor/`](ResearchPapersVerification/Section5_KleinAttractor/README.md) — Klein Attractor — Ergodic Dynamics and the NSE Bridge
- [`ResearchPapersVerification/Section6_RiemannZeros/`](ResearchPapersVerification/Section6_RiemannZeros/README.md) — Riemann Zeros — the Hilbert–Pólya Programme

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`Main.lean`](Main.lean) | 160 B | type-check entry point — imports and elaborates the whole library |
| [`ResearchPapersVerification/`](ResearchPapersVerification/) | — | subdirectory with 16 files (see its own README) |
| [`TODO_sorry.md`](TODO_sorry.md) | 6.5 KB | # Список незавершённых доказательств Lean 4 > Этот файл содержит полный перечень всех `sorry` (теорем с пропущенными > доказательствами) и `axiom` (аксиоматизированных утверждений)… |
| [`Test.lean`](Test.lean) | 169 B | numerical bridge executable — prints reference values |
| [`lakefile.lean`](lakefile.lean) | 508 B | Lake package manifest — library/executable targets |
| [`lean-toolchain`](lean-toolchain) | 25 B | Lean toolchain pin (elan reads this file) |

## 🗂 Directory Layout

```
lean4/
├── ResearchPapersVerification/   # 16 files
│   ├── Common/   # 2 files
│   │   ├── Foundation.lean
│   │   └── README.md  (this file)
│   ├── Section1_CorrectionB/   # 2 files
│   │   ├── Basic.lean
│   │   └── README.md  (this file)
│   ├── Section2_PreprintNSE/   # 2 files
│   │   ├── ProofChain.lean
│   │   └── README.md  (this file)
│   ├── Section3_ABCloud/   # 2 files
│   │   ├── HofstadterHamiltonian.lean
│   │   └── README.md  (this file)
│   ├── Section4_KdV/   # 2 files
│   │   ├── README.md  (this file)
│   │   └── Soliton.lean
│   ├── Section5_KleinAttractor/   # 2 files
│   │   ├── KleinQuartic.lean
│   │   └── README.md  (this file)
│   ├── Section6_RiemannZeros/   # 2 files
│   │   ├── HilbertPolya.lean
│   │   └── README.md  (this file)
│   ├── Basic.lean
│   └── README.md  (this file)
├── lakefile.lean
├── lean-toolchain
├── Main.lean
├── README.md  (this file)
├── Test.lean
└── TODO_sorry.md
```

## ▶️ How to Run

```bash
cd verification/lean4
lake build && lake exe check
```
Build step: `lake build`.

## 🇷🇺 Краткое резюме (Russian Summary)

**verification/lean4/** — слой верификации на Lean 4 (v4.14): машинно проверяемые доказательства на базе Mathlib4 с собственными определениями. Шесть портов по разделам (1: Correction b, 2: Preprint NSE, 3: AB-Cloud, 4: KdV, 5: Klein Attractor, 6: Riemann Zeros); единый контракт PASS/JSON; команды сборки — в разделе How to Run.

---

<div align="center">

**[⬆ Back to top](#-lean-4--formalnumerical-verification-layer)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>