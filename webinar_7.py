from tkinter import *
def button_2():
    l.config(text=int(int(a.get())*int(a.get())*int(a.get())))
def button_1():
    l.config(text=int(int(a.get())*int(a.get())))
root=Tk()
root.title("приложение")
root.geometry("500x300")
a=Entry(root, width=15,bg="gray",fg="cyan",font="consolas")
a.pack()
Button(root, text="возвести в квадрат",width=15,height=2,bg="white",command=button_1).pack()
Button(root, text="возвести в куб",width=15,height=2,bg="white",command=button_2).pack()
l=Label(root,width=15,bg="gray",fg="cyan",font="consolas")
l.pack()
root.mainloop()
