"""
Napisz funkcję zwracającą zbiór wszystkich znaków występujących w
napisie więcej niż zadana liczba razy.

Przykład użycia:

>>> wiecej_niz('ala ma kota a kot ma ale', 3)
{' ', 'a'}

>>> wiecej_niz('', 3)
set()


assert wiecej_niz('', 3 ) == set()

>>> wiecej_niz('aaa', 3)
set()

>>> wiecej_niz('aaa', 0)
{'a'}

>>> wiecej_niz('bbb', 2)
{'b'}

>>> wiecej_niz('aaaa', 3)
{'a'}


"""

def wiecej_niz(napis: str, prog: int) -> set:
    wynik = set()
    for znak in set(napis):
        if napis.count(znak) > prog:
            wynik.add(znak)
    return wynik