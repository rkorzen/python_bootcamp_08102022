# licznik liter
# napisz skrypt, który utworzy słownik zawierajacy liczbe wystapien danego znaku
# w zadanym tekscie

zadany_text = "ala ma kota"

#ver1
zliczenia = {}
for znak in zadany_text:
    if znak in zliczenia:
        zliczenia[znak] += 1
    else:
        zliczenia[znak] = 1

print(zliczenia)

#ver2
zliczenia = {}
for znak in zadany_text:
    try:
        zliczenia[znak] += 1
    except KeyError:
        zliczenia[znak] = 1

print(zliczenia)

#ver 3

zliczenia = {}
for znak in zadany_text:
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

print(zliczenia)

# ver 4

from collections import defaultdict

zliczenia = defaultdict(int)

for znak in zadany_text:
    zliczenia[znak] += 1
    # zliczenia[znak] = zliczenia[znak] + 1

print(zliczenia)
print(dict(zliczenia))

# ver 5

from collections import Counter
zliczenia = Counter(zadany_text)
print(zliczenia)
print(dict(zliczenia))

# ver 6

zliczenia = {}
i = 0
for znak in zadany_text:
    zliczenia[znak] = zadany_text.count(znak)
    i += 1
print(zliczenia)
print(i)
# ver 6

zliczenia = {}
i = 0
for znak in set(zadany_text):
    zliczenia[znak] = zadany_text.count(znak)
    i += 1
print(zliczenia)
print(i)
