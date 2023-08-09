import requests
import json

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Rekenmachine")
root.configure(background="#BBCCE1")


def onClick(e_target):
    # functionaliteit rekenmachine
    current_input = input.get()
    input.delete(0, END)
    input.insert(0, str(current_input) + str(e_target))
    sum = input.get()
    if e_target == "=":
        input.delete(0, END)
        input.insert(0, calculate_sum(sum))


def calculate_sum(sum):
    # rekent de som uit
    sum = sum.replace("=", "")
    # check of het + - / of * is
    if "+" in sum:
        x, y = sum.split("+")
        print(int(x) + int(y))
        return int(x) + int(y)
    elif "-" in sum:
        x, y = sum.split("-")
        print(int(x) - int(y))
        return int(x) - int(y)
    elif "*" in sum:
        x, y = sum.split("*")
        print(int(x) * int(y))
        return int(x) * int(y)
    elif "/" in sum:
        x, y = sum.split("/")
        print(int(x) / int(y))
        return int(x) / int(y)


def onClear():
    # leegt het input veld
    input.delete(0, END)


# input field van de rekenmachine
# googlen hoe ik die height hiervan kan veranderen?
input = Entry(root, width=60, borderwidth=5)
input.grid(row=0, columnspan=4, padx=10, pady=20)

# buttons, lambda is een anonieme functie die gebruik ik zodat ik argumenten/parameters door kan geven.
button_1 = Button(root, text="1", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(9))
button_0 = Button(root, text="0", padx=40, pady=20,
                  bg="#BBCCE1", command=lambda: onClick(0))
button_plus = Button(root, text="+", padx=40, pady=20,
                     bg="#BBCCE1", command=lambda: onClick("+"))
button_min = Button(root, text="-", padx=40, pady=20,
                    bg="#BBCCE1", command=lambda: onClick("-"))
button_delen = Button(root, text="/", padx=40, pady=20,
                      bg="#BBCCE1", command=lambda: onClick("/"))
button_keer = Button(root, text="*", padx=40, pady=20,
                     bg="#BBCCE1", command=lambda: onClick("*"))
button_clear = Button(root, text="C", padx=40, pady=20,
                      bg="#E1BBCC", command=onClear)
button_is = Button(root, text="=", padx=40, pady=20,
                   bg="#CCE1BB", command=lambda: onClick("="))


# zet buttons op juiste plek
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_delen.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_keer.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_min.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_is.grid(row=4, column=2)
button_plus.grid(row=4, column=3)


root.mainloop()
