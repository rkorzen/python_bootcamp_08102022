class Odcinek:
    def __init__(self, x):
        self._x = x  # konwencja

    @property
    def x(self):
        return self._x

    @x.getter
    def x(self):
        return "figa z makiem"

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError
        self._x = value

    def wazne_obliczenie(self):
        """ta funkcja jest publiczna"""

    def _wazne_obliczenia(self):
        print("tu robie magie")



o = Odcinek(10)

# print(o.__x)  # tak się nie powinno robic

o.x = 15   # konswekcja i ryzyko

# rozwiazanie zgodne z konwencja

print(o.x)
print(dir(o))

print(o._x)