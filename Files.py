import os
def AddinFile():
    std = open("Students", "at")
    StdId = int(input("Enter ID. \nEnter -1 to Exit \n"))
    while StdId != -1:
        Stdname = input("Enter Name: ")
        StdClass = input("Enter class: ")
        std.write(str(StdId) + "\n")
        std.write(Stdname + "\n")
        std.write(StdClass + "\n")
        StdId = int(input("Enter ID. \nEnter -1 to Exit \n"))
    std.close()

def DeleteinFile():
    std = open("Students", "rt")
    item = int(input("Enter ID to be deleted"))
    temp = open("Studenttemp", "wt")
    deleted = False
    while True:
        try:
            StdId = int(std.readline())
            Stdname = std.readline()
            StdClass = std.readline()
            if StdId != item:
                temp.write(str(StdId) + "\n")
                temp.write(Stdname + "\n")
                temp.write(StdClass + "\n")
            else:
                deleted = True
        except:
            break
    std.close()
    temp.close()
    if not deleted:
        print("No Item Deleted")
        os.remove(temp)
    else:
        print("Id Removed")
        os.remove("Students")
        std = open("Students", "wt")
        temp = open("Studenttemp", "rt")
        while True:
            try:
                Stdid = temp.readline()
                Stdname = temp.readline()
                StdClass = temp.readline()

                std.write(Stdid + "\n")
                std.write(Stdname + "\n")
                std.write(StdClass + "\n")
            except:
                break
    std.close()
    temp.close()
    os.remove("Studenttemp")

AddinFile()
DeleteinFile()





