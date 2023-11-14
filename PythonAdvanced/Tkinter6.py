from tkinter import *

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

label1=Label(text="Ali",bg="#FFFFFF",master=root)
label2=Label(text="Hasan",bg="#FFFFFF",master=root)
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

button1=Button(master=root,bg="white",foreground="blue",height="0",width="10",text="ok")
button2=Button(master=root,bg="white",foreground="blue",height="0",width="10",text="ok")
button1.grid(row=0,column=1,padx=5,pady=10)
button2.grid(row=1,column=1,padx=5,pady=10)

root.mainloop()
