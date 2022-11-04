def AddinSerialFile():
    std = open("StudentsSerial.txt", "at")
    StdName = input("Enter Name: ")
    while StdName != "":
        StdAge = float(input("Enter Age: "))
        StdClass = input("Enter class: ")
        std.write(StdName + "#" + str(StdAge) + "#" + StdClass + "\n")
        StdName = input("Enter Name: ")
    std.close()
    DisplaySerialFile()


def DisplaySerialFile():
    std = open("StudentsSerial.txt", "rt")
    thisline = std.readline()
    while thisline != "":
        StdName = ""
        StdAge = ""
        StdClass = ""
        field = 0
        for i in range(len(thisline) - 1):
            thischar = thisline[i]
            if thischar == "#":
                field += 1
            elif field == 0:
                StdName += thischar
            elif field == 1:
                StdAge += thischar
            else:
                StdClass += thischar
        print(StdName, StdAge, StdClass)
        thisline = std.readline()
    std.close()


def SearchInSerialFile():
    std = open("StudentsSerial.txt", "rt")
    thisline = std.readline()
    SearchName = input("Enter Name to be searched: ")
    while thisline != "":
        StdName = ""
        StdAge = ""
        StdClass = ""
        field = 0
        for i in range(len(thisline) - 1):
            thischar = thisline[i]
            if thischar == "#":
                field += 1
            elif field == 0:
                StdName += thischar
            elif field == 1:
                StdAge += thischar
            else:
                StdClass += thischar
        if StdName == SearchName:
            print(StdName, StdAge, StdClass)
        thisline = std.readline()
    std.close()


def DeleteInSerialFile():
    std = open("StudentsSerial.txt", "rt")
    thisline = std.readline()
    DeleteRecord = input("Enter Name of Record to be deleted: ")
    Deleted = False
    RecordArray = []
    while thisline != "":
        StdName = ""
        StdAge = ""
        StdClass = ""
        field = 0
        for i in range(len(thisline) - 1):
            thischar = thisline[i]
            if thischar == "#":
                field += 1
            elif field == 0:
                StdName += thischar
            elif field == 1:
                StdAge += thischar
            else:
                StdClass += thischar
        if StdName == DeleteRecord:
            Deleted = True
        else:
            RecordArray.append(thisline)
        thisline = std.readline()
    std.close()
    if not Deleted:
        print("Given Name doesnot Exist in File!!")
    else:
        print("Given Record/s Deleted\nUpdated File is: ")
        std = open("StudentsSerial.txt", "wt")
        for i in range(len(RecordArray)):
            thisline = RecordArray[i]
            std.write(thisline)
    std.close()
    DisplaySerialFile()


def EditinSerialFile():
    std = open("StudentsSerial.txt", "rt")
    thisline = std.readline()
    EditRecord = input("Enter Name of Record to be Edited: ")
    Edited = False
    RecordArray = []
    while thisline != "":
        StdName = ""
        StdAge = ""
        StdClass = ""
        field = 0
        for i in range(len(thisline) - 1):
            thischar = thisline[i]
            if thischar == "#":
                field += 1
            elif field == 0:
                StdName += thischar
            elif field == 1:
                StdAge += thischar
            else:
                StdClass += thischar
        if StdName == EditRecord:
            Edited = True
            StdName = input("Enter Name: ")
            StdAge = float(input("Enter Age: "))
            StdClass = input("Enter class: ")
            thisline = StdName + "#" + str(StdAge) + "#" + StdClass
            RecordArray.append(thisline + "\n")
        else:
            RecordArray.append(thisline)
        thisline = std.readline()
    if not Edited:
        print("Given Name doesnot Exist in File!!")
    else:
        print("Given Record/s Edited\nUpdated File is: ")
        std = open("StudentsSerial.txt", "wt")
        for i in range(len(RecordArray)):
            thisline = RecordArray[i]
            std.write(thisline)
    std.close()
    DisplaySerialFile()

    std.close()


Choice = int(
    input(
        "Enter 1 to Addinfile: \nEnter 2 to SearchInFile: \nEnter 3 to DeleteInFile: \nEnter\
 4 to EditinFile: \nEnter 5 to DisplaySerialFile: \nEnter -1 to Exit: "
    )
)
while Choice != -1:
    if Choice == 1:
        AddinSerialFile()
    elif Choice == 2:
        SearchInSerialFile()
    elif Choice == 3:
        DeleteInSerialFile()
    elif Choice == 4:
        EditinSerialFile()
    elif Choice == 5:
        DisplaySerialFile()
    Choice = int(
        input(
            "Enter 1 to Addinfile: \nEnter 2 to SearchInFile: \nEnter 3 to DeleteInFile: \nEnter\
 4 to EditinFile: \nEnter 5 to DisplaySerialFile: \nEnter -1 to Exit: "
        )
    )
