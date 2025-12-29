import tkinter as tk
import number

class Btrainer:
    def init_add(self):
        pass

    def changefont(self):
        # erstmal alle anpassen
        # dann die speziellen Widgets
        #

        for widget in self.root.winfo_children():
            widget.config(font=(self.font, self.fontsize))

        self.lbl_ueber.config(font=(self.font, int(self.fontsize*1.5)))
        self.btn_plus.config(font=(self.font, int(self.fontsize/2)))
        self.btn_minus.config(font=(self.font, int(self.fontsize/2)))
        self.btn_close.config(font=(self.font, int(self.fontsize/2)))

    def fontplus(self):
        self.fontsize += 1
        self.changefont()

    def fontminus(self):
        if self.fontsize > 3:
            self.fontsize -= 1
            self.changefont()

    def destroy(self):
        self.root.destroy()
        if self.top != -1:
            self.top.zahlenmenu.entryconfig("Binärrechner", state='normal')

    def __init__(self, top=-1):
        self.top = top
        self.fontsize =24
        self.font = "Curier"
        self.elements = []
        x = 1
        y = 1
        if top == -1:
            self.root = tk.Tk()
        else:
            self.root = tk.Frame(top.root)
            self.root.pack()
        self.var_cb = []
        wertigkeit = 128
        for i in range(8):
            lbl1 = tk.Label(self.root, text=str(wertigkeit), font=(self.font, self.fontsize))
            lbl1.grid(column=x+i, row=y)

            wertigkeit //= 2
            # self.var_cb.append(tk.IntVar())
            var = tk.IntVar()
            cb1 = tk.Checkbutton(self.root, 
                text="", 
                font=(self.font, self.fontsize), 
                variable=var,
                command=self.cb_click
            )
            cb1.grid(column=x+i, row=y+1)

            lbl2 = tk.Label(self.root, text="0", font=(self.font, self.fontsize))
            lbl2.grid(column=x+i, row=y+2)

            self.elements.append((lbl1, cb1, lbl2, var))

        self.lbl_ueber = tk.Label(self.root, text="Binärrechner", font=(self.font, int(self.fontsize*1.5)))
        self.lbl_ueber.grid(row=0, column=1, columnspan=8)

        self.lbl_ges_dez = tk.Label(self.root, text="0", font=(self.font, self.fontsize))
        self.lbl_ges_dez.grid(row=1, column=9)

        self.lbl_ges_hex = tk.Label(self.root, text="00", font=(self.font, self.fontsize))
        self.lbl_ges_hex.grid(row=2, column=9)

        self.lbl_ges_bin = tk.Label(self.root, text="0000.0000", font=(self.font, self.fontsize))
        self.lbl_ges_bin.grid(row=3, column=9)

        self.btn_plus = tk.Button(self.root, text="+", font=(self.font, int(self.fontsize/2)), command=self.fontplus)
        self.btn_plus.grid(row=0, column=97)
        self.btn_minus = tk.Button(self.root, text="-", font=(self.font, int(self.fontsize/2)), command=self.fontminus)
        self.btn_minus.grid(row=0, column=98)
        self.btn_close = tk.Button(self.root, text="x", font=(self.font, int(self.fontsize/2)), command=self.destroy)
        self.btn_close.grid(row=0, column=99)

        self.init_add()  

        # self.root.mainloop()
    
    def cal_erg(self):
        erg_dez = 0
        erg_hex = 0
        wertigkeit = 128
        erg_bin = ""
        char_hex = "0123456789ABCDEF"
        werthex = 8   
        for i in range(8):
            # test = tk.IntVar()
            # test=self.elements[i][1].get()
            # print(self.elements[i][3].get())
            wert = self.elements[i][3].get()
            # wert = self.var_cb[i].get()
            erg_bin = erg_bin + str(wert)
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
    def destroy(self):
        self.root.destroy()
        if self.top != -1:
            self.top.zahlenmenu.entryconfig("Binärtrainer", state='normal')

    def changefont(self):
        super().changefont()


    def init_add(self):
        self.right_counter = 1
        self.lbl_ges_hex.config(text="")
        self.lbl_ges_dez.config(text="")
        # self.lbl_ges_bin.config(text="")
        self.lbl_ueber.config(text="Binärtrainer")

        self.lbl_aufg = tk.Label(self.root, text=str(self.right_counter)+". Vorgabe", font=(self.font, self.fontsize))
        self.lbl_aufg.grid(row=4, column=0,columnspan=4)

        self.quest = number.Number()
        self.count_wrong = 0
        self.lbl_vorg = tk.Label(self.root, text=str(self.quest), font=(self.font, self.fontsize))
        self.lbl_vorg.grid(row=4, column=4, columnspan=2)
        self.antw = tk.Button(self.root, text="Abgabe", font=(self.font, self.fontsize), background="lightgreen", command=self.btn_ant)
        self.antw.grid(row=4, column=9,columnspan=1)
        self.lbl_antw = tk.Label(self.root, text="", font=(self.font, self.fontsize))
        self.lbl_antw.grid(row=5, column=1, columnspan=7)

    def btn_ant(self):
        erg_dez, erg_bin, str_erg_hex = self.cal_erg()
        self.erg_dez = erg_dez
        if erg_dez == self.quest.get_dec():
            self.count_wrong = 0
            str_antw = "richtig"
            self.quest = number.Number()
            self.right_counter += 1
            self.lbl_aufg.config(text=str(self.right_counter)+". Vorgabe")
            self.lbl_vorg.config(text=str(self.quest))
            self.lbl_ges_dez.config(text="")
            for i in range(8): 
                self.elements[i][3].set(0)
            self.cal_erg()

        else:
            self.count_wrong +=1
            str_antw = "falsch"
            if self.count_wrong >= 2:
                self.lbl_ges_dez.config(text=str(self.erg_dez))

        self.lbl_antw.config(text = str_antw)
    
    def cb_click(self):
        erg_dez, erg_bin, str_erg_hex = self.cal_erg()
        self.lbl_ges_bin.config(text=str(erg_bin))


