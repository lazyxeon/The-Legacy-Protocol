# phi_modules.py

import torch
import torch.nn as nn
import math

# --- Golden Ratio Constant
PHI = (1 + 5 ** 0.5) / 2

# --- φ-Scaled Dense Layer
class PhiDense(nn.Module):
    """
    Fully connected layer scaled by golden ratio.
    """
    def __init__(self, in_features, out_features=None, phi_scale=True):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features or int(in_features * PHI)
        self.linear = nn.Linear(in_features, self.out_features)

    def forward(self, x):
        return torch.tanh(self.linear(x))


# --- φ Dropout (scaled attention dampening)
class PhiDropout(nn.Module):
    def __init__(self, p=0.382):  # 1/φ^2
        super().__init__()
        self.dropout = nn.Dropout(p)

    def forward(self, x):
        return self.dropout(x)


# --- φ-Modulated Attention (minimal self-attention wrapper)
class PhiSelfAttention(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query = nn.Linear(dim, dim)
        self.key = nn.Linear(dim, dim)
        self.value = nn.Linear(dim, dim)
        self.scale = math.sqrt(dim * PHI)

    def forward(self, x):
        Q, K, V = self.query(x), self.key(x), self.value(x)
        attn_weights = torch.softmax(Q @ K.transpose(-2, -1) / self.scale, dim=-1)
        return attn_weights @ V


# --- φ Block Composition (stacked pattern)
class PhiBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.layer1 = PhiDense(dim)
        self.dropout = PhiDropout()
        self.attn = PhiSelfAttention(int(dim * PHI))

    def forward(self, x):
        x = self.layer1(x)
        x = self.dropout(x)
        x = self.attn(x)
        return x
