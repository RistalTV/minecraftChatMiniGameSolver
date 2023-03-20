import json

import requests

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.46",
    "sec-ch-ua": '"Opera GX";v="83", "Chromium";v="97", ";Not A Brand";v="99"',
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
}


def decode_anagram(word="привет мир"):
    url = f'https://anagram.poncy.ru/anagram-decoding.cgi?name=anagram_main&inword={word}&answer_type=1'
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data['result']


