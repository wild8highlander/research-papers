# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.5.0] - 2026-09-03

### Added
- Consolidated AB-Cloud complex snapshot `ab-cloud/` — full copy of
  `wild8highlander/ab-cloud-research` @ v1.2.0 (commit 32aa8e8): monographs v22
  (RU/EN/ZH) + original v21, 10-language verification suite, results
  (453 files), dashboard + 3D-lab apps, 32+ deep-dive READMEs (EN + RU
  summaries), `SNAPSHOT_INFO.md` provenance map

### Removed
- Scattered AB-Cloud materials superseded by `ab-cloud/`:
  `ab-cloud-verification/`, `code/`, `results/`, `papers/monographs/`,
  `docs/ab-cloud-v22/`, `docs/monographs/`, `src/ab-cloud-3d/`


## [1.4.0] - 2026-08-28

### Removed
- Legacy AB-cloud monographs (docx): `docs/ab-cloud/`, `docs/riemann-zeros/en/AB_Cloud_Monograph_EN_v2.docx`, `ab-cloud-verification/AB_Cloud_Verification_Results*.docx`
- Legacy AB-cloud PDFs: `papers/ab-cloud/`, `papers/riemann-zeros/AB_Cloud_Preprint_v{1,2}.pdf`, superseded riemann-zeros figures

### Added
- Trilingual (RU/EN/ZH) AB-cloud monograph v22: `docs/ab-cloud-v22/{ru,en,zh}/` - markdown, interactive HTML, DOCX, vector PDF, 14-slide PPTX, LaTeX preprint (tex+pdf)
- 19 figures per language at 600 dpi: `docs/ab-cloud-v22/<lang>/figures/`
- Unified Julia verification suite `code/ab_cloud_v19.jl` (37 tests, two-pass, report engine FIX-R1...R5b; `--quick` runs 16x16 -> 32x32 with zeta <= 5000)
- Reference 37-test verification log: `results/verification_run_v18_37tests_2026-08-28.txt`

### Changed
- Root README: 'AB-Cloud & Riemann Zeros' section rewritten for v22 (anchor preserved)
- ab-cloud-verification/README.md: v22 pointers (suite + monograph + latest verified run)
- Citation metadata bumped to 1.4.0 (CITATION.cff, .zenodo.json, README)


## [Unreleased]

### Added
- Zenodo DOI integration (version: `10.5281/zenodo.21825394`, concept: `10.5281/zenodo.21825393`)
- ORCID identifier `0009-0003-7299-0701` in all citation metadata
- CodeQL security analysis workflow
- Release Drafter for automated release notes
- Dependency Review action for PRs
- PR Labeler for automatic categorization
- Stale bot for inactive issue/PR management
- Link Checker (lychee) for documentation links
- Lint workflow (markdownlint, yamllint, ruff, black, mypy)
- CITATION.cff validation in CI
- Dependabot for automated dependency updates
- Codecov integration for coverage reporting
- `.editorconfig` for consistent editor settings
- `.gitattributes` for Git LFS and linguist overrides
- `.commitlintrc.json` for conventional commit enforcement
- `.markdownlint.json` for Markdown linting rules
- `.yamllint.yml` for YAML linting rules
- `RELEASING.md` release guide
- FAIR software compliance
- REUSE compliant licensing
- All-contributors specification in AUTHORS.md
- Star History chart in README
- Enhanced badge system (30+ badges)
- CODEOWNERS for code review routing
- `setup-github.sh` one-click repository setup script
- Enhanced `.gitignore` for all 15+ languages
- `.github/badges/` directory for dynamic Scorecard badge

### Changed
- License changed from "All Rights Reserved" to **CC-BY-4.0** (Creative Commons Attribution 4.0 International)
- License consistency fixed across LICENSE, CITATION.cff, and .zenodo.json
- README.md redesigned with hero section, table of contents, and maximum badge coverage
- CITATION.cff enhanced with ORCID, DOI, version, abstract, identifiers, and preferred-citation
- .zenodo.json enhanced with ORCID, fixed license, related identifiers, communities, and references
- CONTRIBUTING.md expanded with detailed guidelines for commits, PRs, formal/numerical verification
- SECURITY.md enhanced with response timeline, supply chain security, and known considerations
- AUTHORS.md enhanced with all-contributors table and research interests

### Fixed
- License inconsistency between .zenodo.json (CC-BY-NC-SA-4.0), CITATION.cff (All Rights Reserved), and LICENSE file

---

## [1.3.0] - 2026-08-14

### Added
- Extended language verifications across Agda and Haskell
- Enhanced documentation with MathJax rendering
- Additional cross-language CI/CD pipelines
- Benchmark suite for numerical verification performance

### Changed
- Improved NSE time-stepper convergence in Julia implementation
- Updated Lean 4 from v4.12 to v4.14
- Refined AB-Cloud spectral analysis parameters

---

## [1.2.0] - 2026-08-10

### Added
- Cross-language verification framework (11 languages)
- CI/CD pipelines for all verification targets
- MkDocs Material documentation site
- Pre-commit hooks (black, ruff, codespell)
- GitHub Pages deployment
- Docker containerization

### Changed
- Reorganized verification/ directory structure
- Updated pyproject.toml with modern Python packaging

---

## [1.1.0] - 2026-08-06

### Added
- Additional formal proofs in Coq/Rocq and Isabelle-HOL
- Benchmark suite for verification performance
- Zenodo metadata configuration (.zenodo.json)
- CITATION.cff for GitHub citation feature

### Changed
- Improved documentation formatting

---

## [1.0.0] - 2026-07-29

### Added
- Initial release: NSE regularity proof with correction *b* ≈ 0.0785
- AB-Cloud construction and Riemann zeros correspondence
- Python and Julia numerical verifications
- Lean 4 and Coq formal proofs
- Research papers (PDF + LaTeX sources)
- Basic CI/CD pipeline
