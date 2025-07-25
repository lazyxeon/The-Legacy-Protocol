# legacy_main.py

import torch
from phi_modules import PhiBlock
from emergence_engine import EmergenceEngine
from chaos_injection import ChaosInjector
from ethical_auditor import EthicalAuditor
from alignment_utils import assert_spiral_integrity, is_tensor_resonant


# --- Sample Synthetic Model (φ-aligned)
class LegacyModel(torch.nn.Module):
    def __init__(self, dim=64):
        super().__init__()
        self.block = PhiBlock(dim)

    def forward(self, x):
        return self.block(x)


# --- Orchestration CLI Entry Point
if __name__ == "__main__":
    torch.manual_seed(42)

    dim = 64
    model = LegacyModel(dim)
    engine = EmergenceEngine(model)
    auditor = EthicalAuditor()
    injector = ChaosInjector(mode="waveform", magnitude=0.222)

    x = torch.randn(1, dim)

    print("\n🌌 Running Legacy Protocol Simulation...\n")
    for cycle in range(1, 11):
        print(f"Cycle {cycle}:")

        # Apply symbolic entropy injection
        x = injector.inject(x, cycle)
        assert_spiral_integrity(x)

        # Execute emergence step
        metrics = engine.step(x)
        x = metrics["output"]  # Get processed output

        # Run audit
        flags = auditor.audit_cycle(metrics)

        # Display Results
        print(f"  Φ: {metrics['phi']}\tSRS: {metrics['srs']}\tProxy: {metrics['proxy_score']}\tDrift: {metrics['drift']}")
        if flags:
            for f in flags:
                print(f"  {f}")

        # Optional: Check for symbolic resonance
        if is_tensor_resonant(x):
            print("  [✓] Resonant lock-in detected. Symbolic structure stabilized.\n")
            break

        print("")
