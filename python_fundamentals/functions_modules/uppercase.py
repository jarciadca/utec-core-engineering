#!/usr/bin/env python3
"""Módulo con la función uppercase para convertir a mayúsculas vía ASCII."""


def uppercase(text):
    """Imprime la cadena en mayúsculas seguida de una nueva línea."""
    result = ""
    for c in text:
        code = ord(c)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += c
    print("{}".format(result))
