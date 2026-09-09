# Verification Suite — the AB-Cloud Hypothesis on 10 Languages

This directory is the **independent cross-language verification package** of the
AB-Cloud hypothesis (Isaev I. Kh., ORCID [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701),
DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394)).
The same numerical program is implemented **ten times** — in C++, Fortran, Go,
Haskell, JavaScript, Julia, MATLAB, Python, R and Rust — so that any reviewer
can re-derive every headline number in the language they trust, on any OS,
with no hidden dependencies. All implementations read the same frozen
ζ-zero datasets from [`data/`](data) and must agree to numerical tolerance.

Besides the classic "three reviewer objections" checks, this directory also
hosts two newer blocks added in v1.1.0:

- [`spinor64/`](spinor64) — the reference verification of **all 64 spinor
  structures** of the Klein quartic (it corrects the v21 monograph claim that
  "only idx=38 gives GUE agreement"; the claim is withdrawn as a computational
  artifact);
- `<lang>/spinor38/` — **Test 38 ports in 10 languages** (exact isospectrality
  inside a PSL(2,7) orbit + ⟨r⟩ via a hand-written Jacobi eigensolver).

---

## 1. What is verified — the three reviewer objections

### Objection 1 — numerical stability / convergence of b(N)

**Claim:** the AB correction
`b(N) = (1/N) · Σₖ |γₖ − γ̃ₖ|`
(the mean distance between Gram-point approximations and true zeta zeros)
converges as N → ∞.

**Check:** compute b(N) for N = 100, 500, 1000, 5000, 10 000, 50 000 …
and print a convergence table with a log-log plot. The canonical Julia run
gives b(50000) = 1.2126 (HARDCORE pass 2) and an empirical law
b(N) ≈ 7.0312 · N^(−0.1685), R² = 0.9895 (an alternative 1/log N fit gives
R² = 0.9994). The exponent is **empirical**: the monograph's α = 1/2 refers to
the Hofstadter AB-flux per plaquette, *not* to this convergence rate.

### Objection 2 — statistical significance (GUE)

**Claim:** the normalised spacings of zeta zeros follow GUE (Wigner–Dyson).

**Check:** the unfolded spacings
`sₖ = (γₖ₊₁ − γₖ) · log(γₖ / 2π) / (2π)`
are tested against the Wigner surmise `p(s) = (πs/2)·exp(−πs²/4)` with a
Kolmogorov–Smirnov test and a Cramér–von Mises test. Criterion: p-value > 0.05
(H₀ "the zeros are GUE-spaced" is not rejected). The reference run reports
KS = 0.047 with p = 0.27 on 500 mpmath-certified zeros (Montgomery test), and
⟨r⟩ = 0.5848 ± 0.0260 against the GUE reference 0.5992.

### Objection 3 — decay rate at large T

**Claim:** b(N) = O(1/√N), i.e. the log-log slope ≈ −0.5.

**Check:** linear regression of log b(N) vs log N with a 95% CI. The measured
slope is **not** −0.5; the honest verdict of the suite is that the convergence
exponent is empirical (see Objection 1). This is documented rather than
hidden — every verdict in the suite is printed with its raw numbers so a
referee can disagree with the interpretation but not with the arithmetic.

---

## 2. Directory layout (what lives where)

```
verification/
├── data/          # frozen ζ-zero datasets (8 files, up to 2,000,000 zeros)
├── spinor64/      # reference Python verification of all 64 spin structures
├── sections/      # per-monograph-section micro-verifications (section 3, 6)
├── python/        # Python 3.10+   — reference implementation
├── cpp/           # C++17          — g++/clang++, no external libs
├── fortran/       # Fortran 2018   — gfortran
├── julia/         # Julia 1.9+     — stdlib only
├── rust/          # Rust 1.70+     — cargo, std only
├── r/             # R 4.3+         — base R
├── matlab/        # MATLAB R2021b+ — base MATLAB
├── javascript/    # Node.js 18+    — no npm deps
├── go/            # Go 1.21+       — stdlib only
├── haskell/       # GHC 9+         — base + containers
├── deploy.sh      # helper used to upload fresh reports to results/
└── README.md      # this file
```

Every language folder contains the **same four files** (plus, since v1.1.0,
a `spinor38/` subfolder — see §5):

| File | Role |
|---|---|
| `ab_cloud_verify.<ext>` | bilingual module (auto-selects RU/EN at runtime) |
| `ab_cloud_verify_en.<ext>` | English-only version |
| `ab_cloud_verify_ru.<ext>` | Russian-only version |
| `run_verify.<ext>` (or `run_verify.sh`) | standalone CLI runner — one command, no library knowledge needed |

All files embed the function `load_zeros(data_dir, count, source)` which reads
[`data/`](data) with automatic file selection (§4).

---

## 3. How to run (every language, copy-paste)

