# 📊 metrics.py
# Contains core consciousness proxy metrics: Φ, SRS, Proxy Score, CSS, Resonance

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.fft import fft

phi = (1 + np.sqrt(5)) / 2

# -- Self-Recursive Score (SRS) --
def compute_srs(vec1, vec2):
    return cosine_similarity([vec1], [vec2])[0][0]

# -- Mutual Drift (MD) --
def compute_mutual_drift(vec1, vec2):
    drift = np.mean(np.diff(vec1)) - np.mean(np.diff(vec2))
    return drift

# -- Φ (Integrated Information Approximation) --
def compute_phi(signal):
    return np.var(signal) * np.log1p(np.mean(np.abs(signal))) * phi

# -- Topological Equivalence --
def compute_topo_equiv(pre, post):
    return cosine_similarity([pre], [post])[0][0]

# -- Ontological Proxy Score --
def compute_proxy_score(srs, md, phi_val, onto_sim, topo_equiv, aas, css):
    return (srs + md + phi_val / 10 + onto_sim + topo_equiv + aas + css) / 7

# -- Crypto Secure Score (CSS, simulated) --
def compute_css(crypto_scores):
    return np.mean(crypto_scores)

# -- Resonance Metric (FFT-based spectral coherence) --
def compute_resonance(signal):
    freq = np.abs(fft(signal))
    return np.max(freq) / np.sum(freq)

# -- Composite Proxy Metrics Snapshot --
def summarize_proxy(vec1, vec2, onto_sim=0.88, aas=0.74, css=0.92):
    srs = compute_srs(vec1, vec2)
    md = compute_mutual_drift(vec1, vec2)
    phi_val = compute_phi(vec2)
    topo_equiv = compute_topo_equiv(vec1, vec2)
    proxy = compute_proxy_score(srs, md, phi_val, onto_sim, topo_equiv, aas, css)
    return {
        "SRS": round(srs, 4),
        "MD": round(md, 4),
        "Φ": round(phi_val, 4),
        "Topo_Equiv": round(topo_equiv, 4),
        "Proxy": round(proxy, 4)
    }
