

class Car:
    counter: int = 0

    def __init__(self, brand):
        self.brand = brand
        Car.counter += 1

    def __del__(self):
        Car.counter -= 1
        super().__del__()

    def drive(self):  # metoda instancji
        print(f"Samochód {self.brand} jedzie")

    @classmethod
    def create_super_auto(cls):
        return cls("Porshe")

    @staticmethod
    def brands():
        return ["Fiat", "Porshe"]

c = Car("Fiat")
x = [c]
c = Car("BMW")
c.drive()
x[0].drive()
# del x[0]

d = Car.create_super_auto()
d.drive()
print("czy 2? ", Car.counter)
Car.counter = 10

print(d.counter)
d.counter = 15
print(d.counter)
print(Car.counter)

print(d.brands())
print(Car.brands())
