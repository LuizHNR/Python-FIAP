consumo = float(input("Qual foi o consume de KWh ==> "))
instalacao = input("Qual o tipo de instalação, R/I/C ==> ")

instalacao = {'R': {500: 0.4, 'resto': 0.65},
              'I': {5000: 0.55, 'resto': 0.55},
              'C': {1000: 0.55, 'resto': 0.60}}
 
val_comp = list(instalacao[tipo])[0]
 
if consumo <= val_comp:
    preco = instalacao[tipo][val_comp]
else:
    preco = instalacao[tipo]['resto']
 
custo = consumo * preco
print(f"Valor a pagar: R$ {custo:7.2f}")

#######

consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")
if tipo == "R":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "I":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "C":
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preço
print(f"Valor a pagar: R$ {custo:7.2f}")