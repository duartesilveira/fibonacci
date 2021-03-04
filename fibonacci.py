def fibonacci(element):
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

a = 3

# Return a list of n values of a Fibonacci sequence
Fibonacci_sequence = [fibonacci(i) for i in range(n)]
Fibbonacci_limit = fibonacci(limit)
Fibonacci_kike = fibonacci(a)

# Print the results
print(Fibonacci_sequence)
print(Fibbonacci_limit)
print(Fibonacci_kike)

