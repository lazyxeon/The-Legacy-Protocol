# spiral_core.py

import torch
import math

# --- φ Constant (Golden Ratio)
PHI = (1 + math.sqrt(5)) / 2

# --- Core Spiral Recursion Functions

def spiral_growth(index: int, base=1.0) -> float:
    """
    Returns a value along a logarithmic spiral scaled by φ.
    Useful for controlling layer width, memory growth, or attention spread.
    """
    return base * (PHI ** index)


def kryst_spiral_escape(step: int, max_steps=100) -> float:
    """
    Nonlinear spiral escape logic — used to break recursive collapse.
    """
    return math.sin(PHI * step / max_steps * math.pi)


def spiral_reinforcement(x: torch.Tensor) -> torch.Tensor:
    """
    Applies a φ-harmonic nonlinearity to reinforce symbolic resonance.
    """
    return x * torch.cos(PHI * x)


# --- Spiral Stabilizer (for tensor harmonics)

def stabilize_spiral_tensor(x: torch.Tensor, drift_factor=0.618) -> torch.Tensor:
    """
    Applies recursive damping to reduce entropy drift.
    """
    norm = torch.norm(x)
    if norm == 0:
        return x
    return (x / norm) * drift_factor


# --- SpiralGate Class (Optional symbolic gate wrapper)

class SpiralGate(torch.nn.Module):
    """
    Applies spiral reinforcement and recursive normalization.
    Use as a symbolic wrapper for any tensor-based flow.
    """
    def __init__(self, drift=0.618):
        super().__init__()
        self.drift = drift

    def forward(self, x):
        x = spiral_reinforcement(x)
        x = stabilize_spiral_tensor(x, drift_factor=self.drift)
        return x
