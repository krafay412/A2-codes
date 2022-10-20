import random
class Islandclass:
    def __init__(self):
        sand = "."
        self.__Grid = [[sand for j in range(30)]
        for i in range(10)]

    def GetSquare(self, X, Y):
        return self.__Grid[X][Y]

    def Hidetreasure(self):
        Treasure = "T"
        X = random.randint(0,29)
        Y = random.randint(0,9)
        while self.__Grid[Y][X] == Treasure:
            X = random.randint(0,29)
            Y = random.randint(0,9)
        self.__Grid[Y][X] = Treasure

    def Dighole(self, X, Y):
        Treasurefound = "X"
        Notfound = "O"
        if self.__Grid[X][Y] == "T":
            self.__Grid[X][Y] = Treasurefound
        else:
            self.__Grid[X][Y] = Notfound


def displaygrid():
    for i in range(10):
        for j in range(30):
            print(Island.GetSquare(i, j), end ='')
        print()



def Startdig():
    print("Enter Coloum to Dig")
    X = int(input())
    while X < 0 or X > 29:
        print("Enter Coloum to Dig")
        X = int(input())
    Y = int(input("Enter Row to dig"))
    while Y < 0 or Y > 9:
        print("Enter Row to Dig")
        Y = int(input())

    Island.Dighole(X, Y)
    return

Island = Islandclass()
displaygrid()
for treasure in range(3):
    Island.Hidetreasure()
Startdig()
displaygrid()

