# 1. Recursive factorial function
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

# 2. Function with return value and message formatting
def factorial_with_message(number: int) -> str:
    result = factorial(number)
    return f"The factorial of {number} is {result}."

# 3. Main block to prompt user and handle input
def main():
    try:
        user_input = input("Enter a positive integer: ")
        number = int(user_input)

        if number < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            message = factorial_with_message(number)
            print(message)

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# 4. Run the script
if __name__ == "__main__":
    main()
