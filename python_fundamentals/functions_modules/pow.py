#!/usr/bin/env python3
"""Módulo con la función pow que calcula a elevado a b sin **."""


def pow(a, b):
    """Devuelve a elevado a b (b entero) usando bucle, sin ** ni imports."""
    exp = b if b >= 0 else -b
    result = 1
    i = 0
    while i < exp:
        result = result * a
        i = i + 1
    if b < 0:
        result = 1 / result
    return result
