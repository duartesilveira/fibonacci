def fibonacci(element):
    """
    Simple function that returns N numbers of a Fibonnaci sequence

    """

    if element <= 1:
        return element
    else:
        return fibonacci(element - 1) + fibonacci(element - 2)


# Set n numbers
n = 35

# Return a list of n values of a Fibonacci sequence
Fibonacci_sequence = [fibonacci(i) for i in range(n)]

# Print the results
print(Fibonacci_sequence)
