import tkinter as tk
import number

class Btrainer:
    def init_add(self):
        pass

    def __init__(self):
        self.fontsize =24
        self.font = "Curier"
        self.elements = []
        x = 1
        y = 1
        self.root = tk.Tk()
        self.root.title="BFW Rechner"
        self.var_cb = [0] * 8
        wertigkeit = 128
        for i in range(8):
            lbl1 = tk.Label(self.root, text=str(wertigkeit), font=(self.font, self.fontsize))
            lbl1.grid(column=x+i, row=y)

            wertigkeit //= 2
            self.var_cb[i] = tk.IntVar()
            cb1 = tk.Checkbutton(self.root, 
                text="", 
                font=(self.font, self.fontsize), 
                variable=self.var_cb[i],
                command=self.cb_click
            )
            cb1.grid(column=x+i, row=y+1)

            lbl2 = tk.Label(self.root, text="0", font=(self.font, self.fontsize))
            lbl2.grid(column=x+i, row=y+2)

            self.elements.append((lbl1, cb1, lbl2))

        self.lbl_ueber = tk.Label(self.root, text="Binärrechner", font=(self.font, int(self.fontsize*1.5)))
        self.lbl_ueber.grid(row=0, column=1, columnspan=8)

        self.lbl_ges_dez = tk.Label(self.root, text="0", font=(self.font, self.fontsize))
        self.lbl_ges_dez.grid(row=1, column=9)

        self.lbl_ges_hex = tk.Label(self.root, text="00", font=(self.font, self.fontsize))
        self.lbl_ges_hex.grid(row=2, column=9)

        self.lbl_ges_bin = tk.Label(self.root, text="0000.0000", font=(self.font, self.fontsize))
        self.lbl_ges_bin.grid(row=3, column=9)

        self.init_add()  

        self.root.mainloop()
    
    def cal_erg(self):
        erg_dez = 0
        erg_hex = 0
        wertigkeit = 128
        erg_bin = ""
        char_hex = "0123456789ABCDEF"
        werthex = 8        
        for i in range(8):
            wert = self.var_cb[i].get()
            erg_bin = erg_bin +str(wert)
            erg_hex += werthex * wert
            erg_dez += wertigkeit * wert
            wertigkeit //= 2
            werthex //= 2
            if i == 3:       # hex 1. Ziffer
                str_erg_hex = char_hex[erg_hex]
                werthex = 8
                erg_hex = 0
            self.elements[i][2].config(text = str(wert))
        str_erg_hex += char_hex[erg_hex]
        erg_bin = erg_bin[:4]+"."+erg_bin[4:]
        return erg_dez, erg_bin, str_erg_hex
    
    def cb_click(self):
        erg_dez, erg_bin, str_erg_hex = self.cal_erg()
        self.lbl_ges_hex.config(text=str_erg_hex)
        self.lbl_ges_dez.config(text=str(erg_dez))
        self.lbl_ges_bin.config(text=str(erg_bin))

class Btester(Btrainer):

    def init_add(self):
        self.lbl_ges_hex.config(text="")
        self.lbl_ges_dez.config(text="")
        self.lbl_ges_bin.config(text="")
        self.lbl_ueber.config(text="Binärtrainer")

        self.lblaufg = tk.Label(self.root, text="Vorgabe", font=(self.font, self.fontsize))
        self.lblaufg.grid(row=4, column=0,columnspan=4)

        self.quest = number.Number()
        self.lbl_vorg = tk.Label(self.root, text=str(self.quest), font=(self.font, self.fontsize))
        self.lbl_vorg.grid(row=4, column=4, columnspan=2)
        self.antw = tk.Button(self.root, text="Abgabe", font=(self.font, self.fontsize), background="lightgreen", command=self.btn_ant)
        self.antw.grid(row=4, column=7,columnspan=2)
        self.lbl_antw = tk.Label(self.root, text="", font=(self.font, self.fontsize))
        self.lbl_antw.grid(row=5, column=1, columnspan=7)

    def btn_ant(self):
        erg_dez, erg_bin, str_erg_hex = self.cal_erg()
        print(erg_dez)
        if erg_dez == self.quest.get_dec():
            str_antw = "richtig"
            self.quest = number.Number()
            self.lbl_vorg.config(text=str(self.quest))
            for i in range(8): 
                self.var_cb[i]=tk.IntVar()
            self.cal_erg()

        else:
            str_antw = "falsch"
        self.lbl_antw.config(text = str_antw)
    
    def cb_click(self):
        self.cal_erg()


test0 = Btester()
# test1 = Btrainer()