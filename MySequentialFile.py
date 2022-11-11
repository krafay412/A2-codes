import os
def AddinSequentialFile(StdId,StdName,StdClass):
    try:
        sf = open("StudentsSeqfile.txt","rt")
    except:
        sf= open("StudentsSeqfile.txt","xt")
        sf = open("StudentsSeqfile.txt","rt")
    tf = open("StudentsSeqfileTemp.txt","wt")
    RecStdID = sf.readline()
    Added = False
    while RecStdID != "":
        RecStdID = int(RecStdID)
        RecStdName = sf.readline()
        RecStdClass = sf.readline()
        if StdId == RecStdID:
            print("Id already Exists")
            Added = True
        if not Added and StdId < RecStdID:
            tf.write(str(StdId) + "\n")
            tf.write(StdName + "\n")
            tf.write(StdClass + "\n")
            Added = True
        tf.write(str(RecStdID) + "\n")
        tf.write(RecStdName)
        tf.write(RecStdClass)
        RecStdID = sf.readline()
    if not Added:
        tf.write(str(StdId) + "\n")
        tf.write(StdName + "\n")
        tf.write(StdClass + "\n")
    sf.close()
    tf.close()
    os.remove("StudentsSeqfile.txt")
    os.rename("StudentsSeqfileTemp.txt", "StudentsSeqfile.txt")

def AddMenu():
    StdId = int(input("Enter ID\n-1 To Exit: "))
    while StdId != -1:
        StdName = input("Enter Name: ")
        StdClass = input("Enter Class: ")
        AddinSequentialFile(StdId,StdName,StdClass)
        StdId = int(input("Enter ID\n-1 To Exit: "))

def DeleteinSequentialFile():
    sf = open("StudentsSeqfile.txt","rt")
    tf = open("StudentsSeqfileTemp.txt","wt")
    Deleted = False
    StdId = int(input("Enter Id to be removed: "))
    RecStdID = sf.readline()
    while RecStdID != "":
        RecStdID = int(RecStdID)
        RecStdName = sf.readline()
        RecStdClass = sf.readline()
        if StdId != RecStdID:
            tf.write(str(RecStdID) + "\n")
            tf.write(RecStdName)
            tf.write(RecStdClass)
        else:
            Deleted = True
        RecStdID = sf.readline()
    if Deleted:
        print("ID Removed")
    else:
        print("ID not found")
    sf.close()
    tf.close()
    os.remove("StudentsSeqfile.txt")
    os.rename("StudentsSeqfileTemp.txt", "StudentsSeqfile.txt")

def EditinSequentialFile():
    sf = open("StudentsSeqfile.txt","rt")
    tf = open("StudentsSeqfileTemp.txt","wt")
    Edited = False
    StdId = int(input("Enter Id to be edited: "))
    RecStdID = sf.readline()
    while RecStdID != "":
        RecStdID = int(RecStdID)
        RecStdName = sf.readline()
        RecStdClass = sf.readline()
        if StdId != RecStdID:
            tf.write(str(RecStdID) + "\n")
            tf.write(RecStdName)
            tf.write(RecStdClass)
        else:
            StdName = input("Enter Name: ")
            StdClass = input("Enter Class: ")
            tf.write(str(StdId) + "\n")
            tf.write(StdName + "\n")
            tf.write(StdClass + "\n")
            Edited = True
        RecStdID = sf.readline()
    if Edited:
        print("ID Edited")
    else:
        print("ID not found")
    sf.close()
    tf.close()
    os.remove("StudentsSeqfile.txt")
    os.rename("StudentsSeqfileTemp.txt", "StudentsSeqfile.txt")

Choice = int(input("Enter 1 To AddinFile\n2-DeleteInFile\n3-EditInFile\n-1 - Exit"))
while Choice != -1:
    if Choice == 1:
        AddMenu()
    elif Choice == 2:
        DeleteinSequentialFile()
    elif Choice == 3:
        EditinSequentialFile()
    Choice = int(input("Enter 1 To AddinFile\n2-DeleteInFile\n3-EditInFile\n-1 - Exit"))





















