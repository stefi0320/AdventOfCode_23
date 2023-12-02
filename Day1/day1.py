"""Module providing a function reading files."""
from pathlib import Path
import re
import time

string_to_digit = {
    'one':   'o1e',
    'two':   't2e',
    'three': 't3e',
    'four':  '4',
    'five':  '5e',
    'six':   '6',
    'seven': '7n',
    'eight': 'e8t',
    'nine':  'n9e',
}


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


def replace_to_digits(line):
    """ Replace text to digit """   
    for key, value in string_to_digit.items():
        line = line.replace(key, value)
    return line


def day1():
    """Day 1 of Advent o f code """
    # record start time
    start = time.time()

    input_txt = open_file_safely("day1.txt")
    sum_num = 0

    for line in input_txt:
        tmp_line = replace_to_digits(line)
        digits = re.findall("\d", tmp_line)
        num = digits[0] + digits[-1]
        sum_num += int(num)
    print(sum_num)

    # record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")


day1()
