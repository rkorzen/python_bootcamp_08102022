class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def obwod(self):
        return self.bok * 4
    #           kw1   kw2
    def __add__(self, other):
        return Kwadrat(bok=self.bok + other.bok)


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



