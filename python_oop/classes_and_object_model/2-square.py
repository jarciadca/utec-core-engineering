#!/usr/bin/env python3
"""Definiendo la clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0):
        """Inicializa un cuadrado"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
