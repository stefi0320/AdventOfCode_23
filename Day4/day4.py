"""Module providing a function reading files."""
from pathlib import Path
import time

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

def day4():
   """Day 4 of Advent o f code """

   # record start time
   start = time.time()

   input_txt = open_file_safely("day2.txt")


   for line in input_txt:
      line = line.strip()

   #part1


   # record end time
   end = time.time()
   print("Runtime :", (end-start) * 10**3, "ms")

day4()
