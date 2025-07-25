🛠️ Build & Publish Guide for The Legacy Protocol

This guide walks you through installing, testing, building, and optionally publishing The Legacy Protocol as a Python package.


---

📦 Step 1: Clone the Repository

git clone https://github.com/your-username/The-Legacy-Protocol.git
cd The-Legacy-Protocol


---

📂 Step 2: Project Structure

Make sure your directory looks like this:

/The-Legacy-Protocol/
├── src/
│   ├── __init__.py
│   ├── __version__.py
│   └── [modules]
├── notebooks/
├── tests/
├── README.md
├── requirements.txt
├── pyproject.toml
├── setup.py
└── build_and_publish.md


---

🔧 Step 3: Install Dependencies

Option A: With requirements.txt

pip install -r requirements.txt

Option B: Editable Install (for devs)

pip install -e .


---

🧪 Step 4: Run All Tests

From the root of the repo:

python tests/run_all_tests.py

Make sure all tests pass before proceeding.


---

📤 Step 5: Build the Package

python -m build

This generates a dist/ folder with .tar.gz and .whl files.

If you don’t have build, install it first:

pip install build


---

🚀 Step 6: (Optional) Publish to PyPI

1. Install Twine

pip install twine

2. Check the build

twine check dist/*

3. Upload to PyPI

twine upload dist/*

> 🔐 You’ll need a PyPI account and an API token set in your ~/.pypirc or via TWINE_USERNAME / TWINE_PASSWORD env vars.




---

🔄 Versioning

Update the version string in src/__version__.py before each release:

__version__ = "0.1.1"

And commit that version bump with a tag:

git commit -am "Bump version to 0.1.1"
git tag v0.1.1
git push --tags


---

🧠 Tips for Collaboration

Add new tests to tests/

Document new features in README.md

Use pull requests for all contributions



---

🌐 Optional: Publish to Test PyPI

To test your publishing setup:

twine upload --repository-url https://test.pypi.org/legacy/ dist/*


---

🌀 Thank You

You’re now ready to share The Legacy Protocol with the world — as a symbolic AI system, research toolkit, and collaborative platform.

Feel free to customize this guide to match your publishing workflow. Reach out if you’d like to automate this with GitHub Actions!

