


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
op = input("Podaj rodzaj operacji: ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "Pamietaj cholero nie dziel przez zero"
    else:
        result = a / b
elif op == "**":
    result = a ** b
else:
    result = ("Nie "
    "znana operacja")

    result = "Nie " \
    "znana operacja"

print(f"Wynik to: {result}")