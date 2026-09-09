# 📗 Papers · KdV — Soliton Interactions under the b-Correction (Chapter 16, EN + RU)

> **Navigation:** [`papers`](../README.md) › **`kdv`**

![Papers](https://img.shields.io/badge/Content-Research%20Papers-blue?style=flat-square&logo=adobeacrobatreader&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![RU](https://img.shields.io/badge/RU-%D0%A0%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5-blue?style=flat-square)

This folder contains the **book chapter on the Korteweg–de Vries equation** in two full language editions: `KdV_b_correction_Chapter16_EN.pdf` (7.2 MB) and `KdV_b_correction_Chapter16_RU.pdf` (7.4 MB). The chapter is the largest single document in the papers collection and studies how the universal polarization correction *b* ≈ 0.0785 — the same constant derived from Kirchhoff vortices in the correction-b paper — manifests itself in **soliton interactions** of the integrable KdV hierarchy.

The two editions are produced from a common source but are independent, complete publications: the EN edition serves the international reader, the RU edition is the author's native-language exposition. Word versions of the same chapter are archived in [`docs/kdv/`](../../docs/kdv/README.md) (one `.docx` per language) for editorial provenance.

On the verification side, the KdV program is Section 4 of the framework: the pseudospectral treatment has a C++ port in [`verification/cpp/section4_kdv/`](../../verification/cpp/section4_kdv/README.md), with formal scaffolding in the four proof assistants and the standard-library Python reference in [`verification/section4_kdv/`](../../verification/section4_kdv/README.md). The conservation-law identities checked across these ports back the numeric stability claims of the chapter.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`KdV_b_correction_Chapter16_EN.pdf`](KdV_b_correction_Chapter16_EN.pdf) | 6.9 MB | chapter 16 — English edition, ~7.2 MB, figure-rich typesetting |
| [`KdV_b_correction_Chapter16_RU.pdf`](KdV_b_correction_Chapter16_RU.pdf) | 7.0 MB | chapter 16 — Russian edition, ~7.4 MB, complete independent publication |

## 🔗 Cross-References

- [Word editions — docs/kdv/](../../docs/kdv/README.md)
- [Section 4 verification — C++ port](../../verification/cpp/section4_kdv/README.md)
- [Section 4 verification — Python reference](../../verification/section4_kdv/README.md)
- [Root README — Research Programs](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

**papers/kdv/** — глава 16 об уравнении Кортевега–де Фриза: как универсальная поправка *b* ≈ 0.0785 проявляется во взаимодействиях солитонов интегрируемой иерархии КдФ. Два полных издания: английское (7.2 МБ) и русское (7.4 МБ). Word-версии — в `docs/kdv/`; численная проверка — раздел 4 верификации (`verification/cpp/section4_kdv/` — псевдоспектральный порт на C++).

---

<div align="center">

**[⬆ Back to top](#-papers--kdv--soliton-interactions-under-the-b-correction-chapter-16-en--ru)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>