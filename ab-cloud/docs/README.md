# docs — MkDocs Material Documentation Site

The sources of the GitHub Pages documentation site
(<https://wild8highlander.github.io/ab-cloud-research>), built with
**MkDocs Material**. Navigation is defined in `../mkdocs.yml`; deployment
is automated by the `deploy-docs` workflow (`.github/workflows/deploy-docs.yml`).

## Pages

| Page | Contents |
|---|---|
| `index.md` | landing: what the project is, headline results |
| `quickstart.md` | fastest paths: Julia suite, Python verification, apps |
| `julia-suite.md` | the 37-test two-pass suite explained (modes, flags, outputs) |
| `verification.md` | the 10-language verification suite and the three objections |
| `monographs.md` | the trilingual v22 monograph package and formats |
| `monograph-v21.md` | the original v21 monograph and the v21.1 corrections |
| `results.md` | how to read `results/run_20260902_134759/` and the reference logs |
| `lab3d.md` | the 3D laboratory: modes A–J, committed runs |
| `citation.md` | citation formats, DOI, ORCID |
| `faq.md` | frequent questions and misconceptions |
| `license.md` | CC BY-NC-SA 4.0 summary |
| `javascripts/mathjax.js` | MathJax bootstrap for inline formulas |

## Build locally

```bash
pip install mkdocs mkdocs-material
mkdocs serve        # live-reload on http://localhost:8000
mkdocs build        # static site into site/
```

Or from the repository root: `make docs` / `make docs-serve`.

## Conventions

- Pages stay short and link into the repository (the deep documentation
  lives next to the code, in the per-folder READMEs).
- Math is rendered by MathJax; keep formulas in `$…$` / `$$…$$`.
- New pages must be registered in `../mkdocs.yml` `nav:` — otherwise they
  are orphaned and the link-checker workflow flags them.

## Кратко (по-русски)

- Исходники сайта документации (MkDocs Material), публикуемого на GitHub
  Pages воркфлоу `deploy-docs`.
- Локально: `pip install mkdocs mkdocs-material && mkdocs serve`.
- Страницы: quickstart, julia-suite, verification, monographs (+v21),
  results, lab3d, citation, faq, license; навигация — в `mkdocs.yml`.

---
---

## 🧱 The Snapshot's Documentation Site

This directory is the MkDocs source tree of the snapshot's own documentation site (configured by the sibling [`mkdocs.yml`](../mkdocs.yml)):

| Page | Content |
|---|---|
| `index.md` | the snapshot's front page |
| `quickstart.md` | the fast path: run the suite in one command |
| `verification.md` | the three objections and the 10-language answer |
| `monographs.md` / `monograph-v21.md` | the edition guide (v22 trilingual; v21 historical) |
| `julia-suite.md` | the Julia provenance archive and runners |
| `lab3d.md` | the 3D laboratory and its bundles |
| `results.md` | the archive and how to diff against it |
| `citation.md` | how to cite the snapshot and its versions |
| `faq.md` | the snapshot-level FAQ |
| `license.md` | the licence notice (authoritative texts at the snapshot/root level) |

MathJax rendering is enabled via `javascripts/mathjax.js`. Build locally: `cd ab-cloud && mkdocs serve`.

The page sources complement — not duplicate — the folder READMEs: the READMEs document *directories*, these pages document *topics*. Keep both in mind when extending the snapshot's documentation.

## 🇷🇺 Краткое резюме (Russian Summary)

**ab-cloud/docs/** — исходники собственного MkDocs-сайта снапшота: quickstart, верификация, монографии, Julia-набор, лаборатория, результаты, цитирование, FAQ. Математика — MathJax; локально: `cd ab-cloud && mkdocs serve`.

---
## ✍️ Extending the Snapshot Site

Adding a page to the snapshot's MkDocs site is a three-file change:

1. the page source (`docs/<page>.md`, house style applies);
2. the nav entry in [`../mkdocs.yml`](../mkdocs.yml);
3. cross-links from the folder READMEs the page documents.

The site's job is *topics*; the folder READMEs' job is *directories*; the root README's job is *the repository as a whole*. A change is fully documented when all three layers agree.

---
## 🔗 Page-to-README Cross-Map

| Site page | Companion README |
|---|---|
| `index.md` | [`../README.md`](../README.md) |
| `quickstart.md` | [`../README.md` quick start](../README.md) |
| `verification.md` | [`../verification/README.md`](../verification/README.md) |
| `monographs.md` | [`../monographs/README.md`](../monographs/README.md) |
| `julia-suite.md` | [`../code/julia/README.md`](../code/julia/README.md) |
| `lab3d.md` | [`../lab-3d/README.md`](../lab-3d/README.md) |
| `results.md` | [`../results/README.md`](../results/README.md) |
| `citation.md` | root README Citation |
| `faq.md` | root README FAQ |

<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../README.md)
- 📖 [Как верифицируются утверждения](../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../papers/README.md) · 📚 [Монографии](../../../docs/README.md) · 🧾 [LaTeX](../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

