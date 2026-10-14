#!/usr/bin/env python3
"""Importa add desde add_0 y muestra la suma 1 + 2."""

from add_0 import add


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
