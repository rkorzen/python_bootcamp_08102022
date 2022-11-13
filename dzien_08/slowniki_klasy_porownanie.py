from datetime import datetime

kolo = {
    "promien": 3,
    "kolor": "Czerwony"
}

class Kolo:
    def __init__(self, promien, kolor):
        self.promien = promien
        self.kolor = kolor

    def to_dict(self):
        return {
            "promien": self.promien,
            "kolor": self.kolor
        }
    def __repr__(self):
        return f"Kolo(promien={self.promien}, kolor={self.kolor})"

pole = kolo["promien"] ** 2 * 3.14
kolo = Kolo(3, "Czerwony")
# print(kolo)
pole = kolo.promien ** 2 * 3.14

# print(kolo.to_dict())
# print(kolo.__dict__)

class Kolo2:
    promien = 3
    kolor = "Czerwony"

    def __repr__(self):
        return f"Kolo(promien={self.promien}, kolor={self.kolor})"

k = Kolo2()
# print(k)
# print(k.promien)
# print(k.kolor)
print(k.__dict__, "przed ustawieniem atrybutu")
k.kolor = "Zielony"  # isntancja ma teraz zielony kolor
print(k.__dict__, "po ustawieniu atrybutu")
Kolo2.kolor = "Fiołkowy"
# print(Kolo2)
# print(Kolo2.kolor)
# print(k)

# k2 = Kolo2(3, "Niebieski")


from dataclasses import dataclass

@dataclass
class Kolo3:
    promien: int = 3
    kolor: str = "Niebieski"
    date: datetime = None

    def serlialize(self):

        date_value = self.date
        if date_value:
            date_value = date_value.isoformat()

        return {
            "promien": self.promien,
            "kolor": self.kolor,
            "date": date_value
        }

# def __init__(self, promien=3, kolor="Niebieski"):
#     self.promien = promien
#     self.kolor = kolor

k3 = Kolo3(5, "Czarny")
print(k3)

print(dir(k3))


import json

k3.date = datetime.now()
print(k3.date)
napis_json = json.dumps(k3.serlialize())

dane_z_jsona = json.loads(napis_json)
# dane_z_jsona["x"] =10
print(dane_z_jsona, type(dane_z_jsona))

print(Kolo3(**dane_z_jsona))
# print(Kolo3(promien=dane_z_jsona["promien"], kolor=dane_z_jsona["kolor"]), x=dane_z_jsona["x"])
