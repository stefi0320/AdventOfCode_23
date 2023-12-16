from pathlib import Path
import time
from collections import namedtuple

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
def calc_hash(tmp):
    temp_sum = 0
    for i in tmp:
        temp_sum= ((temp_sum+(ord(i)))*17) % 256
    return temp_sum

def day15():
    """Day 15 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day15.txt")

    part1 = input_txt[0].split(',')
    sum_hash = 0
    for tmp in part1:
        sum_hash += calc_hash(tmp)
    print('Part 1:', sum_hash)

    box_dict = {}
    for lens in part1:
        if '=' in lens:
            tmp = lens.split('=')
            lens_id = calc_hash(tmp[0])
            if box_dict and lens_id in box_dict.keys():
                box_dict[lens_id].update({tmp[0]: int(tmp[1])})
            else:
                box_dict[lens_id] = {tmp[0]: int(tmp[1])}
        else:
            tmp = lens.split('-')
            lens_id = calc_hash(tmp[0])
            if lens_id in box_dict:
                if(tmp[0] in box_dict[lens_id]):
                    box_dict[lens_id].pop(tmp[0])
    focus_power = 0           
    for box in box_dict.items():
        for i, lens in enumerate(box[1].items()):
            focus_power += (box[0]+1) * (i+1) * lens[1]

    print('Part 2: ', focus_power)
  
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day15()
