# Verification Framework

Multi-language computational verification of six interconnected research papers.

## Languages

### Original (numerical + symbolic)
- Python (NumPy, SciPy, Matplotlib)
- Julia (LinearAlgebra, SpecialFunctions)
- Java (Apache Commons Math)
- Wolfram (Mathematica)
- TypeScript (Next.js dashboard)

### Extended — Formal proofs
- Lean 4 (Mathlib4 hybrid)
- Coq (Reals, Lra)
- Isabelle/HOL (Complex_Main)
- Agda (dependent types)

### Extended — Numerical
- Rust (ndarray)
- C++ (STL)
- Haskell (cabal)

## Build

```bash
make verify-all       # original languages
make verify-extended  # 7 new languages
```

## Docker

```bash
make docker-up
```
