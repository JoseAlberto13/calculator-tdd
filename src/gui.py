import tkinter as tk
from ttkbootstrap import Bootstyle, Style, ttk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self):
        self.calculator = Calculator()
        
        self.root = tk.Tk()
        self.style = Style(theme='darkly')
        self.root.title("Calculadora")
        
        # Hacer que la ventana sea responsiva
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
        # Configurar el estilo de los botones
        self.style.configure('Calculator.TButton',
                           font=('SF Pro Display', 16), # Tamaño de fuente
                           padding=15)
        self.style.configure('Operation.TButton',
                           background='#FF9F0A',
                           foreground='white',
                           font=('SF Pro Display', 18))  # Configuración específica para operaciones
        self.style.configure('Number.TButton',
                           background='#333333',
                           foreground='white',
                           font=('SF Pro Display', 12))  # Configuración específica para números
        
        # Display
        self.validate_cmd = self.root.register(self.validate_input)
        self.display = ttk.Entry(self.root,
                               font=('SF Pro Display', 36),
                               justify='right',
                               bootstyle="dark",
                               state='readonly')  # Cambiar a readonly
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew',
                         padx=5, pady=5, ipady=10)
        
        # Definir botones con sus estilos
        buttons = [
            ('C', 1, 0, 'Operation'), ('√', 1, 1, 'Operation'), ('x²', 1, 2, 'Operation'), ('÷', 1, 3, 'Operation'),
            ('7', 2, 0, 'Number'), ('8', 2, 1, 'Number'), ('9', 2, 2, 'Number'), ('×', 2, 3, 'Operation'),
            ('4', 3, 0, 'Number'), ('5', 3, 1, 'Number'), ('6', 3, 2, 'Number'), ('-', 3, 3, 'Operation'),
            ('1', 4, 0, 'Number'), ('2', 4, 1, 'Number'), ('3', 4, 2, 'Number'), ('+', 4, 3, 'Operation'),
            ('0', 5, 0, 'Number', 2), ('.', 5, 2, 'Number'), ('=', 5, 3, 'Operation')
        ]
        
        # Crear botones
        for button in buttons:
            if len(button) == 5:  # Botón especial (0) que ocupa 2 columnas
                text, row, col, style, colspan = button
                btn = ttk.Button(self.root, text=text,
                               style=f'{style}.TButton',
                               command=lambda x=text: self.click(x))
                btn.grid(row=row, column=col, columnspan=colspan,
                        sticky='nsew', padx=2, pady=2)
            else:
                text, row, col, style = button
                btn = ttk.Button(self.root, text=text,
                               style=f'{style}.TButton',
                               command=lambda x=text: self.click(x))
                btn.grid(row=row, column=col, sticky='nsew',
                        padx=2, pady=2)
        
        # Agregar binding para eventos del teclado
        self.root.bind('<Key>', self.handle_keypress)
        self.root.bind('<Return>', lambda e: self.click('='))
        self.root.bind('<BackSpace>', lambda e: self.handle_backspace())
        self.root.bind('<Escape>', lambda e: self.clear())
        
        # Mapeo de teclas especiales
        self.key_mapping = {
            'plus': '+',
            'minus': '-',
            'asterisk': '×',
            'slash': '÷',
            'period': '.',
            'Return': '=',
        }

    def click(self, key):
        # Habilitar temporalmente el display para escritura
        self.display.configure(state='normal')
        
        if key == 'C':
            self.clear()
        elif key == '=':
            try:
                expression = self.display.get()
                expression = expression.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == '√':
            try:
                value = float(self.display.get())
                result = self.calculator.square_root(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'x²':
            try:
                value = float(self.display.get())
                result = self.calculator.power(value, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)
        
        # Volver a poner el display en modo readonly
        self.display.configure(state='readonly')

    def clear(self):
        # Habilitar temporalmente el display para limpiarlo
        self.display.configure(state='normal')
        self.display.delete(0, tk.END)
        # Volver a poner el display en modo readonly
        self.display.configure(state='readonly')

    def handle_backspace(self):
        # Habilitar temporalmente el display para borrar
        self.display.configure(state='normal')
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current[:-1])
        # Volver a poner el display en modo readonly
        self.display.configure(state='readonly')

    def run(self):
        # Establecer un tamaño mínimo para la ventana
        self.root.minsize(220, 300)
        # Establecer tamaño inicial
        self.root.geometry("280x400")
        self.root.mainloop()

    def validate_input(self, new_text):
        # Permitir que el campo esté vacío
        if not new_text:
            return True
        return self.calculator.is_valid_input(new_text)

    def handle_keypress(self, event):
        key = event.keysym.lower()
        # Manejar números
        if key.isdigit():
            self.click(key)
        # Manejar operadores y teclas especiales
        elif key in self.key_mapping:
            self.click(self.key_mapping[key])
        # Manejar teclas especiales para raíz y potencia
        elif key == 'r':
            self.click('√')
        elif key == 'p':
            self.click('x²')

if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()