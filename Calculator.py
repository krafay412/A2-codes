from tkinter import *

Main = Tk(className="Calculator")

Text_Enter = Entry(Main, width= 40, borderwidth= 5)
Text_Enter.grid(row=0, columnspan=3)



def Button_Insert(x):
    Old_Value = str(Text_Enter.get())
    Text_Enter.delete(0,END)
    Text_Enter.insert(0, Old_Value + str(x))


def Button_Equals():
    global Operator,F_Val
    try:
        Last_Val = Text_Enter.get()
        Text_Enter.delete(0,END)

        if Operator == "+":
            Result = int(F_Val) + int(Last_Val)
        elif Operator == "-":
            Result = int(F_Val) - int(Last_Val)
        elif Operator == "*":
            Result = int(F_Val) * int(Last_Val)
        elif Operator == "/":
            Result = int(F_Val) / int(Last_Val)

        
        Text_Enter.insert(0,Result)
    except ValueError as e:
        Text_Enter.insert(0,"Invalid Operation")
    except ZeroDivisionError as e:
        Text_Enter.insert(0, e)
    except NameError as e:
        Text_Enter.insert(0,"Invalid Operation")




def Button_Clear():
    Text_Enter.delete(0,END)

def Button_Add():
    FirstVal = Text_Enter.get()
    global F_Val,Operator
    Operator = "+"
    F_Val = str(FirstVal)
    Text_Enter.delete(0,END)


def Button_Subtracts():
    FirstVal = Text_Enter.get()
    global F_Val,Operator
    Operator = "-"
    F_Val = str(FirstVal)
    Text_Enter.delete(0,END)

def Button_Multiplys():
    FirstVal = Text_Enter.get()
    global F_Val,Operator
    Operator = "*"
    F_Val = str(FirstVal)
    Text_Enter.delete(0,END)

def Button_Divides():
    FirstVal = Text_Enter.get()
    global F_Val,Operator
    Operator = "/"
    F_Val = str(FirstVal)
    Text_Enter.delete(0,END)




Button_0 = Button(Main, text="0",padx= 40, pady= 40 ,command=lambda: Button_Insert(0))
Button_1 = Button(Main, text="1",padx= 40, pady= 40 ,command=lambda: Button_Insert(1))
Button_2 = Button(Main, text="2",padx= 40, pady= 40 ,command=lambda: Button_Insert(2))
Button_3 = Button(Main, text="3",padx= 40, pady= 40 ,command=lambda: Button_Insert(3))
Button_4 = Button(Main, text="4",padx= 40, pady= 40 ,command=lambda: Button_Insert(4))
Button_5 = Button(Main, text="5",padx= 40, pady= 40 ,command=lambda: Button_Insert(5))
Button_6 = Button(Main, text="6",padx= 40, pady= 40 ,command=lambda: Button_Insert(6))
Button_7 = Button(Main, text="7",padx= 40, pady= 40 ,command=lambda: Button_Insert(7))
Button_8 = Button(Main, text="8",padx= 40, pady= 40 ,command=lambda: Button_Insert(8))
Button_9 = Button(Main, text="9",padx= 40, pady= 40 ,command=lambda: Button_Insert(9))
Button_add = Button(Main, text="+",padx= 39, pady= 40 ,command = Button_Add)
Button_Subtract = Button(Main, text="-",padx= 40, pady= 40 ,command = Button_Subtracts)
Button_Multiply = Button(Main, text="*",padx= 39, pady= 40 ,command = Button_Multiplys)
Button_Divide = Button(Main, text="/",padx= 39, pady= 40 ,command = Button_Divides)
Button_equal = Button(Main, text="=",padx= 135, pady= 40 ,command=Button_Equals)
Button_clear = Button(Main, text="Clear",padx= 30, pady= 40,borderwidth=1 ,command=Button_Clear)




Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

Button_0.grid(row=4,column=0)
Button_add.grid(row =4,column=1)
Button_Subtract.grid(row=4,column=2)

Button_Multiply.grid(row=5,column=0)
Button_Divide.grid(row=5,column=1)

Button_equal.grid(row = 7,column=0,columnspan=3)
Button_clear.grid(row=5,column=2,columnspan=2)

Main.mainloop()