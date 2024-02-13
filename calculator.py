class Calculator:
    def __init__(self):
        # Initialize the calculator with result and values entered
        self.result = 0
        self.values_entered = 0

    def add(self, num):
        # Add the given number to the result
        self.result += num
        # Increment the values entered
        self.values_entered += 1

    def subtract(self, num):
        # Subtract the given number from the result
        self.result -= num
        # Increment the values entered
        self.values_entered += 1

    def multiply(self, num):
        # Multiply the result by the given number
        self.result *= num
        # Increment the values entered
        self.values_entered += 1

    def divide(self, num):
        # Check if the divisor is not zero to avoid division by zero
        if num != 0:
            # Divide the result by the given number
            self.result /= num
            # Increment the values entered
            self.values_entered += 1
        else:
            # Raise a ValueError if division by zero is attempted
            raise ValueError("Cannot divide by zero")

    def get_result(self):
        # Get the current result
        return self.result

    def get_values_entered(self):
        # Get the total values entered
        return self.values_entered
