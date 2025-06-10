from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyuqspice',
    version='0.0.1',
    description='Tools for uncertainty quantification and LTSpice simulation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/karylsienn/PyUQSpice',
    author='Karol Niewiadomski',
    author_email='niewiadomski.k@wp.pl',
    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        'pandas>=1.4.3',
        'numpy>=1.20.0',
        'openturns>=1.19',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov',
            'black',
            'flake8',
        ],
    },
    zip_safe=False,
    include_package_data=True,
)
