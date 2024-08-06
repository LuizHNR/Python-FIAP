print("Calculos de áreas de retangulos")

while True: 
    base = float(input("Digite o tamanho da base em cm:\n"))
    altura = float(input("Digite a altura do retangulo em cm:\n"))
    area = base * altura

    print(f"A area do retangulo é: {area} cm²")

    print("voce deseja calcular novamente? (S/N)")
    novamente = input().lower()

    if novamente[0] == "n":
        break #Quebra o programa
    
print("\nFim do programa")




