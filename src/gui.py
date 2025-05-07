import tkinter as tk
from ttkbootstrap import Style, ttk
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
                           font=('SF Pro Display', 14),
                           padding=10)
        self.style.configure('Operation.TButton',
                           background='#FF9F0A',
                           foreground='white')
        self.style.configure('Number.TButton',
                           background='#333333',
                           foreground='white')
        
        # Display
        self.display = ttk.Entry(self.root,
                               font=('SF Pro Display', 36),
                               justify='right')
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

    def click(self, key):
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

    def clear(self):
        self.display.delete(0, tk.END)

    def run(self):
        # Establecer un tamaño mínimo para la ventana
        self.root.minsize(300, 400)
        self.root.mainloop()

if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()