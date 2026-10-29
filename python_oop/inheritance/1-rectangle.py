#!/usr/bin/env python3
"""Module for the BaseGeometry class."""
BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo"""

    def __init__(self, width, height):
        """Inicializa un rectángulo"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
