import requests
import json
from django.http import JsonResponse

URL = "http://127.0.0.1:8000/usercreate/"

data = {
    'id': 5,
    'nom': 'Edgar',
    'prenom': 'Emmounei',
    'email': 'gduuizoop1@hhj.com',
    'motdepass': 'ggdjdoo1',
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

data = r.json()


# print(data)