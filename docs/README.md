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