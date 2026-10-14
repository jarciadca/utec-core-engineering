#!/usr/bin/env python3
"""Detectar letras minúsculas ASCII."""

def islower(c):
    """Devuelve True si c es una letra minúscula ASCII, False en caso contrario."""
    return ord('a') <= ord(c) <= ord('z')
