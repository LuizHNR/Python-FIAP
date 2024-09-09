import requests

url = "https://tdspm-luiz-default-rtdb.firebaseio.com/contatos.json"

contato = { "nome": "Alberto Santos",
            "email": "alberto@teste",
            "telefone": "11111-1111" 
        }

response = requests.post(url, json=contato)
print(response)