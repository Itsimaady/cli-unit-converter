import argparse
import sys

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Argument parser setup
parser = argparse.ArgumentParser(
    description="Convert temperature between Celsius and Fahrenheit."
)

group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--celsius", type=float, help="Temperature in Celsius to convert to Fahrenheit")
group.add_argument("-f", "--fahrenheit", type=float, help="Temperature in Fahrenheit to convert to Celsius")

args = parser.parse_args()

# If command-line args are given, use them
if args.celsius is not None:
    result = celsius_to_fahrenheit(args.celsius)
    print(f"{args.celsius}°C = {result:.2f}°F")

elif args.fahrenheit is not None:
    result = fahrenheit_to_celsius(args.fahrenheit)
    print(f"{args.fahrenheit}°F = {result:.2f}°C")

# If no args are given, show interactive mode
else:
    print("🌡️  Welcome to the CLI Unit Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {result:.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {result:.2f}°C")
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")
