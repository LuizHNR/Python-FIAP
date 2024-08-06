print("Programa da Tabuada")

numero = int(input("Por favor digite um numero para eu calcular a tabuada:\n"))

i = 0   #inicialização 

while i < 11:  #condição
    res = numero * i
    print(f"{numero} X {i:>2} = {res}")
    i = i + 1   #incremento