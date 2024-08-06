print("Programa para calcular a média")

lista = []

for i in range(4):
    n = float(input(f"Qual é a sua {i + 1} nota?:\n"))
    lista.append(n)

print(f"Suas notas são: {lista}")

soma = 0
for i in range(4):
    numero = lista[i]
    soma = soma + numero
    print("numero: ", numero, "\tSoma é: ", soma)

media = soma / 5

print(f"Sua media é: {media}")
