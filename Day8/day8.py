"""Module providing a function reading files."""
from pathlib import Path
import time
import re

turn_dict = {'L': 0, 'R': 1}

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

def find_path(act_node, node_dict, turns):
    """Finds path length to reach **Z"""
    sum_steps = 0
    turn_it = 0
    while act_node[2] != 'Z':
        act_node = node_dict[act_node][turn_dict[turns[turn_it]]]
        sum_steps += 1
        if turn_it + 1 < len(turns):
            turn_it+= 1
        else:
            turn_it = 0
    return(sum_steps)

def day8():
    """Part1 of day 7 of Advent of code"""
    # record start time
    start = time.time()
    
    start_nodes = []
    input_txt = open_file_safely("day8.txt")
    turns = list(input_txt[0])
    node_dict = {}
    for line in range(2, len(input_txt)):
        reg = re.compile(r'(\w\w\w)').findall(input_txt[line])
        node_dict[reg[0]] = [reg[1], reg[2]]
        if reg[0][2] == 'A':
           start_nodes.append(reg[0])

    #part1
    print(find_path('AAA', node_dict, turns))
    
    #part2
    lnko_path = 1
    for node in start_nodes:
       lnko_path *= find_path(node, node_dict, turns) / len(turns)
    print(lnko_path*len(turns))
    
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day8()
