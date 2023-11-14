from tkinter import *

root=Tk()
root.title("Python GUI")
root.iconbitmap("PythonAdvanced/python_18894.ico")

root.geometry('%dx%d+%d+%d'%(255,140,230,250))

label1=Label(master=root,
             text="Reza hoseini",
             width=14,
             height=0,
             background="#12a2a2",
             foreground="#001245",
             cursor="heart",
             anchor="nw", #w e n s
             relief=GROOVE  
             )
label1.pack()

root.mainloop()