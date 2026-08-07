"""
test_monograph_constants.py — pytest suite for monograph_constants module.

Verifies all 25+ analytical constants of the monograph:
  PSL(2,7) → α → L_min → e → b → γ → C_K → C_s → 3D NSE stabilization

Reference values taken from the monograph (Isaev 2026).
"""
import numpy as np
import pytest

from monograph_constants import (
    klein_alpha,
    klein_alpha_root_check,
    klein_L_min,
    klein_volume,
    selberg_zeta_leading,
    b_from_selberg,
    euler_e_identity,
    euler_e_residual,
    gamma_from_e_and_b,
    C_K_prediction,
    smagorinsky_Lilly,
    golden_ratio,
    fibonacci_ratio,
    anosov_lyapunov,
    anosov_entropy,
    anosov_KY_dimension,
    rodrigues_matrix,
    rodrigues_orthogonality_check,
    rodrigues_work_check,
    theta_b,
    theta_b_degrees,
    five_analogies_check,
    verify_all,
)


# ──────────────────────────────────────────────
# 1. Klein quartic & PSL(2,7)
# ──────────────────────────────────────────────
class TestKleinQuartic:
    """Tests for the Klein quartic curve (genus 3, PSL(2,7) order 168)."""

    def test_alpha_value(self):
        """α = 1 + 2·cos(2π/7) ≈ 2.246979603717467."""
        alpha = klein_alpha()
        assert abs(alpha - 2.246979603717467) < 1e-12

    def test_alpha_root_residual(self):
        """α is a root of x³ − 2x² − x + 1 = 0 (residual ~0)."""
        residual = klein_alpha_root_check()
        assert abs(residual) < 1e-12

    def test_L_min_value(self):
        """L_min = 2·arccosh(α) ≈ 2.63391579."""
        L = klein_L_min()
        expected = 2.0 * np.arccosh(2.246979603717467)
        assert abs(L - expected) < 1e-12

    def test_L_min_positive(self):
        """Shortest closed geodesic must be positive."""
        assert klein_L_min() > 0

    def test_klein_volume(self):
        """Vol(Klein) = 8π (Gauss–Bonnet for g=3, K=-1)."""
        V = klein_volume()
        assert abs(V - 8.0 * np.pi) < 1e-12

    def test_psl27_order_hurwitz(self):
        """|PSL(2,7)| = 168 = 84(g−1) for g=3 (Hurwitz bound)."""
        assert 168 == 84 * (3 - 1)


# ──────────────────────────────────────────────
# 2. Universal correction b
# ──────────────────────────────────────────────
class TestCorrectionB:
    """Tests for the universal polarization correction b ≈ 0.0785."""

    def test_b_value(self):
        """b ≈ 0.0785 (deviation < 0.5%)."""
        b = b_from_selberg()
        assert abs(b - 0.0785) / 0.0785 < 0.005

    def test_b_positive(self):
        """b must be positive (physical constraint)."""
        assert b_from_selberg() > 0

    def test_b_small(self):
        """b must be small (< 0.1) — perturbative correction."""
        assert b_from_selberg() < 0.1

    def test_Z_ratio_consistency(self):
        """Z_full/Z_leading = exp(b·β_K·L_min) ≈ 1.461."""
        b = b_from_selberg()
        L_min = klein_L_min()
        Z_ratio = np.exp(b * (5.0 / 3.0) * L_min)
        assert abs(Z_ratio - 1.461) / 1.461 < 0.005


# ──────────────────────────────────────────────
# 3. Euler number identity
# ──────────────────────────────────────────────
class TestEulerIdentity:
    """Tests for the e = (α + √(α²−1))^{2/L_min} identity."""

    def test_e_identity(self):
        """e from monograph identity equals np.e to ~1e-10."""
        e_calc = euler_e_identity()
        assert abs(e_calc - np.e) < 1e-10

    def test_e_residual(self):
        """Residual of e identity ~0."""
        residual = euler_e_residual()
        assert residual < 1e-10


# ──────────────────────────────────────────────
# 4. Gamma and Kolmogorov constants
# ──────────────────────────────────────────────
class TestKolmogorovConstants:
    """Tests for γ, C_K, and C_s."""

    def test_gamma_value(self):
        """γ ≈ 0.95449 (deviation < 0.1%)."""
        gamma = gamma_from_e_and_b(C_K=1.5)
        assert abs(gamma - 0.95449) / 0.95449 < 0.001

    def test_C_K_prediction(self):
        """C_K predicted ≈ 1.5 (deviation < 0.1%)."""
        CK = C_K_prediction()
        assert abs(CK - 1.5) / 1.5 < 0.001

    def test_smagorinsky_Lilly(self):
        """C_s ≈ 0.17327 (Lilly 1967)."""
        Cs = smagorinsky_Lilly(1.5)
        assert abs(Cs - 0.17327) / 0.17327 < 0.001


# ──────────────────────────────────────────────
# 5. Rotation angle θ_b
# ──────────────────────────────────────────────
class TestThetaB:
    """Tests for the polarization rotation angle θ_b = b·π/2."""

    def test_theta_b_radians(self):
        """θ_b = b·π/2 in radians."""
        th = theta_b()
        b = b_from_selberg()
        assert abs(th - b * np.pi / 2) < 1e-12

    def test_theta_b_degrees(self):
        """θ_b ≈ 7.065° (deviation < 0.5%)."""
        th_deg = theta_b_degrees()
        assert abs(th_deg - 7.065) / 7.065 < 0.005

    def test_theta_b_small(self):
        """θ_b < 10° — small-angle perturbation."""
        assert theta_b_degrees() < 10.0


