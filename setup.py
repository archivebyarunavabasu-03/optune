from setuptools import find_packages, setup

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="optune",
    version="0.0.1",
    description="A package for implementing os algos",
    package_dir={"": "optune"},
    packages=find_packages(where="optune"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    author="arunavabasu-03",
    author_email="arunavabasudev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
    },
    python_requires=">=3.9",
)