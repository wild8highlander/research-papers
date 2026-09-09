# 📄 Papers — Published PDF Research Papers

> **Navigation:** **`papers`**

![Papers](https://img.shields.io/badge/Content-Research%20Papers-blue?style=flat-square&logo=adobeacrobatreader&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Repo](https://img.shields.io/badge/Repo-wild8highlander%2Fresearch--papers-181717?style=flat-square&logo=github&logoColor=white)

This directory is the **journal-facing face of the repository**: the finished, typeset PDF papers that present the research programs to the scientific community. Each subfolder bundles one paper (or one paper in two language editions), stored as final PDFs exactly as they circulate — with LaTeX sources available separately in [`src/`](../src/README.md) and Word-form monographs in [`docs/`](../docs/README.md).

Three collections are hosted here. The **correction-b** pair (`main.pdf`, `main_v2.pdf`) is the full-length paper on the universal polarization correction *b* = π/(4π² + 2π√3) ≈ 0.0785 and the analytical proof of 3D Navier–Stokes regularity without dissipation. The **KdV chapter** (EN and RU editions of `KdV_b_correction_Chapter16`) extends the same constant to soliton interactions of the Korteweg–de Vries equation. The **NSE preprint** (`preprint_v1/v2`) is the compact statement of the regularity argument — the fastest complete read for a newcomer, with the title *"Correction b as Polarization Twisting: Analytical Proof of 3D Navier–Stokes Regularity without Dissipation"*.

All numbers quoted in these papers are cross-verified in this very repository: the [verification framework](../verification/README.md) re-derives each headline constant in eleven languages, and the AB-Cloud companion suite does the same in ten more. Citing these papers is always welcome — see the [citation block](../README.md#-citation) in the root README (BibTeX, APA, and [`CITATION.cff`](../CITATION.cff)).

## 📑 The Collections at a Glance

| Collection | Editions | Volume | Research program |
|---|---|---|---|
| **correction-b** | `main.pdf`, `main_v2.pdf` (identical 2.3 MB typeset editions) | ~2.3 MB each | NSE regularity via polarization correction *b* |
| **kdv** | `KdV_b_correction_Chapter16_EN.pdf` (7.2 MB), `..._RU.pdf` (7.4 MB) | ~14.6 MB total | KdV soliton interactions under the b-correction |
| **preprint** | `preprint_v1.pdf`, `preprint_v2.pdf` (identical 120 KB) | ~0.24 MB total | Compact NSE preprint — best first read |

The two PDFs inside each of `correction-b/` and `preprint/` are byte-identical twins kept under two filenames for convenience (`main` vs `main_v2`, `v1` vs `v2`) — they represent the same final revision, so either may be cited. The KdV chapter ships as two genuinely separate language editions produced from the same source.

## 🧭 Which Paper Should You Read First?

1. **`preprint/preprint_v2.pdf`** — ~100 KB, the shortest complete statement of the NSE result: the correction *b*, the rotation angle θ_b ≈ 7.07°, and the 3.5× BKM-criterion reduction. Read this if you have fifteen minutes.
2. **`correction-b/main_v2.pdf`** — the full paper: derivation of *b* from the Kirchhoff point-vortex system, the regularity proof, and the numerical stress-tests.
3. **`kdv/KdV_b_correction_Chapter16_EN.pdf`** — the integrable-systems continuation: how the same constant shows up in soliton interactions; read the RU edition instead if you prefer Russian.

After the papers, the natural next steps are the formal/computational verification in [`verification/`](../verification/README.md) and the AB-Cloud complex in [`ab-cloud/`](../ab-cloud/README.md).

## 🔬 Verification Backing

Every quantitative claim in these papers maps onto a section of the multi-language verification framework:

- **Section 1** — the value and bounds of *b* (asserted in all 8 language ports, proved in all 4 proof assistants);
- **Section 2** — the preprint's regularity argument chain;
- **Section 4** — the KdV soliton results (pseudospectral port in C++);
- **Sections 3 & 6** — the AB-Cloud ↔ ζ-zero correspondence for the spectral claims referenced by the correction-b paper.

The Word monographs backing these papers (with figure-rich layouts) live in [`docs/correction-b/`](../docs/correction-b/README.md) and [`docs/kdv/`](../docs/kdv/README.md).

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`correction-b/`](correction-b/) | — | the correction-b paper — two identical typeset editions (main / main_v2) |
| [`kdv/`](kdv/) | — | the KdV book chapter — English and Russian editions |
| [`preprint/`](preprint/) | — | the compact NSE preprint — v1 and v2 (same revision) |

## 🗂 Directory Layout

```
papers/
├── correction-b/   # 3 files
│   ├── main.pdf
│   ├── main_v2.pdf
│   └── README.md  (this file)
├── kdv/   # 3 files
│   ├── KdV_b_correction_Chapter16_EN.pdf
│   ├── KdV_b_correction_Chapter16_RU.pdf
│   └── README.md  (this file)
├── preprint/   # 3 files
│   ├── preprint_v1.pdf
│   ├── preprint_v2.pdf
│   └── README.md  (this file)
└── README.md  (this file)
```

## 🇷🇺 Краткое резюме (Russian Summary)

**papers/** — готовые PDF-статьи репозитория. Три подборки: **correction-b/** — полная статья о поправке *b* ≈ 0.0785 и доказательстве регулярности 3D Navier–Stokes без диссипации (два идентичных издания main/main_v2); **kdv/** — глава о солитонах КдФ с той же поправкой (английское и русское издания, ~7 МБ каждый); **preprint/** — компактный препринт о регулярности NSE — лучшая первая статья для знакомства. LaTeX-исходники — в `src/`, вёрстки Word — в `docs/`. Все числа из статей воспроизводятся верификацией в 11 языках (см. `verification/`).

---

<div align="center">

**[⬆ Back to top](#-papers--published-pdf-research-papers)** · 
**[Repository root](README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>


---

## 📖 Deep Reading Guide

### The Three Collections in Detail

**`correction-b/` — the flagship paper.** Two byte-identical typeset editions (`main.pdf`, `main_v2.pdf`, ~2.3 MB each) present the full-length argument: the derivation of the universal polarization correction *b* from the Kirchhoff point-vortex system, its interpretation as a −90° polarization twist (rotation angle θ_b ≈ 7.07°), the analytical proof of 3D Navier–Stokes regularity without artificial dissipation, and the numerical stress-tests that bracket the analytic claims. Read `main_v2.pdf` when citing — both files are the same final revision, but the `_v2` filename is the one referenced across the repository's documentation.

**`kdv/` — the integrable-systems continuation.** *KdV_b_correction_Chapter16* ships as two genuinely distinct language editions: English (7.2 MB) and Russian (7.4 MB), typeset independently from the same content. The chapter studies soliton interactions of the Korteweg–de Vries equation under the same *b*-correction — phase shifts, shape preservation, conserved quantities — and connects the integrable-systems picture back to the polarization twist of the flagship paper. The computational backbone is the C++ pseudospectral port in [`verification/cpp/section4_kdv/`](../verification/cpp/section4_kdv/README.md).

**`preprint/` — the fifteen-minute read.** `preprint_v1.pdf` and `preprint_v2.pdf` (identical, ~120 KB) state the regularity result compactly: the constant, the angle, the 3.5× reduction of the BKM blow-up integral, and the structure of the proof. If you cite one thing from this repository, this is the fastest complete reference; its LaTeX source is [`src/preprint/preprint.tex`](../src/preprint/preprint.tex).

### How These Papers Are Backed

Every quantitative statement in the PDFs has a verification path inside this same repository — that is the house style. The mapping:

| Paper claim | Verification path |
|---|---|
| Value and bounds of *b* | [`verification/section1_correction_b/`](../verification/section1_correction_b/README.md) — 4 proof assistants + 4 computational languages |
| Rotation algebra (sin θ_b = b, R_b orthogonal) | formal tier: `R_b_orthogonal`, `R_b_det_one` in Lean 4; mirrors in Coq/Isabelle/Agda |
| BKM integral reduction 3.5× | Sections 1–2 computational ports; formal bounds in Lean 4 / Isabelle |
| KdV soliton phase shifts | [`verification/cpp/section4_kdv/`](../verification/cpp/section4_kdv/README.md) + Python port |
| Spectral claims referenced from correction-b | Sections 3 & 6 + the AB-Cloud suite ([`ab-cloud/verification/`](../ab-cloud/verification/README.md)) |

The Word-layer editions with figure-rich layouts live in [`docs/correction-b/`](../docs/correction-b/README.md) and [`docs/kdv/`](../docs/kdv/README.md); the trilingual AB-Cloud monographs (which are a separate editorial line) live in [`ab-cloud/monographs/`](../ab-cloud/monographs/README.md).

### Citing These Papers

Cite the repository as a whole for software, and the specific PDF for the research result. The ready-made BibTeX and APA blocks are in the root README's [Citation](../README.md#-citation) section, and machine-readable metadata is in [`CITATION.cff`](../CITATION.cff) — GitHub renders it in the "Cite this repository" button. The Zenodo version DOI (`10.5281/zenodo.21825394`) pins the exact release; the concept DOI (`10.5281/zenodo.21825393`) covers all versions.

### File Manifest and Sizes

| Path | Size | Notes |
|---|---|---|
| [`correction-b/main.pdf`](correction-b/) | ~2.3 MB | typeset edition 1 (identical to v2) |
| [`correction-b/main_v2.pdf`](correction-b/) | ~2.3 MB | typeset edition 2 (citing preferred) |
| [`kdv/KdV_b_correction_Chapter16_EN.pdf`](kdv/) | ~7.2 MB | English edition |
| [`kdv/KdV_b_correction_Chapter16_RU.pdf`](kdv/) | ~7.4 MB | Russian edition |
| [`preprint/preprint_v1.pdf`](preprint/) | ~120 KB | identical to v2 |
| [`preprint/preprint_v2.pdf`](preprint/) | ~120 KB | identical to v1 |

The `papers/` tree intentionally contains **only** final PDFs — no drafts, no working files. Working manuscripts (Word) are in [`docs/`](../docs/README.md); compilable LaTeX is in [`src/`](../src/README.md). This separation keeps the "what do I cite?" question answerable at a glance.

---
## 🎓 Reading the Papers Critically

A short companion for readers who want to engage with the papers as a reviewer would — the questions each paper must answer, and where in the repository the answers live.

**For the correction-b paper, the three critical questions are:**

1. *Is the constant truly universal — or an artifact of the Kirchhoff normalization?* The derivation is algebraic and parameter-free; the formal tier compiles the constant's defining properties (positivity, bound, the sine identity) in four independent systems, and the numeric value is re-derived in eight language ecosystems. Universality here means exactly this: no input data, no fitting.
2. *Does the twist mechanism survive the passage from Euler to Navier–Stokes?* Section 2 of the verification framework is dedicated to precisely this chain; the computational ports construct the rotation matrices and verify unitarity and the BKM reduction numerically, while the formal tier compiles the algebraic skeleton.
3. *What is assumed but not proved?* The honest answer is itemised in [`verification/lean4/TODO_sorry.md`](../verification/lean4/TODO_sorry.md) — the numerical bound lemmas are the admitted gap; the structural core is closed. The paper's claims live in the PDF; the formal tier's coverage is stated exactly.

**For the KdV chapter:** the critical question is conservation. Soliton interactions must conserve mass, momentum and energy to machine precision — the C++ port's conserved-quantity checks are the direct answer, reproducible with one command from the [command reference](../README.md#%EF%B8%8F-appendix-k--full-command-reference).

**For the preprint:** the critical question is whether the compression lost anything essential. It did not — every move in the preprint expands to a numbered section of the flagship paper, and the verification mapping (Section 1 → constant, Section 2 → chain) is unchanged between the two documents.

## 🧾 Version and Provenance Notes

- Both correction-b editions are the **same final revision**; the `_v2` naming is a citation convenience, not a content revision. Nothing was revised silently: the repository's changelog and the documentation track record every content-affecting change.
- The KdV chapter's two editions were typeset independently — figure captions and hyphenation are native to each language; content is identical.
- The preprint's v1/v2 duplication mirrors the correction-b convention.
- All PDFs in this directory are committed as final — the directory is append-only by convention: new editions would arrive as new files, never as silent overwrites.

## 📎 Quick Links

- Citation blocks (BibTeX, APA, CFF): root README [Citation](../README.md#-citation) · [`CITATION.cff`](../CITATION.cff)
- Reading order for newcomers: root README [Navigation Map](../README.md#%EF%B8%8F-repository-navigation-map)
- The formal skeleton behind all three papers: root README [Appendix W](../README.md#-appendix-w--formal-verification-deep-dive)
- Licence for quoting and reuse: [`../LICENSE.md`](../LICENSE.md) (IPL-RP-1.0) — academic quotation with attribution is explicitly permitted

---
## 🧾 Paper-to-Verification Traceability Cards

One card per paper — the exact verification anchors, for citation reviews:

**correction-b (main/main_v2).**
Constant & bounds → Section 1 ports + 4 assistants · rotation algebra → Lean `R_b_*` lemmas + numeric echo · BKM reduction → Sections 1–2 · full derivation → this PDF, source in `src/main/`.

**KdV chapter (EN/RU).**
Conserved quantities → C++ port `section4_kdv` · two-soliton closed form → Python port Section 4 · integrability identities → formal tier Section 4 files.

**Preprint (v1/v2).**
Chain assertions → Section 2 ports + assistants · constant → Section 1 · the shortest citable statement of Program 1.

Each card's arrows resolve to concrete commands in the root README's [command reference](../README.md#%EF%B8%8F-appendix-k--full-command-reference) — traceability here is executable, not rhetorical.

---
## 🖨 Reproducing the Typesetting

To rebuild any PDF from source (see [`src/`](../src/README.md)):

```bash
cd src/main && pdflatex main.tex && pdflatex main.tex      # correction-b paper
cd src/preprint && pdflatex preprint.tex && pdflatex preprint.tex   # preprint
```

The KdV chapter has no LaTeX source in this repository (it arrived as typeset PDFs); its Word editions in `docs/kdv/` are the editable layer. When citing, always cite the committed PDF — a locally recompiled PDF can drift from the archived typesetting.

<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../README.md)
- 📖 [Как верифицируются утверждения](../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../papers/README.md) · 📚 [Монографии](../../docs/README.md) · 🧾 [LaTeX](../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

