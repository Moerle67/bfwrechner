import random
import tkinter as tk 

from bbasis import Bbasis
from number import Number

class Bhdtrainer(Bbasis):
    def __init__(self, top):
        super().__init__(top)

        self.anzahl_numbers = 15

        # Zufallszahlen erstellen
        self.init_number()

        # Tabelle erstellen
        self.lbl_bin = tk.Label(self.root, text="Bin", font=(self.font, self.fontsize))
        self.lbl_bin.grid(column=1, row=101)
        self.lbl_hex = tk.Label(self.root, text="Hex", font=(self.font, self.fontsize))
        self.lbl_hex.grid(column=2, row=101)
        self.lbl_bin = tk.Label(self.root, text="Dez", font=(self.font, self.fontsize))
        self.lbl_bin.grid(column=3, row=101)
        
        self.elements =  []

        for i in range(self.anzahl_numbers):
            tk.Label(self.root,text=str(i+1), font=(self.font, self.fontsize)).grid(row=102+i,column=0)
            var1 = tk.StringVar()
            inp1 = tk.Entry(self.root, textvariable=var1, font=(self.font, self.fontsize))
            inp1.grid(row=102+i, column=1)
            var2 = tk.StringVar()
            inp1 = tk.Entry(self.root, textvariable=var2, font=(self.font, self.fontsize))
            inp1.grid(row=102+i, column=2)
            var3 = tk.StringVar()
            inp1 = tk.Entry(self.root, textvariable=var3, font=(self.font, self.fontsize))
            var3.set(str(self.lst_number[i][0]))
            inp1.grid(row=102+i, column=3)
        

    def init_number(self):
        self.lst_number = []
        for i in range(self.anzahl_numbers):
            number = Number()
            format = random.randint(0, 2)
            self.lst_number.append((number.get_dec(),format))
    