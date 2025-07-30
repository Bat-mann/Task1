# Task1
//Simple Calculator
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def main():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

   choice = input("Enter choice (1/2): ")
   if choice == '1':
        try:
            f = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F = {c:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a number.")
   elif choice == '2':
       try:
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C = {f:.2f}°F")
       except ValueError:
            print("Invalid input. Please enter a number.")
   else:
        print("Invalid choice")
