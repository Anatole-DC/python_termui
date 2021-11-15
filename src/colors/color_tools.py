from src.colors.colors import COLORS, RESET

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

