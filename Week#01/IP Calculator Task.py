# INTERNSHIP PAKISTAN
# TASK_1
# Build a basic calculator in python that performs addition, subtraction, multiplication, and division.
print("******Calculator******") 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Select operation you want to Perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = input("Enter choice (1/2/3/4): ")

            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")

                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                
                # Ask if the user wants another calculation
                next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
                if next_calculation != 'yes':
                    break

            else:
                print("Invalid input. Please choose a valid operation (1/2/3/4).")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the calculator
calculator()
