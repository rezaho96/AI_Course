from tkinter import *

def click_show_name(even):
    print("Reza Hoseini")
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

frame1=Frame(master=root,bg="red",width=150,height=20)
frame1.pack()
frame2=Frame(master=root,bg="#00a1a1",width=150,height=20)
frame2.pack()
frame3=Frame(master=root,bg="#a1a100",width=150,height=20)
frame3.pack()

label1=Label(text="Ali",bg="#FFFFFF",master=frame3)
label2=Label(text="Hasan",bg="#FFFFFF",master=frame1)

label1.place(x=100,y=0)
label2.place(x=110,y=3)

button1=Button(master=root,bg="white",foreground="blue",height="0",width="20",text="Show Name")
button1.pack()
button1.bind("<Button>",click_show_name)
button1.pack()

root.mainloop()
