def menu():
    print(" Menu\n"
      "(C)adastrar\n"
      "(M)ostrar\n"
      "(R)emover\n"
      "(A)tualizar\n"
      "(S)air")

menu()
opcao = input("Escolha a sua opcão: ").upper()[0]

match opcao:
    case "C": print("Voce escolheu cadastrar")
    case "M": print("Voce escolheu Mostrar")
    case "R": print("Voce escolheu Remover")
    case "A": print("Voce escolheu Atualizar")
    case "S": print("Voce escolheu Sair")
    case _ : print("Opção invalida")