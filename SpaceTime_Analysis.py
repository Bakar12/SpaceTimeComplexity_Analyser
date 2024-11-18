import timeit
import sys
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate time and space complexity
def analyze_function(func, *args, repeats=5):
    """
    Analyzes time and space complexity of a given function.
    
    Parameters:
        func (function): The Python function to analyze.
        *args: Arguments to pass to the function.
        repeats (int): Number of times to repeat for timing analysis.
    
    Returns:
        dict: Time and space complexity results.
    """
    # Measure time complexity
    timer = timeit.Timer(lambda: func(*args))
    time_taken = min(timer.repeat(repeat=repeats, number=1))
    
    # Measure space complexity
    space_usage = sys.getsizeof(args) + sys.getsizeof(func)
    
    return {"time": time_taken, "space": space_usage}

# Function to visualize results
def visualize_results(results, input_sizes, metric="time"):
    """
    Visualizes time or space complexity results.
    
    Parameters:
        results (dict): A dictionary of algorithm names and their results.
        input_sizes (list): The sizes of inputs analyzed.
        metric (str): Either 'time' or 'space' for the metric to visualize.
    """
    plt.figure(figsize=(10, 6))
    
    for func_name, complexities in results.items():
        plt.plot(input_sizes, complexities[metric], label=func_name)
    
    plt.title(f"{metric.capitalize()} Complexity Analysis")
    plt.xlabel("Input Size")
    plt.ylabel(f"{metric.capitalize()} ({'seconds' if metric == 'time' else 'bytes'})")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main workflow
def main():
    print("Welcome to the Time and Space Complexity Analyzer!")
    
    # Input functions from the user
    print("\nDefine your functions below (or use built-in ones).")
    print("For example:\n"
          "def sample_function(arr):\n"
          "    return sorted(arr)\n")
    user_code = input("Enter your function definition (as Python code):\n")
    exec(user_code, globals())  # Execute the function definition in the global scope

    func_name = input("Enter the name of the function you just defined: ")
    func = globals()[func_name]  # Get the function object by name
    
    # Input sizes and testing setup
    print("\nDefine input sizes to analyze (e.g., [10, 100, 1000]):")
    input_sizes = eval(input("Input Sizes: "))
    
    print("\nDefine input generation logic for testing.")
    print("For example: lambda size: list(range(size))")
    input_generator = eval(input("Input Generator (as a lambda function): "))
    
    # Run analysis
    print("\nAnalyzing...")
    results = {func_name: {"time": [], "space": []}}
    
    for size in input_sizes:
        inputs = input_generator(size)
        complexity = analyze_function(func, inputs)
        results[func_name]["time"].append(complexity["time"])
        results[func_name]["space"].append(complexity["space"])
    
    # Visualize results
    print("\nVisualization:")
    visualize_results(results, input_sizes, metric="time")
    visualize_results(results, input_sizes, metric="space")
    print("Analysis complete!")

if __name__ == "__main__":
    main()
