from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-HOTEL_RESERVATIONS_PROJECT",
    version="0.1",
    author="Dinesh",
    packages=find_packages(),
    install_requires=requirements,
)
