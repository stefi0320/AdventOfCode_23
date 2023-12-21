from pathlib import Path
import time
import math

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

def locate_rating(condition, part):
    tmp = []
    for rating in part:
        if condition[0][0] == rating[0]:
            tmp = rating
     
    return tmp
    
def day19():
    """Day 19 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day19.txt")
    
    workflows = {}
    parts = []  
    separator_line =  input_txt.index('')
    
    for i in range(separator_line):
        workflow_id, tmp =  input_txt[i].split('{')
        conditions = [x.split(':') for x in tmp.replace('}','').split(',')]
        workflows[workflow_id] = conditions

    for i  in range(separator_line+1, len(input_txt)):
        part_nums = input_txt[i].replace('{', '').replace('}', '').split(',')
        parts.append([x.split('=') for x in part_nums])

    sum_accepted = 0
    for part in parts:
        result  = 'in'
        while 1:
            found = False
            for i in range(len(workflows[result])-1):
                if found is False:
                    rating = locate_rating(workflows[result][i], part)                    
                    temp = workflows[result][i][0].replace(rating[0], rating[1])
                    if eval(str(temp)):
                        result = workflows[result][i][1]
                        found = True
                if found is True:
                    break
            if found is False:
                result = workflows[result][-1][0]
            if result == 'A' or result == 'R':
                break
        if result == 'A':
            for i in part:
                sum_accepted += int(i[1])

    cat_dict = {'x': 0, 'm': 1, 'a': 2, 's': 3}

    print('Part 1: ', sum_accepted)
    comb_accepted = 0
    start_part = ('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))
    queue = [start_part]
    while queue:
        curr, *intervals = queue.pop()
        if curr in ('A', 'R'):
            if curr == 'A':
                comb_accepted += math.prod(hi-lo+1 for lo, hi in intervals)
            continue
        
        for i in range(len(workflows[curr])-1):
            curr_id = cat_dict[workflows[curr][i][0][0]]          
            lo, hi = intervals[curr_id]                
            op_num = int(workflows[curr][i][0][2:])
            op = workflows[curr][i][0][1]
            res = workflows[curr][i][1]
            # All passthrough, no transfer
            if (op == '>' and op_num >= hi) or (op == '<' and op_num <= lo):
                continue

            # All transfer no passthrough
            if (op == '>' and op_num < lo) or (op== '<' and op_num > hi):
                queue.append((res, *intervals))
                break

            # Some of both
            if op == '>':
                transfer = (op_num+1, hi)
                passthrough = (lo, op_num)
            else:
                transfer = (lo, op_num-1)
                passthrough = (op_num, hi)
            intervals[curr_id] = passthrough
            intervals2 = intervals.copy()
            intervals2[curr_id] = transfer
            queue.append((res, *intervals2))
                
        else: # Remaining is transferred
            queue.append((workflows[curr][-1][0], *intervals))  

    print('Part 2: ', comb_accepted)
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day19()