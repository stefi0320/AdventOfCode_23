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

def check_seed(m, seed):
    tmp_seeds = []
    if seed:
        found_seed = False
        for rows in m:
            if rows.s_start <= seed[0] <= seed[1] <= rows.s_end:
                found_seed = True
                new_seed = [seed[0] + rows.convert, seed[1] + rows.convert]
                tmp_seeds.append(new_seed)
            elif seed[0] < rows.s_start <=  rows.s_end < seed[1]:
                found_seed = True
                new_seed = [seed[0], rows.s_start - 1]
                tempi = check_seed(m,new_seed)
                if tempi: 
                    for t in tempi:
                        if t not in tmp_seeds:
                            tmp_seeds.append(t)
                else:
                    tmp_seeds.append(new_seed)
                new_seed = [rows.s_start + rows.convert, rows.s_end + rows.convert]
                tmp_seeds.append(new_seed)
                new_seed = [rows.s_end + 1, seed[1]]
                tempi = check_seed(m,new_seed)
                if tempi: 
                    for t in tempi:
                        if t not in tmp_seeds:
                            tmp_seeds.append(t)
                else:
                    tmp_seeds.append(new_seed)
            elif seed[0] < rows.s_start <= seed[1] <= rows.s_end:
                found_seed = True
                new_seed = [seed[0], rows.s_start - 1]
                tempi = check_seed(m,new_seed)
                if tempi: 
                    for t in tempi:
                          if t not in tmp_seeds:
                            tmp_seeds.append(t)
                else:
                    tmp_seeds.append(new_seed)
                new_seed = [rows.s_start + rows.convert, seed[1]  + rows.convert]
                tmp_seeds.append(new_seed)
            elif rows.s_start <= seed[0] <= rows.s_end < seed[1]:
                found_seed = True
                new_seed = [seed[0] + rows.convert, rows.s_end + rows.convert]
                tmp_seeds.append(new_seed)
                new_seed = [rows.s_end + 1, seed[1]]
                tempi = check_seed(m,new_seed)
                if tempi: 
                    for t in tempi:
                        if t not in tmp_seeds:
                            tmp_seeds.append(t)
                else:
                    tmp_seeds.append(new_seed)
        if not found_seed and seed not in tmp_seeds:
            tmp_seeds.append(seed)
    return tmp_seeds

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

    seeds_list = [int(x) for x in input_txt[0].split('seeds: ')[1].split(' ')]
    seeds_range = []
    for i, seed in enumerate(seeds_list):
        if i%2 != 0:
            continue
        seeds_range.append([seed, seed + seeds_list[i+1]-1])

    #part1
    to_convert = namedtuple('to_convert', 'found_seeds, convert')
    for m in maps:
        convert_list = []
        for rows in m:  
            found_seeds = list(locate(seeds_list, lambda x: rows.s_start <= x <= rows.s_end))
            convert_list.append(to_convert(found_seeds= found_seeds, convert= rows.convert))
        for item in convert_list:
            for seed in item.found_seeds:
                seeds_list[seed] = seeds_list[seed] + item.convert
    print(min(seeds_list))

    #part2
    lista = []
    lista.append(seeds_range)
    for i in range(7):
        temp_seeds = []
        for seed in lista[i]:
            tmp = check_seed(maps[i], seed)
            for t in tmp:
                if t not in temp_seeds:
                    temp_seeds.append(t)               
        lista.append(temp_seeds)   

    print(min(lista[-1])[0])
    
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")
day5()
