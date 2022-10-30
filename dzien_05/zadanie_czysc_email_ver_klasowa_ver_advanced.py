# wersja prosta - działająca... tak zrobi początkujacy
import csv


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = f.readlines()
        return data


def get_data_from_csv(filename: str) -> list[str]:
    data = []
    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            data.append(row["email"])
    return data


def write_data_line_by_line(filename: str, data: list[str]):
    with open(filename, "w") as f:
        for el in data:
            f.write(el + "\n")


def write_data_once(filename: str, data: list[str]):
    with open(filename, "w") as f:
        data = "\n".join(data)
        f.write(data)


class EmailCleaner:

    def __init__(self, in_filename: str, out_filename: str, function_to_read, function_to_write):
        self.in_file = in_filename
        self.out_file = out_filename
        self.data: list = []
        self.cleaned_data: list = []
        self.get_data = function_to_read
        self.write_data = function_to_write

    def clean_data(self):
        self.cleaned_data = sorted({email.strip().lower() for email in self.data if email.count("@") == 1})

    def process(self):
        print("procesuję...")
        self.data = self.get_data(self.in_file)
        self.clean_data()
        self.write_data(self.out_file, self.cleaned_data)


em = EmailCleaner(
    in_filename="data/emaile.csv",
    out_filename="data/cleaned_emails4.txt",
    function_to_read=get_data_from_csv,
    function_to_write=write_data_line_by_line
)

em.process()

