def konto():
    return {'stan': 0}

def zwiekszenie(konto, wartosc):
    konto['stan'] += wartosc
    return konto['stan']

def zmniejszenie(konto,wartosc):
    konto['stan'] -= wartosc
    return konto['stan']

konto1 = konto()
zwiekszenie(konto1, 100)
zmniejszenie(konto1, 80)
print(konto1)

konto2 = konto()
zwiekszenie(konto2, 1200)
zmniejszenie(konto2, 280)
print(konto2)