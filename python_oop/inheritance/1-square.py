#!/usr/bin/env python3
"""Module for the Square class."""
Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Representa un cuadrado"""

    def __init__(self, size):
        """Inicializa un cuadrado"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calcula el área del cuadrado"""
        return self.__size ** 2
