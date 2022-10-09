x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

szesciany = []
for el in x:
    szesciany.append(el ** 3)

szesciany2 = [el ** 3 for el in x]

szesciany_liczb_parzystych = []
for el in x:
    if el % 2 == 0:
        szesciany_liczb_parzystych.append(el ** 3)

szesciany_liczb_parzystych2= [el ** 3 for el in x if el % 2 == 0]

print(szesciany, szesciany2)
assert szesciany == szesciany2
assert szesciany_liczb_parzystych == szesciany_liczb_parzystych2


szesciany2 = (el ** 3 for el in x)
print(szesciany2)

for el in szesciany2: print(el)



szesciany2 = {el:el ** 3 for el in x}
print(szesciany2)


wiersze = []
for i in range(1, 11):
    wiersz = []
    for j in range(1, 11):
        wiersz.append(i * j)
    wiersze.append(wiersz)

print(wiersze)

print([[i * j for i in x] for j in x])



print("XXX", end="")
print("uuu")


for i in range(10):
    ...
    for j in range(10):
        ...