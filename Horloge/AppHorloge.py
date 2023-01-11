from tkinter import*
from Horloge.Chronometre import *
from Horloge.Minuteur import*

class AppHorloge :
    def __init__(self,mainColor,textColor):
        self.screen = Tk()
        self.screen.title("Horloge")
        self.screen.minsize(500,500)
        self.screen.maxsize(500,500)
        self.screen.config(bg=mainColor)
        self.btn1 = Button(self.screen,text="Chronometre",command=self.Chronometre).pack(side="left")
        self.btn2 = Button(self.screen,text="Minuteur",command=self.Minuteur).pack(side="right")
        self.screen.mainloop()
        
    def Chronometre(self):
        CHRONOMETRE(self.screen)
    def Minuteur(self):
        MINUTEUR(self.screen,100)