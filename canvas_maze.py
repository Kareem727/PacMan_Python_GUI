# from tkinter import *
# import random

# G_width = 1000
# G_height = 500
# Agent_Speed = 50
# Space_part = 50
# Agent_size = 1

# Obstcal_color = '#8B3626'
# Agent_color = "#DC143C"
# Target_color = "#00FFFF"
# BackGround_color = "#C5C1AA"

# window = Tk()
# window.title("PacMan Game");
# window.resizable();
# canvas = Canvas(window, bg=BackGround_color, height=G_height, width=G_width);
# canvas.pack()


# class Agent:
#     pass


# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# x = int((screen_width / 2) - (window_width / 2))
# y = int((screen_height / 2) - (window_height / 2))
# window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# window.mainloop()
from tkinter import *
from tkinter.ttk import *
from cmath import rect
 
root = Tk()
root.geometry('200x100')
myCanvas = Canvas(root)
myCanvas.pack()
 
  
# these lines are showing the
# working of bind function
# it is universal widget method






grid = [[" "]*50 for n in range(100)]
grid[0][0] = -1
grid[50][100] = -1

w = 60

def setup():
    size(800,500)
    
def draws():
    x,y = 0,0
    for row in grid:
        for col in row:
            if col == -1:
                fill("#")
            else:
                fill("")
            
            rect(x, y, w, w)
            x = x+w
  
draws()
 
root.mainloop()           
