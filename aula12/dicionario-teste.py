d1 = {}

d1["nome"] = "Maria"
d1["Telefone"] = "(11) 99034-433"

d2 = {"nome": "Joao", "telefone": "(11) 9999-999"} 
d3 = {"nome": "Carlos", "telefone": "(11) 9989-999"} 

lista = []
lista.append(d2)
lista.append(d3)

print(d1["nome"])
print(d1["Telefone"])

print(d2["nome"],"\n",d2["telefone"])

d = lista[1]
print("Nome: ", d["nome"])