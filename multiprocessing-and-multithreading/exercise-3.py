# 3. Define a math function and then use `multiprocessing` to compute in 
# parallel function values for different parameter sets.

import multiprocessing
from multiprocessing import Pool

def math_function(x):
    """
    Example mathematical function: f(x) = x^2 + 2x + 1
    
    Parameters:
    x (float): Input value.
    
    Returns:
    float: Computed value of the function.
    """
    return x**2 + 2*x + 1

def compute_function_values(params):
    """
    Computes function values for a list of parameters in parallel.
    
    Parameters:
    params (list of float): List of input values.
    
    Returns:
    list of float: Computed values of the function for each input.
    """
    num_workers = multiprocessing.cpu_count()
    with Pool(processes=num_workers) as pool:
        results = pool.map(math_function, params)
    return results

if __name__ == "__main__":
    parameter_sets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computed_values = compute_function_values(parameter_sets)
    print(f"Computed values: {computed_values}")
