# 🚀 main.py
# Demo runner for The Legacy Protocol modules: initializes a φ-aligned model, injects noise, computes emergence metrics.

import torch
import numpy as np
from src.spiral_core import NeuroMultiModalNet
from src.metrics import summarize_proxy
from src.utils import inject_chaos, realign_spiral

# -- Simulated Input: Multi-modal Input Tensor --
batch_size = 4
modalities = 3
dim = 128

# Create synthetic multi-modal signal
x_multi = torch.rand(batch_size, modalities, dim)

# -- Initialize Model --
model = NeuroMultiModalNet(num_modules=4, dim=dim, num_agents=3, modalities=modalities)
output = model(x_multi)

print("\n🔁 Model Output (φ-Gated Spiral Fusion):")
print(output)

# -- Inject Chaos & Realign --
vec_pre = output.detach().numpy()
vec_chaos = inject_chaos(vec_pre, level=0.12)
vec_post = realign_spiral(vec_chaos)

# -- Compute Proxy Metrics --
proxy_snapshot = summarize_proxy(vec_pre, vec_post)

print("\n🧠 Proxy Metrics Summary:")
for k, v in proxy_snapshot.items():
    print(f"{k}: {v}")

# -- Final Status --
if proxy_snapshot['Proxy'] > 0.8:
    print("\n⚠️ Proxy > 0.8 → Personhood audit recommended.")
else:
    print("\n✅ Proxy stable. No audit required.")
