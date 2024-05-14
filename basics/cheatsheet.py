

numbers = [1, 2, 3, 4, 5]

# C

# Comprehensions -  concise way to create containers such as lists, dictionaries, sets, and even generators. They provide a readable 
#                   and expressive way to create new sequences based on existing sequences, applying a specific condition or operation 
#                   to each element

squares = [x**2 for x in range(10)]  # List
square_dict = {x: x**2 for x in range(5)} # Dictionary
unique_squares = {x**2 for x in [-1, 1, 2]}  # Set

squares_gen = (x**2 for x in range(10)) # Generator
for square in squares_gen:
    print(square)


# G

# Generator -   a type of iterable, like a list or a tuple, but unlike lists, generators don't store all their values in memory at once. 
#               Instead, they generate values on the fly as needed, which allows them to be more memory-efficient when dealing with large 
#               datasets or complex sequences of data.

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num)




# M

# map()         function applies a specified function to each item of an iterable (like list or tuple) and returns an iterator that 
#               provides the results. This function is often used for transforming data. 

def square(x):
    return x ** 2

squared_numbers = map(square, numbers)
print(list(squared_numbers))


# R

# reduce()      used to apply a given function cumulatively to the items of an iterable, optionally starting with an initial value, 
#               to reduce the iterable to a single value. This function is useful for performing computations that cumulatively 
#               combine all elements of a list into a single result. 

from functools import reduce

def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)

