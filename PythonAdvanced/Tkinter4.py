from tkinter import *

flag=True
def btnOk_click(even):
    global flag
    if flag==False:
        button1.config(bg="green")
        label1.config(text="hello")
        flag=True
    else:
        button1.config(bg="red")
        label1.config(text="salam")
        flag=False   
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

label1=Label(text="salam",bg="#FFFFFF",master=root)
label1.pack()

button1=Button(master=root,bg="white",foreground="blue",height="0",width="20",text="Ok")
button1.pack()
button1.bind("<Button>",btnOk_click)
button1.pack()

root.mainloop()
