"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes, )


# Replace this with your code
while True:
    user_input = input("Enter your equation: ")
    tokens = user_input.split(" ")

    if "q" in tokens:
        print("Exited Calculator program")
        break
    elif len(tokens) < 2:
        print("Please enter 2 inputs")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"

    else: num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("Please enter valid numbers")
        continue

    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))
    
    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))
    
    elif operator == "square":
        result = square(float(num1))
    
    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "power":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))    
    
    elif operator == "x+":
        result = add_mult(float(num1), float(num2), float(num3))
    
    elif operator == "cubes+":
        result = add_cubes(float(num1), float(num2))

    else:
        result = "Please enter a valid operator followed by 2 numbers"
    
    print(result)