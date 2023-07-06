import math

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def power(a, b):
  return a ** b

def square_root(a):
  return math.sqrt(a)

def main():
  print("Welcome to the advanced calculator!")

  while True:
    # Get the operator and operands from the user.
    operator = input("Enter an operator (+, -, *, /, ^, sqrt): ")
    a = float(input("Enter the first operand: "))
    b = float(input("Enter the second operand: "))

    # Calculate the result and print it to the user.
    if operator == "+":
      result = add(a, b)
    elif operator == "-":
      result = subtract(a, b)
    elif operator == "*":
      result = multiply(a, b)
    elif operator == "/":
      result = divide(a, b)
    elif operator == "^":
      result = power(a, b)
    elif operator == "sqrt":
      result = square_root(a)
    else:
      print("Invalid operator.")
      continue

    print("The result is:", result)

    # Check if the user wants to continue.
    continue_input = input("Do you want to continue? (y/n): ")
    if continue_input == "n":
      break

main()