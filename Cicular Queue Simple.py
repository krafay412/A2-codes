
def AddinQueue(Val):
    global Items,Basepointer
    if Items == Qsize:
        print("Queue Full")
    else:
        Items += 1
        if Basepointer == Ub:
            Basepointer = -1
        Basepointer += 1
        Queue[Basepointer] = Val
        ShowQueue()
def DeleteinQueue():
    global Items,Toppointer
    if Items == 0:
        print("UnderFlow")
        return -1
    else:
        Items -= 1
        if Toppointer > Ub:
            Toppointer = 0
        ThisVal = Queue[Toppointer]
        Queue[Toppointer] = ""
        Toppointer += 1
        ShowQueue()
        return ThisVal

def ShowQueue():
    print("Toppointer: ", Toppointer)
    print("BasePointer", Basepointer)
    for i in range(Qsize):
        print(Queue[i])

def CreateQueue():
    global Queue,Qsize,Items,Toppointer,Basepointer,Ub,Items
    X = int(input("Enter Length of Queue: "))
    Items = 0
    Queue = []
    Qsize = X
    Ub = X - 1
    for i in range(Qsize):
        Queue.append("")
    Toppointer = 0
    Basepointer = -1

Choice = int(input("1-Add\n2-Delete\n3-Initialise Queue\n4-Exit: "))
while Choice != 4:
    if Choice == 1:
        X = int(input("Enter Val: "))
        AddinQueue(X)
    elif Choice == 3:
        CreateQueue()
    elif Choice == 2:
        print("Value = ",DeleteinQueue())
    else:
        print("InvalidOption")
    Choice = int(input("1-Add\n2-Delete\n3-Initialise Queue\n4-Exit: "))



