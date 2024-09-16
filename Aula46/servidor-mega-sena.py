from random import randint

def numeros_mega_sena():
    numeros = []
    for i in range(6):
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
            i = i + 1
    return numeros
        
for i in range(20):
    print(numeros_mega_sena())        