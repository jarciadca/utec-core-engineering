#!/usr/bin/env python3
"""Impresion segura de enteros utilizando try/except."""


def safe_print_integer(value):
    """Imprime un entero de manera segura."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