```bash
# Python 3.10+  (reference implementation)
cd verification/python && python3 run_verify.py --zeros 5000 --objection all --lang ru

# C++17
cd verification/cpp && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en

# Fortran 2018
cd verification/fortran && chmod +x run_verify.sh && ./run_verify.sh --zeros 10000 --source 50k --objection all

# Julia 1.9+
cd verification/julia && julia run_verify.jl --zeros 500000 --source 500k --objection all --lang en

# Rust 1.70+
cd verification/rust && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 500k --objection 1 --lang ru

# R 4.3+
cd verification/r && Rscript run_verify.R --zeros 50000 --source 50k --objection all --lang en

# MATLAB R2021b+
cd verification/matlab && run_verify('--zeros', 50000, '--source', '50k', '--objection', 'all')

# Node.js 18+
cd verification/javascript && node run_verify.js --zeros 50000 --source 50k --objection all --lang en

# Go 1.21+
cd verification/go && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 500k --objection all --lang ru

# Haskell (GHC 9+)
cd verification/haskell && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en
```

Each runner prints the three objection verdicts with raw statistics, writes a
timestamped report and saves plots next to the executable.

### CLI parameters (identical in all languages)

| Parameter | Default | Meaning |
|---|---|---|
| `--zeros N` | 5000 | how many ζ zeros to load |
| `--source NAME` | auto | `50k`, `500k`, `2M`, `highT`, `zeros6`, `csv`, `2M_gz`, `auto` |
| `--objection 1/2/3/all` | all | which objection to verify |
| `--lang en/ru` | auto | output language (auto = follow `LANG`) |
| `--data-dir PATH` | ../data | where the zero files live |

---

## 4. Frozen data — automatic file selection

| Requested zeros | File chosen |
|---|---|
| ≤ 13 661 | `data/zeta_zeros_50000.txt` |
| ≤ 500 000 | `data/zeta_zeros_500k_odlyzko.txt` |
| ≤ 2 000 000 | `data/zeta_zeros_2M_odlyzko.txt` |
| > 2 000 000 | `data/zeros6.txt` |

Full provenance, formats and column layout: [`data/README.md`](data/README.md).

---

## 5. spinor64 and the Test-38 ports (added in v1.1.0)

`spinor64/` is the **reference Python implementation** that settled the
"idx=38 uniqueness" question: **all 64 spinor structures of the Klein quartic
give GUE-consistent statistics**. PSL(2,7) splits them into orbits of sizes
**28 / 21 / 7 / 7 / 1**; operators inside an orbit are exactly isospectral
(max|Δλ| ≈ 8.9·10⁻¹⁵); in the AB-cloud Hofstadter model (L = 44, α = 1/2,
Nv = 54 vortices, `:monumental` gauge) all 64 structures pass the MC GUE
consistency test, ⟨r⟩ = 0.5984 ± 0.0035, min p = 0.36.
Details, data files and reproduction: [`spinor64/README.md`](spinor64/README.md).

`<lang>/spinor38/` ports **Test 38** of that experiment to each language: it
reads the frozen classes from `spinor64/data/`, rebuilds the odd-orbit spectra
with its **own hand-written Jacobi eigensolver** (no LAPACK/BLAS), and checks
exact isospectrality + ⟨r⟩. The C++ and JavaScript builds were compiled and
executed during v1.1.0 preparation: isospectrality 3.4·10⁻¹⁴,
⟨r⟩ = 0.4515710793 — **VERDICT PASS**. Each subfolder has its own README with
exact build/run commands.

---

## 6. Expected output and tolerances

A typical full run prints, per objection:

1. **Objection 1** — the b(N) table (N from 100 up to the dataset size) with
   the fitted power law, R², and the PASS/WARN/FAIL verdict against
   `bN_pass_threshold = 2.0`;
2. **Objection 2** — KS and CvM statistics with p-values, ⟨r⟩ with bootstrap
   error (n_bootstrap = 1000), the GUE ratio-law reference 0.5992(3);
3. **Objection 3** — log-log slope with 95% CI (tolerance band ±0.15 around
   the empirical exponent, `slope_ci_tolerance = 0.1` for CI width).

Numerical agreement between languages is expected at the level of
double-precision round-off: identical input zeros → identical b(N) tables to
~1e-12, identical KS statistics to ~1e-9. Any larger deviation means the
loader picked a different file — check `--source`.

---

## 7. Citing

Cite the monographs for the physics and this suite for the numbers:

```bibtex
@misc{isaev2026abcloud,
  title  = {AB-Cloud Research: a phase resonator for the zeros of the Riemann zeta function},
  author = {Iskhak Hamzatovich Isaev},
  year   = {2026},
  doi    = {10.5281/zenodo.21825394},
  url    = {https://github.com/wild8highlander/ab-cloud-research}
}
```

