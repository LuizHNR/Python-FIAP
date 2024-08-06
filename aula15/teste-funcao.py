def somar_lista():
    soma = 0
    for numero in lista:
        soma = soma + numero
    return soma


lista = [1, 2, 3, 4 ,5 ,6]

executando = True
while executando:
    print("PROGRAMA PARA CALCULAR SOMA E MEDIA")
    menu = """
        Calcular a (S)oma da Lista
        Calcular a (M)edia da Lista
        (X) Sair
    """
    opcao = input(menu + "\nResposta :").upper()[0]

    if opcao == 'S':
        s = somar_lista()
        print("Resultado da função é: ", s)
    elif opcao == 'M':
        s = somar_lista()
        media = s / len(lista)
        print("Media da função é: ", media)

    elif opcao == 'X':
        print("Até breve... !!")
        executando = False

print("Fim do programa")