from pathlib import Path
import time
import re
from functools import cache


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
@cache   
def arrangements(input_line: str, *res: re.Pattern):
    if len(res) == 0:
        return 0 if "#" in input_line else 1

    matches = 0
    index = 0
    
    while (m := res[0].search(input_line[index:])) and "#" not in input_line[:index + m.start()]:
        matches += arrangements(input_line[index + m.end() - 1:], *res[1:])
        index += m.start() + 1

    return matches   
    
def day12():
    """Day 11 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day12.txt")
     
    sum_perm = 0
    sum_folded = 0
    for line in input_txt:    
        input_line, broken = line.split()
        spring_res = [re.compile(f"[.?][#?]{{{int(s)}}}[.?]") for s in broken.split(",")]
        sum_perm += arrangements(f".{input_line}.", *spring_res)
        
        input_line = '?'.join((input_line, ) * 5)
        spring_res = [re.compile(f"[.?][#?]{{{int(s)}}}[.?]") for s in (broken.split(",") * 5)]
        sum_folded += arrangements(f".{input_line}.", *spring_res)

    print('Part 1:', sum_perm)
    print('Part 2:', sum_folded)
    
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")
    
day12()
