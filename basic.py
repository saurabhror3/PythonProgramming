print("Hello World!")

num1 = float(input("Enter the first number: "))

print(num1)

num2 = float(input("Enter the second number: "))

print(num2)

print(f"Addition: {num1} + {num2} = {num1 + num2}")

print(f"Subtraction: {num1} - {num2} = {num1 - num2}")

print(f"Multiplication: {num1} * {num2} = {num1 * num2}")


if num2 != 0:
  print(f"Division: {num1} / {num2} = {num1 / num2}")
else:
  print("Division: Cannot divide by zero!")
