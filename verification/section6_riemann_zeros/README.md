# 🐍 Section 6 — Riemann Zeros — the Hilbert–Pólya Programme (Python Reference)

> **Navigation:** [`verification`](../README.md) › **`section6_riemann_zeros`**

![Python](https://img.shields.io/badge/Python-3.10–3.12-informational?style=flat-square&logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Section](https://img.shields.io/badge/Section-6-blue?style=flat-square)

This directory is the **Python reference implementation** of research Section 6 — the sixth section of the framework, covering the spectral correspondence between the AB-Cloud and the non-trivial zeros of the Riemann zeta function. Within the framework's layout it is the *numerical reference tier*: the simplest, dependency-free port that every other language port can be diffed against.

The implementation is intentionally minimal — pure standard library (`math` only), a single `verify.py` entry point, and the framework's uniform output contract: the computed quantities are printed, each expected property is asserted with a `[PASS]` line, and the run ends with the `JSON:` verdict. For Section 6 the quantities are the Hilbert–Pólya realisation, the Montgomery–Dyson GUE correspondence and the statistical identity of the two spectra; the assertions exercise spectral-correspondence identities and the statistical machinery (⟨r⟩, KS, permutation tests) in constructive and classical form.

Run it with `python3 python/verify.py` — total runtime is well under a second. The same section exists in the formal tier ([`lean4`](../lean4/README.md), [`coq`](../coq/README.md), [`isabelle`](../isabelle/README.md), [`agda`](../agda/README.md)) and in the extended computational ports ([`cpp`](../cpp/README.md), [`rust`](../rust/README.md), [`haskell`](../haskell/README.md)); CI runs them all in [`ci-cross-language.yml`](../../.github/workflows/README.md).

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`python/`](python/) | — | the Python reference port — single verify.py entry point |

## 🗂 Directory Layout

```
section6_riemann_zeros/
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

**verification/section6_riemann_zeros/** — Python-референс раздела 6 (Riemann Zeros — the Hilbert–Pólya Programme): чистый stdlib, один verify.py, вывод PASS/JSON; результат — the Hilbert–Pólya realisation, the Montgomery–Dyson GUE correspondence and the statistical identity of the two spectra.

---

<div align="center">

**[⬆ Back to top](#-section-6--riemann-zeros--the-hilbertpólya-programme-python-reference)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>