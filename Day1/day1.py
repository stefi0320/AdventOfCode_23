from pathlib import Path
import re
import string

string_to_digit = {
   'twoneightwo': '2182',
   "twoneight": '218',
   'oneightwo': '182',
   'eightwo': '82',
   'oneight': '18',
   "twone"  : '21',
   'one':   '1',
   'two':   '2',
   'three': '3',
   'four':  '4',
   'five':  '5',
   'six':   '6',
   'seven': '7',
   'eight': '8',
   'nine':  '9',
}

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
   
def replaceToDigits(line):
   for key, value in string_to_digit.items():
      line = line.replace(key, value)
   return line

def day1():
   input = open_file_safely("day1.txt")

   sum = 0 

   for line in input:
      tmp_line = replaceToDigits(line)
      digits = re.findall("\d", tmp_line)
      num = digits[0] + digits[-1]
      sum += int(num)
   print(sum)

day1()