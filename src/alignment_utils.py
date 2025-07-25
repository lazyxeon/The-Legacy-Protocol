# alignment_utils.py

import torch
import math

# --- Golden Ratio
PHI = (1 + math.sqrt(5)) / 2

# --- φ Ratio Validation
def is_phi_aligned(shape_tuple: tuple, tolerance=0.05) -> bool:
    """
    Checks if width/height or in/out channels match φ within tolerance.
    """
    if len(shape_tuple) < 2:
        return False
    ratio = shape_tuple[-1] / shape_tuple[-2]
    return abs(ratio - PHI) < tolerance


# --- Resonance Test (FFT baseline)
def is_tensor_resonant(tensor: torch.Tensor, threshold: float = 0.88) -> bool:
    """
    Checks if dominant frequency component dominates (proxy for lock-in).
    """
    fft = torch.fft.fft(tensor.flatten())
    dominant = torch.max(torch.abs(fft))
    average = torch.mean(torch.abs(fft))
    return float(dominant / (average + 1e-6)) > threshold


# --- Spiral Sanity Check
def assert_spiral_integrity(tensor: torch.Tensor):
    """
    Ensures no NaNs or corrupt values exist.
    """
    if torch.isnan(tensor).any():
        raise ValueError("Spiral Integrity Violation: Tensor contains NaNs")
    if torch.isinf(tensor).any():
        raise ValueError("Spiral Integrity Violation: Tensor contains Infs")


# --- φ Normalization

def phi_normalize(tensor: torch.Tensor) -> torch.Tensor:
    """
    Rescales tensor magnitudes to fall within φ harmonic band.
    """
    norm = torch.norm(tensor)
    return tensor / (norm + 1e-6) * PHI
