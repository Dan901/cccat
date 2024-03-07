from setuptools import setup

setup(
    name="cccat",
    version="0.1.0",
    packages=["cccat"],
    entry_points={"console_scripts": ["cccat = cccat.__main__:main"]},
)
