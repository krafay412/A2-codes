import os


def AddinFile():
    std = open("Students.txt", "wt")
    StdId = int(input("Enter ID. \nEnter -1 to Exit \n"))
    while StdId != -1:
        Stdname = input("Enter Name: ")
        StdClass = input("Enter class: ")
        std.write(str(StdId) + "\n")
        std.write(Stdname + "\n")
        std.write(StdClass + "\n")
        StdId = int(input("Enter ID. \nEnter -1 to Exit \n"))
    std.close()


def DeleteinFile():  # Using 2 Files
    std = open("Students.txt", "rt")
    item = int(input("Enter ID to be deleted"))
    temp = open("Studenttemp.txt", "wt")
    deleted = False
    while True:
        try:
            StdId = int(std.readline())
            Stdname = std.readline()
            StdClass = std.readline()
            if StdId != item:
                temp.write(str(StdId).strip() + "\n")
                temp.write(Stdname.strip() + "\n")
                temp.write(StdClass.strip() + "\n")
            else:
                deleted = True
        except:
            break
    std.close()
    temp.close()
    if not deleted:
        print("No Item Deleted")
    else:
        print("Id Removed")
        std = open("Students.txt", "wt")
        temp = open("Studenttemp.txt", "rt")
        while True:
            Stdid = temp.readline()
            if Stdid == "":
                break
            Stdname = temp.readline()
            StdClass = temp.readline()

            std.write(Stdid.strip() + "\n")
            std.write(Stdname.strip() + "\n")
            std.write(StdClass.strip() + "\n")
    std.close()
    temp.close()
    os.remove(r"C:\Users\texon ware\mu_code\Studenttemp.txt")


def DeleteinFileArray():  # Using Array
    std = open("Students.txt", "rt")
    item = int(input("Enter ID to be deleted"))
    temparray = []
    deleted = False
    while True:
        try:

            StdId = int(std.readline())
            Stdname = std.readline()
            StdClass = std.readline()
            if StdId != item:
                temparray.append(str(StdId))
                temparray.append(Stdname)
                temparray.append(StdClass)
            else:
                deleted = True
        except:
            break
    std.close()
    if not deleted:
        print("No Item Deleted")
    else:
        print("Id Removed")
        std = open("Students.txt", "wt")
        j = 0
        total = len(temparray) - 1
        while j <= total:
            StdId = temparray[j]
            j += 1
            StdName = temparray[j]
            j += 1
            StdClass = temparray[j]
            j += 1
            std.write(StdId + "\n")
            std.write(StdName)
            std.write(StdClass)
    std.close()


choice = int(
    input(
        "Enter 1 To add in File: \nEnter 2 To DeleteinFile using 2 Files: \nEnter 3 To DeleteinFileUsingArray:\nEnter -1 to Exit: "
    )
)
while choice != -1:
    if choice == 1:
        AddinFile()
    elif choice == 2:
        DeleteinFile()
    elif choice == 3:
        DeleteinFileArray()
    choice = int(
        input(
            "Enter 1 To add in File: \nEnter 2 To DeleteinFile(using 2 Files): \nEnter 3 To DeleteinFileUsingArray:\nEnter -1 to Exit: "
        )
    )
