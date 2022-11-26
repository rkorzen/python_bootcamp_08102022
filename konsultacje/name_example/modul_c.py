from modul_b import Square


s = Square()

print(s.a)


class Circle:
    pl_name = "Okrąg"

    def __init__(self, r):
        """Ta funkcja wykonywana jest tylko raz na poczatku gdy obiekt jest inicjalizowany

        >> c = Circle(r=10)
        >> c.r
        10

        """
        self.r = r
        self.color = None

    def area(self):
        return 3.14 * self.r ** 2

    def set_color(self, value):
        self.color = value

    @property   # atrybut dynamiczny
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        if value < 0:
            raise ValueError("Promien mniejszy niz zero!!!")
        self._r = value

c = Circle(r=2)
c.color = "Blue"
print(c.color)
c.set_color("Red")
print(c.color)
print(c.r)
print(c.pl_name)

print(c.area())

c2 = Circle(r=3)
print(c2.color)


c3 = Circle(r=10)
print(c3.r)
c3.r = 11
print(c3.area())

