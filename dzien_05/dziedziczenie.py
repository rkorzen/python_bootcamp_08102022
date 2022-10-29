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

user = User("Bartek", "19991010")
print(user.dataurodzenia)


class Administrator(User):

    def dostep(self):
        return True


administrator = Administrator("Adam","20001212")
print(administrator.dataurodzenia)


class Wlasciciel(Administrator):
    pass


class Magazyn: #stanu - ilosci
    pass

class Zatowarowanie(Magazyn):
    pass

class RozschodTowaru(Magazyn):
    pass

class Sklep(Zatowarowanie, RozschodTowaru):
    pass



class Trojkat:
    def pole_trojkata(self):
        pass

class Kolo:
   def pole_kola(self):
       pass

class Kwadrat:
    def pole_kwadrat(self):
        pass

class Figury(Trojkat, Kolo, Kwadrat):
    pass


