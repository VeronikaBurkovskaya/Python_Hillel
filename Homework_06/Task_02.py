"""У додатку є json файл. Написати програму, яка прочитає його та порахує загальну тривалість всіх треків в альбомі.

  Базовий кейс - поверне кількість секунд.

  * Дод. ускладнення повернути у вигляді рядка години:хвилини:секунди, прик. 0:41:39"""

import json
import time


def convert_json_to_list(file_name: str):
    with open(file_name, 'r') as file_json:
        return json.load(file_json)


def get_duration(list_of_track) -> list[int]:
    result = []
    for i in list_of_track['album']['tracks']['track']:
        result.append(int(i['duration']))
    return result


def sum_of_duration(tracks: list[int]) -> str:
    result = 0
    for i in tracks:
        result += i
    print(result)
    return covert_sec_to_min(result)


def covert_sec_to_min(seconds: int) -> str:
    result = time.strftime('%H:%M:%S', time.gmtime(seconds))
    return result


fl = convert_json_to_list('acdc.json')
tracks = get_duration(fl)

print(get_duration(fl))
print(sum_of_duration(tracks))

