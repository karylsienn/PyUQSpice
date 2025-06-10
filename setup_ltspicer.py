import os
from setuptools import setup, find_packages

# Read requirements from requirements.txt
def read_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='ltspicer',
    version='0.0.1',
    description='LTSpice interface tools for Python - extracted from PyUQSpice',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
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
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
    packages=['ltspicer'],
    package_dir={'ltspicer': 'pyuqspice/ltspicer'},
    python_requires=">=3.8",
    install_requires=[
        'pandas>=1.4.3',
        'numpy>=1.20.0',
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
