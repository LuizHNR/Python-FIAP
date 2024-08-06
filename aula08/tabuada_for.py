print("Programa da Tabuada")

numero = int(input("Por favor digite um numero para eu calcular a tabuada:\n"))
      #inicializção          termino    incrementação
for i in range(0,              11,          1):
    res = numero * i
    print(f"\n{numero} X {i:>2} = {res:>2}")

