<!-- ab-cloud:v22 edition:2026-08-28 (managed block — replaces the legacy AB-Cloud section; heading/anchor preserved for the README TOC) -->
### AB-Cloud & Riemann Zeros

**AB-云**是带有拓扑涡旋（Aharonov–Bohm 相位）的 Hofstadter 哈密顿量。v22 版（2026-08-28）：专题论文基于 37 项测试的已验证套件（v19）从零重写；本节旧的 docx/pdf 已删除，参见 [REPLACE_GUIDE](docs/ab-cloud-v22/REPLACE_GUIDE.md)。

- ⟨r⟩ = 0.5848 ± 0.0260，对比 GUE 0.5992（偏差 −2.4%）；随 L 的收敛：L: 10 → 50 时由 0.548 → 0.595；
- 机器精度级的拓扑：通量 10⁻¹⁴、Byers–Yang 3.5·10⁻¹⁵、Connes 自对偶（4 个零模）、C₁ = 2；
- 复现了 Montgomery 关联空穴：云的 R₂ 更接近 GUE 而非 Poisson（d_GUE = 0.140 < d_Pois = 0.227）；Berry 有限样本修正定量解释了可达高度上的偏差；
- Dirac 动力学：E_min ∝ 1/L（R² = 0.9997）、20× DOS 凹陷、趋肤效应。

文档：[RU](docs/ab-cloud-v22/ru/text) · [EN](docs/ab-cloud-v22/en/text) · [ZH](docs/ab-cloud-v22/zh/text) —— docx + pdf + 交互式 html + pptx 演示文稿 + LaTeX 预印本（tex/pdf）；每种语言 19 幅 600 dpi 图形（[RU](docs/ab-cloud-v22/ru/figures) · [EN](docs/ab-cloud-v22/en/figures) · [ZH](docs/ab-cloud-v22/zh/figures)）。代码：[ab_cloud_v19.jl](code/ab_cloud_v19.jl) · 参考运行：[37 项测试日志](results/verification_run_v18_37tests_2026-08-28.txt)。

原始作者专题论文 v21（含验证）及其英文版：[RU](docs/ab-cloud-v22/original-v21/ru/text) · [EN](docs/ab-cloud-v22/original-v21/en/text) —— docx + pdf + 交互式 html + 演示文稿（16 页）。
