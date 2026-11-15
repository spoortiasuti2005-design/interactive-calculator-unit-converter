# Interactive Calculator and Unit Converter

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Function to convert kilometres to miles
def km_to_miles(km):
    return km * 0.621371


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Function to get a valid number from the user
def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input! Please enter a number.")


# Main program
while True:
    print("\n===== INTERACTIVE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Kilometres to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

    elif choice == "5":
        km = get_number("Enter distance in kilometres: ")
        print("Distance in miles:", km_to_miles(km))

    elif choice == "6":
        celsius = get_number("Enter temperature in Celsius: ")
        print("Temperature in Fahrenheit:",
              celsius_to_fahrenheit(celsius))

    elif choice == "7":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice! Please select from 1 to 7.")
