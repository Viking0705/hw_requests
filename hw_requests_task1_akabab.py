from pprint import pprint

import requests

TOKEN = ""

def test_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    return response.json()

list_superhero = ['Hulk', 'Captain America', 'Thanos']
dict_superhero = {}
data = test_request()
pprint(type(data))
for object in data:
    if object["name"] in list_superhero:
        dict_superhero.setdefault(object["name"],object["powerstats"]["intelligence"])
print(f'Самый умный супергерой: {max(dict_superhero)}, intelligence={dict_superhero[max(dict_superhero)]}')
