from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox

def suma():
    a_value = float(a.get())
    b_value = float(b.get())
    if b_value == 0:
        messagebox.showerror("Dzielenie przez 0!!!", "Zmień b")
    wynik.configure(text=f"{a_value / b_value}")


root = Tk()
root.columnconfigure(1, weight=1)
label_a = Label(master=root, text="Liczba a: ")
label_a.grid(row=0, column=0)
a = Entry(master=root)
a.grid(row=0, column=1)

label_b = Label(master=root, text="Liczba b: ")
label_b.grid(row=1, column=0)
b = Entry(master=root)
b.grid(row=1, column=1)

sum_button = Button(master=root, text="Dziel", command=suma)
sum_button.grid(row=2, column=0)

wynik = Label(master=root, text="-")
wynik.grid(row=2, column=1)

root.mainloop()
