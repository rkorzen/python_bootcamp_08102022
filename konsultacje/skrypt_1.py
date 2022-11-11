print("Hello world")

integer = 1

"""
+-/ 
// - całkowite dzielenie
% dzielenie modulo
** - potęgowanie
"""

print(4 / 2)
print(4 // 2)
print(4 % 3)
print(4 ** 2)

# bool

True
False

print(True + False)  # 1 + 0

print(1 > 2)
print(1 < 2)

"""Operatory porównania
==  coś innego samo = - jedno = przypisuje wartośc z prawej do lewej
<=
>=
<
>
!=

"""

print(1 != 2)

x = 1

_zmienna = 1
x = y = 1

z = 2

nazwaZmiennej = 0  # niepoprawna nazwa
nazwa_zmiennej = 0

# ------ wyrażenia warunkowe

# if jakis_warunek
x = 1
y = 2
True
False
if x > y:
    print("x większe")
else:
    print("y większe")

if x > y:
    print("x większe")
elif x == 1:
    print("x to jedynka")
else:
    print("y większe")


if x:
    print("x to prawda")


if x is True:
    print("x to prawda - x na pewno jest wartością True")

if x == True:
    print("x to prawda - x na pewno jest wartością True")

print(1 == True) # to jest prawda w Pythonie
""" uogólnione wartosci logiczne

0, "", [], {}, set(), () -> False
1, 2, -1 itd, "1", [1, 2] ... wsztstko co jest niepuste i nie jest zerem -> True


"""
print(bool(0))
print(bool([]))
print(bool([1]))

z = True
# id - sprawdza adres w pamięci - tak z grubsza
print(id(z), id(True))

# napisy w Python

"to jest napis"
'to też jest napis'

print("\n1\n2\n3\n4\n" == """
1
2
3
4
""")
print("-" * 40)
x = "" and "2"
print(x, type(x))


x = 0 and 2
print(x, type(x))


produkt = "Piwo"
cena = 12.50
ilosc = 1

raport = print(produkt, cena, ilosc)
print(raport)

raport = produkt + " " + str(cena)
print(raport)

raport = f"{produkt}   {cena}"


raport = f"""{produkt}   

    {cena}"""
print(raport)

raport = f"{produkt} cena:{cena:.2f} PLN ilosc: {ilosc}"
print(raport)

raport = f"{produkt:30} cena:{cena:6.2f} PLN ilosc: {ilosc:.3f}"
print(raport)

raport = f"{produkt:>30} cena:{cena:6.2f} PLN ilosc: {ilosc:.3f}"
print(raport)

raport = f"{produkt:^30} cena:{cena:6.2f} PLN ilosc: {ilosc:.3f}"
print(raport)


# pyformat.info
#        0123456789            # index
napis = "konsultacje z pythona"
print(len(napis))

print(napis[9])
print("konsultacje z pythona"[9])

print(napis[21])


# slicing  [poczatek:koniec:krok] [poczatek:koniec] [::krok]
print(napis[::2])

print(napis[:10])
print(napis[:11])

print(napis[-2])

print(napis[-30:-2])
print(napis[:100])

napis2 = tuple(napis)

print(napis2[:100])
print(napis2[:10])
print(napis2[6])

"1" + "2"

print((1, 2) + (1, 2, 3))

# napis[7] = "h"  # napis jest niemutowalny- niezmienialny
# napis2[7] = 1

# dir
print(dir(napis2))

print(napis2.index("a"))  # wynik printowany to int
# help
print(napis2.index)       # wynik printowany to obiekt metody -funkcji
print(help(napis2.index))

print(napis2.index("a", 8))

print(help(print))
print(1, 2, 3, end="to byłaby nowa linia")

print(1, 2, 3, sep="----")
print()
print("cos")

print(dir(napis))

print("x" in napis)
print("do pliku")