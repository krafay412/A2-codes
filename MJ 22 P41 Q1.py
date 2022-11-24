#MJ22 P41
#Q1
class Player:
    def __init__(self):
        self.Name = ""
        self.Score = 0
PlayerArray = [Player() for i in range(11)]

def ReadHighScores():
    global PlayerArray
    try:
        sf = open("HighScore.txt","rt")
        PlayerName = sf.readline().strip()
        i = 0
        while PlayerName != "":
            PlayerScore = int(sf.readline().strip())
            PlayerArray[i].Name = PlayerName
            PlayerArray[i].Score = PlayerScore
            i += 1
            PlayerName = sf.readline().strip()
        sf.close()
    except IOError:
        print("File not Found")


def PrintAll():
    print("Before")
    for i in range(10):
        print(PlayerArray[i].Name,PlayerArray[i].Score)

PlayerName = input("Enter PlayerName: ")
while len(PlayerName) != 3:
    PlayerName = input("Enter PlayerName: ")
PlayerScore = int(input("Enter PlayerScore: "))
while PlayerScore < 0 or PlayerScore > 100000:
    PlayerScore = int(input("Enter PlayerScore: "))

def NewHighScoreList(PlayerName,PlayerScore):
    global PlayerArrayNew
    PlayerArray[10].Name = PlayerName
    PlayerArray[10].Score = PlayerScore
    Boundary = len(PlayerArray) - 1
    NoSwap = False
    while not NoSwap:
        NoSwap = True
        for i in range(Boundary):
            if PlayerArray[i].Score < PlayerArray[i+1].Score:
                TempName = PlayerArray[i].Name
                TempScore = PlayerArray[i].Score
                PlayerArray[i].Name = PlayerArray[i+1].Name
                PlayerArray[i].Score = PlayerArray[i+1].Score
                PlayerArray[i+1].Name = TempName
                PlayerArray[i+1].Score = TempScore
                NoSwap = False
        Boundary -= 1
    PlayerArrayNew = PlayerArray.copy()

def PrintAllNew():
    print("New List ")
    for i in range(11):
        print(PlayerArrayNew[i].Name,PlayerArrayNew[i].Score)

ReadHighScores()
PrintAll()
NewHighScoreList(PlayerName,PlayerScore)
PrintAllNew()

def WriteTopTen():
    sf = open("NewHighScore.txt","wt")
    i = 0
    while i <=9:
        PlayerName = PlayerArrayNew[i].Name
        PlayerScore = str(PlayerArrayNew[i].Score)
        sf.write(PlayerName + "\n")
        sf.write(PlayerScore + "\n")
        i += 1
    sf.close()
WriteTopTen()

















