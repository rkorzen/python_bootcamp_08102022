
postac = {
    "ekwipunek": [
        {"nazwa": "miecz", "sila":15},
        {"nazwa": "topor", "sila":25},
        {"nazwa": "tarcza", "sila":1},
    ],
    "sila": 1500,
    "energia": 1000,
}

print(postac["ekwipunek"][2]["sila"])
postac # slownik opisujacy postac
ekwipunek = postac["ekwipunek"] # lista
tarcza = ekwipunek[2]
sila_tarczy = tarcza["sila"]

sila_tarczy = postac["ekwipunek"][2]["sila"]
sila_toporu = postac["ekwipunek"][1]["sila"]