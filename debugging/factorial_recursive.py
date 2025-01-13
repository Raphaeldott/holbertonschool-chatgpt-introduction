#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial of the given integer `n`. If `n` is 0, returns 1.

    Raises:
        RecursionError: If the recursion depth is exceeded for very large values of `n`.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Entry point: Read input from the command line and calculate the factorial
if len(sys.argv) > 1:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
else:
    print("Usage: ./factorial_recursive.py <non-negative integer>")

