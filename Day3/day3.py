from pathlib import Path
import time

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
   
def day2():
   # record start time
   start = time.time()

   input = open_file_safely("day2.txt")


   for line in input:
      line = line.strip()

   #part1


   # record end time
   end = time.time()
   print("Runtime :", (end-start) * 10**3, "ms")

day2()