from tkinter import *
dann =[]
columns=('name', 'lastname', 'klass') 
def button_1():
   
    name = a.get()
    lastname=b.get()
    klass=c.get()
    dann.append((name,lastname,klass))

    write_to_file("./dann.csv")
def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(columns)+'\n')
        for line in dann:
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')

root=Tk()
root.title("приложение")
root.geometry('500x300')
a=Entry(root,width=15, bg='gray', fg='cyan', font='consolas')
b=Entry(root,width=15, bg='gray', fg='cyan', font='consolas')
c=Entry(root,width=15, bg='gray', fg='cyan', font='consolas')
a.pack()
b.pack()
c.pack()
Button(root, text='записать данные', width=15,height=2,bg='white',command=button_1).pack()
root.mainloop()
columns=( 'name', 'lastname', '', 'height', 'weight')
