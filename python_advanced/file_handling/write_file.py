#!/usr/bin/env python3
"""Escribir cadena en archivo de texto (UTF-8)."""


def write_file(filename="", text=""):
    """
    Escribe una cadena en un archivo de texto (UTF-8).

    Crea el archivo si no existe y sobrescribe su contenido si ya
    existe. Devuelve el número de caracteres escritos.

    Args:
        filename (str): Ruta del archivo a escribir. Por defecto "".
        text (str): Cadena de texto a escribir. Por defecto "".

    Returns:
        int: Número de caracteres escritos.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    write_file()