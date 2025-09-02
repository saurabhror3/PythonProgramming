# Define the calculate function
def calculate(num1: float, num2: float, operation) -> float:
    return operation(num1, num2)

# Lambda functions for operations
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero"

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation_input = input("Choose an operation (add, subtract, multiply, divide): ").lower()

    # Use if-elif to select the operation
    if operation_input == "add":
        result = calculate(num1, num2, add)
    elif operation_input == "subtract":
        result = calculate(num1, num2, subtract)
    elif operation_input == "multiply":
        result = calculate(num1, num2, multiply)
    elif operation_input == "divide":
        result = calculate(num1, num2, divide)
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
        exit()

    print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter numeric values.")

