#Q2
class Balloon:
    #PRIVATE Health As INTEGER
    #PRIVATE Colour As String
    #PRIVATE DefenceItem As String
    
    def __init__(self,Colour,DefenceItem):
        self.__Health = 100
        self.__Colour = Colour
        self.__DefenceItem = DefenceItem
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self,Change):
        self.__Health += Change
    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

DefenceItem = input("Enter DefenceItem for Balloon: ")
Colour = input("Enter Colour For Balloon: ")
Balloon1 = Balloon(Colour,DefenceItem)

def Defend(Balloon1):
    Strenth = int(input("Enter Strenth of Oppponent: "))
    Balloon1.ChangeHealth(-Strenth)
    DefenceItem = Balloon1.GetDefenceItem()
    print("Defence Item of Balloon:",DefenceItem)
    HealthRemaining = Balloon1.CheckHealth()
    if HealthRemaining:
        print("NO HEALTH LEFT!!")
    else:
        print("Balloon is Still in air !!")
    return Balloon1
Balloon1 = Defend(Balloon1)
