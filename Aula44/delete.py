import requests
import json

url = "https://tdspm-luiz-default-rtdb.firebaseio.com/contatos/-O6LkvSoBAp51B8fLUgX.json"

response = requests.delete(url)

print(response)