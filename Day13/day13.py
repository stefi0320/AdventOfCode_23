from pathlib import Path
from more_itertools import locate
import time

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
    
def transpose_pattern(pattern):
    transposed_pattern = []
    for col in range(len(pattern[0])):
        tmp = []
        for row in pattern:
            tmp.append(row[col])
        transposed_pattern.append(tmp)
    return transposed_pattern

def find_copy(pattern):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            j = 1
            if i == len(pattern) - 2:
                return i+1
            elif i != 0:
                while i-j >= 0  and i+1+j < len(pattern) and pattern[i-j] == pattern[i+1+j]:
                    if i-j == 0 or i+1+j ==  len(pattern)-1:
                        return(i+1)
                    j+=1
            else:
                return 1                
    return 0

def find_copytwo(pattern):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            j = 1
            while i-j >= 0  and i+1+j < len(pattern):
                count = 0 
                for l in range(len(pattern[i])):
                    if pattern[i-j][l] == pattern[i+1+j][l]:
                        count+= 1
                if  len(pattern[i]) - count == 1:
                    print(pattern[i-j])
                    print(pattern[i+1+j])   
                j+=1
        else:
            count = 0 
            for l in range(len(pattern[i])):
                if pattern[i][l] == pattern[i+1][l]:
                    count+= 1
            if  len(pattern[i]) - count == 1:
                print(pattern[i])
                print(pattern[i+1])   
    return 0

    
def day13():
    """Day 13 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day13.txt")
    input_txt.append('')
    input_array = []
    patterns = []
    for line in input_txt:
        if line: 
            input_array.append(list(line))
        else:
            patterns.append(input_array) 
            input_array = []
    transposed_patterns = []
    for pattern in patterns:
        transposed_patterns.append(transpose_pattern(pattern))
        
    sum_mirrored = 0
    found_lines = []
    
    for i, pattern in enumerate(patterns):
        tmp = find_copy(pattern)
        if tmp == 0:
            temp = find_copy(transposed_patterns[i])
            sum_mirrored+= temp 
            found_lines.append([i, temp-1, 'col'])
        else:
            sum_mirrored+= 100 * tmp
            found_lines.append([i, tmp-1, 'row'])

    print('Part 1:', sum_mirrored)
    
    for i, pattern in enumerate(patterns):
        print('rows')
        find_copytwo(pattern)
        print('cols')
        find_copytwo(transposed_patterns[i])
    
    print('Part 2:')
    
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")
    
day13()