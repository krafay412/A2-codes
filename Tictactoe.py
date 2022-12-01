import random
import os
User1SinglePlayer = 0
Computer = 0
U2Multiplayer = 0
def InitialiseBoard():
    global TicTacToe
    TicTacToe = [["." for i in range(3)]for j in range(3)]
def DisplayTicTacToe():
    os.system('cls')
    print("\n#############TIC TAC TOE#################\n")
    for i in range(3):
        for j in range(3):
            print(TicTacToe[i][j]," ",end = '')
        print()
# DisplayTicTacToe()

def TictacToe(thischar,X,Y):
    global TicTacToe
    if TicTacToe[X][Y] != ".":
        return -1
    else:
        TicTacToe[X][Y] = thischar
    DisplayTicTacToe()
    return 1

def Winnercheck():
    if (TicTacToe[0][0] == "X" and TicTacToe[0][1] == "X" and TicTacToe[0][2] == "X") or \
    (TicTacToe[1][0] == "X" and TicTacToe[1][1] =="X" and TicTacToe[1][2]== "X") or \
    (TicTacToe[2][0] == "X" and TicTacToe[2][1] == "X" and TicTacToe[2][2] == "X") or \
    (TicTacToe[0][0] == "X" and TicTacToe[1][0] == "X" and TicTacToe[2][0]== "X") or \
    (TicTacToe[0][1] == "X" and TicTacToe[1][1] == "X" and TicTacToe[2][1] == "X") or \
    (TicTacToe[0][2] == "X" and TicTacToe[1][2] == "X" and TicTacToe[2][2] == "X") or \
    (TicTacToe[0][0] == "X" and TicTacToe[1][1] == "X"and TicTacToe[2][2] == "X") or \
    (TicTacToe[2][0] == "X" and TicTacToe[1][1] =="X" and TicTacToe[0][2] == "X"):
        return 1
    elif (TicTacToe[0][0] == "0" and TicTacToe[0][1] == "0" and TicTacToe[0][2] == "0") or \
    (TicTacToe[1][0] == "0" and TicTacToe[1][1] =="0" and TicTacToe[1][2]== "0") or \
    (TicTacToe[2][0] == "0" and TicTacToe[2][1] == "0" and TicTacToe[2][2] == "0") or \
    (TicTacToe[0][0] == "0" and TicTacToe[1][0] == "0" and TicTacToe[2][0]== "0") or \
    (TicTacToe[0][1] == "0" and TicTacToe[1][1] == "0" and TicTacToe[2][1] == "0") or \
    (TicTacToe[0][2] == "0" and TicTacToe[1][2] == "0" and TicTacToe[2][2] == "0") or \
    (TicTacToe[0][0] == "0" and TicTacToe[1][1] == "0"and TicTacToe[2][2] == "0") or \
    (TicTacToe[2][0] == "0" and TicTacToe[1][1] =="0" and TicTacToe[0][2] == "0"):
        return 2
    else:
        return -1
