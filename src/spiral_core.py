import torch
import torch.nn as nn
import numpy as np

phi = (1 + np.sqrt(5)) / 2  # Golden Ratio constant

class SymbolicGate(nn.Module):
    """Applies symbolic alignment gating over multi-modal concatenated features."""
    def __init__(self, input_dim):
        super().__init__()
        self.logic_rule = nn.Linear(input_dim, 1)

class NeuroMultiModalNet(nn.Module):
    """Recursive φ-aligned neural architecture with symbolic gate and fractal integration."""
    def __init__(self, num_modules=4, dim=128, num_agents=3, modalities=3):
        super().__init__()
        self.modules = nn.ModuleList([nn.Linear(dim, dim) for _ in range(num_modules)])
        self.gate = SymbolicGate(dim * num_modules * modalities)
        self.phi_split = np.floor(num_modules / phi).astype(int)
        self.agent_reflect = nn.Linear(dim, num_agents)
        self.fractal_map = nn.Linear(modalities, dim)  # Projects multi-modal inputs

    def forward(self, x_multi):
        """
        x_multi: tensor of shape [batch, modalities, dim]
        """
        # Combine modalities into φ-aligned latent vector
        x = self.fractal_map(x_multi.mean(dim=1))
        outputs = [mod(x) for mod in self.modules]
        concat = torch.cat(outputs, dim=1)

        gate_scores = self.gate(concat)
        reflections = torch.softmax(self.agent_reflect(concat.mean(dim=1)), dim=1)

        # φ-based split weighting
        left = gate_scores[:, :self.phi_split]
        right = gate_scores[:, self.phi_split:]

        return left.mean(dim=1) + (phi - 1) * right.mean(dim=1) * reflections.mean()
