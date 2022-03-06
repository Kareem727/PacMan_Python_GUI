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
