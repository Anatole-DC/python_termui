from src.colors.colors import COLORS, RESET
from random import randint

def colored(text: str, color: str, color_type: str="font") -> str:
    """
        Return the colorized version of the text passed in parameters
    """

    return colorize(text, get_color(color, color_type))

def get_color(color: str, color_type: str) -> str:
    """
        Fetch the color from the color pannel
    """

    try:
        color = COLORS[color.upper()][color_type]
        return color
    except:
        print(f"{color} does not have any {color_type} code registered. Default will be taken.")
        return RESET

def colorize(text: str, color: str) -> str:
    """
        Take a string and a color, and returns the string colorized.
    """
    return f"{color}{text}{RESET}"

def rgb_colored(text: str, red: int, green: int, blue: int) -> str:
    return f"\033[38;2;{red};{green};{blue}m{text}\033[38;2;255;255;255m"

def multicolored(text: str) -> str:
    colored_text = ""
    for char in text:
        colored_text += rgb_colored(
                            text=char,
                            red=randint(0, 255),
                            green=randint(0, 255),
                            blue=randint(0, 255)
                        )

    return colored_text