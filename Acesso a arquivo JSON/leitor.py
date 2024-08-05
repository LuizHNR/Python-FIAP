import json

arquivo = open("./dados.json", "r", encoding="utf-8")
conteudo = arquivo.read()

lista = json.loads(conteudo)

print("lista: ")
print(lista)

for objeto in lista:
    print("Nome: ", objeto["nome"])