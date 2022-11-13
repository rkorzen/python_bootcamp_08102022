from tkinter import Tk, Label, Entry, Button
from main import spalanie, koszt

def suma():
    per_100 = float(a.get())
    dystans = float(b.get())
    koszt_litra = float(c.get())

    litry = spalanie(spalanie_na_100=per_100, dystans=dystans)
    koszt_przejazdu = koszt(litry, koszt_litra)

    wynik.configure(text=f"{koszt_przejazdu:.2f}")


root = Tk()
root.columnconfigure(1, weight=1)
label_a = Label(master=root, text="Spalanie na 100 km: ")
label_a.grid(row=0, column=0)
a = Entry(master=root)
a.grid(row=0, column=1)

label_b = Label(master=root, text="Dystans: ")
label_b.grid(row=1, column=0)
b = Entry(master=root)
b.grid(row=1, column=1)

label_c = Label(master=root, text="Cena litra: ")
label_c.grid(row=2, column=0)
c = Entry(master=root)
c.grid(row=2, column=1)

sum_button = Button(master=root, text="Oblicz", command=suma)
sum_button.grid(row=3, column=0)

wynik = Label(master=root, text="-")
wynik.grid(row=3, column=1)

root.mainloop()
