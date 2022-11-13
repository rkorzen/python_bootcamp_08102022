import re

pattern_zip_code = r"\b\d{2}-\d{3}\b"
pattern_email = r"[\w\d\-\.]*@[\w\d\-\.]+[\w\d]"
pattern_date = "[0-3]\d \w{3} \d{4}"

PATTERN_ZIP_CODE = re.compile(r"\b\d{2}-\d{3}\b")
PATTERN_EMAIL = re.compile(r"[\w\d\-\.]*@[\w\d\-\.]+[\w\d]")
PATTERN_DATE = re.compile("[0-3]\d \w{3} \d{4}")

re.findall(pattern_date, text)
PATTERN_DATE.findall(text)


def find_emails(text):
    return PATTERN_EMAIL.findall(text)


def find_zip_codes(text):
    return PATTERN_ZIP_CODE.findall(text)


def find_dates(text):
    return PATTERN_DATE.findall(text)


with open("input.txt") as f:
    text = f.read()

    print(find_emails(text))
    print(find_dates(text))
    print(find_zip_codes(text))
