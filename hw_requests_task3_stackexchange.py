# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime

import requests
import datetime
import datetime as DT

TOKEN = ""

def test_request():
    url = "https://api.stackexchange.com/2.3/questions"

    dt_str_today = str(datetime.datetime.now())
    data_str_today = dt_str_today.split('.')[0]
    dt = DT.datetime.strptime(data_str_today, '%Y-%m-%d %H:%M:%S')
    print(f'Сейчас ({data_str_today}): {int(dt.timestamp())}')
    print(f'Два дня назад: {int(dt.timestamp()- 86400 * 2)}')
    fromdate = int(dt.timestamp()- 86400 * 2)
    today = int(dt.timestamp())

    params = {"fromdate":fromdate,"today":today,"tagged":"Python","site":"stackoverflow","sort":"week", "pagesize": 100}
    response = requests.get(url=url, params=params)
    print(response.status_code)
    return response.json()

data = test_request()

print("Найдены следующие вопросы про Python:")
for obj in data['items']:
    pprint(obj["link"])

if len(data["items"]) < 100:
    print(f'Количество вопросов про Python за 2 дня: {len(data["items"])}')
else:
    print(f'Количество вопросов про Python за 2 дня >= 100')



