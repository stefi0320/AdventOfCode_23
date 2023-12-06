import time

def calc_winners(time_limit, distance):
    """ Calculate product of winning distances """
    mult = 1

    for t, limit in enumerate(time_limit):
        sum_dist = 0
        half_time = limit//2
        if limit % 2 == 0:
            max_distance = half_time * half_time
            sum_dist+=1
            for i in range(half_time):
                max_distance = max_distance - (1+(2*i))
                if max_distance > distance[t]:
                    sum_dist+=2
                else:
                    break
        else:
            max_distance = half_time * (limit -half_time)
            sum_dist+=1
            for i in range(half_time+1):
                max_distance = max_distance - (2+(2*i))
                if max_distance > distance[t]:
                    sum_dist+=1
                else:
                    break
            sum_dist *= 2
        mult *= sum_dist
    return mult

def day6():
    """Day 6 of Advent of code """
    # record start time
    start = time.time()

    #part1
    print(calc_winners([38,94,79,70],[241,1549,1074,1091]))

    #part2
    print(calc_winners([38947970],[241154910741091]))

    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day6()
