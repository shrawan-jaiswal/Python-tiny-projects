# main_script.py

# Importing the functions from math_operations module
import math_operations

def main():
    """Main function to use imported math operations."""
    print("Using functions from the math_operations module.")
    
    # Using imported functions
    a, b = 7, 3
    print(f"Add: {a} + {b} = {math_operations.add(a, b)}")
    print(f"Subtract: {a} - {b} = {math_operations.subtract(a, b)}")
    print(f"Multiply: {a} * {b} = {math_operations.multiply(a, b)}")

if __name__ == '__main__':
    main()
