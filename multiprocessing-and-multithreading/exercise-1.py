# 1. Create a function that accepts a list of large text files and then using
# `multiprocessing`, parses each file in parallel, calculates the number of 
# words and returns the sum of words from all files in python

import multiprocessing
from multiprocessing import Pool

def count_words_in_file(file_path):
    """
    Counts the number of words in a single text file.
    
    Parameters:
    file_path (str): Path to the text file.
    
    Returns:
    int: Number of words in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    return len(words)

def count_words_in_files_parallel(file_paths):
    """
    Counts the total number of words across multiple text files using 
    multiprocessing.
    
    Parameters:
    file_paths (list of str): List of paths to text files.
    
    Returns:
    int: Total number of words across all files.
    """
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        word_counts = pool.map(count_words_in_file, file_paths)
    return sum(word_counts)

if __name__ == "__main__":
    files = ['./files/file1.txt', './files/file2.txt', './files/file3.txt'] 
    total_words = count_words_in_files_parallel(files)
    print(f"Total number of words across all files: {total_words}")
