import unittest
from src.validator import InputValidator

class TestInputValidator(unittest.TestCase):
    def setUp(self):
        self.validator = InputValidator()
    
    # Pruebas para is_valid_input
    def test_valid_numeric_input(self):
        self.assertTrue(self.validator.is_valid_input("123.45"))
    
    def test_valid_operation_input(self):
        self.assertTrue(self.validator.is_valid_input("123+456"))
    
    def test_valid_complex_input(self):
        self.assertTrue(self.validator.is_valid_input("123.45×(67.8÷9.0)-√4"))
    
    def test_invalid_input_with_letters(self):
        self.assertFalse(self.validator.is_valid_input("123abc"))
    
    def test_invalid_input_with_special_chars(self):
        self.assertFalse(self.validator.is_valid_input("123$%^"))
    
    # Pruebas para validate_expression
    def test_valid_expression(self):
        is_valid, _ = self.validator.validate_expression("123+456")
        self.assertTrue(is_valid)
    
    def test_consecutive_operators(self):
        is_valid, error_msg = self.validator.validate_expression("123++456")
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "Operadores consecutivos no permitidos")
    
    def test_division_by_zero(self):
        is_valid, error_msg = self.validator.validate_expression("123/0")
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "División por cero no permitida")
    
    def test_division_by_zero_with_symbol(self):
        is_valid, error_msg = self.validator.validate_expression("123÷0")
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "División por cero no permitida")
    
    def test_unbalanced_parentheses(self):
        is_valid, error_msg = self.validator.validate_expression("123+(456")
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "Paréntesis no balanceados")
    
    def test_ending_with_operator(self):
        is_valid, error_msg = self.validator.validate_expression("123+")
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "La expresión no puede terminar con un operador")
    
    def test_multiple_decimal_points(self):
        is_valid, error_msg = self.validator.validate_expression("123.45.6+7")
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "Formato de número inválido")
    
    # Pruebas para _check_balanced_parentheses
    def test_balanced_parentheses(self):
        self.assertTrue(self.validator._check_balanced_parentheses("(123+456)"))
    
    def test_nested_balanced_parentheses(self):
        self.assertTrue(self.validator._check_balanced_parentheses("((123)+(456))"))
    
    def test_unbalanced_open_parenthesis(self):
        self.assertFalse(self.validator._check_balanced_parentheses("(123+456"))
    
    def test_unbalanced_close_parenthesis(self):
        self.assertFalse(self.validator._check_balanced_parentheses("123+456)"))
    
    # Pruebas para format_result
    def test_format_integer_result(self):
        self.assertEqual(self.validator.format_result(123.0), "123")
    
    def test_format_float_result(self):
        self.assertEqual(self.validator.format_result(123.45), "123.45")
    
    def test_format_integer_result_from_int(self):
        self.assertEqual(self.validator.format_result(123), "123")
    
    # Pruebas adicionales para validar caracteres específicos
    def test_valid_square_root_symbol(self):
        self.assertTrue(self.validator.is_valid_input("√25"))
    
    def test_valid_parentheses(self):
        self.assertTrue(self.validator.is_valid_input("(123+456)"))
    
    def test_valid_decimal_point(self):
        self.assertTrue(self.validator.is_valid_input("123.456"))
    
    def test_valid_negative_number(self):
        self.assertTrue(self.validator.is_valid_input("-123"))
    
    def test_valid_complex_expression(self):
        self.assertTrue(self.validator.is_valid_input("-(123+456)×√2÷3.14"))

if __name__ == "__main__":
    unittest.main()