"""Module providing a function reading files."""
import itertools
from pathlib import Path
import time

from more_itertools import locate

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
    
def day11():
    """Day 11 of Advent of code """
    # record start time
    start = time.time()
    
    input_txt = open_file_safely("day11.txt")
    galaxy_points = []
    empty_rows = []
    empty_cols = []
    col_empty =  [True for i in range(len(input_txt[0]))]
    for i, line in enumerate(input_txt):
        galaxies = list(locate(line, lambda x: x =='#'))
        if not galaxies:
            empty_rows.append(i)
        else:
            for galaxy in galaxies:
                galaxy_points.append((i, galaxy))
                col_empty[galaxy] = False
    
    for i, item in enumerate(col_empty):
        if item:
            empty_cols.append(i)
            
    #part 1 expand by 1
    expanded_points = []
    for point in galaxy_points:
        x_expand = len(list(locate(empty_rows, lambda x: x < point[0])))
        y_expand = len(list(locate(empty_cols, lambda x: x < point[1])))
        expanded_points.append((point[0]+x_expand, point[1]+y_expand))
                 
    combinations = set(itertools.combinations(expanded_points, 2))
    sum_of_shortest = 0
    for pair in combinations:
        sum_of_shortest += abs(pair[0][0] -pair[1][0]) + abs(pair[0][1] -pair[1][1])

    print('Part 1:', sum_of_shortest)
    
    #part 2 expand by 1milion
    m_expanded_points = []
    for point in galaxy_points:
        x_expand = len(list(locate(empty_rows, lambda x: x < point[0])))
        y_expand = len(list(locate(empty_cols, lambda x: x < point[1])))
        m_expanded_points.append((point[0]+(999999*x_expand), point[1]+(999999*y_expand)))
    m_combinations = set(itertools.combinations(m_expanded_points, 2))
    shortest = 0
    for pair in m_combinations:
        shortest += abs(pair[0][0] -pair[1][0]) + abs(pair[0][1] -pair[1][1])
    
    print('Part 2:', shortest)
    
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day11()
