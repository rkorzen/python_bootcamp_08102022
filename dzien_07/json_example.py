import json

data = (
    {"temperatura": 45.0, "cisnienie": 1200, "data": "2022-07-12"},
    {'temperatura': 47, "ciśnienie": 1250, "data": "2022-07-13"},
)

print(data)
# python -> text(json)
json_data = json.dumps(data)
print(json_data, type(json_data))

raw_data = '[{"temperatura": 45, "cisnienie": 1200, "data": "2022-07-12"}, {"temperatura": 47, "ci\u015bnienie": 1250, "data": "2022-07-13"}]'
raw_data = json_data
# text(json) -> python

python_data = json.loads(raw_data)

print(python_data, type(python_data))

# zapis do jsona
with open("dane.json", "w") as f:
    json.dump(python_data, f)

with open("dane.json") as f:
    dane = json.load(f)

print(dane, type(dane))
