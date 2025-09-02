while True:
    user_input = input("Enter a positive integer to generate its multiplication table: ")

    if not user_input.isdigit() or int(user_input) <= 0:
        print("Invalid input. Please enter a **positive integer**.")
        continue

    number = int(user_input)

    print(f"\nMultiplication Table for {number}:\n")
    for i in range(1, 11):
        product = number * i
        print(f"{number} x {i} = {product}")

    # Ask if the user wants to continue
    choice = input("\nDo you want to generate another table? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Thank you! Goodbye.")
        break
