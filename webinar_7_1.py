from tkinter import *

def button_1():
    name_result.setvar()
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

name_result=Entry(root, width=15,bg="gray",fg="cyan",font="consolas")
name_result.pack()
lastname_result=Entry(root, width=15,bg="gray",fg="cyan",font="consolas")
lastname_result.pack()
tel_result=Entry(root, width=15,bg="gray",fg="cyan",font="consolas")
tel_result.pack()

Button(root, text="скопировать",width=15,height=2,bg="white",command=button_1).pack()



l=Label(root,width=15,bg="gray",fg="cyan",font="consolas")
l.pack()
root.mainloop()