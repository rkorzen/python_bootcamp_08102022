from dataclasses import dataclass
from datetime import datetime
from typing import Optional


class Osoba:

    def __init__(self, imie, nazwisko, rok_ur, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_ur = rok_ur
        self.stanowisko = stanowisko
        self.wiek = datetime.now().year - self.rok_ur

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.rok_ur} {self.stanowisko}"

os = Osoba("Rafał", "Korzeniewski", 1980, "Szef wszystkich szefów")
print(os)
print(os.imie)
print(dir(os))

@dataclass
class OsobaV2:
    imie: str
    nazwisko: str
    rok_ur: int
    stanowisko: str
    wiek: Optional[int] = None

    def __post_init__(self):
        self.wiek = datetime.now().year - self.rok_ur



os = OsobaV2("Rafał", "Korzeniewski", 1980, "Szef wszystkich szefów")
print(os)
print(os.imie)
print(dir(os))

