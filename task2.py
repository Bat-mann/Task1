Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fahrenheit_to_celsius(f):
...     return (f - 32) * 5 / 9
... 
... def celsius_to_fahrenheit(c):
...     return (c * 9 / 5) + 32
... 
... def main():
...     print("Temperature Converter")
...     print("1. Fahrenheit to Celsius")
...     print("2. Celsius to Fahrenheit")
... 
...     choice = input("Enter choice (1/2): ")
... 
...     if choice == '1':
...         try:
...             f = float(input("Enter temperature in Fahrenheit: "))
...             c = fahrenheit_to_celsius(f)
...             print(f"{f}°F = {c:.2f}°C")
...         except ValueError:
...             print("Invalid input. Please enter a number.")
...     elif choice == '2':
...         try:
...             c = float(input("Enter temperature in Celsius: "))
...             f = celsius_to_fahrenheit(c)
...             print(f"{c}°C = {f:.2f}°F")
...         except ValueError:
...             print("Invalid input. Please enter a number.")
...     else:
...         print("Invalid choice")
