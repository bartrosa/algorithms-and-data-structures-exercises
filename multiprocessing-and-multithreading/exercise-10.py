# 10. Use `multiprocessing` to process a large set of data simultaneously. 
# Split the datainto fragments, and each process processes one fragment of 
# data. Use any data or data from scikitlearn datasets modules.

import multiprocessing
from sklearn.datasets import load_digits
import numpy as np

def process_data_fragment(data_fragment, results, index):
    """
    Process a fragment of the data.
    
    Parameters:
    data_fragment (ndarray): A fragment of the data to process.
    results (list): The list to store the result.
    index (int): The index to store the result in the list.
    """
    try:
        mean_value = np.mean(data_fragment, axis=0)
        results[index] = mean_value
        print(f"Processed fragment {index}")
    except Exception as e:
        results[index] = None
        print(f"Failed to process fragment {index}: {e}")

def main():
    digits = load_digits()
    data = digits.data

    num_processes = 4 
    num_samples = data.shape[0]
    fragment_size = num_samples // num_processes

    fragments = [data[i * fragment_size: (i + 1) * fragment_size] for i in range(num_processes)]
    if num_samples % num_processes != 0:
        fragments[-1] = data[(num_processes - 1) * fragment_size:]  

    manager = multiprocessing.Manager()
    results = manager.list([None] * num_processes)

    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(
            target=process_data_fragment, 
            args=(fragments[i], results, i)
            )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    for i, result in enumerate(results):
        if result is not None:
            print(f"Result from fragment {i}: {result}")
        else:
            print(f"Failed to retrieve result from fragment {i}")

if __name__ == "__main__":
    main()
