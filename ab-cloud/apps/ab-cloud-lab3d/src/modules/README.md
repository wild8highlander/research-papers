# 🧊 lab3d · src · modules — scenes.js & zeta.js

> **Navigation:** [`ab-cloud`](../../../../README.md) › [`apps`](../../../README.md) › [`ab-cloud-lab3d`](../../README.md) › [`src`](../README.md) › **`modules`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The lab-3d app's **two domain modules**. `scenes.js` sets up the Three.js scene graph — camera, lighting, lattice geometry, vortex markers — exposing a small API the shell drives. `zeta.js` loads and normalises the embedded ζ-zero tables (from the same frozen datasets the numeric lab uses) and maps them onto the visual scene. Together they turn the numerical AB-Cloud into an explorable 3D object in the browser.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`scenes.js`](scenes.js) | 7.7 KB | Three.js scene module — lattice geometry, vortices, camera rig (≈8 KB) |
| [`zeta.js`](zeta.js) | 2.8 KB | ζ-zero data module — loading, normalising, mapping zeros to the scene (≈3 KB) |

## 🔗 Cross-References

- [src tree](../README.md)
- [Lab3d root](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Два доменных модуля лаборатории: scenes.js (сцена Three.js, геометрия решётки, вихри) и zeta.js (загрузка/нормализация нулей и их проекция в сцену).

---

<div align="center">

**[⬆ Back to top](#-lab3d--src--modules--scenesjs--zetajs)** · 
**[Repository root](../../../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>
<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../../../../README.md)
- 📖 [Как верифицируются утверждения](../../../../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../../../../papers/README.md) · 📚 [Монографии](../../../../../../docs/README.md) · 🧾 [LaTeX](../../../../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

