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


(done) Then, we will have to create a function update line, that will update(str) the line with the proper modifications.
(    ) We must add a feature that will only update some part of the line, and keep the rest of the line.
(    ) Create a progress bar with the percentages indicated and the progression is controlled with a parameter.
(    ) Create a grid with a character whose position is updated with the arrow

"""

from time import sleep
import keyboard
from src.colors.color_tools import colored

UP = "\033[F"

def generate_grid(grid_content: str="", height: int=10) ->  None:
    for i in range(0, height):
        print(f"{grid_content}")

def update_line(line_number: int, update: str, height: int=10) -> None:
    print(f"{line_to_go_up(line_number, height)}{update}{go_back_to_end(line_number, height)}")

def line_to_go_up(line_number: int, total_number_of_lines: int=10) -> str:
    return UP * (total_number_of_lines - line_number + 1)

def go_back_to_end(line_number: int, total_number_of_lines: int=10) -> str:
    return "\n" * (total_number_of_lines - line_number)

def keyboard_input():
    height = 2
    generate_grid("", height=height)
    choice=0
    update_line(1, "This is the first option", height)
    update_line(2, f"This is the second option", height)

    while keyboard.read_key() != "enter":
        if choice == 0:
            update_line(1, colored("This is the first option", "RED"), height)
            update_line(2, f"This is the second option", height)
        elif choice == 1:
            update_line(2, colored("This is the second option", "RED"), height)
            update_line(1, "This is the first option", height)

        if keyboard.read_key() == "up":
            choice += 1
        if keyboard.read_key() == "down":
            choice -= 1

        if choice < 0:
            choice = 1
        if choice > 1:
            choice = 0

    print(f"Option {choice}")

def tes():
    print(keyboard.read_key())