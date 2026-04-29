#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fichero aleatorios.py para la Cuarta tarea de APA 2023.

Nombre y apellidos: Álvaro Ramo Irurre   # <-- ¡CAMBIA ESTO POR TU NOMBRE REAL!
"""

class Aleat:
    """
    Clase iterable que genera números aleatorios mediante LGC.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.semilla = x0
        self.inicial = x0

    def __next__(self):
        self.semilla = (self.a * self.semilla + self.c) % self.m
        return self.semilla

    def __call__(self, x0):
        self.semilla = x0
        self.inicial = x0


def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números aleatorios mediante LGC.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    semilla = x0
    while True:
        semilla = (a * semilla + c) % m
        nuevo = yield semilla
        if nuevo is not None:
            semilla = nuevo


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)