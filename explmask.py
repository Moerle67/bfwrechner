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
        str_number = number.get_bin()
        i = 0
        bit = 0
        for char in str_number:
            lbl = tk.Label(self.root, text=char, font=(self.font, self.fontsize))
            lbl.grid(row=101, column=101 + i)
            if char != ".":
                clb = tk.Checkbutton(self.root, text="", font=(self.font, self.fontsize),command = lambda: self.chkbutton(bit))
                clb.grid(row=102, column=101 + i)
                bit += 1
            i += 1
    def chkbutton(self, number):
        print(number)