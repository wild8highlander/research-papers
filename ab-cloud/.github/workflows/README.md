# 🔁 ab-cloud · .github · workflows — the Snapshot's CI Catalogue

> **Navigation:** [`ab-cloud`](../../README.md) › [`.github`](../README.md) › **`workflows`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **GitHub Actions workflows of the standalone AB-Cloud repository**, preserved inside the snapshot (8 YAML files). They document how the standalone project ran its own CI before consolidation. Inside this consolidated repository they are inert (GitHub only executes root-level workflows), but they remain for provenance — and as reference material for anyone extracting the AB-Cloud suite back into a standalone setup.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`ci.yml`](ci.yml) | 1.6 KB | name: CI on: push: branches: [main] pull_request: branches: [main] workflow_dispatch: permissions: contents: read jobs: structure: name: Repository structure & metadata runs-on: ub… |
| [`codeql.yml`](codeql.yml) | 472 B | name: CodeQL on: push: branches: [main] pull_request: branches: [main] schedule: - cron: "0 5 * * 3" permissions: contents: read security-events: write jobs: analyze: name: Analyze… |
| [`dependency-review.yml`](dependency-review.yml) | 226 B | name: Dependency review on: pull_request: permissions: contents: read jobs: dependency-review: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - uses: actions/dependency-… |
| [`deploy-docs.yml`](deploy-docs.yml) | 774 B | name: Deploy documentation on: push: branches: [main] workflow_dispatch: permissions: contents: read pages: write id-token: write concurrency: group: pages cancel-in-progress: true… |
| [`julia.yml`](julia.yml) | 1.0 KB | name: Julia quick-test on: push: branches: [main] pull_request: branches: [main] schedule: - cron: "0 3 * * 1" # weekly Monday 03:00 UTC workflow_dispatch: permissions: contents: r… |
| [`link-checker.yml`](link-checker.yml) | 506 B | name: Link checker on: push: branches: [main] schedule: - cron: "0 4 * * 5" workflow_dispatch: permissions: contents: read jobs: lychee: runs-on: ubuntu-latest steps: - uses: actio… |
| [`release-drafter.yml`](release-drafter.yml) | 659 B | name: Release drafter on: push: branches: [main] pull_request: types: [opened, reopened, synchronize] permissions: contents: read pull-requests: write jobs: update-release-draft: r… |
| [`stale.yml`](stale.yml) | 566 B | name: Stale on: schedule: - cron: "0 6 * * 1" permissions: issues: write pull-requests: write jobs: stale: runs-on: ubuntu-latest steps: - uses: actions/stale@v9 with: days-before-… |

## 🔗 Cross-References

- [Snapshot provenance — SNAPSHOT_INFO.md](../../SNAPSHOT_INFO.md)
- [Parent snapshot README](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

8 workflow'ов из standalone-репозитория ab-cloud-research, сохранены для провенанса; в консолидированном репозитории не исполняются (GitHub запускает только root-workflow'ы).

---

<div align="center">

**[⬆ Back to top](#-ab-cloud--github--workflows--the-snapshots-ci-catalogue)** · 
**[Repository root](../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>
<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../../README.md)
- 📖 [Как верифицируются утверждения](../../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../../papers/README.md) · 📚 [Монографии](../../../../docs/README.md) · 🧾 [LaTeX](../../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

