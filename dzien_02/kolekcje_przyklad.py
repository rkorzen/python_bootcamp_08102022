#        012345678910
napis = "Ala ma kota"

print(len(napis))
print("A" in napis)

print(napis.lower().count("a"))
print(napis.index("A"))

print(napis[0])
print(napis[3:6])
print(napis[1:10:2])
print(napis[1:])

print(napis[:6])
print(napis[:6:2])
print(napis[::3])
# [poczatek:koniec(otwarty):krok]

print(napis[1]+napis[5]+napis[8])
print(napis[-1])
print(napis[-4:])

print(napis[::-1])
print("".join(reversed(napis)))


napis2 = "O" + napis[1:]
print(napis2)


# tuple

t = (1, 2, 3, 2, 2, "a")
# print(type(t))
# print(dir(t))

print(t.count(2))
print(t.index(2, 3))

print(help(t.index))

print(t[1::-2])

# t[0]= 10

print(tuple("123"))
print(tuple())

print(type((1,)))

# lista

l = [1, 2, 3, 2, 2, 2.0]
print(dir(l))
print("0", sorted(l))
print("1", l.sort())
print()
print("2", l)

l.append("a")
print(l)
l.insert(1, "b")
print(l)

print(l[2::2])


a = [1, 2, 3]
b = a
b.append(5)

print(a, b)

a = [1, 2, 3]
b = [1, 2, 3]
b.append(5)

print(2, a, b)


a = [1, 2, 3]
b = a.copy()  # płytka kopia - shallow copy
b.append(5)

print(2, a, b)

a = [1, 2, 3]
b = [1, 2, a]
print(b)

c = b.copy()
a.append(4)
print(b, c)


import copy

a = [1, 2, 3]
b = [1, 2, a]
print(b)

c = copy.deepcopy(b)
a.append(4)
print(b, c)

a = (1, 2, 3)
b = a

b = (1, ) + b

print(a, b)

print(dir([]))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

lista = [1, 2,3]
lista.append(4)

# lista.clear()


(1, 2, 3) # niemutowalna. dwie metody: count, index
[1, 2, 3] # mutowalne, 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print((1, 2, 3, 2.0).count(2))

dane = [1, 2, 1, 2, 1, 2.0, 2.0, 2.00000000000000000001, "x"]
print("---"*12)

# szukane = 2
# i = 0
# licznik_wyszukania = 0
# while i < len(dane):
#     if dane[i] == szukane:
#         licznik_wyszukania += 1
#     i += 1
# print(licznik_wyszukania)
# pętle for
szukane = 2
licznik_wyszukania = 0
for el in dane:
    if el == szukane:
        licznik_wyszukania += 1

print(el)

x = 123123123123123
y = (123123123123123,)

print(id(x), id(y[0]))


x = "ala"
y = "ala"

print(x is y)

x = "ala ma kota kot ma ale"
y = "ala ma kota kot ma ale"

print(x is y)


