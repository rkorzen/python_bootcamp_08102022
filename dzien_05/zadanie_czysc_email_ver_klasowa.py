# wersja prosta - działająca... tak zrobi początkujacy

class EmailCleaner:

    def __init__(self, in_filename: str, out_filename: str):
        self.in_file = in_filename
        self.out_file = out_filename
        self.data: list = []
        self.cleaned_data: list = []

    def get_data(self):
        with open(self.in_file) as f:
            self.data = f.readlines()

    def clean_data(self):
        self.cleaned_data = sorted({email.strip().lower() for email in self.data if email.count("@") == 1})

    def write_data_line_by_line(self):
        with open(self.out_file, "w") as f:
            for el in self.cleaned_data:
                f.write(el + "\n")

    def write_data_once(self):
        with open(self.out_file, "w") as f:
            data = "\n".join(self.cleaned_data)
            f.write(data)

    def process(self):
        print("procesuję...")
        self.get_data()
        self.clean_data()
        self.write_data_once()


em = EmailCleaner(in_filename="data/emails.txt", out_filename="data/cleaned_emails2.txt")
em.process()
