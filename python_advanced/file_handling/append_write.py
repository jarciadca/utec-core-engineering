#!/usr/bin/env python3
"""Módulo para añadir texto al final de archivos."""


def append_write(filename="", text=""):
    """Añade una cadena al final de un archivo de texto (UTF-8)"""

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
