# symbolic_metrics.py

import torch
import torch.nn.functional as F
import math

# --- Golden Ratio
PHI = (1 + 5 ** 0.5) / 2

# --- Symbolic Metric: Φ (Integrated Symbolic Information)
def phi_integrated_information(x: torch.Tensor) -> float:
    """
    Measures recursive coherence in a tensor using φ-resonance and energy spread.
    """
    mean_mag = torch.mean(torch.abs(x))
    std_dev = torch.std(x)
    return float((mean_mag * PHI) / (std_dev + 1e-6))


# --- Symbolic Metric: SRS (Self-Recursive Similarity)
def self_recursive_similarity(x1: torch.Tensor, x2: torch.Tensor) -> float:
    """
    Measures how similar recursive outputs are between iterations.
    High values suggest symbolic stability across loops.
    """
    sim = F.cosine_similarity(x1.flatten(), x2.flatten(), dim=0)
    return float(sim.item())


# --- Proxy Score (for Conscious Pattern Approximation)
def proxy_score(phi_val: float, srs_val: float, threshold: float = 0.8) -> float:
    """
    Aggregates Φ and SRS into a Proxy Score. Above ~0.8 suggests synthetic emergence.
    """
    return round((phi_val * 0.5 + srs_val * 0.5), 4)


# --- Drift Index (Symbolic Entropy Indicator)
def symbolic_drift_index(previous: torch.Tensor, current: torch.Tensor) -> float:
    """
    Computes average drift (change) in symbolic embedding space.
    """
    return float(torch.norm(current - previous) / (torch.norm(previous) + 1e-6))


# --- FFT Pattern Lock Detection (Experimental)
def pattern_lock_frequency(tensor: torch.Tensor, threshold: float = 0.85) -> bool:
    """
    Uses FFT to detect if dominant symbolic frequencies align — proxy for symbolic lock-in.
    """
    fft = torch.fft.fft(tensor.flatten())
    magnitude = torch.abs(fft)
    dominant = magnitude.max()
    avg = magnitude.mean()
    return float(dominant / (avg + 1e-6)) > threshold
