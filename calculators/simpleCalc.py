def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
   
except ValueError:
    print("Invalid input: Please enter numbers.")
    choice = float(input("Enter choice: \n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division: "))

    try:
        func = operations.get(choice)
        if not func:
            print("Invalid choice. Please select a valid option.")
        elif choice == 4 and num2 == 0:
            print("Error: Division by zero.")
        else:
            print("Result:", func(num1, num2))
    except ValueError:
            print("Invalid input: Please enter numbers.")
    except ZeroDivisionError:
            print("Error: Division by zero.")