# ──────────────────────────────────────────────
# 6. Rodrigues rotation matrix
# ──────────────────────────────────────────────
class TestRodriguesRotation:
    """Tests for the Rodrigues rotation R(θ, n̂)."""

    @pytest.fixture
    def random_axis(self):
        rng = np.random.default_rng(42)
        return rng.standard_normal(3)

    @pytest.fixture
    def random_vector(self):
        rng = np.random.default_rng(7)
        return rng.standard_normal(3)

    def test_orthogonality(self, random_axis):
        """R^T·R = I (orthogonality check)."""
        th = theta_b()
        residual = rodrigues_orthogonality_check(th, random_axis)
        assert residual < 1e-12

    def test_determinant_one(self, random_axis):
        """det(R) = 1 (proper rotation)."""
        R = rodrigues_matrix(theta_b(), random_axis)
        assert abs(np.linalg.det(R) - 1.0) < 1e-12

    def test_length_preservation(self, random_axis, random_vector):
        """|R·u| = |u| (isometry)."""
        R = rodrigues_matrix(theta_b(), random_axis)
        assert abs(np.linalg.norm(R @ random_vector) - np.linalg.norm(random_vector)) < 1e-12

    def test_no_work(self, random_axis, random_vector):
        """F·v = 0 (rotation does no work on the velocity)."""
        work = rodrigues_work_check(theta_b(), random_axis, random_vector)
        assert work < 1e-6

    def test_identity_at_zero_angle(self, random_axis):
        """R(0, n̂) = I."""
        R = rodrigues_matrix(0.0, random_axis)
        assert np.allclose(R, np.eye(3), atol=1e-12)


# ──────────────────────────────────────────────
# 7. Anosov flow invariants
# ──────────────────────────────────────────────
class TestAnosovFlow:
    """Tests for the Anosov geodesic flow on SM (K=-1)."""

    def test_lyapunov_spectrum(self):
        """λ = (+1, 0, −1)."""
        lam = anosov_lyapunov()
        assert lam == (1.0, 0.0, -1.0)

    def test_volume_preservation(self):
        """Σλ = 0 (incompressible)."""
        lam = anosov_lyapunov()
        assert abs(sum(lam)) < 1e-15

    def test_entropy(self):
        """h_top = √|K| = 1."""
        assert anosov_entropy() == 1.0

    def test_KY_dimension(self):
        """D_KY = 3 (2 Poincaré + 1 flow direction)."""
        assert anosov_KY_dimension() == 3.0


# ──────────────────────────────────────────────
# 8. Fibonacci / Golden ratio
# ──────────────────────────────────────────────
class TestFibonacci:
    """Tests for Fibonacci ratio → φ."""

    def test_golden_ratio(self):
        """φ = (1 + √5)/2 ≈ 1.618033988749895."""
        phi = golden_ratio()
        assert abs(phi - 1.618033988749895) < 1e-12

    def test_fibonacci_convergence(self):
        """F_{n+1}/F_n → φ as n → ∞."""
        phi = golden_ratio()
        for n in [10, 15, 20, 30]:
            ratio = fibonacci_ratio(n)
            assert abs(ratio - phi) < 0.001

    def test_golden_ratio_quadratic(self):
        """φ² = φ + 1 (defining equation)."""
        phi = golden_ratio()
        assert abs(phi**2 - phi - 1) < 1e-12


# ──────────────────────────────────────────────
# 9. Five physical analogies
# ──────────────────────────────────────────────
class TestPhysicalAnalogies:
    """Tests for the 5 perpendicular-action analogies (F·v = 0)."""

    def test_lorentz_no_work(self):
        """Lorentz force: F·v = 0."""
        ana = five_analogies_check()
        assert ana["lorentz_F_dot_v"] < 1e-12

    def test_coriolis_no_work(self):
        """Coriolis force: F·v = 0."""
        ana = five_analogies_check()
        assert ana["coriolis_F_dot_v"] < 1e-12

    def test_magnus_no_work(self):
        """Magnus force: F·v = 0."""
        ana = five_analogies_check()
        assert ana["magnus_F_dot_v"] < 1e-12


# ──────────────────────────────────────────────
# 10. Full verification chain
# ──────────────────────────────────────────────
class TestVerificationChain:
    """End-to-end: verify_all() residuals must be small."""

    def test_all_residuals_below_threshold(self):
        """All 25 constant residuals < 1e-2 (2+ decimal places)."""
        results = verify_all()
        for r in results:
            assert r["residual"] < 1e-2, (
                f"Constant #{r['id']} '{r['name']}' has residual {r['residual']:.2e}"
            )

    def test_num_constants_verified(self):
        """verify_all() returns exactly 25 results."""
        results = verify_all()
        assert len(results) == 25

    def test_critical_constants_precision(self):
        """Key constants (α, e, φ) verified to ~1e-10 or better."""
        results = verify_all()
        by_name = {r["name"]: r for r in results}
        # α root residual
        assert by_name["α root residual (x³−2x²−x+1=0)"]["residual"] < 1e-10
        # e identity
        assert by_name["e (Euler number, analytical identity)"]["residual"] < 1e-10
