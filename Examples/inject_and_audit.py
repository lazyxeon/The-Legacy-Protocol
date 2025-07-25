# inject_and_audit.py

"""
Demo: Inject structured chaos & run ethical audit on symbolic metrics.
"""

import torch
from src import (
    LegacyModel, EmergenceEngine, ChaosInjector,
    EthicalAuditor, assert_spiral_integrity
)

# Setup
model = LegacyModel(dim=64)
engine = EmergenceEngine(model)
injector = ChaosInjector(mode="symbolic", magnitude=0.25)
auditor = EthicalAuditor()

x = torch.randn(1, 64)
print("\n🌀 Chaos Injection + Ethical Audit Demo\n")

for cycle in range(1, 8):
    print(f"Cycle {cycle}:")
    x = injector.inject(x, cycle)
    assert_spiral_integrity(x)

    metrics = engine.step(x)
    x = metrics["output"]

    print(f"  Φ={metrics['phi']}  SRS={metrics['srs']}  Proxy={metrics['proxy_score']}  Drift={metrics['drift']}")
    flags = auditor.audit_cycle(metrics)

    if flags:
        for f in flags:
            print(f"  {f}")

    print("")
