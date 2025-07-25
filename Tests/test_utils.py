import torch from src import is_phi_aligned, is_tensor_resonant, spiral_growth, kryst_spiral_escape

def test_phi_alignment(): aligned_shape = (89, 55)  # ~phi misaligned_shape = (80, 50) assert is_phi_aligned(aligned_shape), "Should be phi-aligned" assert not is_phi_aligned(misaligned_shape), "Should not be phi-aligned"

def test_tensor_resonance(): tensor = torch.randn(89, 55) result = is_tensor_resonant(tensor) assert isinstance(result, bool), "Resonance check should return a boolean"

def test_spiral_growth_output(): points = spiral_growth(50) assert isinstance(points, list), "Spiral output should be a list of points" assert all(isinstance(p, tuple) and len(p) == 2 for p in points), "All points must be 2D tuples"

def test_kryst_spiral_escape_stability(): tensor = torch.randn(34, 21) escaped = kryst_spiral_escape(tensor) assert escaped.shape == tensor.shape, "Escape tensor must preserve shape"