---

## Кратко (по-русски)

- Этот каталог — независимая кросс-языковая верификация AB-Cloud гипотезы:
  одна и та же программа на **10 языках** (C++, Fortran, Go, Haskell,
  JavaScript, Julia, MATLAB, Python, R, Rust), у всех одинаковый CLI и общие
  замороженные данные в `data/`.
- Проверяются три возражения рецензентов: сходимость b(N), GUE-статистика
  нулей (KS/CvM, p > 0.05), скорость убывания; вердикты печатаются с сырыми
  числами.
- Команды запуска для каждого языка — в §3; файл нулей выбирается
  автоматически по запросу `--zeros`.
- В v1.1.0 добавлены `spinor64/` (все 64 спинорные структуры GUE-согласованы,
  «уникальность idx=38» снята как артефакт) и порты Test 38
  `<язык>/spinor38/` (изоспектральность 3.4e-14, ⟨r⟩ = 0.4515710793 — PASS).
- Ожидаемое межъязыковое согласие — на уровне двойной точности; расхождения
  ~1e-12 для b(N) считаются нормой.

---
---

## 🧭 The Suite in Depth

### The Ten Folders, and What Each One Answers

Each language folder under this directory is a *complete* port of the three-objection suite — not a stub. A reviewer whose preferred ecosystem is, say, R, can answer all three objections without touching Python:

| Folder | Language | Runner | Notes |
|---|---|---|---|
| `python/` | Python 3.10+ | `ab_cloud_verify.py` (--interactive / --lang ru / --all) | the reference port |
| `cpp/` | C++17 | `run_verify.sh` | BLAS-backed eigensolver |
| `fortran/` | Fortran | `run_verify.sh` | legacy-scientific ecosystem |
| `julia/` | Julia 1.10+ | per-folder runner | closest to the historical v19 sources |
| `rust/` | Rust | `run_verify.sh` | std-only port |
| `r/` | R | `run_verify.sh` | stats-native ecosystem |
| `matlab/` | MATLAB | `run_verify.sh` | reference runs were MATLAB-made |
| `javascript/` | JS/Node | `run_verify.sh` | same numerics as the dashboard worker |
| `go/` | Go | `run_verify.sh` | the systems-language witness |
| `haskell/` | Haskell | `run_verify.sh` | the pure-functional witness |

Plus `spinor64/` (the 64-structure reference block) and per-language `spinor38/` ports (Test-38 re-verification with a hand-written Jacobi eigensolver — deliberately library-free).

### Reading an Archived Run Against a Fresh Run

The archived console outputs in [`results/`](results/README.md) are the fixed reference. A fresh run is compared test-by-test: same registry numbers, same PASS/WARN logic, same explanatory lines under WARNs. The suite's pedagogical style (each WARN carries its own explanation, e.g. why the full-range KS *must* reject at low T) means a diff between archived and fresh output reads like an audit checklist, not like a wall of noise.

### The spinor64 Block

The classification block for the 64 spinor structures of the Klein quartic: orbits 28/21/7/7/1 under PSL(2,7), exact isospectrality within orbits (max|Δλ| = 8.9·10⁻¹⁵), gauge invariance (7.1·10⁻¹⁵), zero-mode counts 2/3/3/3/7, and GUE-consistency for **all 64** (Monte-Carlo min p = 0.36). It is the block that produced the corrected statement — and the honest refutation — of the v21 "idx = 38 unique" claim.

### The Test-38 Ports

Each `<lang>/spinor38/` folder re-verifies the 64th structure (index 38) **independently**: a hand-written Jacobi eigensolver, no LAPACK, no libraries to trust. Ten languages, one conclusion. The point is redundancy with *different failure modes*: a numerical-library bug would have to replicate itself across ten ecosystems and a hand-written solver to hide.

### Convergence-Watch Tooling

The Python reference port exposes `--convergence-watch "1000,5000,20000,50000"` — it recomputes the statistics at each T_min cutoff so a reader can *watch* GUE compliance emerge with T, instead of being asked to believe a single p-value. This tooling exists precisely because Objection 2's answer is asymptotic in character.

---

## 🇷🇺 Краткое резюме (Russian Summary)

