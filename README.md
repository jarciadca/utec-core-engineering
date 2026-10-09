# Python Fundamentals — Hello World

Módulo introductorio de fundamentos de Python: modos de ejecución del
intérprete, scripts ejecutables y salida determinista.

## 📋 Descripción

Este directorio contiene el script `structured_output.py`, que demuestra:

- Uso del shebang `#!/usr/bin/env python3` para scripts portables.
- Interpolación de cadenas con **f-strings**.
- Formateo numérico a dos decimales (`.2f`).
- Evaluación de expresiones booleanas por comparación.
- Salida determinista y reproducible (sin entrada del usuario).

## 📂 Estructura

```
hello_world/
├── README.md
├── structured_output.py
└── test_structured_output.py
```

## 🚀 Uso

### Requisitos

- Python 3.8.x (versión de corrección)
- Ubuntu 20.04 LTS
- `pycodestyle` 2.7.x

### Ejecución

```bash
chmod +x structured_output.py
./structured_output.py
```

### Verificación de estilo (PEP8)

```bash
pip install pycodestyle==2.7.0
pycodestyle structured_output.py
