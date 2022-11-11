# klasy

class Kwadrat:
    def __init__(self, bok, kolor):
        self.bok = bok  # kwadrat["bok"]
        self.kolor = kolor

    def obwod(self):  # bok to argument funkcji
        """Zwraca obwod kwadratu o boku `bok`
        """
        bok = self.bok  # kwadrat["bok"]
        return bok * 4

    def pole(self):
        bok = self.bok
        return bok ** 2

kwadrat = Kwadrat(2, "czerwony")  # to jest instancja
kw2 = Kwadrat(4, "czarny")
kwadrat.pole()  # pole(kwadrat)
kw2.pole()  # pole(kw2)
# jest poprzez instancję
Kwadrat.pole(kwadrat)  # funkcja - metoda
# dostajemy sie do niej poprzez klasę
# pole2(kwadrat)   # funkcja poza klasa

kwadrat.bok

def obwod(kwadrat): # bok to argument funkcji
    """Zwraca obwod kwadratu o boku `bok`

    kwadrat: obiekt klasy kwadrat, który ma
    atrybut bok. Bok to liczba wyrazajaca długoś boku kwadratu
    """
    bok = kwadrat.bok
    return bok * 4

def pole2(kwadrat):
    bok = kwadrat.bok
    return bok ** 2


# printy pokazuja cos uzytkownikowi

print(obwod(kwadrat))  # wywołuje z argumentem kwadrat
print(kwadrat.obwod())

print(pole2(kwadrat))
print(kwadrat.pole())
# napiszmy testy - oparte o assert
# to są przypadki testowe
assert obwod(Kwadrat(bok=2, kolor="czerwony")) == 8

# TODO: poprawic te testy
# by korzystaly z instancji klasy
# assert obwod({"bok": 3, "kolor": "zólty"}) == 12
# assert obwod({"bok": 10,"kolor":  "niebieski"}) == 40
# assert obwod({"bok": 0, "kolor": "czarny"}) == 0