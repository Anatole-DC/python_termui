from src.colors.color_tools import colorize, get_color
from random import randint

def rgb_colored(text: str, red: int, green: int, blue: int) -> str:
    """
        Return a text colorized according to an rgb code.
    """

    return f"\033[38;2;{red};{green};{blue}m{text}\033[38;2;255;255;255m"

def colored(text: str, color: str, color_type: str="font") -> str:
    """
        Return the colorized version of the text passed in parameters
    """

    return colorize(text, get_color(color, color_type))

def multicolored(text: str) -> str:
    """
        Return a multicolored string (implemented in the name of fun).
    """

    colored_text = ""
    for char in text:
        colored_text += rgb_colored(
                            text=char,
                            red=randint(0, 255),
                            green=randint(0, 255),
                            blue=randint(0, 255)
                        )

    return colored_text