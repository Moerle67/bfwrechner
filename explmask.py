import tkinter as tk 

from bbasis import Bbasis
from number import Number
from ipv4 import IPv4


class Explmask(Bbasis):
    def __init__(self, top):
        super().__init__(top)

        self.fontsize=12
        super().changefont()

        number = IPv4()
        self.cidr = number.cidr
        self.lbl_a = tk.Label(self.root, text="IP-Adresse", font=(self.font, self.fontsize*2))
        self.lbl_a.grid(row=101, column=100)
        self.lbl_m = tk.Label(self.root, text="Maske", font=(self.font, self.fontsize*2))
        self.lbl_m.grid(row=103, column=100)

        str_number = number.get_bin()
        i = 0
        bit = 0
        self.elements = []
        for char in str_number:
            lbl = tk.Label(self.root, text=char, font=(self.font, self.fontsize))
            lbl.grid(row=101, column=101 + i)
            if char != ".":
                clb = self.setcb(bit)
                clb.grid(row=102, column=101 + i)
                val = tk.BooleanVar()
                val_m = tk.StringVar()
                clb.config(variable = val)
                lbl_m = tk.Label(self.root, text=char, font=(self.font, self.fontsize), textvariable=val_m)
                lbl_m.grid(row=103, column=101 + i)
                
                self.elements.append((clb, lbl, val, val_m))
                bit += 1
            else:
                tk.Label(self.root, text=".", font=(self.font, self.fontsize)).grid(row=103, column=101 + i)

            i += 1
            
        self.chkbutton(self.cidr)
            
    def changefont(self):
        # erstmal alle anpassen
        # dann die speziellen Widgets
        #
        super().changefont()

        self.lbl_a.config(font=(self.font, int(self.fontsize*2)))
        self.lbl_m.config(font=(self.font, int(self.fontsize*2)))
    
    def setcb(self, i):
        match i: 
            case 0 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton00)
            case 1 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton01)
            case 2 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton02)
            case 3 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton03)
            case 4 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton04)
            case 5 :
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton05)
            case 6 :
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton06)
            case 7 :
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton07)
            case 8 :
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton08)
            case 9 :
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton09)
            case 10 :
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton10)
            case 11 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton11)
            case 12 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton12)
            case 13 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton13)
            case 14 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton14)
            case 15 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton15)
            case 16 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton16)
            case 17 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton17)
            case 18 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton18)
            case 19 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton19)
            case 20 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton20)
            case 21 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton21)
            case 22 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton22)
            case 23 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton23)
            case 24 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton24)
            case 25 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton25)
            case 26 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton26)
            case 27 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton27)
            case 28 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton28)
            case 29 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton29)
            case 30 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton30)
            case 31 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton31)
            case 32 : 
                return tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = self.chkbutton32)

    def chkbutton00(self):
        self.chkbutton(0)
    def chkbutton01(self):
        self.chkbutton(1)
    def chkbutton02(self):
        self.chkbutton(2)
    def chkbutton03(self):
        self.chkbutton(3)
    def chkbutton04(self):
        self.chkbutton(4)
    def chkbutton05(self):
        self.chkbutton(5)
    def chkbutton06(self):
        self.chkbutton(6)
    def chkbutton07(self):
        self.chkbutton(7)
    def chkbutton08(self):
        self.chkbutton(8)
    def chkbutton09(self):
        self.chkbutton(9)
    def chkbutton10(self):
        self.chkbutton(10)
    def chkbutton11(self):
        self.chkbutton(11)
    def chkbutton12(self):
        self.chkbutton(12)
    def chkbutton13(self):
        self.chkbutton(13)
    def chkbutton14(self):
        self.chkbutton(14)
    def chkbutton15(self):
        self.chkbutton(15)
    def chkbutton16(self):
        self.chkbutton(16)
    def chkbutton17(self):
        self.chkbutton(17)
    def chkbutton18(self):
        self.chkbutton(18)
    def chkbutton19(self):
        self.chkbutton(19)
    def chkbutton20(self):
        self.chkbutton(20)
    def chkbutton21(self):
        self.chkbutton(21)
    def chkbutton22(self):
        self.chkbutton(21)
    def chkbutton23(self):
        self.chkbutton(23)
    def chkbutton24(self):
        self.chkbutton(24)
    def chkbutton25(self):
        self.chkbutton(25)
    def chkbutton26(self):
        self.chkbutton(26)
    def chkbutton27(self):
        self.chkbutton(27)
    def chkbutton28(self):
        self.chkbutton(28)
    def chkbutton29(self):
        self.chkbutton(29)
    def chkbutton30(self):
        self.chkbutton(30)
    def chkbutton31(self):
        self.chkbutton(31)
    def chkbutton32(self):
        self.chkbutton(32)





    def chkbutton(self, number):
        for i in range(32):
            if i<=number:
                self.elements[i][2].set(True)
                self.elements[i][3].set("1")
                self.elements[i][1].config(background="red")
            else:
                self.elements[i][2].set(False)
                self.elements[i][3].set("0")
                self.elements[i][1].config(background="green")
