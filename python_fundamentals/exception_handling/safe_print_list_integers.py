#!/usr/bin/env python3
"""Impresion segura de enteros de una lista utilizando try/except."""


def safe_print_list_integers(my_list=[], x=0):
    """Imprime los primeros x enteros de una lista"""

    contador = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            contador += 1
        except (ValueError, TypeError):
            continue

    print()
    return contador
