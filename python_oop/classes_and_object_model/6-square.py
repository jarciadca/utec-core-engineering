#!/usr/bin/env python3
"""Definiendo la clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado"""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Obtiene la posición del cuadrado"""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición del cuadrado"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcula el área del cuadrado"""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el caracter # y la posicion"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Devuelve una representación en cadena del cuadrado"""
        if self.__size == 0:
            return ""
        lines = []
        for _ in range(self.__position[1]):
            lines.append("")
        for _ in range(self.__size):
            lines.append(
                " " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
