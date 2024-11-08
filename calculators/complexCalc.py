import numpy as np

# Define functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def power(a, b): return np.power(a, b)
def square(a): return np.square(a)
def squareRoot(a): return np.sqrt(a)
def log(a): return np.log(a)
def sin(a): return np.sin(a)
def cos(a): return np.cos(a)
def tan(a): return np.tan(a)
def factorial(a): return np.math.factorial(int(a))  # Factorial requires an integer
def inverse(a): return 1 / a

# Map choices to functions and the number of arguments they need
operations = {
    1: (add, 2),
    2: (subtract, 2),
    3: (multiply, 2),
    4: (divide, 2),
    5: (power, 2),
    6: (square, 1),
    7: (squareRoot, 1),
    8: (log, 1),
    9: (sin, 1),
    10: (cos, 1),
    11: (tan, 1),
    12: (factorial, 1),
    13: (inverse, 1)
}

# Display menu
print("Welcome to my calculator!")
print("\n".join([f"{k}. {v[0].__name__.capitalize()}" for k, v in operations.items()]))

# Get user choice
try:
    choice = int(input("Enter your choice: "))
    if choice not in operations:
        raise ValueError("Invalid choice.")
    
    operation, num_args = operations[choice]

    # Get the required number of inputs based on the operation
    numbers = []
    for i in range(num_args):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Perform the calculation
    result = operation(*numbers)
    print(f"Result: {result}")

except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError:
    print("Error: Division by zero.")
