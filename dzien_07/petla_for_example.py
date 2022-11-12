
print(dir())
for i in [1, 2, 3]:
    print(i)

print(dir())
print(i)
#        0    1    2
lista = ["a", "b", "c"]
i = 0
x = None
try:
    while True:
        print(lista[i])
        i += 1
        x = lista[i]
except IndexError:
    print("Ostatnia wartośc dla i to: ", i)
print("Ostatnia wartośc dla i to: ", i)
print("Co to jest x? ", x)

