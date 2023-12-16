from pathlib import Path
import time

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
    
def tilt_north(spheres, cubes):
    for i, sphere in enumerate(spheres):
        for j in range(1, sphere[0]+1):
            if sphere[0]-j >= 0:
                tmp = [sphere[0]-j, sphere[1]]
                if tmp in spheres or sphere[1] in cubes[sphere[0]-j]:
                    break
                else:
                    spheres[i] = tmp
    return spheres

def load(grid):
    return sum((i + 1) for col in grid for i in range(len(col)) if col[i] == "O")

def tilt(grid):
    return ["#".join("".join(sorted(chunk)) for chunk in column.split("#")) for column in grid]

def rotate(grid):
    return ["".join([line[i] for line in grid[::-1]]) for i in range(len(grid[0]))]

def cycle(grid):
    for i in range(4):
        grid = tilt(grid)
        grid = rotate(grid)
    return grid                                     
    
def day14():
    """Day 14 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day14.txt")

    spheres = []
    cubes = []
    for i, line in enumerate(input_txt):
        cubes.append([j for j, x in enumerate(line) if x == "#"])
        tmp = [j for j, x in enumerate(line) if x == "O"]
        for t in tmp:
            spheres.append([i, t])
   
    """Part 1"""
    spheres = tilt_north(spheres, cubes)
    sum_all = 0
    for sphere in spheres:
        sum_all += len(input_txt) - int(sphere[0])    
    print('Part 1:', sum_all)

    grid = ["".join([line[i] for line in input_txt[::-1]]) for i in range(len(input_txt[0]))]
    cycles = 1_000_000_000
    repeated = []
    i = 0
    while True:
        grid = cycle(grid)
        to_string = "\n".join(grid)
        if to_string in repeated:
            n = repeated.index(to_string)
            break
        repeated.append(to_string)
        i += 1
        
    cycle_length = i - n
    repeated_index = n + (cycles - n) % cycle_length - 1
  
    print('Part 2: ', load(repeated[repeated_index].splitlines()))
  
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day14()
