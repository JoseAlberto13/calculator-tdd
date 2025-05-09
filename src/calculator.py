class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square_root(self, a):
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return a ** 0.5

    def power(self, base, exponent):
        return base ** exponent
    
# Caracteres permitidos: 0123456789.+-×÷
    def is_valid_input(self, text):
        valid_chars = set('0123456789.+-×÷')
        return all(char in valid_chars for char in text)