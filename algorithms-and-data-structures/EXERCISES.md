1. Pack duplicates from the list into sublists. call example: pack(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a','a', 'd', 'e', 'e', 'e', 'e']) result: ["aaaa","b","cc","aa","d","eeee"]
2. Use the result from the previous task to implement the so-called data compression method using run length encoding (RLE) https:pl.wikipedia.org/wiki/RLE. Successive duplicate elements are encoded as lists (N, E), where N is the number of duplicates of element E. call example: encode(["aaaa","b","cc","aa","d","eeee" ]) result: [(4,'a'), (1,'b'), (2,'c'), (2,'a'), (1,'d'), (4,'e ')]
3. Implement BST (binary search tree) Pseudocode: BinarySearchTree: has(value: number) boolean traverseType() DFS_PREORDER string DFS_INORDER string DFS_POSTORDER string BFS string traverse() number[] getColumn(column: number) number[] The has method must return whether a given value is in the tree. The traverse method must return an array of values according to the traverse type. The getColumn method must return an array of values in the specified column. Column 0 is all the elements under the root (including the root). Each step to the right means +1 to the column order, each step to the left means -1 to the column order. The returned array should contain the values in ascending order. getColumn(0) [10,17]

---

General:
• Merge Sort: Implement a sorting algorithm
by merging.
• Binary Search: Implement binary search algorithm in
sorted array.
• Fibonacci Numbers: Write a function that returns the nth Fibonacci number.
• String Reversal: Write a function that reverses a string.
• Finding the greatest common divisor (GCD): Implement
algorithm for determining the greatest common divisor of two numbers.
• Longest Common Substring (LCS) Search: Write a function that
finds the longest common subsequence of two strings.
• Dijkstra's Algorithm: Implement Dijkstra's algorithm for finding the shortest
paths in the graph.
• Prime Numbers: Write a function that checks whether a given number is a number
first.
• Knapsack problem: Implement a solving algorithm
knapsack problem for a given set of items.
• Counting occurrences of items in a list: Write a function that counts occurrences
each item in the list.
• Hash Tables: Implement a simple hash table.
• String permutations: Write a function to generate all possible ones
permutations of a given string of characters.
• Exponentiation by squaring algorithm: Implement
fast exponentiation algorithm.
• Topological sorting: Implement topological sorting algorithm for
a given directed graph.
• BFS (Breadth-First Search) Algorithm: Implement the BFS algorithm to
breadth-first graph search.
• DFS (Depth-First Search) Algorithm: Implement the DFS algorithm to
depth-first graph search.
• Naive pattern matching algorithm:
Implement a naive pattern checking algorithm.
• Kruskal's Algorithm: Implement Kruskal's algorithm for finding
minimal spanning tree in a graph.
• Bubble Sort Algorithm: Implement the algorithm
bubble sort.
• Cycle checking in a directed graph: Write a function that checks whether
a given directed graph contains a cycle.

Bit manipulation:
• Bit Flipping: Write a function that flips the bits of an integer.
• Count set bits: Implement a function that counts a number
set bits in integer.
• Convert a number to binary: Write a function that converts an integer to its
binary representation.
• Bit Parity: Check if an integer has an even number of bits set
bits.
• Bitwise AND, OR, XOR: Implement functions that perform bitwise AND operations,
OR and XOR on two integers.

Recursion:
• Factorial: Write a function that calculates the factorial of an integer using recursion.
• Sum of a sequence: Implement a function that calculates the sum of a numeric sequence
using recursion.
• Print a number in reverse: Write a function that prints the number in
reverse order using recursion.
• Binary Search (Recursive): Implement a search algorithm
binary using recursion.
• Recursion Tree: Write a function that draws a recursion tree for a given function
recursive.

Dynamic programming:
• Fibonacci with memory: Implement the Fibonacci algorithm with cache in
to optimize performance.
• Knapsack problem - with dynamic programming: Solve
knapsack problem using dynamic programming technique.
• Sum of Subsequence with Largest Sum: Find the largest sum among
all possible substrings of a given string using dynamic
programming.
• Longest Common Substring (LCS) with dynamic programming: Solve
longest common subsequence problem using dynamic
programming.
• Jump table: Find the minimum number of jumps needed to move from
beginning to end of an array using dynamic programming.
• Maze path problem: Find the shortest path in the maze using
dynamic programming.
• Counting divisions of a number: Find all possible divisions of a number into smaller ones
numbers using dynamic programming.
• Longest common substring of two strings: Find the longest common substring
substring of two strings using dynamic programming.
• Johnson-Trotter Algorithm: Implement the permutation generation algorithm a
using dynamic programming.
• Dynamic Programming Knapsack Problem 0-1: Solve the problem
backpack (Knapsack) with the restriction that any item can be used
only once, using dynamic programming.

Difficult:
1. Write a function that adds two numbers, do not use + or any other operator
arithmetic.
2. Write a function that counts the number of 2 digits in the number N. E.g. 25 -> 2,12,20,21,22,23,24,25 ->
Score: 9 (22 counts as 2)
3. Distance between words. Write an algorithm that will find the smallest value for the text
the distance between two words in the text.