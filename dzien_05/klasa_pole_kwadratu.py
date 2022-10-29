class PoleKwadratu:
    def __init__(self, a):
        self.a = a

    def oblicz_pole(self):
        print(self.a * self.a)


class PoleFigury:
    def __init__(self, a, b = 0,c = 0,d = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def oblicz_pole_kwadratu(self):
        print(self.a * self.a)

    def oblicz_pole_prostokata(self):
        print(self.a * self.b)