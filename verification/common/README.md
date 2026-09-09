# 🧰 verification · common — Shared Python Utilities

> **Navigation:** [`verification`](../README.md) › **`common`**

![Python](https://img.shields.io/badge/Python-3.10–3.12-informational?style=flat-square&logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **shared utility layer** of the Python side of the framework: the pieces that every front-end (API, demos, notebooks) reuse instead of re-implementing. `python/verifier_base.py` defines the common verifier behaviour — banner printing, assertion bookkeeping and the final JSON verdict — so all front-ends speak the same output contract as the standalone ports; `config.py` centralises paths and tolerances; `main.py` provides a CLI aggregation entry point; `__init__.py` exposes the package surface.

The layer is intentionally tiny (~2 KB total) and pure standard library where possible, matching the framework's "no hidden dependencies" rule. The reference implementations in `section*/python/` do not import it (they are single-file by design); this layer exists for the composed front-ends.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`python/`](python/) | — | the package itself — base classes, config, CLI aggregate |

## 🗂 Directory Layout

```
common/
├── python/   # 5 files
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── README.md  (this file)
│   └── verifier_base.py
└── README.md  (this file)
```

## 🔗 Cross-References

- [Framework root](../README.md)
- [API layer](../api/README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

**verification/common/** — общие утилиты Python-стороны: базовый класс верификатора (баннер, PASS-книга, JSON-вердикт), конфиг путей и допусков, CLI-агрегатор. Используется API/демо/ноутбуками; референс-порты сознательно самодостаточны.

---

<div align="center">

**[⬆ Back to top](#-verification--common--shared-python-utilities)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>