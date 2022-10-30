"""
Otworzyc plik data/emails.txt
Wybrac tylko unikalne i poprawne emaile
Kryterium - 1 małapa w środku
Zapisz wynik w pliku data/cleaned_emails.txt
maja byc tam poprawne, posortowane, unikalne emaile z pliku data/emails.txt


dir(str)

count
strip
lower

to nie jest kod:
with open(sciezka, mode="tryb") as f:
    for line in f:

    f.write()
"""

def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = f.readlines()
        return data

def clean_data(data: list[str]) -> list[str]:
    return sorted({email.strip().lower() for email in data if email.count("@") == 1})


def write_data_line_by_line(filename: str, data: list[str]):
    with open(filename, "w") as f:
        for el in data:
            f.write(el+"\n")

def write_data_once(filename: str, data: list[str]):
    with open(filename, "w") as f:
        data = "\n".join(data)
        f.write(data)

def main():
    print("Działam")
    data = get_data("data/emails.txt")
    data = clean_data(data)
    write_data_once("data/cleaned_emails.txt", data)

if __name__ == "__main__":
    print(dir())
    main()

