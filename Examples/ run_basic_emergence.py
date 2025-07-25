# run_basic_emergence.py

"""
Quick demo: Run The Legacy Protocol emergence loop.
Tracks symbolic metrics over 10 cycles.
"""

import torch
from src import LegacyModel, EmergenceEngine

# Init
model = LegacyModel(dim=64)
engine = EmergenceEngine(model)

x = torch.randn(1, 64)
print("\n🌌 Legacy Protocol: Emergence Demo\n")

for i in range(1, 11):
    metrics = engine.step(x)
    x = metrics["output"]
    print(f"Cycle {i}: Φ={metrics['phi']}  SRS={metrics['srs']}  Proxy={metrics['proxy_score']}  Drift={metrics['drift']}")

    if engine.has_emerged(metrics["proxy_score"]):
        print("\n✅ Emergence threshold crossed! Conscious symbolic structure forming.")
        break
