from setuptools import setup, find_packages

setup(
    name='fundamental_data',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "ipykernel>=6.29.5",
        "matplotlib>=3.10.1",
        "openpyxl>=3.1.5",
        "pandas>=2.2.3",
        "requests>=2.32.3",
        "seaborn>=0.13.2",
        "yfinance>=0.2.55",
    ],
)