from tkinter import *


def printHello():
    print("hello ....")
    
root=Tk()
root.title("Python GUI")
root.iconbitmap("PythonAdvanced/python_18894.ico")

w=300
h=350
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,y,x,y))

label1=Label(master=root,font=("BNazanin",15),text="Iman Ahmadi")
label1.pack()

message1=Message(master=root , font=("tohoma",20),relief=RAISED,text="Hello")
message1.pack()

label1.config(text="Reza Hoseini",bg= "blue")

label1.after(5000,printHello)
root.mainloop()
