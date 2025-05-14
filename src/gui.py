import tkinter as tk
from ttkbootstrap import Bootstyle, Style, ttk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self):
        self.calculator = Calculator()
        self.history = []
        self.history_visible = False
        self.dark_mode = True
        
        self.root = tk.Tk()
        self.style = Style(theme='darkly')
        self.root.title("Calculadora")
        
        # Crear frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky='nsew')
        
        # Configuración inicial del grid del root
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Hacer que la ventana sea responsiva (en main_frame)
        for i in range(7):  # Cambiado a 7 para incluir la fila del botón de historial
            self.main_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.main_frame.grid_columnconfigure(i, weight=1)

        # Inicialización del historial
        self._init_history_components()
        
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
        
        # Display (ahora en main_frame)
        self.validate_cmd = self.root.register(self.validate_input)
        # Display con tamaño ajustado
        self.display = ttk.Entry(self.main_frame,
                               font=('SF Pro Display', 36),
                               justify='right',
                               bootstyle="dark",
                               width=12,  # Ancho fijo para mejor visualización
                               state='readonly')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew',
                         padx=5, pady=5, ipady=10)

        # Definir botones con sus estilos
        buttons = [
            ('C', 1, 0, 'Operation'), ('√', 1, 1, 'Operation'), ('x²', 1, 2, 'Operation'), ('÷', 1, 3, 'Operation'),
            ('7', 2, 0, 'Number'), ('8', 2, 1, 'Number'), ('9', 2, 2, 'Number'), ('×', 2, 3, 'Operation'),
            ('4', 3, 0, 'Number'), ('5', 3, 1, 'Number'), ('6', 3, 2, 'Number'), ('-', 3, 3, 'Operation'),
            ('1', 4, 0, 'Number'), ('2', 4, 1, 'Number'), ('3', 4, 2, 'Number'), ('+', 4, 3, 'Operation'),
            ('0', 5, 0, 'Number', 2), ('.', 5, 2, 'Number'), ('=', 5, 3, 'Operation'),
            ('Historial', 6, 0, 'Operation', 2), ('🌙', 6, 2, 'Operation', 2)
        ]

        # Los botones ahora se crean en main_frame en lugar de root
        for button in buttons:
            if len(button) == 5:
                text, row, col, style, colspan = button
                btn = ttk.Button(self.main_frame, text=text,
                               style=f'{style}.TButton',
                               command=lambda x=text: self.click(x))
                btn.grid(row=row, column=col, columnspan=colspan,
                        sticky='nsew', padx=2, pady=2)
            else:
                text, row, col, style = button
                btn = ttk.Button(self.main_frame, text=text,
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

    def _init_history_components(self):
        """Inicializa los componentes relacionados con el historial"""
        # Crear frame del historial
        self.history_frame = ttk.Frame(self.root)
        
        # Configurar lista del historial con tamaño ajustado
        self.history_list = tk.Listbox(
            self.history_frame,
            font=('SF Pro Display', 12),
            bg='#2d2d2d',
            fg='white',
            selectmode='single',
            width=20  # Ancho fijo para el historial
        )
        self.history_list.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.history_list.bind('<Double-Button-1>', self.use_history_item)
        
        # Botón para limpiar historial
        self.clear_history_btn = ttk.Button(
            self.history_frame,
            text="Limpiar Historial",
            command=self.clear_history
        )
        self.clear_history_btn.grid(row=1, column=0, pady=5, padx=5)
        
        # Configurar grid weights
        self.history_frame.grid_columnconfigure(0, weight=1)
        self.history_frame.grid_rowconfigure(0, weight=1)
        
        # Botón para mostrar/ocultar historial
        self.toggle_history_btn = ttk.Button(
            self.main_frame,
            text="Mostrar Historial",
            command=self.toggle_history
        )
        self.toggle_history_btn.grid(row=6, column=0, columnspan=4, pady=5, padx=5)

    def toggle_history(self):
        """Alterna la visibilidad del panel de historial"""
        if self.history_visible:
            self._hide_history()
        else:
            self._show_history()
    
    def _hide_history(self):
        """Oculta el panel de historial"""
        self.history_frame.grid_remove()
        self.root.grid_columnconfigure(1, weight=0)
        self.toggle_history_btn.configure(text="Mostrar Historial")
        self.history_visible = False
    
    def _show_history(self):
        """Muestra el panel de historial"""
        self.history_frame.grid(row=0, column=1, sticky='nsew')
        self.root.grid_columnconfigure(1, weight=1)
        self.toggle_history_btn.configure(text="Ocultar Historial")
        self.history_visible = True
    
    def add_to_history(self, expression, result):
        """Agrega una operación al historial"""
        history_item = f"{expression} = {result}"
        self.history.append(history_item)
        self.history_list.insert(0, history_item)  # Agregar al inicio de la lista
    
    def use_history_item(self, event):
        """Utiliza un elemento seleccionado del historial"""
        selection = self.history_list.curselection()
        if selection:
            item = self.history_list.get(selection[0])
            result = item.split('=')[1].strip()
            self._update_display(result)
    
    def clear_history(self):
        """Limpia todo el historial de operaciones"""
        self.history = []
        self.history_list.delete(0, tk.END)
    
    def _update_display(self, value):
        """Actualiza el valor mostrado en el display"""
        self.display.configure(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, value)
        self.display.configure(state='readonly')

    def toggle_theme(self):
        """Cambia entre tema oscuro y claro"""
        self.dark_mode = not self.dark_mode
        new_theme = 'darkly' if self.dark_mode else 'litera'
        self.style.theme_use(new_theme)
        
        # Actualizar el ícono del botón
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, ttk.Button) and widget['text'] in ['🌙', '☀️']:
                widget['text'] = '☀️' if self.dark_mode else '🌙'
        
        # Actualizar colores del historial y mantener fuentes consistentes
        if hasattr(self, 'history_list'):
            self.history_list.configure(
                bg='#2d2d2d' if self.dark_mode else '#f5f5f5',  # Gris muy claro para el modo claro
                fg='white' if self.dark_mode else '#333333',     # Gris oscuro para el texto
                font=('SF Pro Display', 12)
            )
            
        # Reconfigurar estilos de botones para mantener consistencia
        self.style.configure('Calculator.TButton',
                           font=('SF Pro Display', 16),
                           padding=15)
        
        # Botones de operaciones con naranja suave en modo claro
        self.style.configure('Operation.TButton',
                           background='#FF9F0A' if self.dark_mode else '#FF9F0A',
                           foreground='white' if self.dark_mode else 'white',
                           font=('SF Pro Display', 18))
        
        # Botones numéricos con gris muy suave en modo claro
        self.style.configure('Number.TButton',
                           background='#333333' if self.dark_mode else '#303030',
                           foreground='white' if self.dark_mode else 'white',
                           font=('SF Pro Display', 18))
        
        # Actualizar el estilo del display
        self.display.configure(
            font=('SF Pro Display', 36),
            bootstyle="dark" if self.dark_mode else "light"
        )

    def click(self, key):
        self.display.configure(state='normal')
        
        if key == 'C':
            self.clear()
        elif key == '=':
            try:
                expression = self.display.get()
                expression_original = expression
                expression = expression.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                # Agregar al historial
                self.add_to_history(expression_original, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == '√':
            try:
                value = float(self.display.get())
                result = self.calculator.square_root(value)
                expression = f"√({value})"
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.add_to_history(expression, result)
            except ValueError as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif key == 'x²':
            try:
                value = float(self.display.get())
                result = self.calculator.power(value, 2)
                expression = f"{value}²"
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.add_to_history(expression, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'Historial':
            self.toggle_history()
        elif key in ['🌙', '☀️']:  # Manejar el cambio de tema
            self.toggle_theme()
        else:
            self.display.insert(tk.END, key)
        
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
        # Establecer un tamaño mínimo más apropiado para la ventana
        self.root.minsize(320, 480)  # Tamaño mínimo ajustado
        # Establecer tamaño inicial más apropiado
        self.root.geometry("320x520")  # Tamaño inicial ajustado
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