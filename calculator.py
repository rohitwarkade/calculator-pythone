import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 

    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return 
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Factorial")

while True:
    choice = input("Enter choice (1-7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        if choice == '6':
            num = float(input("Enter number: "))
            print("Square root:", square_root(num))
        elif choice == '7':
            num = int(input("Enter number: "))
            print("Factorial:", factorial(num))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", exponentiate(num1, num2))
    else:
        print("Invalid input")
