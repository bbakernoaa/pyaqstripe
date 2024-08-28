from setuptools import setup, find_packages

setup(
    name='pyaqstripe',
    version='0.1.0',
    description='A Python wrapper for the AQSTripes following https://airqualitystripes.info/?country=Vatican%20City&city=Vatican%20City',
    author='Barry Baker',
    author_email='barry.baker@noaa.gov',
    url='https://github.com/bbakernoaa/pyaqstripe',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'bokeh'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)