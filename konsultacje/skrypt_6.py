class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    # kw.bok
    @property
    def bok(self):
        return self._bok

    # kw.bok = 10
    @bok.setter
    def bok(self, value):
        if value < 0:
            raise ValueError("Bok ma ujemna dlugosc!!")
        self._bok = value

    def obwod(self):
        return self._bok * 4
    #           kw1   kw2
    def __add__(self, other):
        return Kwadrat(bok=self.bok + other.bok)

kw0 = Kwadrat(3)
kw0.bok = -3
print(kw0.obwod())

kw1 = Kwadrat(3)
kw2 = Kwadrat(4)

print(kw1 + kw2)

# podejscie oparte o slownik
def obwod(self):
    return self["bok"] * 4

def dodaj_kwadraty(self, other):
    """

    :param self: dict z kluczem bok
    :param other: dict z kluczem bok
    :return: dict z kluczem bok
    """
    # return  {"bok": self["bok"] + other["bok"]}
    return dict(bok=self["bok"] + other["bok"])

kw1d = {"bok": 3}
kw2d = {"bok": 4}

# print(kw1d + kw2d) # tak nie mogę zrobic
print(dodaj_kwadraty(kw1d, kw2d))