def StartgameMultiplayer():
    global User1SinglePlayer,U2Multiplayer
    U1 = "X"
    U2 = "0"
    print("Symbol User 1: ", U1)
    print("Symbol User 2: ", U2)
    DisplayTicTacToe()
    i = random.randint(0,1)
    if i == 0:
        UB = 9
    else:
        UB = 10
    Win = -1
    while i < UB and Win == -1:
        if (i % 2) == 0:
            X = int(input("Enter Row User 1 'X': "))
            while X < 1 or X > 3:
                print("Enter again")
                X = int(input("Enter Row User 1 'X': "))
            Y = int(input("Enter Col User 1 'X': "))
            while Y < 1 or Y > 3:
                print("Enter again")
                Y = int(input("Enter Row User 1 'X': "))

            receive = TictacToe(U1,X-1,Y-1)
            while receive == -1:
                X = int(input("Enter Row User 1 'X': "))
                while X < 1 or X > 3:
                    print("Enter again")
                    X = int(input("Enter Row User 1 'X': "))
                Y = int(input("Enter Col User 1 'X': "))
                while Y < 1 or Y > 3:
                    print("Enter again")
                    Y = int(input("Enter Row User 1 'X': "))
                receive = TictacToe(U1,X-1,Y-1)
            i += 1
        else:
            X = int(input("Enter Row User 2 '0': "))
            while X < 1 or X > 3:
                print("Enter again")
                X = int(input("Enter Row User 2 '0': "))
            Y = int(input("Enter Col User 2 '0': "))
            while Y < 1 or Y > 3:
                print("Enter again")
                Y = int(input("Enter Row User 2 '0': "))
            receive = TictacToe(U2,X-1,Y-1)
            while receive == -1:
                X = int(input("Enter Row User 1 '0': "))
                while X < 1 or X > 3:
                    print("Enter again")
                    X = int(input("Enter Row User 2 '0': "))
                Y = int(input("Enter Col User 1 '0': "))
                while Y < 1 or Y > 3:
                    print("Enter again")
                    Y = int(input("Enter Row User 2 '0': "))
                receive = TictacToe(U2,X-1,Y-1)
            i += 1
        Win = Winnercheck()
    if Win == -1:
        print("Draw")
    elif Win == 1:
        print("User 1 Won")
        User1SinglePlayer += 1
    elif Win == 2:
        print("User 2 Won")
        U2Multiplayer += 1

def SinglePlayerGame():
    global User1SinglePlayer,Computer
    U1 = "X"
    Comp = "0"
    print("Symbol User 1: ", U1)
    DisplayTicTacToe()
    i = random.randint(0,1)
    if i == 0:
        UB = 9
    else:
        UB = 10
    Win = -1
    while i < UB and Win == -1:
        if (i % 2) == 0:
            X = int(input("Enter Row User 1 'X': "))
            while X < 1 or X > 3:
                print("Enter again")
                X = int(input("Enter Row User 1 'X': "))

            Y = int(input("Enter Col User 1 'X': "))
            while Y < 1 or Y > 3:
                print("Enter again")
                Y = int(input("Enter Row User 1 'X': "))
            receive = TictacToe(U1,X-1,Y-1)
            while receive == -1:
                X = int(input("Enter Row User 1 'X': "))
                while X < 1 or X > 3:
                    print("Enter again")
                    X = int(input("Enter Row User 1 'X': "))
                Y = int(input("Enter Col User 1 'X': "))
                while Y < 1 or Y > 3:
                    print("Enter again")
                    Y = int(input("Enter Row User 1 'X': "))
                receive = TictacToe(U1,X-1,Y-1)
            i += 1
        else:
            X = random.randint(0,2)
            Y = random.randint(0,2)
            receive = TictacToe(Comp,X,Y)
            while receive == -1:
                X = random.randint(0,2)
                Y = random.randint(0,2)
                receive = TictacToe(Comp,X-1,Y-1)
            print("---------------------")
            i += 1
        Win = Winnercheck()
    if Win == -1:
        print("Draw")
    elif Win == 1:
        User1SinglePlayer += 1
        print("User 1 Won")
    elif Win == 2:
        Computer += 1
        print("Computer Won")


def Menu():
    option = int(input("1: Play With Computer\n2:Multiplayer\n3:END: "))
    while option < 1 or option > 3:
        option = int(input("1: Play With Computer\n2:Multiplayer\n:END: "))
    while option != 3:
        if option == 1:
            InitialiseBoard()
            SinglePlayerGame()
            print("USER 1 SCORE:",User1SinglePlayer)
            print("COMPUTER SCORE:",Computer)
        elif option == 2:
            InitialiseBoard()
            StartgameMultiplayer()
            print("USER 1 SCORE:",User1SinglePlayer)
            print("USER 2 SCORE:",U2Multiplayer)
        print("##################################\n\n")
        print("USER 1 SCORE:",User1SinglePlayer)
        print("COMPUTER SCORE:",Computer)
        print("USER 2 SCORE:",U2Multiplayer)
        print("---------------------")
        option = int(input("1: Play With Computer\n2:Multiplayer\n3:END: "))
Menu()


