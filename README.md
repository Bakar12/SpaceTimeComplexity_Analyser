# SpaceTime Complexity Analyzer

Welcome to the SpaceTime Complexity Analyzer! This tool helps you analyze the time and space complexity of your Python functions. It provides a simple interface to input your functions, define input sizes, and visualize the results.

## Features

- Analyze time complexity of functions
- Analyze space complexity of functions
- Visualize results with plots

## Getting Started

### Prerequisites

- Python 3.x
- `matplotlib` library
- `numpy` library

You can install the required libraries using pip:

```bash
pip install matplotlib numpy
```

### Usage

1. Clone the repository or download the script `spacetime_analysis.py`.
2. Run the script:

```bash
python spacetime_analysis.py
```

3. Follow the prompts to input your function, define input sizes, and input generation logic.
4. The script will analyze the time and space complexity of your function and visualize the results.

### Example

Here is an example of how to use the tool:

1. Define your function:

```python
def sample_function(arr):
    return sorted(arr)
```

2. Define input sizes:

```python
[10, 100, 1000]
```

3. Define input generation logic:

```python
lambda size: list(range(size))
```

The tool will then analyze the `sample_function` and provide visualizations for time and space complexity.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the developers of `matplotlib` and `numpy` for their amazing libraries.









































































