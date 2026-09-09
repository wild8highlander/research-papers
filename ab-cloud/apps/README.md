# apps — Two Interactive React Applications

Two self-contained web apps (React 18 + Vite) that make the project's
results explorable in a browser — no server, no Python, no Julia required.
Both ship **prebuilt static bundles** in `dist/` (committed, GitHub Pages
ready, relative base `./`), so you can serve them with any static file
server or open the Pages deployment directly.

| App | What it shows | Source | Prebuilt |
|---|---|---|---|
| [`ab-cloud-dashboard/`](ab-cloud-dashboard) | 37-test verdict dashboard + real-time ζ statistics (Web Worker) + in-browser 64-spinor Jacobi verification | `src/` | `dist/` |
| [`ab-cloud-lab3d/`](ab-cloud-lab3d) | WebGL 3D laboratory: Hofstadter lattice with vortices, Dirac cone, ζ critical strip (Three.js) | `src/` | `dist/` |

## Run from source

```bash
# app 1 — dashboard
cd apps/ab-cloud-dashboard
npm install
npm run dev          # Vite dev server with HMR
npm run build        # production build → dist/
npm run preview      # serve the production build locally

# app 2 — 3D laboratory
cd ../ab-cloud-lab3d
npm install && npm run dev
```

No environment variables, no backend; the heavy data (50 000 zeros, run
summary, frozen spinor data) is bundled into each app's `public/data/` and
`dist/data/`.

## Deploying to GitHub Pages

Each `dist/` is built with a relative base, so the folders can be served
from any path — e.g. via Pages from the `/docs` root, from a `gh-pages`
branch, or by copying `dist/` to any static host. Serving locally:
`npm run preview` or `python3 -m http.server -d apps/ab-cloud-dashboard/dist`.

## Кратко (по-русски)

- Два React-приложения (React 18 + Vite): дашборд 37 тестов с реальным
  временем (Web Worker) и браузерная спинор-проверка; и 3D-лаборатория на
  Three.js.
- Собранные статики уже в `dist/` (GitHub Pages-совместимы); из исходников —
  `npm install && npm run dev`.
- Данные (50 000 нулей, сводка прогона, замороженные спинор-данные)
  включены в приложение.

---
---

## 🖥 The Applications in Depth

### ab-cloud-dashboard

The statistics front-end: run reports, ζ-zero statistics computed **client-side in a web worker** over the embedded 50 000-zero table (`public/data/zeta_zeros_50000_embedded.txt` — the same frozen file the suites read), a spinor-64 browser, and the run-report viewer. Pages: `ZerosStats`, `Spinor64`, `RunReport` (see `src/pages/`). The worker (`src/worker/stats.worker.js`) keeps the UI responsive while the statistics compute.

### ab-cloud-lab3d

The Three.js laboratory: vortex textures, spectral surfaces, topological phase diagrams, rendered from the same parameter families the Python lab uses (`src/modules/scenes.js`, `zeta.js`). It is the interactive counterpart of the committed `lab-3d/outputs/` bundles.

### Serving and Building

Both apps ship committed `dist/` bundles — deployable to any static host (GitHub Pages included) with **zero build step**:

```bash
# develop
cd ab-cloud/apps/ab-cloud-dashboard && npm install && npm run dev
cd ab-cloud/apps/ab-cloud-lab3d     && npm install && npm run dev

# rebuild the committed bundles
npm run build    # per app; refreshes dist/
```

## 🇷🇺 Краткое резюме (Russian Summary)

**ab-cloud/apps/** — два React-приложения с закоммиченными сборками: **dashboard** (статистика по 50 000 нулей в web-workerе, отчёты прогонов, браузер spinor64) и **lab3d** (Three.js: вихревые текстуры, спектральные поверхности, фазовые диаграммы). Разработка — `npm run dev`, деплой — готовым `dist/` без сборки.

---
## 🧭 App Architecture Notes

Both apps share a minimal, deployment-friendly architecture:

- **Vite + React** — instant dev server, static production build;
- **committed `dist/`** — the built bundles are part of the repository, so Pages-style static serving works without CI;
- **frozen data in `public/`** — the dashboard reads the same committed zero table the suites use; the app never fetches from third parties;
- **web worker for statistics** — `ab-cloud-dashboard`'s `stats.worker.js` keeps heavy computation off the UI thread;
- **per-folder READMEs through the tree** — `src/`, `src/pages/`, `src/components/`, `src/worker/`, `public/`, `dist/` each carry their own documentation (the snapshot's folder-documentation discipline, applied to the apps).

## 🇷🇺 Резюме (Russian Summary)

Общая архитектура: Vite + React, закоммиченные `dist/`, замороженные данные в `public/`, web-worker для статистики, README в каждой папке. Разработка — `npm run dev`; деплой — статика без сборки.

---
## 🚀 Deploying the Apps

The committed `dist/` folders are deployable as-is:

```bash
# any static host: point it at the dist folder
ab-cloud/apps/ab-cloud-dashboard/dist/
ab-cloud/apps/ab-cloud-lab3d/dist/
```

For GitHub Pages, the snapshot's docs deployment is the primary target; the apps can be served from a project subpath unchanged (Vite's relative-base config in `vite.config.js` handles it).

<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../README.md)
- 📖 [Как верифицируются утверждения](../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../papers/README.md) · 📚 [Монографии](../../../docs/README.md) · 🧾 [LaTeX](../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

