import pickle

x = [1, 2, 3, 4]

class Kolo:
    promien = 10

kolo = Kolo()
kolo.promien = 11


print(pickle.dumps(x))
text_pickle = pickle.dumps(kolo)

print(type(text_pickle), text_pickle)
x = pickle.loads(text_pickle)

print(x.promien)


with open("kolo.pickle", "wb") as f:
    pickle.dump(kolo, f)


with open("kolo.pickle", "rb") as f:
    print(pickle.load(f))
