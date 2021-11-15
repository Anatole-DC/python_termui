from src.animations.loading_tools import generate_grid, update_line
from time import sleep

def test():
    generate_grid("[---------]")
    sleep(0.5)

    bar = "█"
    for i in range(1, 10):
        update_line(1, f"[{bar * i}")
        update_line(4, f"[{bar * i}")
        update_line(5, f"[{bar * i}")
        sleep(0.1)