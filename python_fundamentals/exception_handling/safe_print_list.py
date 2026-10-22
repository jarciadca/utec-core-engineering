#!/usr/bin/env python3
"""Impresion segura de lista utilizando try/except."""


def safe_print_list(my_list=[], x=0):
    """Imprime los primeros x elementos de una lista."""
    contador = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            contador += 1
    except IndexError:
        pass
    print()
    return contador
