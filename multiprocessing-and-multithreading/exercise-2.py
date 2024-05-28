# 2. Implement a sorting algorithm (e.g. quicksort) and use `multiprocessing` 
# to parallelize sort list division. Combine sorted lists into one resulting 
# list.

import multiprocessing
from multiprocessing import Pool

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def parallel_quicksort(arr):
    num_workers = multiprocessing.cpu_count()
    pool = Pool(processes=num_workers)
    
    size = len(arr) // num_workers
    sublists = [arr[i*size:(i+1)*size] for i in range(num_workers)]
    
    if len(arr) % num_workers:
        sublists[-1].extend(arr[num_workers*size:])
    
    sorted_sublists = pool.map(quicksort, sublists)
    
    sorted = merge_sorted_lists(sorted_sublists)
    
    pool.close()
    pool.join()
    
    return sorted

def merge_sorted_lists(lists):
    import heapq
    return list(heapq.merge(*lists))

if __name__ == "__main__":
    unsorted_list = [3, 6, 8, 10, 1, 2, 1, 4, 5, 9, 7]
    sorted_list = parallel_quicksort(unsorted_list)
    print(f"Sorted list: {sorted_list}")
