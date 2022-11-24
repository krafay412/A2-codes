#Q3
#HeadPointer As Integer
#TailPointer As Integer
#NumberItems As Integer
#QueueArray OF Array:String
HeadPointer = 0
TailPointer = 0
NumberItems = 0
QueueArray = ["" for i in range(10)]

def Enqueue(QueueArray,HeadPointer,TailPointer,NumberItems,DataToAdd):
    if NumberItems == 10:
        return (QueueArray,HeadPointer,TailPointer,NumberItems,False)
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumberItems += 1
    return (QueueArray,HeadPointer,TailPointer,NumberItems,True)

def Dequeue():
    global QueueArray,HeadPointer,TailPointer,NumberItems
    if NumberItems == 0:
        return (False)
    else:
        Data = QueueArray[HeadPointer]
        QueueArray[HeadPointer] = ""
        HeadPointer += 1
        if HeadPointer >9:
            HeadPointer = 0
        NumberItems -= 1
        return Data

for i in range(11):
    DataToAdd = input("Enter Data: ")
    QueueArray,HeadPointer,TailPointer,NumberItems,Sucess = Enqueue(QueueArray,HeadPointer,TailPointer,NumberItems,DataToAdd)
    if Sucess:
        print("Data Added Sucessfully")
    else:
        print("Data not Added\nQueue Full")

for i in range(2):
    Value = Dequeue()
    if not Value:
        print("Queue Empty")
        continue
    print(f'Value {i+1} is:',Value)
