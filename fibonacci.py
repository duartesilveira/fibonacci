
def fibonacci(n):
    "Simple function that returns N numbers of a Fibonnaci sequence"
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Set n numbers
n = 35
#Return a list of n values of a Fibonacci sequence
Fibonacci_sequence = [fibonacci(i) for i in range(n)]
#Print the results
print(Fibonacci_sequence)