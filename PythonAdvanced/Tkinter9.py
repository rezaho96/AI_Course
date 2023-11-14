from tkinter import *
from tkinter import messagebox

c=0
def counter(label1):
   def count():
       global  c
       label1.config(text=str(c))
       c+=1
       label1.after(100,count) 
   count()
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

root.resizable(width=0,height=0)

label1=Label(text="0",bg="#FFFFFF",master=root)
label1.pack()

counter(label1)

btnStop=Button(master=root,bg="white",foreground="blue",height="0",width="10",text="stop",command=root.destroy)
btnStop.pack()



root.mainloop()
