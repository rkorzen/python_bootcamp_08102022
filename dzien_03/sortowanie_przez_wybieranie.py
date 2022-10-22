"""
Napisz program, który posortuje liczby w liście
przy wykorzystaniu algorytmu
"Sortowanie przez wybieranie"

"""

lista1 = [9, 1, 6, 8, 4, 3, 2, 0]
lista2 = [9, 1, 6, 8, 4, 3, 2, 0, 5]
lista3 = [9, 1, 6, 8, 4, 3, 2, 0, 7]

def sortowanie_przez_wybieranie(lista):
    for i_podstawienia in range(len(lista)):
        i_min_wartosci = i_podstawienia
        for i_ogona in range(i_podstawienia+1, len(lista)):
            if lista[i_ogona] < lista[i_min_wartosci]:
                i_min_wartosci = i_ogona

        # temp = lista[i_min_wartosci]
        # lista[i_min_wartosci] = lista[i_podstawienia]
        # lista[i_podstawienia] = temp

        lista[i_min_wartosci], lista[i_podstawienia] = lista[i_podstawienia], lista[i_min_wartosci]
    return lista


for lista in [lista1, lista2, lista3]:
    sortowanie_przez_wybieranie(lista)


print(lista1)
print(lista2)
print(lista3)
