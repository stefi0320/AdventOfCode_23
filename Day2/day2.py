"""Module providing a function reading files."""
from pathlib import Path
import re
import time


def open_file_safely(file_name):
    """ File open """
    try:
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir / file_name

        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.readlines()
        return content

    except FileNotFoundError:
        print("The file '{file_name}' was not found in the same directory as the script.")
        return None


def possible_by_color(find, tmp_string, max_num):
    """ Find impossible number of cubes """
    possible = True
    rx = r"(\d+) {}".format(find)
    result = re.search(rx, tmp_string)
    if result:
        if int(result.group(1)) > max_num:
            possible = False
    return possible


def min_by_color(find, tmp_string):
    """ Find minimum number of cubes """
    min_num = 0
    rx = r"(\d+) {}".format(find)
    result = re.search(rx, tmp_string)
    if result:
        min_num = int(result.group(1))
    return min_num


def day2():
    """Day 2 of Advent o f code """
    # record start time
    start = time.time()

    input_txt = open_file_safely("day2.txt")
    sum_possible = 0
    sum_min = 0

    for line in input_txt:
        line = line.strip()
        possible = True
        results = re.split('Game |:|;', line)
        # remove empty
        del results[0]
        idx = results[0]
        # remove id
        del results[0]
    # part1
        for result in results:
            possible = possible_by_color('blue', result, 14)
            if not possible:
                break
            possible = possible_by_color('red', result, 12)
            if not possible:
                break
            possible = possible_by_color('green', result, 13)
            if not possible:
                break
        if possible:
            sum_possible += int(idx)
    # part2
        min_red = 1
        min_blue = 1
        min_green = 1
              
        for result in results:
            tmp_min = min_by_color('blue', result)
            min_blue = tmp_min if tmp_min > min_blue else min_blue
            tmp_min = min_by_color('red', result)
            min_red = tmp_min if tmp_min > min_red else min_red
            tmp_min = min_by_color('green', result)
            min_green = tmp_min if tmp_min > min_green else min_green
        sum_min += min_blue*min_red*min_green 


    print("Part1: " + str(sum_possible))
    print("Part2: " + str(sum_min))

    # record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")


day2()
