import random
import tkinter as tk 

from bbasis import Bbasis
from number import Number

class Bhdtrainer(Bbasis):
    def __init__(self, top):
        super().__init__(top)
        
        self.fontsize=16

        self.anzahl_numbers = 10

        self.new()
    
    def new(self):
        # Neustart 
        for widget in self.root.winfo_children():
                widget.destroy()

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
            self.elements.append(((inp1,var1), (inp2, var2), (inp3, var3)))    
        self.antw = tk.Button(self.root, text="Abgabe", font=(self.font, self.fontsize), background="lightyellow", command=self.btn_ant)
        self.antw.grid(row=102+self.anzahl_numbers, column=3,columnspan=1)

    def btn_ant(self):
        correct = True
        for i in range(self.anzahl_numbers):
            # Binaer
            if self.lst_number[i][0].get_dec() == Number(self.elements[i][0][1].get(),"b").get_dec():
                # print(f"Binär Zeile {i+1} korrekt")
                self.elements[i][0][0].config(state=tk.DISABLED)
            else:
                print(f"Binär Zeile {i+1} falsch {Number(self.elements[i][0][1].get(),"b").get_dec()}")
                correct = False
            # Secimal
            if self.lst_number[i][0].get_dec() == Number(self.elements[i][1][1].get(),"h").get_dec():
                # print(f"Hex Zeile {i+1} korrekt")
                self.elements[i][1][0].config(state=tk.DISABLED)
            else:
                print(f"Hex Zeile {i+1} falsch {Number(self.elements[i][1][1].get(),"h").get_dec()}")
                correct = False
            # Dezimal
            if self.lst_number[i][0].get_dec() == Number(self.elements[i][2][1].get(),"d").get_dec():
                #print(f"Dec Zeile {i+1} korrekt")
                self.elements[i][2][0].config(state=tk.DISABLED)
            else:
                print(f"Dec Zeile {i+1} falsch {Number(self.elements[i][2][1].get(),"d").get_dec()}")
                correct = False
            if correct:
               self.antw.config(text="Sehr gut - Neustart", background="lightgreen", command = self.new) 

    def init_number(self):
        ##
        # [number, Code: 0 - dec, 1 - hex, 2 -- bin]
        self.lst_number = []
        for i in range(self.anzahl_numbers):
            number = Number()
            format = random.randint(0, 2)
            self.lst_number.append((number,format))
    