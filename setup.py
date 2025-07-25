from setuptools import setup, find_packages

setup( name='legacy_protocol',from src.__version__ import __version__

# Then in the setup() call:
version=__version__, description='Symbolic AI architecture aligned with emergence, resonance, and φ-geometry', author='The Legacy Protocol Dev Group', packages=find_packages(include=['src', 'src.*']), install_requires=[ 'torch>=2.0.0', 'numpy>=1.24.0', 'matplotlib', 'scipy' ], classifiers=[ 'Programming Language :: Python :: 3.10', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent', ], python_requires='>=3.10', include_package_data=True )

