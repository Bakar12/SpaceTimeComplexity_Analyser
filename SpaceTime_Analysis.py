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


def visualize_results(results, input_sizes, metric="time"):
    """Visualize time or space complexity."""
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, results[metric], marker='o', label=f"{metric.capitalize()} Complexity")
    plt.title(f"{metric.capitalize()} Complexity Analysis")
    plt.xlabel("Input Size")
    plt.ylabel(f"{metric.capitalize()} ({'seconds' if metric == 'time' else 'bytes'})")
    plt.grid(True)
    plt.legend()
    plt.show()


def analyze_and_plot(function_text, function_name, input_sizes, input_generator_text):
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
        visualize_results(results, input_sizes, metric="time")
        visualize_results(results, input_sizes, metric="space")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def start_analysis():
    """Handle the start analysis button."""
    function_text = function_input.get("1.0", tk.END).strip()
    function_name = func_name_input.get().strip()
    input_sizes = input_sizes_input.get().strip()
    input_generator_text = input_generator_input.get("1.0", tk.END).strip()
    
    if not function_text or not function_name or not input_sizes or not input_generator_text:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    analyze_and_plot(function_text, function_name, input_sizes, input_generator_text)


# Tkinter GUI
root = tk.Tk()
root.title("Time and Space Complexity Analyzer")
root.geometry("800x600")

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

# Analyze Button
analyze_button = tk.Button(root, text="Analyze", font=("Arial", 14), command=start_analysis, bg="green", fg="white")
analyze_button.pack(pady=10)

# Run the application
root.mainloop()
