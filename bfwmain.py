import tkinter as tk

from btrainer import Btester, Btrainer
class Main_app():

    def newfile(self):
        pass

    def openfile(self):
        pass
    
    def about(self):
        pass

    def btrainer(self):
        self.btraining = Btrainer(self) 
        self.zahlenmenu.entryconfig("Binärrechner", state='disabled')


    def btester(self):
        self.btest = Btester(self) 
        self.zahlenmenu.entryconfig("Binärtrainer", state='disabled')
        
    def setmenue(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.newfile)
        self.filemenu.add_command(label="Open...", command=self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.destroy)

        self.zahlenmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Zahlensysteme", menu=self.zahlenmenu)
        self.zahlenmenu.add_command(label="Binärrechner", command=self.btrainer)
        self.zahlenmenu.add_command(label="Binärtrainer", command=self.btester)
        
        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.about)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title="BFW Trainingscenter"

        self.setmenue()
        self.root.mainloop()

        


# test0 = Btester()
# test1 = Btrainer()
main = Main_app()