from typing import List

import keyboard
from src.colors.color_tools import colored

from src.animations.loading_tools import generate_grid, update_line

def select(choices: List[str], default_line_selected:int=2):

    # Initiating grid
    height = len(choices)

    generate_grid(height=height)

    # Outputting choices
    index = 1
    for choice in choices:
        if index == default_line_selected:
            choice = colored(choice, "RED")
        
        update_line(index, choice, height)
        index += 1

    # Selector
    choice = default_line_selected

    while keyboard.read_key() != "enter":

        if keyboard.read_key() == "up":
            update_line(choice, choices[choice - 1], height)
            choice -= 1
            if choice < 1:
                choice = height + 1
            update_line(choice, colored(choices[choice - 1], "RED"), height)

        if keyboard.read_key() == "down":
            update_line(choice, choices[choice - 1], height)
            choice += 1
            if choice > height + 1:
                choice = 1
            update_line(choice, colored(choices[choice - 1], "RED"), height)

    print(choice)