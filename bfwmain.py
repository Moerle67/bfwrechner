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


    def btester(self):
        self.btest = Btester(self) 
        self.root.mainloop() 

    def __init__(self):
        self.root = tk.Tk()
        self.root.title="BFW Trainingscenter"

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.newfile)
        filemenu.add_command(label="Open...", command=self.openfile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.destroy)

        zahlenmenu = tk.Menu(menu)
        menu.add_cascade(label="Zahlensysteme", menu=zahlenmenu)
        zahlenmenu.add_command(label="Binärrechner", command=self.btrainer)
        zahlenmenu.add_command(label="Binärtrainer", command=self.btester)
        
        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about)

        self.root.mainloop()

        


# test0 = Btester()
# test1 = Btrainer()
main = Main_app()