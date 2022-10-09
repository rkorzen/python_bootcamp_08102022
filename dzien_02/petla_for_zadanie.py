#
# lista = [1, 2, 3, -1, -2, 10, 20, -400, 200, 24]
#
# dodatnich = 0
# ujemnych = 0
#
#
# for el in lista:
#     if el > 0:
#         dodatnich += 1
#     elif el < 0:
#         ujemnych += 1
#
# print(f"{dodatnich=} {ujemnych=}")
#

dane = []

while True:
    d = input("Podaj liczbę lub k by zkończyć: ")
    if d == "k": break
    dane.append(int(d))

print(f"Średnia={sum(dane) / len(dane)}, min={min(dane)} max={max(dane)}")