# 🐍 Section 4 — KdV — Soliton Interactions under the b-Correction (Python Reference)

> **Navigation:** [`verification`](../README.md) › **`section4_kdv`**

![Python](https://img.shields.io/badge/Python-3.10–3.12-informational?style=flat-square&logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Section](https://img.shields.io/badge/Section-4-blue?style=flat-square)

This directory is the **Python reference implementation** of research Section 4 — the fourth section of the framework, covering the Korteweg–de Vries equation and its soliton interactions. Within the framework's layout it is the *numerical reference tier*: the simplest, dependency-free port that every other language port can be diffed against.

The implementation is intentionally minimal — pure standard library (`math` only), a single `verify.py` entry point, and the framework's uniform output contract: the computed quantities are printed, each expected property is asserted with a `[PASS]` line, and the run ends with the `JSON:` verdict. For Section 4 the quantities are pseudospectral treatment of the KdV hierarchy and the manifestation of the polarization correction in soliton collision dynamics; the assertions exercise conservation-law identities of the integrable KdV hierarchy and the numeric stability of the pseudospectral scheme.

Run it with `python3 python/verify.py` — total runtime is well under a second. The same section exists in the formal tier ([`lean4`](../lean4/README.md), [`coq`](../coq/README.md), [`isabelle`](../isabelle/README.md), [`agda`](../agda/README.md)) and in the extended computational ports ([`cpp`](../cpp/README.md), [`rust`](../rust/README.md), [`haskell`](../haskell/README.md)); CI runs them all in [`ci-cross-language.yml`](../../.github/workflows/README.md).

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`python/`](python/) | — | the Python reference port — single verify.py entry point |

## 🗂 Directory Layout

```
section4_kdv/
├── python/   # 2 files
│   ├── README.md  (this file)
│   └── verify.py
└── README.md  (this file)
```

## ▶️ How to Run

```bash
python3 python/verify.py
```

## 🔗 Cross-References

- [Framework root](../README.md)
- [Root README — verification matrix](../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

**verification/section4_kdv/** — Python-референс раздела 4 (KdV — Soliton Interactions under the b-Correction): чистый stdlib, один verify.py, вывод PASS/JSON; результат — pseudospectral treatment of the KdV hierarchy and the manifestation of the polarization correction in soliton collision dynamics.

---

<div align="center">

**[⬆ Back to top](#-section-4--kdv--soliton-interactions-under-the-b-correction-python-reference)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>