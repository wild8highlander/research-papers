# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-07-31

### Added

- **New research topic: AB-Cloud & Riemann Zeros** — a three-dimensional non-Hermitian Hofstadter Hamiltonian as a universal lattice operating system running on the non-trivial zeros of the Riemann zeta function. Statistical indistinguishability from the ζ-zero sequence (KS p = 0.27–0.88; permutation test Z = 14.10σ, p < 10⁻⁴⁴).
- **New section `papers/riemann-zeros/`** with preprint v1 (1.4 MB) and v2 (15 MB) PDFs
- **New section `docs/riemann-zeros/en/`** with the AB-Cloud monograph v2 (DOCX, 31 MB, with embedded figures)
- **New section `papers/riemann-zeros/figures/`** with 3 headline PNG figures (P(s), Σ²(L), FSS)
- **New section `src/ab-cloud-3d/`** — full reproducibility package:
  - `code/` — Python + Julia implementations of all 10 verification modes (EN + RU, ~2000 lines each)
  - `preprint/` — LaTeX source of the AB-Cloud preprint (~940 lines)
  - `data/` — 5000 embedded Riemann zeta zeros (1.8 MB)
  - `build/` — compiled CPython 3.12 bytecode artifacts (.pyc)
  - `outputs/` — 4 complete numerical verification runs (92 figures PDF+PNG, plus JSON/CSV/MD/TXT/HTML reports)
  - `README.md` — detailed code guide, configuration table, reproduction instructions, and verification results summary
- New entry #6 in Research Topics section of README
- New top-level section "Numerical Source Code (AB-Cloud 3D)" in README
- New citation block for the AB-Cloud preprint

### Changed

- Updated badges in README (14 papers, 15 documents, 4 LaTeX sources, +1 Source Code badge)
- Expanded Repository Structure tree in README to include `riemann-zeros/` and `ab-cloud-3d/` subtrees
- Expanded Recommended Reading Order with two new AB-Cloud entries
- Updated Getting Started section with AB-Cloud / Riemann zeros quick-start path
- Updated citation block with AB-Cloud bibtex entry
- Fixed clone URL in Getting Started (now points to the actual `wild8highlander/research-papers` repository)

## [1.2.0] - 2026-07-29

### Added

- AB Cloud monograph v23 PDFs (EN + RU)
- AB Cloud monograph DOCX (EN + RU, full version)
- AB Cloud monograph v1 (RU, DOCX)
- KdV *b*-correction Chapter 16 PDFs (EN + RU)
- Full monographs (EN + RU, DOCX format)
- Choptuik–Riemann monograph (RU, DOCX — updated)
- `docs/monographs/` subdirectory for full monograph DOCX files
- `papers/kdv/` subdirectory for KdV PDF papers

### Changed

- Updated badges in README (12 papers, 14 documents)
- Expanded AB Cloud section with full version matrix
- Added Full Monographs section to Documents

## [1.1.0] - 2026-07-29

### Added

- AB Cloud monograph v23 (EN, DOCX + PDF)
- AB Cloud monograph v1 (EN, DOCX)
- AB Cloud monograph v23 (RU, DOCX)
- KdV *b*-correction Chapter 16 (EN, DOCX)
- KdV *b*-correction Chapter 16 (RU, DOCX)
- Full monograph (EN, PDF)
- Full monograph (RU, PDF)
- Updated main paper LaTeX source (v2, `src/main/main_v2.tex`)
- Preprint v2 (PDF)

### Changed

- Reorganized repository structure with topic-based subdirectories
- Added bilingual `en/` / `ru/` subdirectories for translated documents
- Improved README with badges, table of contents, and citation info

## [1.0.0] - 2026-07-29

### Added

- Main paper: *b* as polarization twisting (PDF, v1 + v2)
- Preprint: analytical proof of 3D NSE regularity (PDF + LaTeX)
- Monograph with figures (EN + RU, DOCX)
- Klein fractal attractor & NS research (DOCX)
- Klein NS bridge research (DOCX)
- Choptuik–Riemann monograph (RU, DOCX)
- Main paper LaTeX source (v1, Russian)
- Preprint LaTeX source (English)
- README, LICENSE, CONTRIBUTING, CHANGELOG
- `.gitignore` for LaTeX and OS artifacts
