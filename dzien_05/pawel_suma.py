def suma_with_cast(liczby: list() or dict() or tuple(), cast_to_int: bool = False) -> int:
    s = 0
    for i in liczby:
        if type(liczby) == dict:
            if type(liczby[i]) == int:
                s += liczby[i]
            elif type(liczby[i]== str) and cast_to_int is True:
                if liczby[i].isnumeric():
                    s += int(liczby[i])
        else:
            if type(i) == int:
                s += i
            elif (type(i) == str) and cast_to_int is True:
                if i.isnumeric():
                    s += int(i)
    return s

# def sum_with_cast(liczby):
#     # if type(liczby) is dict
#     if isinstance(liczby, dict):
#         liczby = liczby.values()
#     for liczba in liczby


print(suma_with_cast((1, "a", 3, 5, 8), True))
print(suma_with_cast(["b", "a", 3, 5, 9, 1, "11"], True))
print(suma_with_cast([8, 2, 3, "s", "8"], True))  # == 21
print(suma_with_cast([1, 2, "a"])) #== 3
print(suma_with_cast({1: 8, 2: 2, 3: 3, 4: 0, 5: 9}))  # == 22
print(suma_with_cast({1: "8", 2: "a", 3: 3, 4: 0, 5: 9}, True))  # == 20

