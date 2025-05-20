
class InputValidator:
    def __init__(self):
        # Caracteres válidos para operaciones matemáticas
        self.valid_chars = set("0123456789.+-×÷*/()√")
        # Operadores matemáticos
        self.operators = set("+-×÷*/")
    
    def is_valid_input(self, text):
        """
        Verifica si el texto proporcionado tiene caracteres válidos para operaciones matemáticas.
        Args:
            text (str): El texto a validar 
        Returns:
            bool: True si el texto contiene solo caracteres válidos, False en caso contrario
        """
        # Verificar que solo contiene caracteres válidos
        return all(char in self.valid_chars for char in text)
    
    def validate_expression(self, expression):
        """
        Valida si una expresión matemática es válida antes de evaluarla.
        Verifica problemas comunes como divisiones por cero o formatos incorrectos.
        Args:
            expression (str): La expresión matemática a validar
        Returns:
            tuple: (bool, str) - (es_válido, mensaje_error)
        """
        # Verificar si hay operadores consecutivos (no permitidos)
        for i in range(len(expression) - 1):
            if expression[i] in self.operators and expression[i + 1] in self.operators:
                return False, "Operadores consecutivos no permitidos"
        
        # Verificar división por cero
        if "/0" in expression or "÷0" in expression:
            return False, "División por cero no permitida"
        
        # Verificar paréntesis balanceados
        if not self._check_balanced_parentheses(expression):
            return False, "Paréntesis no balanceados"
        
        # Verificar que no termina con un operador
        if expression and expression[-1] in self.operators:
            return False, "La expresión no puede terminar con un operador"
        
        # Verificar punto decimal repetido en un número
        numbers = ''.join([c if c.isdigit() or c == '.' else ' ' for c in expression]).split()
        for num in numbers:
            if num.count('.') > 1:
                return False, "Formato de número inválido"
        
        return True, ""
    
    def _check_balanced_parentheses(self, expression):
        """
        Verifica si los paréntesis en una expresión están correctamente balanceados.
        Args:
            expression (str): La expresión a verificar
        Returns:
            bool: True si los paréntesis están balanceados, False en caso contrario
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        
        return len(stack) == 0
    
    def format_result(self, result):
        """
        Formatea el resultado para mostrar en la calculadora.
        Elimina decimales innecesarios (.0) si el resultado es un entero.  
        Args:
            result (float): El resultado a formatear
        Returns:
            str: El resultado formateado como string
        """
        # Si el resultado es un entero, mostrar sin parte decimal
        if isinstance(result, (int, float)) and result == int(result):
            return str(int(result))
        return str(result)