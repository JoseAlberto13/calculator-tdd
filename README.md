# Calculadora TDD

Este proyecto es una implementación de una calculadora usando la metodología Test-Driven Development (TDD). El proyecto demuestra cómo desarrollar software siguiendo el ciclo Red-Green-Refactor.

## 📝 Registro de Desarrollo

### Fase 1: Configuración Inicial y Primera Prueba
- Configuración del entorno de desarrollo con Python y unittest
- Implementación de la primera prueba para la suma
- Creación de la estructura básica del proyecto

### Fase 2: Implementación de Operaciones Básicas
- Desarrollo de las operaciones de suma y resta siguiendo TDD
- Refactorización del código para mejorar la estructura
- Implementación de multiplicación y división

### Fase 3: Interfaz Gráfica
- Desarrollo de la GUI usando tkinter
- Integración de la lógica de la calculadora con la interfaz
- Pruebas de integración

### Fase 4: Mejoras y Funcionalidades Avanzadas
- Implementación de operaciones avanzadas (raíz cuadrada, potencia al cuadrado)
- Validación de entrada para prevenir caracteres inválidos
- Soporte completo para entrada por teclado
- Implementación de atajos de teclado personalizados
- Diseño responsivo con grid layout
- Manejo robusto de errores en todas las operaciones

## 🚀 Características
- Operaciones básicas: suma, resta, multiplicación y división
- Interfaz gráfica intuitiva
- Desarrollado siguiendo principios TDD
- Manejo de errores robusto

## 🛠️ Tecnologías Utilizadas
- Python 3.x
- unittest para pruebas unitarias
- tkinter para la interfaz gráfica
- ttkbootstrap para dar un aspecto moderno y profesional

## 📸 Demostración
[Aquí agregar capturas de pantalla o GIFs de la calculadora en funcionamiento]

## 🔧 Instalación y Uso

1. Clonar el repositorio:
git clone [URL de tu repositorio]
2. Instalar dependencias:
pip install -r requirements.txt
3. Ejecutar la aplicación:
python src/gui.py

## 📁 Estructura del Proyecto

```plaintext
calculator-tdd/
├── src/
│   ├── calculator.py         # Lógica de la calculadora
│   ├── gui.py                # Interfaz gráfica usando tkintery ttkbootstrap
│   └── validator.py          # Verificación de expresiones matemáticas válidas
├── tests/
│   ├── test_calculator.py    # Pruebas unitarias con unittest
│   └── test_validator.py     # Pruebas unitarias con unittest
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto