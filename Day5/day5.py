"""Module providing a function reading files."""
from pathlib import Path
from collections import namedtuple
from more_itertools import locate
import time

def open_file_safely(file_name):
    """ File open """
    try:
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir / file_name

        with open(file_path, 'r', encoding="utf-8") as file:
            content =  [line.strip() for line in file]
        return content

    except FileNotFoundError:
        print("The file '{file_name}' was not found in the same directory as the script.")
        return None


def day5():
    """Day 5 of Advent o f code """

    # record start time
    start = time.time()

    input_txt = open_file_safely("day5.txt")

    map_to_map = namedtuple('map_to_map', 's_start, s_end, convert')
    maps = []
    tmp_map = []
    for line in range(2, len(input_txt)):
        if input_txt[line] == '':           
            maps.append(tmp_map)
            tmp_map = []
        else:
            tmp = input_txt[line].split(' ')
            if 'map:' not in tmp:
                tmp_map_to_map = map_to_map(s_start= int(tmp[1]), s_end= (int(tmp[1])+int(tmp[2])-1), convert= (int(tmp[0])-int(tmp[1])))
                tmp_map.append(tmp_map_to_map)
    maps.append(tmp_map)
    
    #part1
    seeds = [int(x) for x in input_txt[0].split('seeds: ')[1].split(' ')]
    to_convert = namedtuple('to_convert', 'found_seeds, convert')
    for m in maps:
        convert_list = []
        for rows in m:  
            found_seeds = list(locate(seeds, lambda x: rows.s_start <= x <= rows.s_end))
            convert_list.append(to_convert(found_seeds= found_seeds, convert= rows.convert))
        for item in convert_list:
            for seed in item.found_seeds:
                seeds[seed] = seeds[seed] + item.convert
    print(min(seeds))

    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

    #part2
    

    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")
day5()
