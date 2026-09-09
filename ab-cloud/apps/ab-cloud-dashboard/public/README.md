# 📦 dashboard · public — Static Assets Copied into the Build

> **Navigation:** [`ab-cloud`](../../../README.md) › [`apps`](../../README.md) › [`ab-cloud-dashboard`](../README.md) › **`public`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **static asset folder** of the dashboard: everything here is copied verbatim into the production bundle (`dist/`) by Vite at build time. It holds the static data payload the front-end fetches — `data/` with the JSON datasets backing the RunReport and Spinor64 pages — plus any root-level static files. Because this folder is committed, the dashboard renders identically whether served from `dist/` locally or from GitHub Pages.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`data/`](data/) | — | JSON datasets fetched by the dashboard pages |

## 🗂 Directory Layout

```
public/
├── data/   # 3 files
│   ├── README.md  (this file)
│   ├── run_summary.json
│   └── zeta_zeros_50000_embedded.txt
└── README.md  (this file)
```

## 🔗 Cross-References

- [Dashboard src](../src/README.md)
- [Apps layer](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Статические ассеты дашборда: Vite копирует их в dist как есть; data/ — JSON-датасеты, которые фетчат страницы.

---

<div align="center">

**[⬆ Back to top](#-dashboard--public--static-assets-copied-into-the-build)** · 
**[Repository root](../../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>