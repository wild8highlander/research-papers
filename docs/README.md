# 📚 Docs — Research Monographs, Word Editions & Static Site

> **Navigation:** **`docs`**

![Documents](https://img.shields.io/badge/Content-Monographs%20%2B%20Site-green?style=flat-square&logo=googledocs&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Repo](https://img.shields.io/badge/Repo-wild8highlander%2Fresearch--papers-181717?style=flat-square&logo=github&logoColor=white)

This directory is the **editorial and documentary layer** of the repository: Word-format research monographs, bilingual manuscript pairs, and the assets of the static landing site. Where [`papers/`](../papers/README.md) holds final journal-style PDFs, `docs/` preserves the **working manuscript layer** — figure-rich `.docx` editions that are easier to annotate, comment and circulate among collaborators, plus a couple of documents that exist only here.

Five research groups live here:

- **[`correction-b/`](correction-b/README.md)** — the correction-b monograph with figures, in EN and RU editions (each ~8.6 MB of Word manuscript);
- **[`kdv/`](kdv/README.md)** — the KdV chapter manuscript, EN and RU (~7.3 MB each);
- **[`klein-attractor/`](klein-attractor/README.md)** — two dedicated research reports on the Klein attractor: *Klein_FAttractor_NS_Research* (~1.0 MB) and *Klein_NS_Bridge_Research* (~1.9 MB);
- **[`choptuik-riemann/`](choptuik-riemann/README.md)** — the Choptuik–Riemann monograph (RU, ~4.5 MB), connecting critical-collapse scaling with the Riemann spectral story;
- **[`site/`](site/README.md)** — the standalone static landing page (`index.html` + `style.css`), a no-build fallback mirror of the project's front page.

In addition, [`license.md`](license.md) mirrors the licence notice for the MkDocs documentation build, which pulls page sources from this directory tree. The trilingual full licence texts themselves remain at the repository root — [`LICENSE.md`](../LICENSE.md) (authoritative EN), [`LICENSE.ru.md`](../LICENSE.ru.md) and [`LICENSE.zh.md`](../LICENSE.zh.md) — and are not modified here.

Everything in `docs/` is documentation of the research, not code; nothing here is executed by CI. The AB-Cloud monographs (v22, trilingual, in five formats each) are **not** in this directory — they live in the consolidated snapshot at [`ab-cloud/monographs/`](../ab-cloud/monographs/README.md), which is the single authoritative location for them since v1.5.0.

## 🗺 How docs/ Relates to papers/ and src/

| Layer | Directory | Format | Role |
|---|---|---|---|
| Final papers | [`papers/`](../papers/README.md) | PDF | journal-facing typeset editions |
| LaTeX sources | [`src/`](../src/README.md) | `.tex` | compilable sources of the PDFs |
| **Manuscripts** | **`docs/`** | `.docx` | figure-rich Word monographs, EN+RU pairs |
| AB-Cloud monographs | [`ab-cloud/monographs/`](../ab-cloud/monographs/README.md) | md/tex/docx/pdf/html/pptx | the trilingual v22 editions + v21 original |
| Docs site | [`mkdocs.yml`](../mkdocs.yml) + this tree | Markdown/HTML | GitHub Pages build input |

For any given research program, the reading chain is: preprint PDF → full paper PDF → Word monograph (this directory) → verification section. The Word layer is intentionally redundant: it preserves the manuscripts as circulated during the research process, with figure placements and editorial marks intact.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`choptuik-riemann/`](choptuik-riemann/) | — | Choptuik–Riemann monograph (Word, RU) |
| [`correction-b/`](correction-b/) | — | correction-b monograph, EN + RU Word editions |
| [`kdv/`](kdv/) | — | KdV chapter manuscript, EN + RU Word editions |
| [`klein-attractor/`](klein-attractor/) | — | two Klein-attractor research reports (Word) |
| [`license.md`](license.md) | 973 B | # License / Лицензия / 许可证 **© 2026 Isaev Iskhak Khamzatovich (wild8highlander). All Rights Reserved.** This project is distributed under the **Individual Proprietary License (IPL-… |
| [`site/`](site/) | — | static landing page (HTML + CSS) |

## 🗂 Directory Layout

