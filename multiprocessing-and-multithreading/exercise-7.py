# 7. Create a multi-threaded version of the Monte Carlo algorithm for 
# approximating Pi. Use one process per thread.

import threading
import random
import math

def monte_carlo_pi(num_points, results, index):
    """
    Monte Carlo simulation to approximate the value of Pi.
    
    Parameters:
    num_points (int): Number of points to generate.
    results (list): List to store the result.
    index (int): Index to store the result in the list.
    """
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = (inside_circle / num_points) * 4
    results[index] = pi_estimate

def main():
    num_threads = 4
    num_points_per_thread = 1000000
    total_points = num_threads * num_points_per_thread

    results = [0] * num_threads

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(
            target=monte_carlo_pi, 
            args=(num_points_per_thread, results, i)
            )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi_estimate = sum(results) / num_threads
    print(f"Estimated value of Pi: {pi_estimate}")

if __name__ == "__main__":
    main()
