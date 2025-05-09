import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
        self.assertEqual(self.calc.square_root(2), 1.4142135623730951)
        self.assertEqual(self.calc.square_root(0), 0)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(2, 0), 1)
        self.assertEqual(self.calc.power(2, -2), 0.25)

    def test_validate_input(self):
        calculator = Calculator()
        # Prueba caracteres válidos
        self.assertTrue(calculator.is_valid_input('123'))
        self.assertTrue(calculator.is_valid_input('123.456'))
        self.assertTrue(calculator.is_valid_input('123+456'))
        self.assertTrue(calculator.is_valid_input('123-456'))
        self.assertTrue(calculator.is_valid_input('123×456'))
        self.assertTrue(calculator.is_valid_input('123÷456'))
        
        # Prueba caracteres inválidos
        self.assertFalse(calculator.is_valid_input('abc'))
        self.assertFalse(calculator.is_valid_input('123abc'))
        self.assertFalse(calculator.is_valid_input('!@#'))

if __name__ == '__main__':
    unittest.main()