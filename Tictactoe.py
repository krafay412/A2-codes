
TicTacToe = [["." for i in range(3)]for j in range(3)]
def DisplayTicTacToe():
    for i in range(3):
        for j in range(3):
            print(TicTacToe[i][j]," ",end = '')
        print()
#DisplayTicTacToe()

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
def Startgame():
    U1 = "X"
    U2 = "0"
    print("Symbol User 1: ", U1)
    print("Symbol User 2: ", U2)
    DisplayTicTacToe()
    i = 0
    Win = -1
    while i < 9 and Win == -1:
        if (i % 2) == 0:
            X = int(input("Enter Row User 1 'X': "))
            while X < 0 or X > 2:
                print("Enter again")
                X = int(input("Enter Row User 1 'X': "))
            Y = int(input("Enter Col User 1 'X': "))
            while Y < 0 or Y > 2:
                print("Enter again")
                Y = int(input("Enter Row User 1 'Y': "))

            receive = TictacToe(U1,X,Y)
            while receive == -1:
                X = int(input("Enter Row User 1 'X': "))
                Y = int(input("Enter Col User 1 'X': "))
                receive = TictacToe(U1,X,Y)
            i += 1
        else:
            X = int(input("Enter Row User 2 'X': "))
            while X < 0 or X > 2:
                print("Enter again")
                X = int(input("Enter Row User 2 'X': "))
            Y = int(input("Enter Col User 2 'X': "))
            while Y < 0 or Y > 2:
                print("Enter again")
                Y = int(input("Enter Row User 2 'Y': "))
            receive = TictacToe(U2,X,Y)
            while receive == -1:
                X = int(input("Enter Row User 1 'X': "))
                Y = int(input("Enter Col User 1 'X': "))
                receive = TictacToe(U2,X,Y)
            i += 1
        Win = Winnercheck()
    if Win == -1:
        print("Draw")
    elif Win == 1:
        print("User 1 Won")
    elif Win == 2:
        print("User 2 Won")

Startgame()
