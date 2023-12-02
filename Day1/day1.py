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
    try:
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir / file_name

        with open(file_path, 'r') as file:
            content = file.readlines()
        return content

    except FileNotFoundError:
        print(f"The file '{
              file_name}' was not found in the same directory as the script.")
        return None


def replaceToDigits(line):
    for key, value in string_to_digit.items():
        line = line.replace(key, value)
    return line


def day1():
    # record start time
    start = time.time()

    input = open_file_safely("day1.txt")
    sum = 0

    for line in input:
        tmp_line = replaceToDigits(line)
        digits = re.findall("\d", tmp_line)
        num = digits[0] + digits[-1]
        sum += int(num)
    print(sum)

    # record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")


day1()
