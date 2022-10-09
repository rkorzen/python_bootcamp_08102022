i = 0
if i == 0:
    while True:
        print("Działam")
        i += 1
        if i == 7:
            break

print()

i = 0
while i < 7:
    print("Działam")
    i += 1

print()

i = 0
while i < 7:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i < 7:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("zakończyłem bez przerwań")
