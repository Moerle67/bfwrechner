import tkinter as tk

class Bbasis():
    def __init__(self, top):
        # Basisfonts
        self.top = top
        self.fontsize = 24
        self.font = "Curier"
        if top == -1:
            self.root = tk.Tk()
        else:
        #    self.root = tk.Frame(top.frame)
            top.root.geometry("")
            self.root = top.frame
            self.root.pack()

        self.btn_plus = tk.Button(self.root, text="+", font=(self.font, int(self.fontsize/2)), command=self.fontplus)
        self.btn_plus.grid(row=0, column=97)
        self.btn_minus = tk.Button(self.root, text="-", font=(self.font, int(self.fontsize/2)), command=self.fontminus)
        self.btn_minus.grid(row=0, column=98)

    def changefont(self):
        # erstmal alle anpassen
        # dann die speziellen Widgets
        #
        for widget in self.root.winfo_children():
                widget.config(font=(self.font, self.fontsize))
        self.btn_plus.config(font=(self.font, self.fontsize//2))
        self.btn_minus.config(font=(self.font, self.fontsize//2))

    def fontplus(self):
        self.fontsize += 1
        self.changefont()

    def fontminus(self):
        if self.fontsize > 3:
            self.fontsize -= 1
        self.changefont()