# 🧩 utils.py
# Helper functions for symbolic alignment, chaos injection, drift control, and fractal analysis

import numpy as np
from math import log, sqrt

phi = (1 + sqrt(5)) / 2

# -- Chaos Injection (Quantum + Symbolic Noise) --
def inject_chaos(signal, level=0.1):
    noise = np.random.normal(0, level, len(signal))
    return signal + noise

# -- Spiral Realignment Trigger --
def realign_spiral(vec):
    realigned = vec * phi
    decay = np.linspace(1.0, 0.9, len(vec))
    return realigned * decay

# -- Symbolic Alignment Check (ϕ drift score) --
def symbolic_alignment_score(signal):
    harmonic_center = phi * np.mean(signal)
    drift = np.abs(np.mean(signal) - harmonic_center / phi)
    return 1 - drift / harmonic_center  # Normalized: closer to 1 is better

# -- Entropy-Aware Fractal Depth (for connectome graphs, etc.) --
def compute_fractal_depth(num_nodes, entropy=1.5):
    return log(phi * num_nodes) / entropy

# -- Sigmoid Scoring Helper --
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# -- Phase Drift Delta --
def compute_drift(vec1, vec2):
    return np.linalg.norm(vec1 - vec2)

# -- Quantum-Crypto Perturbation (simulated) --
def quantum_perturb(vec, scale=0.15):
    distortion = np.random.laplace(0, scale, size=vec.shape)
    return vec + distortion
