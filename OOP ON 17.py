import random

class animal:
    def __init__(self):
        x = random.randint(0,39)
        y = random.randint(0,39)
        self.score = 0
        self.across = x
        self.down = y
    def Setacross(A):
        self.across = A
    def getacross():
        return self.across
    def Move(self) :
        self.Across += GenerateChangeInCoordinate(self.Across)
        self.Down += GenerateChangeInCoordinate(self.Down)
        if Grid[self.Across][self.Down] == 'F':
            self.EatFood()



class desert:
    def __init__(self):
        self.__Grid = [["" for i in range(40)]for j in range(40)]
        self.Animallist = []
        self.stepcounter = 0
        for i in range(5):
            newanimal = animal()
        self.Animallist.append(newanimal)
        self.Generatefood()

def GenerateDirection(Coord) :
 lowerBound = -1
 upperBound = 1
 if Coord == 0:
    lowerBound = 0
 elif Coord == 39:
    upperBound = 0
 return random.randint(lowerBound, upperBound)



