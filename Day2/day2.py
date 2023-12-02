from pathlib import Path
import re

def open_file_safely(file_name):
   try:
      script_dir = Path(__file__).resolve().parent
      file_path = script_dir / file_name

      with open(file_path, 'r') as file:
         content = file.readlines()
      return content
   
   except FileNotFoundError:
      print(f"The file '{file_name}' was not found in the same directory as the script.")
      return None
   
def possible_by_color(find, tmp_string, max):
   possible = True
   rx = r"(\d+) {}".format(find)
   result = re.search(rx, tmp_string)
   if result:
      if int(result.group(1)) > max:
         possible = False
   return possible

def min_by_color(find, tmp_string):
   min_num = 0
   rx = r"(\d+) {}".format(find)
   result = re.search(rx, tmp_string)
   if result:
      min_num = int(result.group(1))
   return min_num

def day2():
   input = open_file_safely("day2.txt")
   sum_possible = 0
   sum_min = 0
   for line in input:
      line = line.strip()
      possible = True
      results = re.split('Game |:|;', line)
      # remove empty
      del results[0]
      id = results[0]
      # remove id
      del results[0]
   #part1
      for result in results:
        possible = possible_by_color('blue', result, 14)
        if False == possible:
            break
        possible = possible_by_color('red', result, 12)
        if False == possible:
           break
        possible = possible_by_color('green', result, 13)
        if False == possible:
           break
      if possible:
         sum_possible += int(id)
   #part2
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

day2()