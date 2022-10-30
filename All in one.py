def binarysearch(val, ub, lb):
    global mylist
    mid = int((lb + ub) / 2)
    if lb > ub:
        return -1
    elif mylist[mid] == val:
        return mid
    elif mylist[mid] > val:
        return binarysearch(val, mid - 1, lb)
    else:
        return binarysearch(val, ub, mid + 1)

def CreateList():
    global mylist
    mylist = []
    y = int(input("how many number you want in list: "))
    for i in range(y):
        val1 = int(input("enter value : "))
        mylist.append(val1)
    print(mylist)

def LinearSearch(Val):
    for i in range(len(mylist)):
        if Val == mylist[i]:
            return i
    return -1

def Bubblesort():
    global mylist
    boundary = len(mylist) - 1
    Swap = False
    while not Swap:
        Swap = True
        for i in range(boundary):
            if mylist[i] > mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
                Swap =  False
        boundary -= 1
    print(mylist)
def Insertionsort():
    global mylist
    for i in range(1, len(mylist)):
        temp = mylist[i]
        thisptr = i
        while thisptr > 0 and mylist[thisptr-1] > temp:
            mylist[thisptr] = mylist[thisptr -1]
            thisptr -= 1
        mylist[thisptr] = temp
    print(mylist)
mysentence = '''Please Enter your choice
                1 - Create List
                2 - Bubble sort
                3 - Linear search
                4 - Binary Search
                5 - Insertionsort
                -1 - End:
                '''

mylist = []
choice = int(input(mysentence))
while choice != -1:
    if choice == 1:
        CreateList()
    elif choice == 2:
        Bubblesort()
    elif choice == 3:
        X = int(input("Enter Value to be searched: "))
        Y = LinearSearch(X)
        print(Y)
    elif choice == 4:
        X = int(input("Enter Value to be searched: "))
        UB = len(mylist) - 1
        lb = 0
        print(binarysearch(X,UB, lb))
    elif choice == 5:
        Insertionsort()
    choice = int(input(mysentence))

