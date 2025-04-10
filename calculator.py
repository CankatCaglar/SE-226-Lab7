import math_utils

operations = {
    '+': math_utils.add,
    '-': math_utils.subtract,
    '*': math_utils.multiply,
    '/': math_utils.divide,
    '^': math_utils.power,
    '%': math_utils.mod
}

def calculate():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /, ^, %): ")
        
        if operator not in operations:
            print("Invalid operator!")
            return
        
        result = operations[operator](num1, num2)
        print(f"Result: {num1} {operator} {num2} = {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Simple Calculator")
    print("----------------")
    calculate() 