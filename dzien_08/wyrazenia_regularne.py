import re

re.match
re.findall
re.search

"xxx-xxx-xx-xx"
text = "123-233-12-23"
print(re.match('^\d{3}-\d{3}-\d{2}-\d{2}', text))

text2 = "ATTAGAGACCTTGGATGAAAC"
result = re.search("(AT)|(GA)", text2)
print(result)
print(result.group())
print(result.groups())


result = re.findall("AT|GA", text2)
print(result)


text3 = "The price of PINEAPPLE ice cream is 20"

result = re.search(r"(\b[A-Z]+\b).*(\b\d+)", text3)
print(result)
print(result.groups())


target_string = """Szukam zawsze i wszędzie
Pierwszego co tylko będzie
Słowa bo boli głowa"""

result = re.findall(r"^\w+", target_string, re.MULTILINE)
print(result)
result = re.findall(r"\w+$", target_string, re.MULTILINE)
print(result)