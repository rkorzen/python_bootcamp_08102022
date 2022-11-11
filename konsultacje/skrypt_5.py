


class Kwadrat:
    def __init__(self, bok, kolor):
        self.bok = bok
        self.kolor = kolor

    def obwod(self):  # bok to argument funkcji
        """Zwraca obwod kwadratu o boku `bok`
        """
        if type(self) is dict:
            bok = self["bok"]
        elif type(self) is list:
            bok = self[0]
        else:
            bok = self.bok # instancja klasy kwadrat
        return bok * 4

    def pole(self):
        print("Metoda w klasie")
        bok = self.bok
        return bok ** 2


instancja_kwadrat = Kwadrat(bok=3, kolor="Czarny")  # instancha klasy Kwadrat
slownik_kwadrat = {"bok": 3, "kolor":"Czarny"}      # slownik
lista_kwadrat = [3, "Czarny"]


def obwod(self):  # bok to argument funkcji
    """Zwraca obwod kwadratu o boku `bok`
    """
    if type(self) is dict:
        bok = self["bok"]
    elif type(self) is list:
        bok = self[0]
    else:
        bok = self.bok
    return bok * 4

def pole(self):
    print("Funkcja zewnetrzna")
    bok = self.bok
    return bok ** 2

print(obwod(lista_kwadrat))
print(obwod(slownik_kwadrat))
print(obwod(instancja_kwadrat))

print(instancja_kwadrat.obwod())

# slownik_kwadrat.obwod()

print(instancja_kwadrat.pole())  # metoda w klasie
print(pole(instancja_kwadrat))   # funkcja zewnetrzna