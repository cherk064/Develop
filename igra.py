import random
from tkinter import *
from tkinter import messagebox
spisok=[]
def button_1():
    c=int(a.get())
    result=''
    b=random.randint(1,5)
    spisok.append(b)
    if c>b:
        result="вы выйграли.число компа " +str(b)
    else:
        result="вы проиграли.число компа " +str(b)
    messagebox.showinfo('Результат',result)   
def button_2():
    messagebox.showinfo('Результат',spisok)   
root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root, width=10,  bg='gray', fg='cyan', font='consolas')
a.pack()
Button(root, text='старт', width=10, height=2, bg='red',command=button_1).pack()
Button(root, text='закрыть', width=10, height=2, bg='red',command=button_2).pack()

root.mainloop()