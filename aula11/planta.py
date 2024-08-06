print("programa para calcular a media de crescimento da planta\n")

meses = int(input("Quanto meses voce deixou a planta crescer?:\n"))
lista = []

for i in range(meses):
    alt = float(input(f"Qual a altura da {i + 1} mes:\n"))
    lista.append(alt)

soma = 0
for l in range(meses):
    soma = soma + lista[l]

media = soma / meses

print(lista)
print(f"A media de crescimeto é: {media}")
