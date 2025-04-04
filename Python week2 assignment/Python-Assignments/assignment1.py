# Get user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Initialize result
result = None

# Perform the requested operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please enter +, -, *, or /.")

# Function to format numbers as integers when appropriate
def format_number(n):
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

# Display the result if calculation was valid
if result is not None:
    formatted_num1 = format_number(num1)
    formatted_num2 = format_number(num2)
    formatted_result = format_number(result)
    print(f"{formatted_num1} {operation} {formatted_num2} = {formatted_result}")# Get user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Initialize result
result = None

# Perform the requested operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please enter +, -, *, or /.")

# Function to format numbers as integers when appropriate
def format_number(n):
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

# Display the result if calculation was valid
if result is not None:
    formatted_num1 = format_number(num1)
    formatted_num2 = format_number(num2)
    formatted_result = format_number(result)
    print(f"{formatted_num1} {operation} {formatted_num2} = {formatted_result}")