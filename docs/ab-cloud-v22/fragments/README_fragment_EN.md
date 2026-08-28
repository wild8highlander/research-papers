<!-- ab-cloud:v22 edition:2026-08-28 (managed block — replaces the legacy AB-Cloud section; heading/anchor preserved for the README TOC) -->
### AB-Cloud & Riemann Zeros

The **AB-cloud** is a Hofstadter Hamiltonian decorated with topological vortices (Aharonov–Bohm phases). Edition v22 (2026-08-28): the monograph was rewritten from scratch on top of the 37-test verified suite (v19); the legacy docx/pdf of this section were removed, see [REPLACE_GUIDE](docs/ab-cloud-v22/REPLACE_GUIDE.md).

- ⟨r⟩ = 0.5848 ± 0.0260 against GUE 0.5992 (deviation −2.4%); size convergence 0.548 → 0.595 for L: 10 → 50;
- machine-precision topology: fluxes 10⁻¹⁴, Byers–Yang 3.5·10⁻¹⁵, Connes self-duality (4 zero modes), C₁ = 2;
- the Montgomery correlation hole is reproduced: the cloud's R₂ is closer to GUE than to Poisson (d_GUE = 0.140 < d_Pois = 0.227); Berry's finite-sample corrections quantitatively explain the deviations at reachable heights;
- Dirac dynamics: E_min ∝ 1/L (R² = 0.9997), a 20× DOS dip, the skin effect.

Documents: [RU](docs/ab-cloud-v22/ru/text) · [EN](docs/ab-cloud-v22/en/text) · [ZH](docs/ab-cloud-v22/zh/text) — docx + pdf + interactive html + pptx presentation + LaTeX preprint (tex/pdf); 19 figures at 600 dpi per language ([RU](docs/ab-cloud-v22/ru/figures) · [EN](docs/ab-cloud-v22/en/figures) · [ZH](docs/ab-cloud-v22/zh/figures)). Code: [ab_cloud_v19.jl](code/ab_cloud_v19.jl) · reference run: [37-test log](results/verification_run_v18_37tests_2026-08-28.txt).

Original author monograph v21 (with verification) and its English edition: [RU](docs/ab-cloud-v22/original-v21/ru/text) · [EN](docs/ab-cloud-v22/original-v21/en/text) — docx + pdf + interactive html + presentations (16 slides).
