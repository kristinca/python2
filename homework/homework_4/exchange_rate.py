import tkinter as tk
import requests


API_KEY =


class ExchangeRate:

    def __init__(self, api_key, *args, **kwargs):

        self.URL = f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}'
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
root.geometry("400x200")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)

frame = tk.Frame(root, padx=50, pady=50, bg='#66CC66')
frame.grid(row=0, column=0, sticky='nsew')

label1 = tk.Label(frame, pady=10, padx=10, text='Currency Converter', font='24', bg='#ff4d4d')
label1.grid(row=0, column=3, sticky=(tk.W + tk.E))


clicked = tk.StringVar()
click = str(clicked.get())
entry_vals = tk.Entry(frame, width=10)
entry_vals.grid(row=6, column=2)

myLbl = tk.Label(frame)

def show():
    global myLbl
    myLbl.destroy()
    myLbl = tk.Label(frame, text=(rates1.get(clicked.get())*int(entry_vals.get())))
    myLbl.grid(row=6, column=3)

button1 = tk.Button(frame, text="EUR")
button1.grid(row=4, column=2)

button2 = tk.Button(frame, text='CONVERT', command=lambda: show())
button2.grid(row=4, column=4)

drop = tk.OptionMenu(frame, clicked, *rates1.keys())

drop.grid(row=4, column=3)
root.mainloop()
