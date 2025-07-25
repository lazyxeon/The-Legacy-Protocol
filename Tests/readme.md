🧪 tests/ – Unit Testing Suite for The Legacy Protocol

This folder contains automated test coverage for the core symbolic modules in The Legacy Protocol. Use these tests to verify:

Functional stability of core components (LegacyModel, EmergenceEngine, etc.)

Consistency of symbolic utilities (spirals, φ checks, resonance)

Accuracy and safety of metric calculations (Φ, SRS, Drift, Proxy Score)



---

🚀 Running All Tests

From the root directory:

python tests/run_all_tests.py

This script discovers and runs all test files matching test_*.py.


---

📂 Test Files

test_core.py

Ensures proper execution of model, engine, chaos injection, and auditing


test_utils.py

Verifies φ-alignment, spiral growth, and tensor resonance behavior


test_metrics.py

Tests emergence metrics: Φ, SRS, Proxy Score, Drift scoring


run_all_tests.py

Entry point to run everything above at once



---

🔧 Notes

All test scripts use Python's built-in unittest framework

Requires dependencies listed in requirements.txt

Ensure src/ is structured as an importable module



---

🧠 Contribution Tips

Want to add tests?

1. Create a new file like test_newmodule.py


2. Use unittest.TestCase or inline-style tests


3. Verify with python tests/run_all_tests.py



Pull requests with improved coverage, fuzz testing, or CI integrations are welcome.


---

Test with intention. Stay symbolically aligned.

