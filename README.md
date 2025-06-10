# PyUQSpice

Tools for uncertainty quantification and LTSpice.

The `ltspicer` library provides an interface to LTSpice. This means it is possible to create netlists, run LTSpice, and read the data from an LTSpice simulation. 
The library `pystatemc` is an interface for creating a Polynomial Chaos analysis, including sensitivity analysis. This library is for further development.


### Installation Options

## Option 1: Install Complete PyUQSpice Package

```bash
# Navigate to the repository root
cd PyUQSpice

# Install in development mode (recommended for development)
pip install -e .

# Or install normally
pip install .
```

## Option 2: Install LTSpicer as Standalone Library

```bash
# Navigate to the repository root
cd PyUQSpice

# Install ltspicer as standalone package
pip install -e . --config-settings editable_mode=compat

# Then you can import it as:
# from pyuqspice.ltspicer import readers, runners, pathfinder, sweepers
```

## Option 3: Create Standalone LTSpicer Package

If you want to extract just the ltspicer functionality:

```bash
# Use the provided setup_ltspicer.py script
python setup_ltspicer.py sdist bdist_wheel
pip install dist/ltspicer-0.0.1-py3-none-any.whl
```

## Usage Examples

### Using the complete package:
```python
import pyuqspice
from pyuqspice.ltspicer.readers import RawReader
from pyuqspice.ltspicer.runners import LTSpiceRunner
from pyuqspice.pystatemc.pcarchitects import PCArchitect

# Read LTSpice raw files
reader = RawReader("path/to/file.raw")
data = reader.get_data()

# Run LTSpice simulations
runner = LTSpiceRunner()
runner.run("path/to/circuit.asc")
```

### Using just ltspicer functionality:
```python
from pyuqspice.ltspicer import readers, runners, pathfinder, sweepers

# All ltspicer functionality is available
reader = readers.RawReader("path/to/file.raw")
runner = runners.LTSpiceRunner()
```

## Dependencies

The following dependencies are required and will be installed automatically:
- pandas >= 1.4.3
- numpy >= 1.20.0  
- openturns >= 1.19
- setuptools >= 65.5.1

## Testing

Run the test suite to verify installation:
```bash
python -m pytest pyuqspice/tests/ -v
```

All tests should pass (49 passed, 1 skipped as of last run).

## Development Setup

For development work:
```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest pyuqspice/tests/

# Run with coverage
pytest pyuqspice/tests/ --cov=pyuqspice
```
