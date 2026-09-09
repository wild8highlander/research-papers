# 🧊 lab3d · src — React Source of the 3D Lattice Laboratory

> **Navigation:** [`ab-cloud`](../../../README.md) › [`apps`](../../README.md) › [`ab-cloud-lab3d`](../README.md) › **`src`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Type](https://img.shields.io/badge/Type-Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white)

The **React source tree of the AB-Cloud lab-3d web app** — the browser-based 3D visualisation of the lattice and its vortex decoration, rendered with Three.js. The tree is minimal: `App.jsx` (shell), `main.jsx` (entry), `styles.css`, and a `modules/` folder with the two domain modules — 3D scenes and the ζ-zero handling. The committed production bundle lives in `../dist/` for GitHub Pages hosting.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`App.jsx`](App.jsx) | 3.2 KB | app shell of the 3D laboratory |
| [`main.jsx`](main.jsx) | 188 B | entry point |
| [`modules/`](modules/) | — | domain modules — scenes.js (Three.js setup) and zeta.js (zero data handling) |
| [`styles.css`](styles.css) | 1.1 KB | global stylesheet |

## 🗂 Directory Layout

```
src/
├── modules/   # 3 files
│   ├── README.md  (this file)
│   ├── scenes.js
│   └── zeta.js
├── App.jsx
├── main.jsx
├── README.md  (this file)
└── styles.css
```

## 🔗 Cross-References

- [Lab3d app root](../README.md)
- [Apps layer](../../README.md)
- [lab-3d numeric package](../../../lab-3d/README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

React-исходники веб-лаборатории 3D (Three.js): оболочка, вход, стили и модули scenes.js (сцена) + zeta.js (данные нулей). Прод-сборка — ../dist/.

---

<div align="center">

**[⬆ Back to top](#-lab3d--src--react-source-of-the-3d-lattice-laboratory)** · 
**[Repository root](../../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>
<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../../../README.md)
- 📖 [Как верифицируются утверждения](../../../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../../../papers/README.md) · 📚 [Монографии](../../../../../docs/README.md) · 🧾 [LaTeX](../../../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