```
docs/
├── choptuik-riemann/   # 2 files
│   ├── Choptuik_Riemann_Monograph_RU.docx
│   └── README.md  (this file)
├── correction-b/   # 5 files
│   ├── en/   # 2 files
│   │   ├── monograph_with_figures.docx
│   │   └── README.md  (this file)
│   ├── ru/   # 2 files
│   │   ├── monograph_with_figures.docx
│   │   └── README.md  (this file)
│   └── README.md  (this file)
├── kdv/   # 5 files
│   ├── en/   # 2 files
│   │   ├── KdV_b_correction_Chapter16.docx
│   │   └── README.md  (this file)
│   ├── ru/   # 2 files
│   │   ├── KdV_b_correction_Chapter16.docx
│   │   └── README.md  (this file)
│   └── README.md  (this file)
├── klein-attractor/   # 3 files
│   ├── Klein_FAttractor_NS_Research.docx
│   ├── Klein_NS_Bridge_Research.docx
│   └── README.md  (this file)
├── site/   # 3 files
│   ├── index.html
│   ├── README.md  (this file)
│   └── style.css
├── license.md
└── README.md  (this file)
```

## 🇷🇺 Краткое резюме (Russian Summary)

**docs/** — редакционный слой репозитория: Word-монографии с рисунками и статический сайт. Здесь лежат: монография correction-b (EN + RU), рукопись главы КдФ (EN + RU), два отчёта об аттракторе Клейна, монография Чоптуика–Римана (RU) и лендинг `site/` (HTML+CSS). Итоговые PDF — в `papers/`, LaTeX — в `src/`, трёхъязычные монографии AB-Cloud — в `ab-cloud/monographs/`. Все тексты покрыты лицензией IPL-RP-1.0.

---

<div align="center">

**[⬆ Back to top](#-docs--research-monographs-word-editions--static-site)** · 
**[Repository root](README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>


---

## 📖 Working With the Manuscript Layer

### Why Word Editions Exist

The `.docx` monographs are not duplicates of the PDFs — they are the **working layer** of the research, preserved deliberately. They carry the figure placements, editorial marks and annotation-friendly formatting that collaborators used while the research was in progress. When a reviewer asks "show me the manuscript as it circulated", this directory is the answer. The journal-facing PDFs in [`papers/`](../papers/README.md) are the frozen outcome; this directory is the process record.

### Per-Group Guides

**[`correction-b/`](correction-b/README.md)** — `monograph_with_figures.docx` in EN (~8.6 MB) and RU editions, each in its own subfolder with its own README. This is the full correction-b manuscript with all figures inline — the same argument as the paper, at manuscript depth.

**[`kdv/`](kdv/README.md)** — `KdV_b_correction_Chapter16.docx` EN and RU (~7.3 MB each). The Word twin of the KdV chapter in [`papers/kdv/`](../papers/kdv/README.md).

**[`klein-attractor/`](klein-attractor/README.md)** — two dedicated research reports that exist *only* here (no PDF edition): *Klein_FAttractor_NS_Research.docx* (~1.0 MB), the ergodic-theoretic study of the attractor, and *Klein_NS_Bridge_Research.docx* (~1.9 MB), the bridge back to Navier–Stokes. Together they cover Section 5 of the verification framework.

**[`choptuik-riemann/`](choptuik-riemann/README.md)** — `Choptuik_Riemann_Monograph_RU.docx` (~4.5 MB, RU): the widest-ranging document in the collection, connecting Choptuik critical-collapse scaling with the Riemann spectral story. A bridge document between the gravitational-collapse literature and this repository's spectral programme.

**[`site/`](site/README.md)** — the standalone static landing page: `index.html` + `style.css`, no build step. It mirrors the project front page for offline/off-Pages use, and it is the emergency fallback if the MkDocs Pages deployment is unavailable.

### Reading Chain Per Research Program

For any given program, the documents form a chain with verification at the end:

| Program | Preprint / summary | Full paper | Word manuscript | Verification |
|---|---|---|---|---|
| NSE regularity | [`papers/preprint/`](../papers/preprint/README.md) | [`papers/correction-b/`](../papers/correction-b/README.md) | `correction-b/` (this dir) | Sections 1–2 |
| KdV solitons | — | [`papers/kdv/`](../papers/kdv/README.md) | `kdv/` (this dir) | Section 4 |
| Klein attractor | — | — | `klein-attractor/` (this dir) | Section 5 |
| Choptuik–Riemann | — | — | `choptuik-riemann/` (this dir) | cross-links to Sections 3, 6 |
| AB-Cloud | — | — | [`ab-cloud/monographs/`](../ab-cloud/monographs/README.md) (v22, RU/EN/ZH) | AB-Cloud suites |

### The licence.md Note

[`license.md`](license.md) in this directory is a short notice mirror for the MkDocs build (which pulls page sources from this tree) — the authoritative trilingual licence texts remain at the repository root: [`LICENSE.md`](../LICENSE.md) (EN, authoritative), [`LICENSE.ru.md`](../LICENSE.ru.md), [`LICENSE.zh.md`](../LICENSE.zh.md). Nothing in this directory modifies those files, and folder-level documentation is covered by the same IPL-RP-1.0 licence.

### For Editors and Annotators

When circulating the Word editions, keep in mind the licence's narrow permissions: viewing, one personal backup, academic quotation with attribution. Annotation of a personal copy for review purposes falls under viewing; redistribution of edited versions does not and requires written consent. Cite with attribution — it is always welcome.

---
## 🖥 The Static Site

[`site/`](site/README.md) deserves a paragraph of its own. It is a deliberately dependency-free artifact: `index.html` + `style.css`, openable by double-click from a filesystem, no server, no build. Its roles:

1. **Emergency front page** — if the MkDocs Pages deployment is down or not yet initialised, this page mirrors the project's essential links;
2. **Offline mirror** — a personal backup copy (one of the licence's permitted uses) remains navigable;
3. **Template** — the minimal look the MkDocs Material theme renders on top of.

It is regenerated by hand only when the front-page essentials change; the MkDocs site is the living documentation, this is the snapshot.

## 🗃 File Inventory With Sizes

| File | Size | Language | Verification anchor |
|---|---|---|---|
| `correction-b/en/monograph_with_figures.docx` | ~8.6 MB | EN | Sections 1–2 |
| `correction-b/ru/monograph_with_figures.docx` | ~8.6 MB | RU | Sections 1–2 |
| `kdv/en/KdV_b_correction_Chapter16.docx` | ~7.3 MB | EN | Section 4 |
| `kdv/ru/KdV_b_correction_Chapter16.docx` | ~7.3 MB | RU | Section 4 |
| `klein-attractor/Klein_FAttractor_NS_Research.docx` | ~1.0 MB | EN | Section 5 |
| `klein-attractor/Klein_NS_Bridge_Research.docx` | ~1.9 MB | EN | Section 5 |
| `choptuik-riemann/Choptuik_Riemann_Monograph_RU.docx` | ~4.5 MB | RU | cross-links 3, 6 |
| `site/index.html` + `site/style.css` | small | EN | — |
| `license.md` | 973 B | trilingual notice | — |

## 🧭 Documentation Layers, Once More

The repository's documentation is layered, and `docs/` is the middle layer:

1. **Root README** — orientation, results, quick start (the front door);
2. **Folder READMEs** — per-directory self-documentation, 250+ files (the map);
3. **This directory** — the manuscript layer of the *research itself* (the record);
4. **MkDocs site** — the searchable web rendering (the shop window);
5. **Static site** — the no-build fallback (the lifeboat).

When you extend any layer, check the others for consistency — the [house style](../README.md#%EF%B8%8F-appendix-o--makefile-reference) keeps them structurally aligned, and the link checker workflow flags anything that rots.

---
## 🧷 Preservation Notes

The Word layer's long-term readability is part of the repository's contract with the future:

- the `.docx` files are committed as-is (no LFS roundtripping beyond the repository's `.gitattributes` policy), so any Git-aware tool twenty years from now can extract them;
- the monographs' **figure sets** live inside the documents and alongside them (AB-Cloud editions keep per-language `figures/` trees);
- where a format risk exists, the same content exists in a second format — the AB-Cloud monographs ship six formats per language precisely for this reason;
- the licence's "one personal unmodified backup" clause exists so that a reader can hold this layer offline without legal ambiguity.

**For annotators:** comment and track-changes in your private copy; the permitted uses cover review workflows. Redistributing an annotated edition is a derivative work — that requires written consent under IPL-RP-1.0.

---
## 🧾 Manuscript-to-Verification Anchors

Each manuscript group's verification anchor, for review workflows:

| Manuscript | Anchor |
|---|---|
| correction-b (EN/RU) | Sections 1–2 of the framework |
| KdV chapter (EN/RU) | Section 4 (C++ workhorse) |
| Klein attractor reports | Section 5 |
| Choptuik–Riemann monograph | cross-links Sections 3 & 6 |

The anchoring is one-directional by design: manuscripts cite verification, verification never depends on manuscripts — code is the dependency root.

<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../README.md)
- 📖 [Как верифицируются утверждения](../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../papers/README.md) · 📚 [Монографии](../../docs/README.md) · 🧾 [LaTeX](../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

