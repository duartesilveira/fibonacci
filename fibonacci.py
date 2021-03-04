def fibonacci(element):

	print("hellow world")
    """

    A brief description of the function, And a new comment.

    Args:

        element: Integer

    Returns:

    """

    if element <= 1:
        return element
    else:
        return fibonacci(element - 1) + fibonacci(element - 2)


# Set n numbers
n = 35
limit = 0

# Return a list of n values of a Fibonacci sequence
Fibonacci_sequence = [fibonacci(i) for i in range(n)]
Fibbonacci_limit = fibonacci(limit)

# Print the results
print(Fibonacci_sequence)
print(Fibbonacci_limit)
