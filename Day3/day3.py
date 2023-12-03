"""Module providing a function reading files."""
from pathlib import Path
import time
import numpy as np

special_chars = {
    '@',
    '#',
    '$',
    '%',
    '&',
    '*',
    '/',
    '-',
    '+',
    '=',
    '!'
}

indexer =[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, +1], [1, -1], [1, 0], [1, 1]]

def open_file_safely(file_name):
    """ File open """
    try:
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir / file_name

        with open(file_path, 'r', encoding="utf-8") as file:
            content =  list(line for line in (l.strip() for l in file) if line)
        return content

    except FileNotFoundError:
        print("The file '{file_name}' was not found in the same directory as the script.")
        return None

def find_neighbours(tmp_array, row, col, symbol, part2):
    """ Find neighbours of special char """
    sum_part = 0
    nums = []
    prev_row = 0
    for idx in indexer:
        if ((row + idx[0] < tmp_array.shape[0]-1)  or (row + idx[0] > 0)) and ((col + idx[1] > 0)  or (col + idx[1] <  tmp_array.shape[1]-1)):
            if tmp_array[row + idx[0],col + idx[1]] != '.' and  tmp_array[row + idx[0],col + idx[1]] != symbol:
                #number found
                item = find_numbers(tmp_array[row + idx[0]], row + idx[0], col + idx[1], tmp_array.shape[1]-1, col, row)
                digit = ''
                for i in range(item[1]-item[0]+1):
                    #if tmp_array[row + idx[0],i+item[0]] not in special_chars:
                        digit += tmp_array[row + idx[0],i+item[0]]
                   # else:
                        #print(tmp_array[row + idx[0],i+item[0]])
                if row + idx[0] == prev_row:
                    if digit not in nums:
                        nums.append(digit)
                else:
                    nums.append(digit)
                prev_row = row + idx[0]               
    if part2 and len(nums) == 2:
        sum_part = int(nums[0]) * int(nums[1])
    if not part2:
        for i in nums:
            sum_part += int(i)

    return sum_part
    
    
def find_numbers(row, row_id, col_id, length, symbol_col, symbol_row):
    """ Find number near id """
    point_index = np.where(row == '.')
    start_point = 0
    end_point = 0
    if symbol_row != row_id:
        if col_id < point_index[0][0]:
            start_point = 0
            end_point = point_index[0][0] - 1
        elif col_id > point_index[0][-1]:
            start_point = point_index[0][-1] + 1
            end_point = length
        else:
            for i in enumerate(point_index[0]):
                if i[1] > col_id:
                    start_point = point_index[0][i[0]-1] + 1
                    end_point = i[1] - 1
                    break
    else:
        if col_id < point_index[0][0]:
            if col_id < symbol_col:
                start_point = 0
                end_point = point_index[0][0] - 2
            else:
                start_point = 1
                end_point = point_index[0][0] - 1
        elif col_id > symbol_col > point_index[0][-1]:
            start_point = point_index[0][-1] + 2
            end_point = length
        elif col_id > point_index[0][-1]:
            start_point = point_index[0][-1] + 1
            end_point = length -1
        else:
            for i in enumerate(point_index[0]):
                if i[1] > col_id:
                    if symbol_col > col_id:
                        start_point = point_index[0][i[0]-1] + 1
                        end_point = symbol_col - 1
                    else:
                        start_point = symbol_col + 1
                        end_point = i[1] - 1
                    break
    point_array = [start_point, end_point]
    return point_array

def day3():
    """Day 3 of Advent o f code """
    # record start time
    start = time.time()
       
    input_txt = open_file_safely("day3.txt")
    input_array = np.array([list(l) for l in input_txt])
    #print(input_array)

    # part1
    sum_part1 = 0
    for s in special_chars:
        specials = np.char.find(input_array,s)
        for row in  enumerate(specials):
            for column in enumerate(row[1]):   
                if specials[row[0]][column[0]] == 0:
                    sum_part1 += find_neighbours(input_array, row[0], column[0], s, False)
    print(sum_part1)
                  
    # part2
    sum_part2= 0
    specials = np.char.find(input_array,'*')
    for row in  enumerate(specials):
        for column in enumerate(row[1]):   
            if specials[row[0]][column[0]] == 0:
                sum_part2 += find_neighbours(input_array, row[0], column[0], s, True)
    print(sum_part2)
    # record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")


day3()
