from tkinter import *
from tkinter import messagebox

def btnSum_click(even):
    number1=int(tbx_number1.get())
    number2=int(tbx_number2.get())
    messagebox.showinfo("حاصل جمع" , str(number1+number2))
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

btn_sum.bind("<Button>",btnSum_click)

root.mainloop()
