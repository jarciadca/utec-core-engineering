#!/usr/bin/env python3
"""Module for the BaseGeometry class."""


class BaseGeometry:
    """Clase base para la geometría"""

    def area(self):
        """Calcula el área de la figura geométrica"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero positivo"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
