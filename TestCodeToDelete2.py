class Calculator:
    def add(self, a, b):
        # Performing a simple addition operation
        result = a + b
        return result

    def multiply(self, a, b):
        # Performing a simple multiplication operation
        result = a * b
        return result

def main():
    # Using the Calculator class to perform operations
    calculator = Calculator()

    # Adding two numbers
    sum_result = calculator.add(5, 3)
    print(f"Sum: {sum_result}")

    # Multiplying two numbers
    product_result = calculator.multiply(4, 7)
    print(f"Product: {product_result}")

if __name__ == "__main__":
    main()