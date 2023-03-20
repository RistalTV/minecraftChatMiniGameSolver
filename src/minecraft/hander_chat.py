import re
from random import randint

from ..clipboard.send_answer import send_answer
from ..solover_anagram.solover import decode_anagram


def handlerChat(text):
    original_text = text
    text = re.sub(r'\[[\w \0-9:]*]', '', text)
    text = text.replace("  ", " ")
    text = text.replace(":", "")
    text = text.strip()
    if "Задание".lower().strip() in text.lower().strip():
        result = None
        if "Расшифруй слово".lower().strip() in text.lower().strip():
            pattern = r"\[[\w \0-9:]*\]$"
            result = re.search(pattern, original_text, re.M | re.I)
            if result is not None:
                result = result.group()
                result = result.replace('[', '')
                result = result.replace(']', '')
                __tmp = decode_anagram(word=result)
                result = []
                for item in __tmp:
                    result.append(str(item).strip().lower())
                # print(f"--- {result_old} => {result}")
                print(f"{result}")
            # print(f"--- {text}")

        if "Угадай число".lower().strip() in text.lower().strip():
            listNumbers = [_ for _ in range(10)]
            result = [listNumbers.index(randint(0, len(listNumbers) - 1)) for _ in range(3)]
            # print(f"--- {text}")
            print(f'Финальный список: {result}')
            print(f'{result}')
        if "Реши пример".lower().strip() in text.lower().strip():
            text_old = text
            pattern = r"\d*\ [\+\-\*\\]*\ \d*"
            text = re.search(pattern, text_old, re.M | re.I)
            if text is not None:
                text = text.group()
                result = [f'{eval(text)}']
                print(f"{result}")
                # print(f"--- {text} = {result}")
                # print(f"--- {text_old}")
        if result is not None:
            send_answer(result)
