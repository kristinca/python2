import tkinter as tk
import requests

API_KEY =


class ExchangeRate:

    def __init__(self, api_key, *args, **kwargs):

        self.URL =
        self.api_key = api_key
        self.url = self.URL.format(api_key=api_key)

    def fetch_rates(self):
        try:
            rates = requests.get(self.url).json()
            return rates
        except requests.RequestException:
            rates = []
            return


erate = ExchangeRate(api_key=API_KEY)
erate.fetch_rates()

rates1 = dict()

for val in erate.fetch_rates().values():
    if isinstance(val, dict):
        rates1 = val

currency = rates1.keys()

root = tk.Tk()
root.title("A very simple app")
root.geometry("600x400")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)

frame = tk.Frame(root, padx=50, pady=50)
frame.pack()

label1 = tk.Label(frame, pady=20, text='Currency Converter', font='24')
label1.pack()

clicked = tk.StringVar()
click = str(clicked.get())


def show():
    myLbl = tk.Label(root, text=rates1.get(str(clicked.get()))).pack()


button1 = tk.Button(frame, text="Choose a currency", command=show)
button1.pack()


drop = tk.OptionMenu(root, clicked, *rates1.keys())

drop.pack()

root.mainloop()