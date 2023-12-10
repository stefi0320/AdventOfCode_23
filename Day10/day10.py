"""Module providing a function reading files."""
from pathlib import Path
import time
import sys
from more_itertools import locate
import matplotlib.pyplot as plt
import numpy as np
sys.setrecursionlimit(1_000_000)

path_down_up = [['F','|','7'],['|','L','J']]
path_left_right = [['F','-','L'],['-','7','J']]

def open_file_safely(file_name):
    """ File open """
    try:
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir / file_name

        with open(file_path, 'r', encoding="utf-8") as file:
            content = [line.strip() for line in file]
        return content

    except FileNotFoundError:
        print(
            "The file '{file_name}' was not found in the same directory as the script.")
        return None
    
    
def dfs(grid, start, visited, first) :
    n = len(grid)
    m = len(grid[0])
    point_stack = []
    point_stack.append(start)
  
    while len(point_stack) != 0:
        current = point_stack.pop()
        i = current[0]
        j = current[1]
        if (grid[i][j] == 'S' and first is not True) or visited[i][j]:
            return
       
        visited[i][j] = True

        if first is True:
            if 'F' in path_down_up[0] and i < n-1 and grid[i+1][j] in path_down_up[1]:
                point_stack.append([i+1, j]) # Move bottom
            if 'F' in path_down_up[1] and i > 0  and grid[i-1][j] in path_down_up[0]:
               point_stack.append([i-1, j]) # Move top
            if 'F' in path_left_right[1] and j > 0 and grid[i][j-1] in path_left_right[0]:
                point_stack.append([i, j-1]) # Move left
            if 'F' in path_left_right[0] and j < m-1 and grid[i][j+1] in path_left_right[1]:
                point_stack.append([i, j+1]) # Move right
            first = False
        else:
            if grid[i][j] in path_down_up[0] and i < n-1  and grid[i+1][j] in path_down_up[1] and visited[i+1][j] is False:
                point_stack.append([i+1, j]) # Move bottom
            if grid[i][j] in path_down_up[1] and i > 0  and grid[i-1][j] in path_down_up[0] and visited[i-1][j] is False:
                point_stack.append([i-1, j]) # Move top
            if grid[i][j] in path_left_right[1] and j > 0 and grid[i][j-1] in path_left_right[0] and visited[i][j-1] is False:
                point_stack.append([i, j-1]) # Move left
            if grid[i][j] in path_left_right[0] and j < m-1 and grid[i][j+1] in path_left_right[1] and visited[i][j+1] is False:
                point_stack.append([i, j+1]) # Move right
                                    
def has_path_dfs(grid, start, visited) :
    dfs(grid, start, visited, True)
       
    sum_path = 0
    for i in visited:
        for j in i:
            if j:
                sum_path+=1
    return sum_path

def flood_fill_util(x, y, target_color, replacement_color, image):
    rows, cols = len(image), len(image[0])
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if image[x][y] != target_color:
        return
    image[x][y] = replacement_color
    flood_fill_util(x-1, y, target_color, replacement_color, image)
    flood_fill_util(x+1, y, target_color, replacement_color, image)
    flood_fill_util(x, y-1, target_color, replacement_color, image)
    flood_fill_util(x, y+1, target_color, replacement_color, image)

def flood_fill(x, y, replacement_color, image):
    target_color = image[x][y]
    if target_color != replacement_color:
        flood_fill_util(x, y, target_color, replacement_color, image)
            
def day10():
    """Day 10 of Advent of code """
    # record start time
    start = time.time()
    
    input_txt = open_file_safely("day10.txt")
    input_seq = []
    start_point = []
    for i, line in enumerate(input_txt):
        tmp = [x for x in line.strip()]
        row = list(locate(tmp, lambda x: x == 'S'))
        if row:
            start_point = [i, row[0]]
        input_seq.append(tmp)

    visited = [[False for i in range(len(input_seq[0]))] for j in range(len(input_seq))]

    print('Part 1:', has_path_dfs(input_seq, start_point, visited)/2)
          
    pipefill = {
        "|" : [[0,1,0],[0,1,0],[0,1,0]],
        "-" : [[0,0,0],[1,1,1],[0,0,0]],
        "L" : [[0,1,0],[0,1,1],[0,0,0]],
        "J" : [[0,1,0],[1,1,0],[0,0,0]],
        "7" : [[0,0,0],[1,1,0],[0,1,0]],
        "F" : [[0,0,0],[0,1,1],[0,1,0]],
        "S" : [[0,1,0],[1,1,1],[0,1,0]],
    }
                 
    gridexp = np.zeros((3*len(input_seq[0]),3*len(input_seq)),dtype=int)

    for i, line in enumerate(visited):
        for j, item in enumerate(line):
            if item:
                t = input_seq[i][j]
                gridexp[3*i:3*i+3,3*j:3*j+3] = pipefill[t]
    flood_fill(0, 0, -1, gridexp)
    _ = plt.figure(figsize=(10,10), dpi=100)
    _ = plt.imshow(gridexp)
    plt.show()
    
    gridnew = np.zeros((len(input_seq[0]),len(input_seq)),dtype=int)

    for y in range(len(gridnew)):
        for x in range(len(gridnew[0])):
            xe = 3*x+1
            ye = 3*y+1
            gridnew[y,x] = gridexp[ye,xe]

    _ = plt.figure(figsize=(8,8), dpi=100)
    _ = plt.imshow(gridnew)
    
    print("Part 2:",len(gridnew[gridnew==0]))
        
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day10()
