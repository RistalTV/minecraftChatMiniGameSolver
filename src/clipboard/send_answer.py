from time import sleep

import pyperclip


def send_answer(words=[]):
    for word in words[::-1]:
        if len(words) > 1:
            sleep(2)
        pyperclip.copy(word)
