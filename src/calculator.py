import math
from validator import InputValidator

class Calculator:
    def __init__(self):
        self.validator = InputValidator()
        
    def add(self, a, b):
        """Suma dos números"""
        return a + b
        
    def subtract(self, a, b):
        """Resta dos números"""
        return a - b
        
    def multiply(self, a, b):
        """Multiplica dos números"""
        return a * b
        
    def divide(self, a, b):
        """Divide dos números"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
        
    def square_root(self, a):
        """Calcula la raíz cuadrada de un número"""
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(a)
        
    def power(self, base, exponent):
        """Calcula la potencia de un número"""
        return base ** exponent
    
    def is_valid_input(self, text):
        """
        Verifica si el texto proporcionado contiene caracteres válidos para operaciones
        
        Args:
            text (str): El texto a validar
            
        Returns:
            bool: True si el texto contiene solo caracteres válidos, False en caso contrario
        """
        return self.validator.is_valid_input(text)
    
    def validate_expression(self, expression):
        """
        Valida si una expresión matemática es correcta
        
        Args:
            expression (str): La expresión a validar
            
        Returns:
            tuple: (es_válido, mensaje_error)
        """
        return self.validator.validate_expression(expression)
    
    def evaluate(self, expression):
        """
        Evalúa una expresión matemática
        
        Args:
            expression (str): La expresión a evaluar
            
        Returns:
            float: El resultado de la expresión
            
        Raises:
            ValueError: Si la expresión es inválida
        """
        # Reemplazar símbolos multiplicación y división por los operadores de Python
        expression = expression.replace('×', '*').replace('÷', '/')
        
        # Validar la expresión
        is_valid, error_msg = self.validator.validate_expression(expression)
        if not is_valid:
            raise ValueError(error_msg)
        
        # Evaluar la expresión
        try:
            result = eval(expression)
            return self.validator.format_result(result)
        except Exception as e:
            raise ValueError(f"Error al evaluar la expresión: {str(e)}")