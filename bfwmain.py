import tkinter as tk

from btrainer import Btester, Btrainer
from bhdtrainer import Bhdtrainer

class Main_app():

    def newfile(self):
        pass

    def openfile(self):
        pass
    
    def about(self):
        pass

    def free_menu(self):
        # Alle Menus aktivieren
        # 
        self.zahlenmenu.entryconfig(self.str_bhd_trainer, state='active')
        self.zahlenmenu.entryconfig(self.str_brechner, state='active')
        self.zahlenmenu.entryconfig(self.str_btrainer, state='active')

    def bhdtrainer(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root)

        self.btraining = Bhdtrainer(self)
        self.free_menu() 
        self.zahlenmenu.entryconfig(self.str_bhd_trainer, state='disabled')
        self.root.title(self.bhdtrainer)
        

    def btrainer(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root)

        self.btraining = Btrainer(self)
        self.free_menu() 
        self.zahlenmenu.entryconfig("Binärrechner", state='disabled')
        self.root.title('BFW Trainer')


    def btester(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root)

        self.btest = Btester(self) 
        self.free_menu()
        self.zahlenmenu.entryconfig(self.str_btrainer, state='disabled')
        self.root.title("BFW Tester")
        
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
        self.zahlenmenu.add_command(label=self.str_brechner, command=self.btrainer)
        self.zahlenmenu.add_command(label=self.str_btrainer, command=self.btester)
        self.zahlenmenu.add_command(label=self.str_bhd_trainer, command=self.bhdtrainer)
        
        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.about)

    def __init__(self):
        self.str_btrainer = "Binärtrainer"
        self.str_brechner = "Binärrechner"
        self.str_bhd_trainer = "BIN HEX DEZ Trainer"
        self.root = tk.Tk()
        self.root.title("BFW Trainingscenter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.lbl1 = tk.Label(self.frame, text="Viel Spaß beim Üben!\nEuer Moerle")
        self.lbl1.pack()

        self.setmenue()
        self.root.mainloop()

        


# test0 = Btester()
# test1 = Btrainer()
main = Main_app()