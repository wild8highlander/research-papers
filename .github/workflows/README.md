# 🔁 .github · workflows — 17 CI/CD Pipelines

> **Navigation:** [`.github`](../README.md) › **`workflows`**

![CI](https://img.shields.io/badge/Workflows-17-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **complete GitHub Actions catalogue** of the repository — 17 YAML workflow definitions covering the full contribution lifecycle. They form four functional layers; every workflow is idempotent, uses pinned action versions, and requires no secrets beyond the built-in `GITHUB_TOKEN` (Codecov optionally accepts a token for coverage upload).

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`benchmark.yml`](benchmark.yml) | 535 B | performance benchmarks of the numerical suites |
| [`ci-cross-language.yml`](ci-cross-language.yml) | 478 B | the cross-language matrix — every language port must PASS with a JSON verdict |
| [`ci-extended-languages.yml`](ci-extended-languages.yml) | 2.9 KB | builds the extended toolchains (Lean, Coq, Isabelle, Agda, Rust, C++, Haskell) |
| [`ci-python.yml`](ci-python.yml) | 613 B | Python reference suite: pytest across the six verification sections |
| [`ci.yml`](ci.yml) | 1.6 KB | primary CI pipeline — orchestrates the layered verification build |
| [`codeql.yml`](codeql.yml) | 1.8 KB | CodeQL static security analysis |
| [`coverage.yml`](coverage.yml) | 1.2 KB | coverage collection and upload (Codecov) |
| [`dependency-review.yml`](dependency-review.yml) | 627 B | dependency diff and vulnerability review on pull requests |
| [`deploy-docs.yml`](deploy-docs.yml) | 1.1 KB | builds MkDocs Material and deploys to GitHub Pages |
| [`docker.yml`](docker.yml) | 524 B | builds and pushes the verification containers |
| [`labeler.yml`](labeler.yml) | 471 B | auto-labels pull requests by touched paths |
| [`link-checker.yml`](link-checker.yml) | 1.5 KB | crawls documentation for dead links |
| [`lint.yml`](lint.yml) | 1.6 KB | pre-commit run — black, ruff, codespell across the tree |
| [`release-drafter.yml`](release-drafter.yml) | 537 B | drafts release notes from merged PRs |
| [`scorecard.yml`](scorecard.yml) | 1.7 KB | OpenSSF Scorecard assessment; publishes .github/badges/scorecard-badge.json |
| [`stale.yml`](stale.yml) | 1.7 KB | marks and closes stale issues/PRs |
| [`zenodo.yml`](zenodo.yml) | 9.0 KB | keeps Zenodo deposit metadata in sync for DOI minting |

## 🔗 Cross-References

- [Parent — .github/](../README.md)
- [Root README — Security](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

**.github/workflows/** — 17 пайплайнов GitHub Actions: четырёхуровневый CI (python → extended → cross-language → главный), линт (black/ruff/codespell), покрытие, бенчмарки, CodeQL + Scorecard + dependency-review, деплой MkDocs, Docker, релизы, Zenodo, проверка ссылок, stale и лейблер.

---

<div align="center">

**[⬆ Back to top](#-github--workflows--17-cicd-pipelines)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>
<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../README.md)
- 📖 [Как верифицируются утверждения](../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../papers/README.md) · 📚 [Монографии](../../../docs/README.md) · 🧾 [LaTeX](../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

