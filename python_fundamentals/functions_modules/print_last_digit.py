#!/usr/bin/env python3
"""Módulo con la función print_last_digit."""


def print_last_digit(number):
    """Imprime y devuelve el último dígito (positivo) de number."""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
