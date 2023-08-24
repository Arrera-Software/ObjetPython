from Calcule.calcule import*
from Horloge.AppHorloge import*

appClock = AppHorloge()
appClock.setAttribut("white","black","image/horloge.png","Arrera","bip.mp3")
val = int(input("1.Calcule\n2.Horloge\n"))

match val :
    case 1 :
        Calcule("white","black","Calcule")
    case 2 : 
        val2 = int(input("1.Chrono\n2.Minuteur\n3.Horloge\n"))
        match val2 :
            case 1 :
                appClock.modeChrono()
            case 2 :
                appClock.modeMinuteur()
            case 3 :
                appClock.modeHorloge()
            case other :
                print("Sa correspont pas ") 

    case other :
        print("Sa correspont pas ") 
            