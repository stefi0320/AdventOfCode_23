"""Module providing a function reading files."""
from pathlib import Path
import time
import re

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

def get_nums(temp):
    """Spiltter for numbers """
    return temp.split(' ')

def check_winner(numbers, winner_numbers):
    """Checks for winning number """
    power = 0
    for number in numbers:
        if number in winner_numbers and number != '':
            power += 1
    return power

def check_copies(input_txt, index):
    """Recursive function for card checking """
    point = 0
    copy = 1
    tmp_input = re.split(': | \| ', input_txt[index].strip())
    numbers = get_nums(tmp_input[1])
    winning_numbers = get_nums(tmp_input[2])
    point = check_winner(numbers, winning_numbers)
    for i in range(point):
        copy += check_copies(input_txt, i+1+index)
    return copy
        
    
def day4():
    """Day 4 of Advent o f code """

    # record start time
    start = time.time()

    input_txt = open_file_safely("day4.txt")

    #part1
    card_sum = 0
    copies = 0
    
    for line in enumerate(input_txt):
        power = -1
        point = 0
        tmp_line = re.split(': | \| ', line[1].strip())
        numbers = get_nums(tmp_line[1])
        winning_numbers = get_nums(tmp_line[2])
        power = check_winner(numbers, winning_numbers)
        if power != 0:
            point = 2**(power - 1)
        card_sum += point
        
        #part2
        for i in range(power):
            copies += check_copies(input_txt, i+1+int(line[0]))
        copies += 1
    print('point sum', card_sum)
    print('copies', copies)
        
   # record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day4()
