def recebe_numero( texto="Digite um numero:\n" ):
    """
        Função utilidazada para pedir numero inteiro    
    """
    valido = False

    while valido == False:
        digitado = input(texto)

        try:
            numero = int(digitado)
            valido = True

        except:
            print("----------!numero invalido----------")
    return numero

n1 = recebe_numero("Digite o numero 1:\n")
n2 = recebe_numero("Digite o numero 2:\n")

soma = n1 + n2

print(f"A soma é: {soma}")