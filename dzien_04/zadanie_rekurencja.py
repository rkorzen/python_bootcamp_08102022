"""

Zaimplementuj funkcję spłaszczającą podaną listę.
Przykład użycia:
>>> splaszcz([])
[]

>>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
[1, 2, 3, 4, 5, 6, 7]

>>> splaszcz([1, 2, 3])
[1, 2, 3]

>>> splaszcz([1, [[2, 3]]])
[1, 2, 3]

"""

def splaszcz(lista: list) -> list:
    result = []
    for element in lista:
        if type(element) is list:
            for el_z_zagniezdzenia in splaszcz(element):
                result.append(el_z_zagniezdzenia)
        else:
            result.append(element)
    return result
#
# def splaszcz(lista: list) -> list:
#     result = []
#     for element in lista:
#         if type(element) is not list:
#             result.append(element)
#         else:
#             for el_z_zagniezdzenia in splaszcz(element):
#                 result.append(el_z_zagniezdzenia)
#     return result

splaszcz([1, 2, 3, [4, 5, [6]], 7])


[1, 2, 3, 7]
[4, 5, ]
[6]

