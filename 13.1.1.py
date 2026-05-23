# Write your code here......

"""n = int(input())

if n > 0:
	fib_series = fibonacci_module.generate_fibonacci_sequence(n)
	print(' '.join(map(str, fib_series)))
else:
	print("Please enter a positive integer")
"""
# Crucial: You must import the module to use it!
import fibonacci_module

# Read the maximum value from user input
try:
    line = input().strip()
    if line:
        n = int(line)

        if n > 0:
            # Call the function from the imported module
            fib_series = fibonacci_module.generate_fibonacci_sequence(n)
            # Convert the list of numbers to a space-separated string
            print(' '.join(map(str, fib_series)))
        else:
            print("Please enter a positive integer")
except EOFError:
    pass
