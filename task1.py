Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x, y):
...     return x + y
... 
... def subtract(x, y):
...     return x - y
... 
... def multiply(x, y):
...     return x * y
... 
... def divide(x, y):
...     if y == 0:
...         return "Error: Cannot divide by zero"
...     return x / y
... 
... def main():
...     print("Simple Calculator")
...     print("Select operation:")
...     print("1. Add")
...     print("2. Subtract")
...     print("3. Multiply")
...     print("4. Divide")
... 
...     choice = input("Enter choice (1/2/3/4): ")
... 
...     if choice in ('1', '2', '3', '4'):
...         try:
...             num1 = float(input("Enter first number: "))
...             num2 = float(input("Enter second number: "))
...         except ValueError:
...             print("Invalid input. Please enter numbers only.")
...             return
... 
...         if choice == '1':
...             print("Result:", add(num1, num2))
...         elif choice == '2':
...             print("Result:", subtract(num1, num2))
...         elif choice == '3':
...             print("Result:", multiply(num1, num2))
...         elif choice == '4':
...             print("Result:", divide(num1, num2))
...     else:
