"""
Setup script for QuantPak - Quantitative Finance Analysis Platform
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read requirements
requirements = []
try:
    with open('requirements.txt', 'r') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    pass

setup(
    name="quantpak",
    version="0.1.0",
    author="QuantPak Development Team",
    author_email="dev@quantpak.com",
    description="A comprehensive quantitative finance package for analysis, backtesting, and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/quantpak",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
        "docs": [
            "sphinx>=7.1.0",
            "sphinx-rtd-theme>=1.3.0",
            "nbsphinx>=0.9.0",
        ],
        "ml": [
            "tensorflow>=2.13.0",
            "torch>=2.0.0",
            "transformers>=4.21.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "quantpak=quantpak.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "quantpak": ["config/*.yaml", "data/sample/*.csv"],
    },
    zip_safe=False,
    keywords="quantitative finance trading backtesting portfolio optimization risk management",
)