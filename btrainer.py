import tkinter as tk

class Btrainer:
    def __init__(self):
        self.fontsize =24
        self.font = "Curier"
        self.elements = []
        x = 1
        y = 1
        root = tk.Tk()
        root.title="BFW Rechner"
        self.var_cb = [0] * 8
        wertigkeit = 128
        for i in range(8):
            lbl1 = tk.Label(root, text=str(wertigkeit), font=(self.font, self.fontsize))
            lbl1.grid(column=x+i, row=y)

            wertigkeit //= 2
            self.var_cb[i] = tk.IntVar()
            cb1 = tk.Checkbutton(root, 
                text="", 
                font=(self.font, self.fontsize), 
                variable=self.var_cb[i],
                command=self.cb_click
            )
            cb1.grid(column=x+i, row=y+1)

            lbl2 = tk.Label(root, text="0", font=(self.font, self.fontsize))
            lbl2.grid(column=x+i, row=y+2)

            self.elements.append((lbl1, cb1, lbl2))

        self.lbl_ueber = tk.Label(root, text="Moerlis Binärrechner", font=(self.font, int(self.fontsize*1.5)))
        self.lbl_ueber.grid(row=0, column=1, columnspan=8)

        self.lbl_ges_dez = tk.Label(root, text="0", font=(self.font, self.fontsize))
        self.lbl_ges_dez.grid(row=1, column=9)

        self.lbl_ges_bin = tk.Label(root, text="0000.0000", font=(self.font, self.fontsize))
        self.lbl_ges_bin.grid(row=3, column=9)

        root.mainloop()
    
    def cb_click(self):
        erg_dez = 0
        wertigkeit = 128
        erg_bin = ""
        for i in range(8):
            wert = self.var_cb[i].get()
            erg_bin = erg_bin +str(wert) 
            erg_dez += wertigkeit * wert
            wertigkeit //= 2
            self.elements[i][2].config(text = str(wert))
        self.lbl_ges_dez.config(text=str(erg_dez))
        erg_bin = erg_bin[:4]+"."+erg_bin[4:]
        self.lbl_ges_bin.config(text=str(erg_bin))

test = Btrainer()