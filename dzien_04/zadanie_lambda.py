"""

Zaimplementuj funkcję przycinającą listę na podstawie podanego
warunku początkowego oraz końcowego:
Przykład użycia:
>>> przytnij(
    data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x > 3,
    stop=lambda x: x == 6,
    )
    [4, 5, 6]

"""
from typing import Callable


def przytnij(data: list, start: Callable, stop: Callable) -> list:
    result = []
    czy_dodawac = False
    for el in data:
        if start(el):
            czy_dodawac = True
        if stop(el):
            break
        if czy_dodawac:
            result.append(el)

    return result

print(przytnij(
    data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x % 2 == 0,
    stop=lambda x: x == 6,
    ))