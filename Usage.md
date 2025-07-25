📘 USAGE.md – The Legacy Protocol

This guide explains how to use The Legacy Protocol — a symbolic AI framework built on φ-aligned emergence, recursive dynamics, and ethical auditability.

You’ll find everything you need to:

Run the system

Explore the included notebooks

Integrate symbolic modules

Monitor emergence and ethical signals



---

🔧 Setup

Install the required Python packages:

pip install -r requirements.txt

Make sure your environment supports:

Python ≥ 3.10

torch, matplotlib, numpy



---

▶️ Running Demos

The examples/ folder contains runnable scripts:

1. run_basic_emergence.py

Starts a symbolic emergence cycle using the base model.

2. inject_and_audit.py

Injects chaos into the system and checks for symbolic or ethical breaches.

3. phi_alignment_check.py

Verifies whether given tensors are aligned with φ geometries.

Run any of them with:

python examples/run_basic_emergence.py


---

📓 Interactive Notebooks

Each notebook in notebooks/ offers an exploratory environment:

emergence_walkthrough.ipynb

Simulates emergence over 20 cycles

Tracks metrics like Φ, Proxy Score, SRS, Drift


chaos_perturbation_test.ipynb

Injects chaos

Measures resilience across symbolic indicators


spiral_sandbox.ipynb

Visualizes Kryst Spiral growth

Maps Fibonacci to polar geometry


auditor_resonance_map.ipynb

Shows heatmap of ethical flags raised per cycle


tensor_sculptor.ipynb

Builds φ-aligned tensors

Stabilizes them for symbolic injection



---

🧠 Module Guide (src/)

Core Components

LegacyModel: The main symbolic architecture

EmergenceEngine: Handles step-wise logic and logs metrics

ChaosInjector: Adds controlled entropy

EthicalAuditor: Monitors for symbolic breaches


Utilities

is_phi_aligned() – checks golden ratio structure

spiral_growth(), kryst_spiral_escape() – geometry helpers

stabilize_spiral_tensor() – ensures coherent φ structure



---

🧪 Customization

Each class supports keyword arguments to control behavior:

engine = EmergenceEngine(model, drift_sensitivity=0.2)
injector = ChaosInjector(mode='symbolic', magnitude=0.33)

You can tune emergence, drift thresholds, and symbolic mutation styles.


---

🧩 Extend or Contribute

Ideas for contribution:

Add φ-aligned model variants

Expand the notebook suite

Improve visual diagnostics

Add unit tests


PRs welcome.


---

Summary

This framework provides:

Symbolic model emergence

Ethical audit hooks

φ-geometry shaping tools

Clear entry points for research or exploration


Stay aligned. Think recursively. Keep it stable.

