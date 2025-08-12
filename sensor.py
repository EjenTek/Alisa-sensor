#!/usr/bin/python3

import requests

url = "https://api.iot.yandex.net/v1.0/devices/" #Заменить ID своего датчика
token = 'Ваш токен'

headers= {"Authorization" : f"Bearer {token}", "Content-Type": "application/json"}

resp = requests.get(url, headers=headers)
resps = dict(resp.json())
for key, values in resps.items():
    if key == 'properties':
        for z in values:
            z = dict(z)
            for keyz, valuez in z.items():
                if keyz == 'state':
                    nameelement = valuez.get('instance')
                    print(valuez.get('value'))
                    text_file = open(nameelement, "w+")
                    text_file.write(str(valuez.get('value')))
                    text_file.close()
