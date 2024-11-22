# Basic Calculator Program

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Main program
def main():
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Calculate the result
    result = calculate(num1, num2, operation)

    # Display the result
    if isinstance(result, str):
        print(result)  # Print error message if there is one
    else:
        print(f"{num1} {operation} {num2} = {result}")

# Run the main program
if __name__ == "__main__":
    main()