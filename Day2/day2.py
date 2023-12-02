from pathlib import Path


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
   input = open_file_safely("day2.txt")
   print(input)

day2()