"""
@TODO
The goal is to create a y axis, on which we will know the coordinates of each line

#1    #####################################################
#2      Some text
#2      ```                 ____  +++
#4
#5
#6             _|_|_
#7             _|_|_
#8              | |
#9
#10   #####################################################


Then, we will have to create a function update line, that will update(str) the line with the proper modifications.

"""

from time import sleep

UP = "\033[F"

def generate_grid(number_of_lines: int=10) ->  None:
    for i in range(0, number_of_lines):
        print(f"")

def update_line(line_number: int, update: str) -> None:
    print(f"{line_to_go_up(line_number)}#{line_number}{update}{go_back_to_end(line_number)}")

def line_to_go_up(line_number: int, total_number_of_lines: int=10) -> str:
    return UP * (total_number_of_lines - line_number + 1)

def go_back_to_end(line_number: int, total_number_of_lines: int=10) -> str:
    return "\n" * (total_number_of_lines - line_number)