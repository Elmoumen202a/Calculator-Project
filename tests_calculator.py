import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Calculator class for each test
        self.calc = Calculator()

    def test_addition(self):
        # Test addition operation
        self.calc.add(5)
        self.assertEqual(self.calc.get_result(), 5)
        self.assertEqual(self.calc.get_values_entered(), 1)

    def test_subtraction(self):
        # Test subtraction operation
        self.calc.subtract(3)
        self.assertEqual(self.calc.get_result(), -3)
        self.assertEqual(self.calc.get_values_entered(), 1)

    def test_multiplication(self):
        # Test multiplication operation
        self.calc.multiply(4)
        self.assertEqual(self.calc.get_result(), 0)  # Initial result is 0
        self.assertEqual(self.calc.get_values_entered(), 1)

    def test_division(self):
        # Test division operation
        self.calc.add(8)
        self.calc.divide(2)
        self.assertEqual(self.calc.get_result(), 4)
        self.assertEqual(self.calc.get_values_entered(), 2)

        with self.assertRaises(ValueError):
            # Test division by zero raises a ValueError
            self.calc.divide(0)

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
