#!/usr/bin/env python3
"""Módulo con la función uppercase para convertir a mayúsculas vía ASCII."""


def uppercase(str):
    """Imprime la cadena en mayúsculas seguida de una nueva línea."""
    result = ""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += c
    print(result)
