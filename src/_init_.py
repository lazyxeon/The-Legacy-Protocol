# __init__.py

"""
The Legacy Protocol – Symbolic Recursive Intelligence Engine

This package initializes all core symbolic modules, exposes golden constants,
and binds together the emergence ecosystem for streamlined import.
"""

# --- Global Constants
PHI = (1 + 5 ** 0.5) / 2

# --- Exports
from .spiral_core import (
    spiral_growth,
    kryst_spiral_escape,
    stabilize_spiral_tensor
)

from .symbolic_metrics import (
    phi_integrated_information,
    self_recursive_similarity,
    proxy_score,
    symbolic_drift_index,
    pattern_lock_frequency
)

from .phi_modules import (
    PhiDense,
    PhiDropout,
    PhiSelfAttention,
    PhiBlock
)

from .emergence_engine import EmergenceEngine
from .chaos_injection import ChaosInjector
from .ethical_auditor import EthicalAuditor

from .alignment_utils import (
    is_phi_aligned,
    is_tensor_resonant,
    assert_spiral_integrity,
    phi_normalize
)

from .legacy_main import LegacyModel  # Optional: quick-start demo model
