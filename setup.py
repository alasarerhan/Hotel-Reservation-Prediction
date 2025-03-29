from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]

setup(
    name="MLOPS-PROJECT-1",
    version="0.1",
    author="Erhan",
    packages=find_packages(),
    install_requires=requirements
)