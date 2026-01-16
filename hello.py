print('I am ready for Hack&Roll')

# Calculate the first 10 Fibonacci numbers
def fibonacci(n):
    """Generate the first n Fibonacci numbers"""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Calculate and print the first 10 Fibonacci numbers
fib_numbers = fibonacci(10)
print("First 10 Fibonacci numbers:", fib_numbers)
