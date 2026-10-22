#!/usr/bin/env python3
"""Lanzamiento de excepcion NameError con un mensaje personalizado."""


def raise_exception_msg(message=""):
    """Lanza una excepcion NameError con un mensaje personalizado."""
    raise NameError(message)
