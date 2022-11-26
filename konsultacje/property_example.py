rok = 2022


class Osoba:

    def __init__(self, imie, rok_ur):
        self.imie = imie
        self.rok_ur = rok_ur

    @property
    def wiek(self):
        return rok - self.rok_ur

    @wiek.setter
    def wiek(self, wiek):
        self.rok_ur = rok - wiek


os = Osoba("Rafał", 1980)
print(os.wiek)

rok = 2023

print(os.wiek)

rok += 1  # 2024

print(os.wiek)

os.wiek = 40

print(os.rok_ur)


class Osoba2:

    def __init__(self, imie, rok_ur):
        self.imie = imie
        self.rok_ur = rok_ur

    def get_wiek(self):
        return rok - self.rok_ur

    def set_wiek(self, wiek):
        self.rok_ur = rok - wiek


os = Osoba2("Rafał", 1980)
print(os.get_wiek())

rok = 2023

print(os.get_wiek())

rok += 1  # 2024

print(os.get_wiek())

# os.wiek = 40
os.set_wiek(40)
print(os.rok_ur)
print(os.get_wiek())
