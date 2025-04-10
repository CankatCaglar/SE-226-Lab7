def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

def power(x, y):
    return x ** y

def mod(x, y):
    if y == 0:
        raise ValueError("Modulo by zero is not allowed")
    return x % y

if __name__ == "__main__":
    print("Testing math_utils module:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(15, 3) = {divide(15, 3)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"mod(17, 5) = {mod(17, 5)}")
    
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}") 