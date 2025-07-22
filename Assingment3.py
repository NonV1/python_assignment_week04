add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error can't divide by zero"

if __name__ == "__main__":
    x = 85
    y = 95
    print("Addition:", add(x, y))         
    print("Subtraction:", subtract(x, y)) 
    print("Multiplication:", multiply(x, y)) 
    print("Division:", divide(x, y))   