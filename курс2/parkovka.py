from tkinter import *
mestoSvobod=[
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
def button_1():
    number=a.get()
    for i in range(0,len(mestoSvobod)):
        if mestoSvobod[i] == 0:
          l.config(text=str(i+1))
          mestoSvobod[i] = 1
          break
   
root=Tk()
root.title("приложение")
root.geometry('500x300')
a=Entry(root,width=15, bg='gray', fg='cyan', font='consolas')
a.pack()
Button(root, text='найти свободное место', width=20,height=2,bg='white',command=button_1).pack()
l=Label(root,width=15, bg='gray', fg='cyan', font='consolas')
l.pack()
root.mainloop()