import datetime


class User:
    def __init__(self, imie, dataurodzenia):
        self.imie = imie
        self.dataurodzenia = dataurodzenia

        self.inicjal = imie[0]
        self.rok_urodzenia = dataurodzenia[0:4]

    def wiek(self):
        dzis = datetime.datetime.now()
        yyyy = int(self.dataurodzenia[0:4])
        wiek = dzis.year - yyyy
        return wiek

#print(help(User))

user = User("Tomek", "19981010")
print(user.dataurodzenia)
print(user.imie)

print(user.inicjal)
print(user.rok_urodzenia)

w = user.wiek()
print("Wiek:",w)


