from tkinter import *
from tkinter import messagebox


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
root.columnconfigure(0,weight=0)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)
root.columnconfigure(3,weight=3)
root.columnconfigure(4,weight=1)
label1=Label(text="number1",bg="#FFFFFF",master=root)
label2=Label(text="number2",bg="#FFFFFF",master=root)
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

tbx_number1=Entry(master=root)
tbx_number2=Entry(master=root)
btn_sum=Button(master=root,bg="white",foreground="blue",height="0",width="10",text="+")
tbx_number1.grid(row=0,column=1,padx=5,pady=10)
tbx_number2.grid(row=1,column=1,padx=5,pady=10)
btn_sum.grid(row=2,column=1,padx=5,pady=10)



root.mainloop()
