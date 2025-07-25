from setuptools import setup, find_packages
from src.__version__ import __version__  # <-- correct import location

setup(
    name='legacy_protocol',
    version=__version__,  # <-- now using the imported version
    description='Symbolic AI architecture aligned with emergence, resonance, and φ-geometry',
    author='The Legacy Protocol Dev Group',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'torch>=2.0.0',
        'numpy>=1.24.0',
        'matplotlib',
        'scipy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.10',
    include_package_data=True
)