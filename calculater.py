def calculator():

    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")

        if operation.lower() == 'q':
            print("Goodbye!")
            return
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Division by zero is not allowed.")
                continue
        
        print("Result:", result)
