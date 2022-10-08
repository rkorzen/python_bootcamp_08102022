# Program do obliczania
# współczynnika BMI

"""
Program do obliczania
współczynnika BMI

"""

nazwa = "Kokoaksoakskodofk oasASD"
nazwa2 = "Rafał"

len_nazwa = len(nazwa)

# wzrost = int(input("Podaj wzrost w cm: ")) / 100
# waga = int(input("Podaj wagę w kg: "))
wzrost, waga = 1.81, 110
bmi = waga / (wzrost ** 2)

# print("Twój współczynnik BMI wynosi", bmi)

print(f"""
{nazwa:{len_nazwa}} X
{nazwa2:{len_nazwa}} X

- Twój współczynnik BMI wynosi {bmi:.0f} (waga:{waga} kg, wzrost={wzrost} m)""")




