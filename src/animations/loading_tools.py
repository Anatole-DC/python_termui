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

UP = "\033[F"

def generate_grid(grid_content: str="", height: int=10) ->  None:
    for i in range(0, height):
        print(f"{grid_content}")

def update_line(line_number: int, update: str) -> None:
    print(f"{line_to_go_up(line_number)}{update}{go_back_to_end(line_number)}")

def line_to_go_up(line_number: int, total_number_of_lines: int=10) -> str:
    return UP * (total_number_of_lines - line_number + 1)

def go_back_to_end(line_number: int, total_number_of_lines: int=10) -> str:
    return "\n" * (total_number_of_lines - line_number)
