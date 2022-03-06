from msilib.schema import Class
from re import M
import queue
from tkinter import *
import random
from turtle import window_height, window_width
# root = Tk()
# w = Label(root, text="Hello, world!")
# w.pack()
# root.mainloop()

G_width = 1000
G_height = 500
Agent_Speed = 50
Space_part = 50
Agent_size = 1

Obstcal_color = '#8B3626'
Agent_color = "#DC143C"
Target_color = "#00FFFF"
BackGround_color = "#C5C1AA"


window = Tk()
window.title("PacMan Game");
window.resizable();
canvas =Canvas(window, bg=BackGround_color, height=G_height, width=G_width);
canvas.pack()


class Agent:

  pass

class Target:
  def __init__(self):
   x= random.randint(0, (G_width / Space_part)-1)*Space_part
   y= random.randint(0, (G_height / Space_part)-1)*Space_part
   self.coordinates =[x,y]
   
   canvas.create_oval(x , y , x+Space_part , y+Space_part , fill=Target_color, tag="Agent")

class Obstcal:
    
  line1 = canvas.create_line(100,200,100,100, fill=Obstcal_color, width=5)
  line2 = canvas.create_line(500,300,300,300, fill=Obstcal_color, width=5)
  line3 = canvas.create_line(600,300,300,450, fill=Obstcal_color, width=5)
  canvas.moveto(line1, 100, 250)
  canvas.moveto(line2, 300, 100)
  canvas.moveto(line3, 500, 250)

# def FindTaarget(): 
def createMaze2():

    maze = []
    maze.append([" "," ", " ", " ", " ", " ", " ", " ", " "])
    maze.append([" "," ", " ", " ", " ", " ", " ", "O", " "])
    maze.append([" "," ", "/", "/", "/", "/", "/", " ", " "])
    maze.append([" "," ", " ", " ", " ", " ", " ", " ", " "])
    maze.append([" ","/", " ", " ", " ", " ", " ", " ", "/"])
    maze.append([" ","/", " ", " ", " ", " ", " ", "/", " "])
    maze.append([" ","/", " ", " ", " ", " ", "/", " ", " "])
    maze.append([" "," ", " ", " ", " ", "/", " ", " ", " "])
    maze.append([" "," ", " ", " ", " ", " ", " ", "X", " "])
    return maze
 

def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
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
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "/"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
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
maze  = createMaze2()

while not findEnd(maze, add): 
    add = nums.get()
    print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)



window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width/2) -(window_width/2))
y = int((screen_height/2) -(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

Target =Target()
Obstcal = Obstcal()
window.mainloop()
