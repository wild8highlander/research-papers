# 📓 verification · notebooks — the Jupyter Entry Point

> **Navigation:** [`verification`](../README.md) › **`notebooks`**

![Type](https://img.shields.io/badge/Type-Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **Jupyter notebook entry point** of the framework. The pinned `requirements.txt` installs the notebook stack plus the framework's Python dependencies so a notebook session can import the section verifiers and the shared utilities from [`common/`](../common/README.md), run them cell-by-cell, and visualise the output. This layer is for exploration and teaching — the authoritative results remain the CLI ports and their CI runs.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`requirements.txt`](requirements.txt) | 40 B | pinned notebook-stack dependencies (jupyter + framework deps) |

## ▶️ How to Run

```bash
pip install -r verification/notebooks/requirements.txt
jupyter lab
```

## 🔗 Cross-References

- [Shared utilities](../common/README.md)
- [Framework root](../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Вход для Jupyter: закреплённые зависимости ноутбука + фреймворка; импортируйте верификаторы разделов и запускайте по ячейкам.

---

<div align="center">

**[⬆ Back to top](#-verification--notebooks--the-jupyter-entry-point)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>