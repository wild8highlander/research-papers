# Contributing to Research Papers

First off, thank you for considering contributing to this project! Every contribution — whether it's a bug report, a new formal verification, a numerical result, or a documentation improvement — helps strengthen the mathematical foundations presented here.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Types of Contributions](#types-of-contributions)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Formal Verification Guidelines](#formal-verification-guidelines)
- [Numerical Verification Guidelines](#numerical-verification-guidelines)
- [Documentation Guidelines](#documentation-guidelines)

---

## Code of Conduct

This project adheres to the [Contributor Covenant v2.1](./CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. Please report unacceptable behavior to [aslan08_05@mail.ru](mailto:aslan08_05@mail.ru).

---

## Types of Contributions

| Type | Description | Example |
|------|-------------|---------|
| 🐛 **Bug fix** | Fix incorrect computation or proof error | Correct NSE boundary condition |
| ✅ **Formal verification** | Add proof in a new or existing proof assistant | Lean 4 proof of AB-Cloud property |
| 🔬 **Numerical verification** | Add or improve numerical computation | Higher-precision KS test |
| 📐 **Mathematical result** | New theorem, lemma, or conjecture | Extension of BKM criterion |
| 📖 **Documentation** | Improve docs, add examples, fix typos | Clarify polarization correction derivation |
| 🔧 **Infrastructure** | CI/CD, build system, tooling | Add new GitHub Actions workflow |
| 🔒 **Security** | Fix vulnerability or improve security posture | Update dependency with CVE |

---

## Getting Started

### Prerequisites

```bash
# Clone the repository
git clone https://github.com/wild8highlander/research-papers.git
cd research-papers

# Install Python environment
make install
# OR: pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
pre-commit install --hook-type commit-msg
```

### Verify Everything Works

```bash
# Run all Python verifications
make verify-all

# Run tests
pytest

# Check code quality
ruff check .
black --check .
```

---

## Development Workflow

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/my-new-verification
   ```

2. **Make your changes** following the guidelines below

3. **Run pre-commit** (runs automatically on commit, or manually):
   ```bash
   pre-commit run --all-files
   ```

4. **Push and create a PR**:
   ```bash
   git push origin feat/my-new-verification
   ```

5. **Wait for CI** — All workflows must pass before merge

---

## Commit Messages

This project follows [Conventional Commits](https://www.conventionalcommits.org) with custom types for mathematical research:

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature or research result |
| `fix` | Bug fix |
| `math` | Mathematical proof or derivation |
| `proof` | Formal proof in a proof assistant |
| `verify` | Numerical verification or benchmark |
| `docs` | Documentation change |
| `ci` | CI/CD change |
| `build` | Build system change |
| `refactor` | Code refactoring |
| `test` | Adding or updating tests |
| `perf` | Performance improvement |
| `style` | Code style (formatting, semicolons, etc.) |
| `revert` | Revert a previous commit |

### Scopes

| Scope | Description |
|-------|-------------|
| `nse` | Navier–Stokes equations |
| `ab-cloud` | AB-Cloud / Riemann zeros |
| `riemann` | Riemann hypothesis related |
| `kdv` | KdV equation |
| `klein` | Klein attractor |
| `lean4` | Lean 4 proofs |
| `coq` | Coq/Rocq proofs |
| `isabelle` | Isabelle-HOL proofs |
| `agda` | Agda proofs |
| `python` | Python verification |
| `julia` | Julia verification |
| `rust` | Rust verification |
| `cpp` | C++ verification |
| `haskell` | Haskell verification |

### Examples

```
proof(lean4): add NSE stability bound verification
math(nse): derive refined BKM criterion with correction b
verify(python): add high-precision KS test for AB-Cloud spectrum
fix(cpp): correct BLAS indexing in Hofstadter Hamiltonian
docs: update AB-Cloud documentation with permutation test results
ci: add CodeQL security analysis workflow
```

---

## Pull Request Process

1. **Fill in the PR template** completely — include motivation, approach, and verification
2. **Ensure all CI checks pass** — CodeQL, lint, test, cross-language verification
3. **Add tests** for any new functionality
4. **Update documentation** if you change public interfaces or add new features
5. **Update CHANGELOG.md** — Add entry under `[Unreleased]` section
6. **Keep PRs focused** — One logical change per PR
7. **Request review** — At least one approval required for merge

### PR Title Format

Follow the same convention as commit messages:
```
proof(lean4): add AB-Cloud spectral gap verification
```

---

## Formal Verification Guidelines

When adding formal proofs in a proof assistant:

1. **Use the project's build system** — Ensure your proof compiles with `make verify-extended`
2. **Document the theorem statement** — Include a comment with the informal statement
3. **Reference the paper** — Cite the specific paper/section/theorem being verified
4. **Keep proofs self-contained** — Minimize dependencies on external libraries not in the project
5. **Cross-verify** — If possible, provide the same verification in another proof assistant

### Lean 4

```lean
/-- Correction b ≈ 0.0785 stabilizes NSE.
    Reference: papers/nse_regularity.pdf, Theorem 3.2 -/
theorem nse_stability_with_correction :
    ∀ t > 0, ‖∇u(t)‖ ≤ C * exp(-b * θ_b * t) := by
  -- proof here
```

### Coq/Rocq

```coq
(** Correction b ≈ 0.0785 stabilizes NSE.
    Reference: papers/nse_regularity.pdf, Theorem 3.2 *)
Theorem nse_stability_with_correction :
  forall t, t > 0 -> norm (grad u t) <= C * exp (- b * theta_b * t).
Proof.
  (* proof here *)
Qed.
```

---

## Numerical Verification Guidelines

When adding numerical verifications:

1. **Use appropriate precision** — At minimum `float64`, prefer `mpmath` for high-precision results
2. **Report convergence** — Include convergence tables or error bounds
3. **Make it reproducible** — Set random seeds, specify library versions
4. **Add to CI** — Fast verifications should run in CI; expensive ones in scheduled workflows
5. **Document tolerances** — State expected precision and actual achieved precision

```python
# Example: KS test for AB-Cloud spectrum
import numpy as np
from scipy.stats import kstest

def verify_riemann_zeros_correspondence():
    """Verify AB-Cloud spectrum matches Riemann zeros.

    Reference: papers/ab_cloud.pdf, Section 5.3
    Tolerance: KS p-value > 0.05
    """
    ab_cloud_eigenvalues = compute_ab_cloud_spectrum(dim=36)
    riemann_zeros = compute_riemann_zeros(n=len(ab_cloud_eigenvalues))
    statistic, p_value = kstest(ab_cloud_eigenvalues, riemann_zeros)
    assert p_value > 0.05, f"KS test failed: p={p_value}"
    return statistic, p_value
```

---

## Documentation Guidelines

- **MkDocs Material** theme with MathJax for math rendering
- **Add pages** to `docs/` and update `mkdocs.yml` navigation
- **Use `$...$` for inline math** and `$$...$$` for display math
- **Cross-reference** papers, theorems, and verification results
- **Build locally** before pushing: `mkdocs serve`

---

Thank you for contributing to mathematical knowledge! 🎓
