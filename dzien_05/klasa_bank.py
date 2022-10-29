# def konto():
#     return {'stan': 0}
#
# def zwiekszenie(konto, wartosc):
#     konto['stan'] += wartosc
#     return konto['stan']
#
# def zmniejszenie(konto,wartosc):
#     konto['stan'] -= wartosc
#     return konto['stan']


class SaldoKontaWBanku:
    def __init__(self):
        self.stan = 0

    def zwiekszenie_salda(self, wartosc):
         self.stan += wartosc
         return self.stan

    def zmniejszenie_salda(self, wartosc):
         self.stan -= wartosc
         return self.stan

    def wyswietl_saldo(self):
        print(self.stan)



a = SaldoKontaWBanku()
a.zwiekszenie_salda(100)
a.zmniejszenie_salda(90)
#print(a.stan)
a.wyswietl_saldo()


SaldoKontaWBanku.wyswietl_saldo(a)