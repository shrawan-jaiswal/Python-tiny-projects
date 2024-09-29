# math_operations.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def main():
    """Test the math operations functions."""
    print("Running math_operations as a standalone script.")
    
    # Test the functions
    x, y = 10, 5
    print(f"Adding {x} and {y}: {add(x, y)}")         # Output: 15
    print(f"Subtracting {y} from {x}: {subtract(x, y)}")  # Output: 5
    print(f"Multiplying {x} and {y}: {multiply(x, y)}")   # Output: 50

# This block ensures the main() function is only executed when this file is run directly
if __name__ == '__main__':
    main()
