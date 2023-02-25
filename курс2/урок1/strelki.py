from tkinter import *
root=Tk()
side = 200
x,y=200,200
canvas_width, canvas_height = 700, 700
canvas=Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
square = canvas.create_rectangle(x, y, x+side, y+side, fill='black')
def change():
    global y
    canvas.delete('all')
    y=y-2    
    square = canvas.create_rectangle(x, y, x+side, y+side, fill='black')
def change_1():
     global x
     canvas.delete('all')
     x=x+2
     square = canvas.create_rectangle(x, y, x+side, y+side, fill='black')
def change_2():
     global x
     canvas.delete('all')
     x=x-2
     square = canvas.create_rectangle(x, y, x+side, y+side, fill='black')
def change_3():
     global y
     canvas.delete('all')
     y=y+2
     square = canvas.create_rectangle(x, y, x+side, y+side, fill='black')

Button(text='/\ ', command=change).pack()
Button(text='--->', command=change_1).pack()
Button(text='<---', command=change_2).pack()
Button(text='\/', command=change_3).pack()
root.mainloop()