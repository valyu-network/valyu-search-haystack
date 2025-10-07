# Installation Guide

## Installing from PyPI

Once published to PyPI, users can install with:

```bash
pip install valyu-search-haystack
```

## Installing from Source

### For Users

Install directly from GitHub:

```bash
pip install git+https://github.com/valyu/valyu-search-haystack.git
```

Or clone and install:

```bash
git clone https://github.com/valyu/valyu-search-haystack.git
cd valyu-search-haystack
pip install .
```

### For Development

1. **Clone the repository:**

```bash
git clone https://github.com/valyu/valyu-search-haystack.git
cd valyu-search-haystack
```

2. **Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install in editable mode with dev dependencies:**

```bash
pip install -e ".[dev]"
```

This installs the package in editable mode, so changes you make to the source code are immediately reflected.

## Verifying Installation

```python
from valyu_haystack import ValyuSearch, ValyuContentFetcher

print("✓ Valyu Haystack components installed successfully!")
```

## Usage

Set your API key:

```bash
export VALYU_API_KEY="your-api-key"
```

Basic usage:

```python
from valyu_haystack import ValyuSearch
from haystack import Pipeline

# Create component
search = ValyuSearch(top_k=5)

# Create pipeline
pipeline = Pipeline()
pipeline.add_component("search", search)

# Run search
result = pipeline.run({"search": {"query": "What is Haystack?"}})
print(result["search"]["documents"])
```

## Building the Package

### Build distribution files:

```bash
pip install build
python -m build
```

This creates:

- `dist/valyu_search_haystack-0.1.0.tar.gz` (source distribution)
- `dist/valyu_search_haystack-0.1.0-py3-none-any.whl` (wheel)

### Upload to PyPI:

```bash
pip install twine
twine upload dist/*
```

For TestPyPI (recommended for testing):

```bash
twine upload --repository testpypi dist/*
```

Then install from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ valyu-search-haystack
```

## Dependencies

The package automatically installs:

- `haystack-ai>=2.0.0` - Haystack framework
- `valyu>=2.2.1` - Valyu Python SDK

Optional development dependencies:

- `pytest>=7.0` - Testing framework
- `pytest-cov>=4.0` - Coverage reporting
- `black>=23.0` - Code formatting
- `ruff>=0.1.0` - Linting
- `mypy>=1.0` - Type checking

## Troubleshooting

### Import errors

If you get import errors, make sure the package is installed:

```bash
pip list | grep valyu
```

You should see:

```
valyu                    2.2.1
valyu-search-haystack    0.1.0
```

### API key issues

Make sure your API key is set:

```bash
echo $VALYU_API_KEY
```

If empty, set it:

```bash
export VALYU_API_KEY="your-api-key"
```

### Virtual environment

Always use a virtual environment to avoid conflicts:

```bash
python -m venv .venv
source .venv/bin/activate
pip install valyu-search-haystack
```

## Next Steps

- Read the [README.md](README.md) for usage examples
- Check out the Haystack documentation: https://docs.haystack.deepset.ai/
- Get your Valyu API key: https://valyu.network/
