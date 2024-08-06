print("Programa para Bom Dia")
executar = True

while executar == True:
    nome = input("digite o seu nome: \n")

    print("Bom dia, ", nome)

    print("Voce deseja continuar (S/N)?")
    continuar = input()

    
    if continuar == "N":
        executar = False
