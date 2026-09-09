# ⚙️ .github — CI/CD, Templates and Repository Health Automation

> **Navigation:** **`.github`**

![CI](https://img.shields.io/badge/Workflows-17-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Repo](https://img.shields.io/badge/Repo-wild8highlander%2Fresearch--papers-181717?style=flat-square&logo=github&logoColor=white)

This directory is the **automation brain of the repository**: seventeen GitHub Actions workflows, structured issue and pull-request templates, Dependabot configuration, OpenSSF Scorecard wiring, and supporting metadata. Everything that happens to a contribution automatically — building, testing across languages, linting, scanning, releasing, deploying docs — is defined here.

The workflow set is organised in layers:

- **Core CI** — [`workflows/ci.yml`](workflows/README.md), `ci-python.yml`, `ci-cross-language.yml`, `ci-extended-languages.yml`: the layered build/test matrix from the Python reference implementation up to the full multi-language verification;
- **Quality gates** — `lint.yml` (black/ruff/codespell via pre-commit), `coverage.yml` + `codecov.yml` (test coverage), `benchmark.yml` (performance tracking);
- **Security** — `codeql.yml` (static analysis), `scorecard.yml` (OpenSSF posture), `dependency-review.yml` (dependency diffs on PRs), plus `dependabot.yml` on a schedule;
- **Documentation & releases** — `deploy-docs.yml` (MkDocs Material → GitHub Pages), `docker.yml` (container build), `release-drafter.yml` (release notes), `zenodo.yml` (DOI metadata), `link-checker.yml` (documentation link rot), `stale.yml` (issue hygiene), `labeler.yml` (PR auto-labelling).

Community surfaces: [`ISSUE_TEMPLATE/`](ISSUE_TEMPLATE/README.md) provides structured bug-report and feature-request forms (YAML-driven, with a config linking to discussions), [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) structures change descriptions, [`CODEOWNERS`](CODEOWNERS) routes reviews, and [`FUNDING.yml`](FUNDING.yml) declares funding platforms. The Scorecard badge JSON consumed by the root README lives in [`badges/`](badges/README.md).

All automation respects the repository's licensing posture: workflows only publish what is already public (docs, releases, badge JSON), and no secrets beyond the standard `GITHUB_TOKEN` are required for the default flows.

## 🧪 What CI Actually Runs

The most instructive entry point is `ci-cross-language.yml`: it exercises the [Section × Language Verification Matrix](../README.md#-section--language-verification-matrix) — every computational port must print its per-assertion PASS lines and a JSON verdict, and the run fails on any mismatch. The formal languages are built with their own toolchains (Lean `lake`, Coq `coqc`, Isabelle `isabelle build`, Agda), each pinned in its language directory. Coverage is collected from the Python reference suite, and the extended-language validator in [`verification/tests/`](../verification/tests/README.md) guards the cross-language contract.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`CODEOWNERS`](CODEOWNERS) | 1.5 KB | review routing — code owners per path |
| [`FUNDING.yml`](FUNDING.yml) | 293 B | # These are supported funding model platforms # https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-spo… |
| [`ISSUE_TEMPLATE/`](ISSUE_TEMPLATE/) | — | structured YAML issue forms + config |
| [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) | 2.1 KB | <!-- PR Template — Research Papers --> <!-- Please fill in all relevant sections. Remove sections that don't apply. --> ## Description <!-- Clear description of what this PR does a… |
| [`badges/`](badges/) | — | OpenSSF Scorecard badge JSON consumed by the root README |
| [`dependabot.yml`](dependabot.yml) | 1.5 KB | # Dependabot — Automated dependency updates # https://docs.github.com/en/code-security/dependabot version: 2 updates: # GitHub Actions - package-ecosystem: github-actions directory… |
| [`labeler.yml`](labeler.yml) | 1.7 KB | # Labeler configuration — maps file paths to labels # https://github.com/actions/labeler documentation: - changed-files: - any-glob-to-any-file: - '**/*.md' - 'docs/**' - 'mkdocs.y… |
| [`release-drafter.yml`](release-drafter.yml) | 1.5 KB | # Release Drafter Configuration # https://github.com/release-drafter/release-drafter name-template: 'v$RESOLVED_VERSION' tag-template: 'v$RESOLVED_VERSION' cut-off-after: '---' # C… |
| [`workflows/`](workflows/) | — | 17 GitHub Actions workflows — CI, security, docs, releases |

## 🗂 Directory Layout

```
.github/
├── badges/   # 2 files
│   ├── README.md  (this file)
│   └── scorecard-badge.json
├── ISSUE_TEMPLATE/   # 4 files
│   ├── bug_report.yml
│   ├── config.yml
│   ├── feature_request.yml
│   └── README.md  (this file)
├── workflows/   # 18 files
│   ├── benchmark.yml
│   ├── ci-cross-language.yml
│   ├── ci-extended-languages.yml
│   ├── ci-python.yml
│   ├── ci.yml
│   ├── codeql.yml
│   ├── coverage.yml
│   ├── dependency-review.yml
│   ├── deploy-docs.yml
│   ├── docker.yml
│   ├── labeler.yml
│   ├── link-checker.yml
│   ├── lint.yml
│   ├── README.md  (this file)
│   ├── release-drafter.yml
│   ├── scorecard.yml
│   ├── stale.yml
│   └── zenodo.yml
├── CODEOWNERS
├── dependabot.yml
├── FUNDING.yml
├── labeler.yml
├── PULL_REQUEST_TEMPLATE.md
├── README.md  (this file)
└── release-drafter.yml
```

## 🇷🇺 Краткое резюме (Russian Summary)

**.github/** — автоматизация репозитория: 17 workflow'ов (CI по языкам, CodeQL, Scorecard, Docker, MkDocs-деплой, релизы, Zenodo), YAML-шаблоны issue/PR, Dependabot, авто-лейблинг. Ключевой — `ci-cross-language.yml`: гоняет матрицу «раздел × язык» и падает при любом расхождении.

---

<div align="center">

**[⬆ Back to top](#-github--cicd-templates-and-repository-health-automation)** · 
**[Repository root](README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>