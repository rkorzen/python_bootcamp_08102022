class Car:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def drive(self):
        print("Samochód rusza")


class ElectricCar(Car):
    def __init__(self, pojemnosc_baterii, *args):
        # Car.__init__(self, *args)
        super().__init__(*args)
        self.pojemnosc_baterii = pojemnosc_baterii

    def drive(self):
        print("Eletrony zaczynają pracowac")
        super().drive()


ec = ElectricCar( 2000, "A")
ec.drive()
