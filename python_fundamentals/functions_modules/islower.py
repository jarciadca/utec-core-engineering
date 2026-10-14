#!/usr/bin/env python3
"""Detectar letras minúsculas ASCII."""


def islower(c):
    """True si c es una letra minúscula ASCII, False en contrario."""
    return ord('a') <= ord(c) <= ord('z')