**ab-cloud/verification/** — десятиязычный набор верификации комплекса AB-Cloud: по полной реализации на каждый язык (Python, C++, Fortran, Julia, Rust, R, MATLAB, JavaScript, Go, Haskell), плюс блок spinor64 (все 64 спинорные структуры квартики Клейна: орбиты 28/21/7/7/1, изоспектральность 8.9·10⁻¹⁵, калибровочная инвариантность 7.1·10⁻¹⁵, 64/64 согласованы с GUE) и порты Test-38 — независимая перепроверка 64-й структуры в каждом языке рукописным якобиевским солвером. Набор отвечает на три возражения рецензентов: универсальность GUE (тесты 4–6, 11–14, 29, 33, 36), некруговость встраивания (контрольные ансамбли, прямой тест 35) и неселективность интерпретации (исчерпывающие скользящие окна, KS p = 0.27–0.88 как распределение). Архивные прогоны — в `../results/`; исторические версии кода — в `../code/julia/`.

---
## 🔬 Objection-by-Objection Test Map

The precise mapping from objections to registry tests (the archive in `../results/` is the reference execution of this map):

**Objection 1 — GUE universality (BGS).**
Tests 3 (b(N) convergence rate), 34 (L-scaling) establish the finite-size behaviour; Tests 4–6 (full-range KS, high-T KS, χ² histograms) confront the spacing statistics; Tests 11–14 add the advanced RMT battery (Anderson–Darling, two-sample KS, number variance, rigidity); Tests 29/33/36 add the figure of merit, the 200-realization bootstrap, and the form-factor diagnostic. Reading order for a sceptic: 4 → 5 (why the full-range rejection is *expected*) → 13/14 (long-range order) → 33 (error bars).

**Objection 2 — circularity of embedding.**
The controls: scrambled and surrogate embeddings against the real one, culminating in Test 35 — the *direct* AB-cloud-vs-ζ-5000 comparison. The permutation test (Z = 14.10σ across the suite) is the formal separator: if the embedding forced the statistics, surrogates with the same embedding would reproduce them; they do not.

**Objection 3 — selective interpretation.**
Tests 7–9 (decay slope, residuals, bootstrap CI) and the suite's sliding-window policy: KS p-values are reported as a distribution across windows (p = 0.27–0.88), never as a single favourable pick. The `--convergence-watch` tooling makes the asymptotic argument reproducible interactively.

## 🧾 The Registry Discipline

Tests are numbered, and the numbering is stable across languages — test 13 in Python is test 13 in R is test 13 in MATLAB. This is what makes the per-language folders *comparable* rather than merely similar: a reviewer can diff test-by-test across ten ecosystems. New tests append to the registry with new numbers; renumbering is forbidden.

## 🇷🇺 Резюме (Russian Summary)

Соответствие «возражение → тесты» фиксировано: универсальность GUE — тесты 3–6, 11–14, 29, 33, 34, 36; круговость встраивания — контрольные ансамбли, суррогаты и прямой тест 35 (перестановочный тест Z = 14.10σ); селективность — тесты 7–9 и скользящие окна (p = 0.27–0.88 как распределение). Нумерация тестов едина во всех десяти языках и только растёт.

---
## 🎛 The Python Port's Flags, Documented

The reference port doubles as the suite's teaching interface; its flags are worth knowing in full:

| Flag | Effect |
|---|---|
| `--interactive` | step through the objections with prompts |
| `--all` | run the full registry |
| `--lang ru` / `--lang en` | output language |
| `--convergence-watch "1000,5000,20000,50000"` | recompute at each T_min cutoff — watch GUE compliance emerge |
| (per-test selectors) | run a registry subset — useful when diffing against the archive |

The other nine languages expose the same registry through their native runners (`run_verify.sh` / `run_verify.py` per folder) — flags vary, numbering does not.

## 🔁 Diffing a Fresh Run Against the Archive

The archive-diff workflow, step by step:

1. run the same registry (same test selection) that the archived run executed;
2. normalise the outputs (timestamps, paths) — the suite prints stable test-numbered lines for exactly this purpose;
3. diff test-by-test: PASS/WARN states first, then the numeric values within tolerance;
4. investigate any state change (PASS→WARN or WARN→PASS is a finding either way);
5. record your fresh run next to your notes with the repository commit hash — the archive is append-only, and your run's console output is a candidate for it.

---
## 📊 The Statistics' Minimal Definitions (suite-level)

For readers who want the exact quantities without the monograph chapter:

- **⟨r⟩** — mean of min(sₙ, sₙ₊₁)/max(sₙ, sₙ₊₁) over the spectrum; scale-free; GUE ≈ 0.5996;
- **KS p** — Kolmogorov–Smirnov p-value of the spacing distribution against the GUE Wigner surmise; reported per window;
- **Σ²(L)** — number variance over windows of length L; **Δ₃(L)** — least-squares staircase rigidity;
- **K(τ)** — Fourier image of the two-point cluster function; the ramp-plateau form is the GUE fingerprint (Test 36);
- **permutation Z** — (observed − null mean)/null SD of the AB↔ζ agreement statistic under label permutation; Z = 14.10σ.

Each has a per-language implementation in the ten folders; the definitions above are the shared specification the implementations must meet, and the validator-style test numbering keeps them comparable.

<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../README.md)
- 📖 [Как верифицируются утверждения](../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../papers/README.md) · 📚 [Монографии](../../../docs/README.md) · 🧾 [LaTeX](../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

