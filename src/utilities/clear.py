from os import system, name
from time import sleep


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for a mac and linux
    else:
        _ = system('clear')
