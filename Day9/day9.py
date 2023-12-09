"""Module providing a function reading files."""
from pathlib import Path
import time
import math

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
    
def nth_pascal(n):
    row = [((-1)**(k+n))*math.comb(n, k) for k in range(n + 1)]
    return row    
    
def day9():
    # record start time
    start = time.time()
    
    input_txt = open_file_safely("day9.txt")
    value_following = 0
    value_previous = 0
    for line in input_txt:
        input_seq = ([int(x) for x in line.split()])
        pascal = nth_pascal(len(input_seq))
        value_following += -sum(input_seq[i]*pascal[i] for i in range(len(input_seq)))
        value_previous += -pascal[0]*sum(input_seq[i]*pascal[i + 1] for i in range(len(input_seq)))

    print('Part 1:',value_following)
    print('Part 2:',value_previous)
    
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day9()