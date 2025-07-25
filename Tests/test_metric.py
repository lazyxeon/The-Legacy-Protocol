import torch from src import compute_phi, compute_srs, compute_proxy_score, compute_drift_score

def test_phi_stability(): x = torch.randn(1, 64) phi = compute_phi(x) assert isinstance(phi, float), "Φ score must be a float" assert 0 <= phi <= 1.5, "Φ score out of expected range"

def test_srs_format(): x = torch.randn(1, 64) srs = compute_srs(x) assert isinstance(srs, float), "SRS must be a float" assert 0 <= srs <= 1.0, "SRS out of bounds"

def test_proxy_score_behavior(): x = torch.randn(1, 64) proxy = compute_proxy_score(x) assert isinstance(proxy, float), "Proxy Score must be float" assert 0 <= proxy <= 1.0, "Proxy Score out of expected range"

def test_drift_computation(): x_prev = torch.randn(1, 64) x_curr = x_prev + torch.randn(1, 64) * 0.05 drift = compute_drift_score(x_prev, x_curr) assert isinstance(drift, float), "Drift must return a float" assert 0.0 <= drift <= 1.0, "Drift score should remain normalized"

