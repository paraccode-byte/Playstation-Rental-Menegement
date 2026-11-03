import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def to_int(n):
    try:
        return int(n)
    except ValueError:
        return False