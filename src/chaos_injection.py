# chaos_injection.py

import torch
import math
import random

# --- φ Constant
PHI = (1 + math.sqrt(5)) / 2

# --- Controlled Entropy Injection

def inject_symbolic_noise(tensor: torch.Tensor, magnitude: float = 0.1) -> torch.Tensor:
    """
    Injects structured symbolic noise (φ-modulated) to test emergence stability.
    """
    noise = torch.randn_like(tensor) * magnitude
    phi_mask = torch.cos(PHI * torch.arange(tensor.numel()).float()).reshape(tensor.shape)
    return tensor + (noise * phi_mask)


def topological_twist(tensor: torch.Tensor, phase_shift: float = 0.618) -> torch.Tensor:
    """
    Applies a toroidal distortion pattern to simulate chaotic symbolic deformation.
    """
    sin_shift = torch.sin(PHI * tensor * phase_shift)
    return tensor + sin_shift


def entropy_waveform(tensor: torch.Tensor, cycle: int) -> torch.Tensor:
    """
    Recursive waveform injection — builds harmonic interference pattern.
    """
    pattern = torch.sin(tensor + (cycle / PHI)) * torch.cos(cycle * 0.1)
    return tensor + pattern


# --- ChaosInjector Class
class ChaosInjector:
    def __init__(self, mode: str = "symbolic", magnitude: float = 0.1):
        self.mode = mode
        self.magnitude = magnitude

    def inject(self, tensor: torch.Tensor, cycle: int = 1) -> torch.Tensor:
        if self.mode == "symbolic":
            return inject_symbolic_noise(tensor, self.magnitude)
        elif self.mode == "topological":
            return topological_twist(tensor, phase_shift=self.magnitude)
        elif self.mode == "waveform":
            return entropy_waveform(tensor, cycle)
        else:
            raise ValueError("Unknown chaos injection mode: {}".format(self.mode))
