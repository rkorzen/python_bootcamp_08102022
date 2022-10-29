class Samochod:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return f'Nazwa samochodu to: {self.nazwa}'


moj_samochod = Samochod('Fiat')
print(moj_samochod)