#!/usr/bin/env python3
"""Escribir cadena en archivo de texto (UTF-8)."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo de texto (UTF-8)"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
