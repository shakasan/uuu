try:
    from setuptools import find_packages, setup
except ImportError:
    print("ImportError: Unable to import 'setup' and 'find_packages' from setuptools.")

from importlib.metadata import entry_points

entry_points = {"console_scripts": ["uuu = uuu.main:main"]}

setup(
    name="uuu",
    version="0.1.10",
    fullname="Universal-Upgrader-Utility",
    description="A tiny utility to update/clean your system",
    author="Francois B (Makoto)",
    author_email="francois@exoseed.be",
    keywords="uuu utility system upgrader arch linux",
    long_description="A tiny utility to update/clean your system",
    url="https://makotonoblog.be",
    licence="GPL-3.0",
    install_requires=["typer>=0.24.1"],
    entry_points=entry_points,
    packages=find_packages(),
)
