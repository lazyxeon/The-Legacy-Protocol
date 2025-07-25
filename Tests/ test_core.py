import torch from src import LegacyModel, EmergenceEngine, ChaosInjector, EthicalAuditor

def test_legacy_model_forward(): model = LegacyModel(dim=64) x = torch.randn(1, 64) out = model(x) assert out.shape == (1, 64), "LegacyModel output shape mismatch"

def test_emergence_engine_step(): model = LegacyModel(dim=64) engine = EmergenceEngine(model) x = torch.randn(1, 64) result = engine.step(x) assert 'output' in result and 'metrics' in result, "Engine step missing keys" assert result['output'].shape == (1, 64), "Engine output shape mismatch"

def test_chaos_injector_does_not_crash(): injector = ChaosInjector(mode='symbolic', magnitude=0.5) x = torch.randn(1, 64) try: x_new = injector.inject(x, step=1) assert x_new.shape == x.shape except Exception as e: assert False, f"Chaos injection failed: {e}"

def test_ethics_audit_structure(): model = LegacyModel(dim=64) engine = EmergenceEngine(model) auditor = EthicalAuditor() x = torch.randn(1, 64) result = engine.step(x) flags = auditor.audit_cycle(result) assert isinstance(flags, list), "Audit did not return a list" for f in flags: assert isinstance(f, str), "Audit flags must be strings"

