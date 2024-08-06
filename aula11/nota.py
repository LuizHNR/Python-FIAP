print("Programa para calcular a média")

lista = []

n = float(input("Qual é a sua primeira nota?:\n"))
lista.append(n)

n = float(input("Qual é a sua segunda nota?:\n"))
lista.append(n)

n = float(input("Qual é a sua terceira nota?:\n"))
lista.append(n)

media = (lista[0] + lista[1] + lista[2] ) / 3

print(" a media final é: ", media)