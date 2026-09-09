# 🚢 dashboard · dist — the Committed Production Bundle

> **Navigation:** [`ab-cloud`](../../../README.md) › [`apps`](../../README.md) › [`ab-cloud-dashboard`](../README.md) › **`dist`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Type](https://img.shields.io/badge/Type-Production%20Bundle-00C853?style=flat-square)

The **committed production build** of the dashboard (Vite output): the compiled JS/CSS in `assets/`, the copied `public/` payload in `data/`, and the entry `index.html`. Committing `dist/` is deliberate — it makes the dashboard deployable to GitHub Pages straight from the repository, with no build step on the Pages side. Treat everything here as generated: rebuild from the sources with `npm run build` in the dashboard root rather than editing by hand.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`assets/`](assets/) | — | compiled JS/CSS bundles (hashed filenames) |
| [`data/`](data/) | — | the copied static data payload |
| [`index.html`](index.html) | 422 B | page markup |

## 🗂 Directory Layout

```
dist/
├── assets/   # 4 files
│   ├── index-B11dp_q8.js
│   ├── index-C2qjEK4Q.css
│   ├── README.md  (this file)
│   └── stats.worker-D2J12aWj.js
├── data/   # 3 files
│   ├── README.md  (this file)
│   ├── run_summary.json
│   └── zeta_zeros_50000_embedded.txt
├── index.html
└── README.md  (this file)
```

## 🔗 Cross-References

- [Dashboard root (build commands)](../README.md)
- [Apps layer](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Закоммиченный прод-бандл дашборда (Vite): assets/, data/ и index.html — GitHub Pages деплоится прямо из репозитория; править руками не нужно, пересобирайте npm run build.

---

<div align="center">

**[⬆ Back to top](#-dashboard--dist--the-committed-production-bundle)** · 
**[Repository root](../../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>