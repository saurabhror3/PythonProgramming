def main():
    try:
        # 1. Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

        # 2. Perform the selected operation
        if operation == 'add':
            result = num1 + num2
            print(f"Result: {result}")
        elif operation == 'subtract':
            result = num1 - num2
            print(f"Result: {result}")
        elif operation == 'multiply':
            result = num1 * num2
            print(f"Result: {result}")
        elif operation == 'divide':
            try:
                result = num1 / num2
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
        else:
            print("Error: Unknown operation.")

    except ValueError:
        # 3. Handle non-numeric input
        print("Error: Invalid input. Please enter numeric values.")

    finally:
        # 4. Final message
        print("Operation complete.")

# Run the program
main()
