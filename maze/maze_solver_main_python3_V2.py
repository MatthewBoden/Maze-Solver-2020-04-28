#########################################
# Programmer: Matthew Bodenstein
# Date: 4.28.2020
# File Name: maze_solver-main.py
# Description: This program solves a maze of arbitrary size.
#   The program follows the algorithm described on the following website:
#       http://www.cs.bu.edu/teaching/alg/maze/
#   Input file must comply with the following guidelines:
#       - walls are one character thick and represented with "#"
#       - alleys are one character wide and represented with spaces
#       - each line, including the last, ends with 'new line' character
#   Module maze contains the following functions:
#       - load_maze(fname)
#       - pick_random_location(maze)
#       - print_maze(maze)
#       - find_path(maze, x, y)
#   After importing the module, use help(function name), to understand how they work.
#   These functions exercise the following:
#       - reading from a file:
#       - nested lists (2D lists)
#       - string.join method:
#               L = ['i', 't', 'e', 'r', 'a', 'b', 'l', 'e']
#               print ''.join(L)
#       - list comprehension
#       - recursion
#########################################
import random
from maze import*
def load_maze(fname):
    maze = []
    file = open(fname,'r')
    lines = file.readlines()
    for i in range(len(lines)):  #
        maze.append([])
        temp = (lines[i][0:len(lines[i]) - 1])
        for o in temp:
            maze[i].append(o)
    file.close()
    return maze

def print_maze(maze):
    for i in maze:
        row = ''
        for j in i:
            row += j
        print(row)

def pick_random_location(maze):
    Sy = random.randint(2, len(maze)-2)
    loop = True
    while loop:
        Sx = random.randint(1, len(maze[0]))
        count = 0
        for i in maze[Sy]:
            for j in i:
                if count == Sx and j == " ":
                    loop = False
                else:
                    count+=1
    return Sx, Sy

def find_path(maze, Sx, Sy):
    blocked = ['#', '+']
    if maze[Sy][Sx] == 'G':
        return True
    elif maze[Sy][Sx] in blocked:
        return False
    else:
        maze[Sy][Sx] = '+'
        if (Sy > 0 and find_path(maze,Sx,Sy-1)):
            return True
        if (Sx > 0 and find_path(maze,Sx-1,Sy)):
            return True
        if (Sy < len(maze)-1 and find_path(maze,Sx,Sy+1)):
            return True
        if (Sx < len(maze[0])-1 and find_path(maze,Sx+1,Sy)):
            return True
        maze[Sy][Sx] = 'x'
        return False


#---------------------------------------#        
# main program                          #
#---------------------------------------#
fname = input("Enter filename: ")
maze = load_maze(fname)
# generate random start and goal locations
Sx,Sy = pick_random_location(maze)
maze[Sy][Sx] = 'S'
Gx,Gy = pick_random_location(maze)
maze[Gy][Gx] = 'G'
print ('\nHere is the maze with start and goal locations:')
print_maze(maze)
# now, find the path from S to G
find_path(maze, Sx, Sy)
print ('\nHere is the maze with the path from start to goal:')
maze[Sy][Sx] = 'S' # shows the start and the end
maze[Gy][Gx] = 'G'
print_maze(maze) # prints final result


