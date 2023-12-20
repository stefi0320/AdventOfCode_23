from pathlib import Path
import time
import math
import numpy as np

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
    
def shoelace(x_y):
    x_y = np.array(x_y, dtype=np.complex128)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

def day18():
    """Day 18 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day18.txt")
    
    tmp_grid = []
    for line in input_txt:
        tmp_grid.append(line.split())

    start_point = (0,0)
    perimeter = 0
    x_y = []
    x_y.append(start_point)
    for t in tmp_grid:
        if t[0] == 'R':
            tmp = [start_point[0], start_point[1] + int(t[1])]
            perimeter += int(t[1])
            x_y.append((tmp[0], tmp[1]))
        elif t[0] == 'L':
            tmp = [start_point[0], start_point[1] - int(t[1])]
            perimeter += int(t[1])
            x_y.append((tmp[0], tmp[1]))
        elif t[0] == 'D':
            tmp = [start_point[0] - int(t[1]), start_point[1]]
            perimeter += int(t[1])
            x_y.append((tmp[0], tmp[1]))       
        elif t[0] == 'U':
            tmp = [start_point[0] + int(t[1]), start_point[1]]
            perimeter += int(t[1])
            x_y.append((tmp[0], tmp[1]))
        start_point = tmp  
    area = shoelace(x_y)

    print('Part 1: ', area + (perimeter/2) +1)

    start_point = (0,0)
    x_y = []
    x_y.append(start_point)
    perimeter = 0
    for t in tmp_grid:
        if t[2][-2]== '0':
            tmp = [start_point[0], start_point[1] + int(t[2][2:-2],16)]
            perimeter+= int(t[2][2:-2],16)
            x_y.append((tmp[0], tmp[1]))
        elif t[2][-2]== '2':
            tmp = [start_point[0], start_point[1] - int(t[2][2:-2],16)]
            perimeter+= int(t[2][2:-2],16)
            x_y.append((tmp[0], tmp[1]))
        elif t[2][-2]== '1':
            tmp = [start_point[0] - int(t[2][2:-2],16), start_point[1]]
            perimeter+= int(t[2][2:-2],16)
            x_y.append((tmp[0], tmp[1]))       
        elif t[2][-2]== '3':
            tmp = [start_point[0] + int(t[2][2:-2],16), start_point[1]]
            perimeter+= int(t[2][2:-2],16)
            x_y.append((tmp[0], tmp[1]))
        start_point = tmp  
    area = shoelace(x_y)
    print(perimeter)
    print(area)
    print('Part 2: ',  area + (perimeter/2) +1)
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day18()