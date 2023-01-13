from Calcule.calcule import*
from Horloge.AppHorloge import*

val = int(input("1.Calcule\n2.Horloge\n"))

match val :
    case 1 :
        Calcule("white","black","Calcule")
    case 2 : 
        AppHorloge("white","black","Horloge","acceuil")
    case other :
        print("Sa correspont pas ") 
            