from tkinter import *

def button_1():
    name_result.config(text=str(name.get()))
    lastname_result.config(text=str(lastname.get()))
    tel_result.config(text=str(tel.get()))
test=0
root=Tk()
root.title("приложение")
root.geometry("500x300")
name=Entry(root, width=15,bg="gray",fg="cyan",font="consolas")
name.pack()
lastname=Entry(root, width=15,bg="gray",fg="cyan",font="consolas")
lastname.pack()
tel=Entry(root, width=15,bg="gray",fg="cyan",font="consolas")
tel.pack()
Button(root, text="скопировать",width=15,height=2,bg="white",command=button_1).pack()
name_result=Label(root,width=15,bg="gray",fg="cyan",font="consolas")
name_result.pack()
lastname_result=Label(root,width=15,bg="gray",fg="cyan",font="consolas")
lastname_result.pack()
tel_result=Label(root,width=15,bg="gray",fg="cyan",font="consolas")
tel_result.pack()
root.mainloop()