from setuptools import find_packages, setup

setup(
    name="pyaqstripe",
    version="0.1.0",
    description=(
        "A Python implementation of the Air Quality Stripes colormap "
        "following https://airqualitystripes.info"
    ),
    author="Barry Baker",
    author_email="barry.baker@noaa.gov",
    url="https://github.com/bbakernoaa/pyaqstripe",
    packages=find_packages(),
    install_requires=["matplotlib", "numpy", "bokeh"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
