"""Module providing a function reading files."""
from pathlib import Path
import time
from collections import Counter
from collections import namedtuple
from functools import reduce

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


camel_dict = {'A': 10, 'K': 11, 'Q': 12, 'J': 13, 'T': 14, '9': 15,
              '8': 16, '7': 17, '6': 18, '5': 19, '4': 20, '3': 21, '2': 22}


joker_dict = {'A': 10, 'K': 11, 'Q': 12, 'T': 13, '9': 14,
              '8': 15, '7': 16, '6': 17, '5': 18, '4': 19, '3': 20, '2': 21, 'J': 22}

def sub_sort_hands(hand, part_true):
    if part_true:
        subs = {v:k for k,v in camel_dict.items()}
    else:
        subs = {v:k for k,v in joker_dict.items()}
    for i,h in enumerate(hand):
        temp = list(map(dict(zip(subs.values(), subs)).get, h.cards))
        hand[i] = h._replace(cards = int(reduce(lambda a, b : str(a)+''+str(b), temp)))
    return(sorted(hand, key=lambda x: x.cards))

def calc_winnings(hand, rank):
    sum_win = 0
    for h in hand:
        sum_win+= rank * h.bid
        rank -= 1
    return sum_win

def part1():
    """Part1 of day 7 of Advent of code"""
    fives = []
    fours=  []
    fulls =  []
    threes =  []
    twos =  []
    ones =  []
    highs =  []
    input_txt = open_file_safely("day7.txt")
    hands = namedtuple('hands','cards, bid')
    for i in input_txt:
        cards, bid = i.split(' ')
        tmp = sorted(Counter(cards).values(), reverse=True)
        match tmp[0]:
            case 5:
                fives.append(hands(cards=cards, bid =int(bid)))
            case 4:
                fours.append(hands(cards=cards, bid =int(bid)))
            case 3:
                if tmp[1] == 2:
                    fulls.append(hands(cards=cards, bid =int(bid)))
                else:
                    threes.append(hands(cards=cards, bid =int(bid)))
            case 2:
                if tmp[1] == 2:
                    twos.append(hands(cards=cards, bid =int(bid)))
                else:
                    ones.append(hands(cards=cards, bid =int(bid)))
            case 1:
                    highs.append(hands(cards=cards, bid =int(bid)))              
    fives = sub_sort_hands(fives, True)    
    fours = sub_sort_hands(fours, True)
    fulls = sub_sort_hands(fulls, True)  
    threes = sub_sort_hands(threes, True)
    twos = sub_sort_hands(twos, True)  
    ones = sub_sort_hands(ones, True)
    highs = sub_sort_hands(highs, True)
    
    rank = 1000
    sum_win = 0
    sum_win += calc_winnings(fives, rank)
    rank -= len(fives)
    sum_win += calc_winnings(fours, rank)
    rank -= len(fours)
    sum_win += calc_winnings(fulls, rank)
    rank -= len(fulls)
    sum_win += calc_winnings(threes, rank)
    rank -= len(threes)
    sum_win += calc_winnings(twos, rank)
    rank -= len(twos)
    sum_win += calc_winnings(ones, rank)
    rank -= len(ones)  
    sum_win += calc_winnings(highs, rank)

    print("part1", sum_win)
    
def part2():
    """Part2 of day 7 of Advent of code """
   
    fives2 = []
    fours2=  []
    fulls2 =  []
    threes2 =  []
    twos2 =  []
    ones2 =  []
    highs2 =  []
    input_txt2 = open_file_safely("day7.txt")
    hands = namedtuple('hands','cards, bid')
    for i in input_txt2:
        cards, bid = i.split(' ')
        temp = Counter(cards)
        del temp['J']
        tmp = sorted(temp.values(), reverse=True)
        jokers = cards.count('J')
        if jokers != 5:
            match tmp[0]:
                case 5:
                    fives2.append(hands(cards=cards, bid =int(bid)))
                case 4:
                    if jokers == 1:
                        fives2.append(hands(cards=cards, bid =int(bid)))
                    else:
                        fours2.append(hands(cards=cards, bid =int(bid)))
                case 3:
                    if len(tmp) > 1: 
                        if tmp[1] == 2:
                            fulls2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 2:
                            fives2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 1:
                            fours2.append(hands(cards=cards, bid =int(bid)))
                        else:
                            threes2.append(hands(cards=cards, bid =int(bid)))
                    else:
                        if jokers == 2:
                            fives2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 1:
                            fours2.append(hands(cards=cards, bid =int(bid)))
                        else:
                            threes2.append(hands(cards=cards, bid =int(bid)))
                case 2:
                    if len(tmp) > 1:
                        if tmp[1] == 2:
                            if jokers == 1:
                                fulls2.append(hands(cards=cards, bid =int(bid)))
                            else:
                                twos2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 3:
                            fulls2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 2:
                            fours2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 1:
                            threes2.append(hands(cards=cards, bid =int(bid)))
                        else:
                            ones2.append(hands(cards=cards, bid =int(bid)))
                    else:
                        if jokers == 3:
                            fives2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 2:
                            fours2.append(hands(cards=cards, bid =int(bid)))
                        elif jokers == 1:
                            threes2.append(hands(cards=cards, bid =int(bid)))
                        else:
                            ones2.append(hands(cards=cards, bid =int(bid)))
                case 1:
                    match jokers:
                        case 4:
                            fives2.append(hands(cards=cards, bid =int(bid)))
                        case 3:
                            fours2.append(hands(cards=cards, bid =int(bid)))
                        case 2:
                            threes2.append(hands(cards=cards, bid =int(bid)))
                        case 1:
                            ones2.append(hands(cards=cards, bid =int(bid)))
                        case 0:
                            highs2.append(hands(cards=cards, bid =int(bid)))    
        else:
            fives2.append(hands(cards=cards, bid =int(bid)))
            
    fives2 = sub_sort_hands(fives2, False)    
    fours2 = sub_sort_hands(fours2, False)
    fulls2 = sub_sort_hands(fulls2, False)  
    threes2 = sub_sort_hands(threes2, False)
    twos2 = sub_sort_hands(twos2, False)  
    ones2 = sub_sort_hands(ones2, False)
    highs2 = sub_sort_hands(highs2, False)

    rank2 = 1000
    sum_win2 = 0
    sum_win2 += calc_winnings(fives2, rank2)
    rank2 -= len(fives2)
    sum_win2 += calc_winnings(fours2, rank2)
    rank2 -= len(fours2)
    sum_win2 += calc_winnings(fulls2, rank2)
    rank2 -= len(fulls2)
    sum_win2 += calc_winnings(threes2, rank2)
    rank2 -= len(threes2)
    sum_win2 += calc_winnings(twos2, rank2)
    rank2 -= len(twos2)
    sum_win2 += calc_winnings(ones2, rank2)
    rank2 -= len(ones2)  
    sum_win2 += calc_winnings(highs2, rank2)

    print("part2", sum_win2)

def day7():
    """Day 7 of Advent of code """
    # record start time
    start = time.time()
    
    part1()
    part2()
    
    # record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")
day7()
