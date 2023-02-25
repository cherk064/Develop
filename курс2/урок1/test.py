from tkinter import *
import random
root=Tk()
side = 200
x,y=200,200
canvas_width, canvas_height = 700, 700
canvas=Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
def change():
    x=random.randint(1,3)
    canvas.delete('all')
    if x==1:
        square = canvas.create_rectangle(x, y, x+side, y+side, fill='black')
    elif x==2:
        cirkle = canvas.create_oval(x, y, x+side, y+side, fill='black')
    else:
        polygon = canvas.create_polygon(x, y, x+side/2, y-100, x+side, y, fill='red')
Button(text='кнопка', command=change).pack()
root.mainloop()