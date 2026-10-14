# Python Fundamentals - Core Data Structures

## 📌 Descripción

Repositorio con ejercicios y ejemplos sobre **estructuras de datos fundamentales** en Python: listas, tuplas, diccionarios y conjuntos. Cada archivo contiene una función o conjunto de funciones que ilustran su uso correcto y las buenas prácticas asociadas.

## 🎯 Objetivos

- Comprender las estructuras de datos básicas de Python
- Diferenciar entre tipos mutables e inmutables
- Aplicar métodos y operaciones propias de cada estructura
- Escribir código limpio y conforme a PEP 8
- Reutilizar funciones mediante módulos

## 📚 Contenido

### 1. Listas (`list`)
- Creación, indexación y slicing
- Métodos: `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`
- Comprensiones de listas
- Listas anidadas

### 2. Tuplas (`tuple`)
- Inmutabilidad
- Desempaquetado
- Uso como claves de diccionario (hashables)

### 3. Diccionarios (`dict`)
- Pares clave-valor
- Métodos: `keys`, `values`, `items`, `get`, `update`, `pop`
- Comprensiones de diccionarios
- Orden de inserción (Python 3.7+)

### 4. Conjuntos (`set`)
- Elementos únicos y no ordenados
- Operaciones: unión, intersección, diferencia
- `frozenset` (inmutable)

### 5. Funciones y modularidad
- Definición de funciones con `def`
- Argumentos por defecto, `*args`, `**kwargs`
- Importación de módulos propios
- Bloque `if __name__ == "__main__"`

## 💡 Ejemplos

### Imprimir una lista de enteros

```python
def print_list_integer(my_list=[]):
    """Imprime todos los enteros de una lista, uno por línea."""
    for number in my_list:
        print("{:d}".format(number))
```

### Eliminar duplicados conservando el orden

```python
names = ["Ana", "Luis", "Ana", "Marta"]
unique_in_order = list(dict.fromkeys(names))
print(unique_in_order)  # ['Ana', 'Luis', 'Marta']
```

### Comprensión de diccionario

```python
lengths = {name: len(name) for name in ["Ada", "Grace"]}
print(lengths)  # {'Ada': 3, 'Grace': 5}
```

## 🛠️ Requisitos

- Python 3.8 o superior
- Editor de código (VS Code, PyCharm, etc.)
- `pycodestyle` para verificar el estilo:
  ```bash
  pip install pycodestyle
  ```

## 🚀 Cómo usar este repositorio

```bash
git clone <url-del-repositorio>
cd python_fundamentals/core_data_structures
python print_list_integer.py
```

## 🧪 Ejercicios propuestos

1. Escribir una función que imprima todos los enteros de una lista.
2. Eliminar duplicados de una lista conservando el orden original.
3. Contar la frecuencia de palabras en una cadena usando un diccionario.
4. Encontrar la intersección de dos conjuntos.
5. Convertir una lista en tupla y viceversa.

## 🧠 Conceptos clave

| Estructura | ¿Mutable? | ¿Ordenada? | ¿Hashable? |
|------------|-----------|------------|------------|
| `list`     | ✅ Sí     | ✅ Sí      | ❌ No      |
| `tuple`    | ❌ No     | ✅ Sí      | ✅ Sí*     |
| `dict`     | ✅ Sí     | ✅ Sí      | ❌ No      |
| `set`      | ✅ Sí     | ❌ No      | ❌ No      |
| `frozenset`| ❌ No     | ❌ No      | ✅ Sí      |

\* Una tupla es hashable solo si todos sus elementos también lo son.

## ⚠️ Buenas prácticas

- No uses listas mutables como argumentos por defecto.
- Usa `dict.fromkeys()` para eliminar duplicados conservando el orden.
- Verifica el estilo con `pycodestyle archivo.py`.
- Mantén el código bajo 79 caracteres por línea.
- Usa docstrings para documentar funciones y módulos.

## 📖 Recursos recomendados

- [Documentación oficial de Python – Estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html)
- [PEP 8 – Guía de estilo](https://peps.python.org/pep-0008/)
- [Real Python – Data Structures](https://realpython.com/python-data-structures/)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Abre un *issue* o envía un *pull request* con mejoras, ejemplos o correcciones.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

✍️ **Autor:** [Tu nombre]
📅 **Última actualización:** [Fecha]
