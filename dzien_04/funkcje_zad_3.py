"""
Napisz funkcję obliczającą liczbę znaków w zadanym napisie
pomiędzy zadanymi znakami. Znaki, pomiędzy którymi ma odbywać
się zliczanie, powinny być argumentami z wartościami domyślnymi -
odpowiednio < i >. Nawiasy mogę być zagnieżdżone i mogą
wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami
liczone są zgodnie z poziomem zagnieżdżenia.
Przykład użycia:

>>> policz_znaki('ala ma <kota> a kot ma ale')
4

>>> policz_znaki('ala ma <kota> a <kot> ma ale')
7

>>> policz_znaki('ala ma [kota] a [kot] ma ale', "[", "]")
7

>>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
18

>>> policz_znaki('ala [kota [a kot]] ma [ale]', start='[', end=']')
18

>>> policz_znaki('a <a<a<a>>>')
6

"""


def policz_znaki(napis: str, start: str = "<", end: str = ">") -> int:
    licznik = 0
    czy_zliczac = False
    poziom = 0
    # 'ala ma <kota> a kot ma ale'
    for znak in napis:
        if znak == start:
            czy_zliczac = True
            poziom += 1
            continue
        elif znak == end:
            czy_zliczac = False
            poziom -= 1

        if czy_zliczac:
            licznik += poziom

    return licznik
