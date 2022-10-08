produkt_1 = "pomidory"
waga_1 = 10
cena_1 = 12.5

produkt_2 = "ogórki"
waga_2 = 1.2
cena_2 = 3.75

produkt_3 = "chleb"
waga_3 = 0.5
cena_3 = 6.25


suma = cena_1 + cena_2 + cena_3

raport = f"""
{produkt_1:30} {waga_1:5.2f} kg {cena_1:5.2f} PLN
{produkt_2:30} {waga_2:5.2f} kg {cena_2:5.2f} PLN
{produkt_3:30} {waga_3:5.2f} kg {cena_3:5.2f} PLN
{"-"*50}
{"suma:":30} {"":8} {suma:5.2f} PLN 
"""

print(raport)