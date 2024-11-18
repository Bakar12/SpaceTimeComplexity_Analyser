import tkinter as tk
from tkinter import messagebox, scrolledtext
import timeit
import sys
import matplotlib.pyplot as plt


def analyze_function(func, *args, repeats=5):
    """Analyze time and space complexity of the given function."""
    # Time complexity
    timer = timeit.Timer(lambda: func(*args))
    time_taken = min(timer.repeat(repeat=repeats, number=1))
    
    # Space complexity
    space_usage = sys.getsizeof(args) + sys.getsizeof(func)
    
    return {"time": time_taken, "space": space_usage}


def calculate_theoretical_complexity(input_sizes, big_o_notation):
    """Calculate theoretical complexity based on input sizes and Big O Notation."""
    complexities = []
    for size in input_sizes:
        if big_o_notation == "O(1)":
            complexities.append(1)
        elif big_o_notation == "O(log n)":
            complexities.append(np.log2(size))
        elif big_o_notation == "O(n)":
            complexities.append(size)
        elif big_o_notation == "O(n log n)":
            complexities.append(size * np.log2(size))
        elif big_o_notation == "O(n^2)":
            complexities.append(size**2)
        elif big_o_notation == "O(2^n)":
            complexities.append(2**size)
        else:
            complexities.append(None)  # Unknown notation
    return complexities


def visualize_results(results, input_sizes, metric="time", big_o_notation=None):
    """Visualize time or space complexity."""
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, results[metric], marker='o', label=f"Observed {metric.capitalize()} Complexity")
    
    if big_o_notation:
        theoretical_complexity = calculate_theoretical_complexity(input_sizes, big_o_notation)
        plt.plot(input_sizes, theoretical_complexity, linestyle="--", label=f"Theoretical {big_o_notation}")

    plt.title(f"{metric.capitalize()} Complexity Analysis")
    plt.xlabel("Input Size")
    plt.ylabel(f"{metric.capitalize()} ({'seconds' if metric == 'time' else 'bytes'})")
    plt.grid(True)
    plt.legend()
    plt.show()


def analyze_and_plot(function_text, function_name, input_sizes, input_generator_text, big_o_notation):
    """Analyze the function and plot results."""
    try:
        # Execute the function definition
        exec(function_text, globals())
        func = globals()[function_name]
        
        # Convert input sizes
        input_sizes = list(map(int, input_sizes.split(',')))
        
        # Execute input generator
        input_generator = eval(input_generator_text, globals())
        
        # Collect results
        results = {"time": [], "space": []}
        for size in input_sizes:
            inputs = input_generator(size)
            complexities = analyze_function(func, inputs)
            results["time"].append(complexities["time"])
            results["space"].append(complexities["space"])
        
        # Plot results
        visualize_results(results, input_sizes, metric="time", big_o_notation=big_o_notation)
        visualize_results(results, input_sizes, metric="space", big_o_notation=None)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def start_analysis():
    """Handle the start analysis button."""
    function_text = function_input.get("1.0", tk.END).strip()
    function_name = func_name_input.get().strip()
    input_sizes = input_sizes_input.get().strip()
    input_generator_text = input_generator_input.get("1.0", tk.END).strip()
    big_o_notation = big_o_input.get().strip()
    
    if not function_text or not function_name or not input_sizes or not input_generator_text or not big_o_notation:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    analyze_and_plot(function_text, function_name, input_sizes, input_generator_text, big_o_notation)


# Tkinter GUI
root = tk.Tk()
root.title("Time and Space Complexity Analyzer with Big O Notation")
root.geometry("800x650")

# Function Input
tk.Label(root, text="Define Your Function:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
function_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=8)
function_input.pack(padx=10, pady=5)

# Function Name
tk.Label(root, text="Function Name:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
func_name_input = tk.Entry(root, font=("Arial", 12), width=50)
func_name_input.pack(padx=10, pady=5)

# Input Sizes
tk.Label(root, text="Input Sizes (comma-separated):", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
input_sizes_input = tk.Entry(root, font=("Arial", 12), width=50)
input_sizes_input.pack(padx=10, pady=5)

# Input Generator
tk.Label(root, text="Input Generator (as Python code):", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
input_generator_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=4)
input_generator_input.pack(padx=10, pady=5)

# Big O Notation
tk.Label(root, text="Expected Big O Notation (e.g., O(n), O(n^2), O(log n)):", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
big_o_input = tk.Entry(root, font=("Arial", 12), width=50)
big_o_input.pack(padx=10, pady=5)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze", font=("Arial", 14), command=start_analysis, bg="green", fg="white")
analyze_button.pack(pady=10)

# Run the application
root.mainloop()
