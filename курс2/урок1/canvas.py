from tkinter import *
def change():
    canvas.itemconfig(cirkle, fill='yellow')
def change_1():
    canvas.itemconfig(krsha, fill='black')
def change_2():
    canvas.itemconfig(square, fill='green')
    print(canvas.itemcget(square, 'fill'))
side = 200
canvas_width, canvas_height = 700, 700
x, y=canvas_width/2 - side/2, 350
root=Tk()
canvas=Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
cirkle = canvas.create_oval(100, 100, 150,150, fill='blue')
krsha = canvas.create_polygon(x, y, x+side/2, y-100, x+side, y, fill='red')
square = canvas.create_rectangle(x, y, x+side, y+side, fill='pink')
Button(text='солнце', command=change).pack()
Button(text='крыша', command=change_1).pack()
Button(text='основание', command=change_2).pack()
root.mainloop()