while True:
    user_input = input("Enter a number (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break

    try:
        number = float(user_input)

        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'quit' to exit.")
