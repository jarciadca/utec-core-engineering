# Python - Funciones y Modularidad

## 📌 Descripción

Este documento/repositorio contiene apuntes, ejemplos y ejercicios sobre **funciones** y **modularidad** en Python, dos conceptos fundamentales para escribir código limpio, reutilizable y mantenible.

## 🎯 Objetivos

- Comprender qué es una función y por qué usarla
- Aprender a definir y llamar funciones en Python
- Conocer los diferentes tipos de argumentos
- Entender el concepto de modularidad
- Crear y utilizar módulos y paquetes propios
- Aplicar buenas prácticas de organización de código

## 📚 Contenido

### 1. Funciones

- ¿Qué es una función?
- Definición con `def`
- Parámetros y argumentos
- Valores de retorno (`return`)
- Argumentos por posición y por nombre
- Argumentos con valores por defecto
- `*args` y `**kwargs`
- Funciones lambda (anónimas)
- Ámbito (scope) de las variables
- Docstrings y documentación

### 2. Modularidad

- ¿Qué es un módulo?
- Importar módulos (`import`, `from ... import`)
- Crear módulos propios
- El bloque `if __name__ == "__main__"`
- Paquetes y `__init__.py`
- Módulos de la biblioteca estándar
- Organización de proyectos

## 💡 Ejemplos

### Función básica

```python
def saludar(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}!"

print(saludar("Ana"))
```

### Argumentos por defecto y `*args`

```python
def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3, 4))  # 10
```

### Módulo propio

**`matematicas.py`**
```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

**`main.py`**
```python
import matematicas

print(matematicas.sumar(5, 3))  # 8
```

## 🛠️ Requisitos

- Python 3.8 o superior
- Editor de código (VS Code, PyCharm, etc.)

## 🚀 Cómo usar este repositorio

```bash
git clone <url-del-repositorio>
cd python-funciones-modularidad
python ejemplos/funciones_basicas.py
```

## 🧪 Ejercicios propuestos

1. Crear una función que calcule el factorial de un número.
2. Escribir una función con `*args` que devuelva el mayor de una lista de números.
3. Crear un módulo `utilidades.py` con funciones de conversión de unidades.
4. Usar `if __name__ == "__main__"` para probar un módulo.
5. Convertir un script largo en varios módulos organizados.

## 📖 Recursos recomendados

- [Documentación oficial de Python – Funciones](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions)
- [Documentación oficial de Python – Módulos](https://docs.python.org/es/3/tutorial/modules.html)
- PEP 8 – Guía de estilo para código Python

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o quieres añadir ejemplos, abre un *issue* o envía un *pull request*.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

✍️ **Autor:** [Tu nombre]  
📅 **Última actualización:** [Fecha]
