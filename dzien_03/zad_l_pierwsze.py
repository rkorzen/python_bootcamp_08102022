"""
Zdefiniuj funkcję która sprawdzi czy dana liczba jest liczbą pierwszą

"""

def czy_pierwsza(arg: int) -> bool:
    for dzielnik in range(2, arg):
        if arg % dzielnik == 0:
            return False
    return True


assert czy_pierwsza(10) is False
assert czy_pierwsza(2) is True
assert czy_pierwsza(3) is True
assert czy_pierwsza(4) is False
assert 3 % 2 == 1
