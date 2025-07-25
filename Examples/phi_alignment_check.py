# phi_alignment_check.py

"""
Demo: Check φ-alignment of tensor structures and test resonance.
"""

import torch
from src import is_phi_aligned, is_tensor_resonant, PHI

# Example tensor
x = torch.randn(89, 55)  # 89/55 ~ φ

print("\n🔍 φ Alignment + Resonance Check\n")
print(f"Tensor shape: {x.shape}")

if is_phi_aligned(x.shape):
    print(f"✓ Aligned to φ ({round(PHI, 4)})")
else:
    print("✗ Not φ-aligned")

if is_tensor_resonant(x):
    print("✓ Tensor shows harmonic resonance (lock-in possible)")
else:
    print("✗ No dominant symbolic resonance")
