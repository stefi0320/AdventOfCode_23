from pathlib import Path
import time
from collections import deque
import copy

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
    
def send_pulses(modules, cycle):
    pulses = deque([['button', 'broadcaster', 'low']])
    dict_signal = {'low':'high', 'high':'low'}
    dict_sum = {'low': 0, 'high': 0}
    cycle_list = []
    while pulses:
        prev_pulse, act_pulse, signal = pulses.popleft()
        if act_pulse in modules:
            dest_modules = modules[act_pulse]
            if act_pulse == 'zp':
                tmp = list(x for x in modules[act_pulse][1].values() if x != 'low')
                if len(tmp) != 0:
                    if cycle not in cycle_list:
                        cycle_list.append(cycle)
            if act_pulse == 'broadcaster':
                for module in dest_modules:
                    pulses.append([act_pulse, module, signal])
                    dict_sum[signal] += 1
            else:
                if dest_modules[0] == '%': #flip-flop
                    if signal == 'low':   
                        new_switch =  dict_signal[dest_modules[1]]
                        modules[act_pulse][1] = new_switch
                        for i in range(2, len(dest_modules)):                
                            pulses.append([act_pulse, dest_modules[i], new_switch])
                            dict_sum[new_switch] += 1
                if dest_modules[0] == '&': #inverter
                    dest_modules[1][prev_pulse] = signal
                    tmp = list(x for x in dest_modules[1].values() if x == 'low')
                    if len(tmp) != 0:
                        for i in range(2, len(dest_modules)):
                            pulses.append([act_pulse, dest_modules[i], 'high'])
                            dict_sum['high'] += 1
                    else:                        
                        for i in range(2, len(dest_modules)):
                            pulses.append([act_pulse, dest_modules[i], 'low'])
                            dict_sum['low']  += 1
    return (dict_sum['low'], dict_sum['high'], cycle_list)
        
def day20():
    """Day 20 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day20.txt")
    module_dict = {}
    con_modules = [] 
    for line in input_txt:
        tmp = line.split(' -> ')
        if tmp[0] == 'broadcaster':
            module_dict[tmp[0]] = list(x for x in tmp[1].split(', '))
        if  tmp[0][0] == '%':
            temp_list = [tmp[0][0], 'low']
            for x in tmp[1].split(', '):
                temp_list.append(x)
            module_dict[tmp[0][1:]] = temp_list
        if  tmp[0][0] == '&':
            con_modules.append(tmp[0][1:])
            temp_list = [tmp[0][0]]
            temp_list.append({})
            for x in tmp[1].split(', '):
                temp_list.append(x)
            module_dict[tmp[0][1:]] = temp_list
            
    for con in con_modules:
        for item in module_dict.items():
            if con in item[1]:
                module_dict[con][1][item[0]] = 'low'
    sum_high = 0
    sum_low = 0
    part1_dict = copy.deepcopy(module_dict)

    for i in range(1000):
        tmp = send_pulses(part1_dict, i)
        sum_high += tmp[1]
        sum_low  += tmp[0]+1

    print('Part 1: ', sum_high*sum_low)

    product = 1
    for i in range(4000):
        tmp = send_pulses(module_dict, i)
        if tmp[2]:
            product *= (tmp[2][0] + 1)
    print('Part 2: ', product)

    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day20()