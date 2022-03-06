from ctypes.wintypes import RECT
from msilib.schema import Class
from re import M
from tkinter import *
import random
from turtle import window_height, window_width

 

G_width = 800
G_height = 500
Agent_Speed = 50
Space_part = 50
Agent_size = 1

x11 =G_width
y11 =G_height
Obstcal_color = '#8B3626'
Agent_color = "#DC143C"
Target_color = "#00FFFF"
BackGround_color = "#C5C1AA"

window = Tk()
window.title("PacMan Game");
window.resizable();
canvas = Canvas(window, bg=BackGround_color, height=G_height, width=G_width);
canvas.pack()


#=================================================================================================
import queue
import random

positionO = random.randint(1, 8)
positionO_j = random.randint(1, 8)

pos_x_x = random.randint(1, 8)
pos_x_y = random.randint(1, 8)
w = 100
h = 50


def createMaze2():
    martix = [[0 for x in range(w)] for y in range(h)]

    maze = []
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze[positionO][positionO_j] = "O"
    maze[pos_x_x][pos_x_y] = "X"

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[positionO]):
        if pos == "O":

            start = x

    i = start
    j = positionO
    pos = set()
    for move in path[:-1]:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            canvas.create_rectangle(start ,  positionO_j  , i*positionO  , positionO_j/Space_part , fill=Agent_color, tag="Target")
           
            if (j, i) in pos:

                print("+ ", end="")
            else:
                print(col + " ", end="")
           


        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[positionO]):

        if pos == "O":
            start = x

    i = start
    j = positionO
    canvas.create_rectangle(start ,  positionO  , i*positionO  , positionO_j/Space_part , fill=Agent_color, tag="Target")

    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[positionO]):
        if pos == "O":
            start = x

    i = start
    j = positionO

    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
 
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze2()

count = 0
while (not findEnd(maze, add)) and count < 4 ** 16:
    count += 1
    add = nums.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
if count >= 4 ** 16:
    print("Not Found")


#=================================================================================================


class Agent:
 def __init__(self):
   x=  pos_x_x*Space_part
   y=  pos_x_y*Space_part
   self.coordinates =[x,y]
   canvas.create_rectangle(x , y , x+Space_part , y+Space_part , fill=Agent_color, tag="Target")
canvas.moveto(pos_x_x, pos_x_y)
 

class Target:
    # def __init__(self):
        #    maze[positionO][positionO_j]
  
    #     self.coordinates = maze[positionO][positionO_j]

  def __init__(self):
   x=  positionO*Space_part
   y=  positionO_j*Space_part
   self.coordinates =[x,y]
   canvas.create_oval(x , y , x+Space_part , y+Space_part , fill=Target_color, tag="Target")
   canvas.moveto([positionO], [positionO_j])  # to rectangle to position 20,20

class Obstcal:
    line1 = canvas.create_line(100, 200, 100, 100, fill=Obstcal_color, width=5)
    line2 = canvas.create_line(500, 300, 300, 300, fill=Obstcal_color, width=5)
    line3 = canvas.create_line(600, 300, 300, 450, fill=Obstcal_color, width=5)
    canvas.moveto(line1, 100, 250)
    canvas.moveto(line2, 300, 100)
    canvas.moveto(line3, 500, 250)




 


window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry('1200x700')

Obstcal = Obstcal()
Agent = Agent()
Target = Target()

window.mainloop()
 