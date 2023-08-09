import requests
import json

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Get a dadjoke")
root.configure(background="#BBCCE1")
root.geometry("300x100")


def fetch_joke():
    # print een grap op het messagebox scherm
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = json.loads(str(res.text))

    messagebox.showinfo(title="My favorite api",
                        message=data['joke'])


dadjoke = Button(root, text="Fetch a dad joke",
                 bg="#BBDDE1", command=fetch_joke)


dadjoke.pack()


root.mainloop()
