import random
import tkinter as tk 

from bbasis import Bbasis
from number import Number

class Bhdtrainer(Bbasis):
    def __init__(self, top):
        super().__init__(top)
        
        self.fontsize=16

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
            var2 = tk.StringVar()
            var3 = tk.StringVar()
            inp1 = tk.Entry(self.root, textvariable=var1, font=(self.font, self.fontsize))
            inp1.grid(row=102+i, column=1)
            inp2 = tk.Entry(self.root, textvariable=var2, font=(self.font, self.fontsize))
            inp2.grid(row=102+i, column=2)
            inp3 = tk.Entry(self.root, textvariable=var3, font=(self.font, self.fontsize))
            inp3.grid(row=102+i, column=3)
            if self.lst_number[i][1] == 2:
                inp1.config(state=tk.DISABLED)
                var1.set(self.lst_number[i][0].get_bin())
            elif self.lst_number[i][1] == 1:
                inp2.config(state=tk.DISABLED)
                var2.set(self.lst_number[i][0].get_hex())
            else:
                inp3.config(state=tk.DISABLED)
                var3.set(str(self.lst_number[i][0]))
        self.antw = tk.Button(self.root, text="Abgabe", font=(self.font, self.fontsize), background="lightgreen", command=self.btn_ant)
        self.antw.grid(row=102+self.anzahl_numbers, column=3,columnspan=1)

    def btn_ant(self):
        pass    

    def init_number(self):
        ##
        # [number, Code: 0 - dec, 1 - hex, 2 -- bin]
        self.lst_number = []
        for i in range(self.anzahl_numbers):
            number = Number()
            format = random.randint(0, 2)
            self.lst_number.append((number,format))
    