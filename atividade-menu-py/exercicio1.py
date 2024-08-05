contato = {}
lista = []

def cadastrar():
    contato["nome"] = input("Digite o seu nome:\n")
    contato["email"] = input("Digite o seu email:\n")
    contato["tel"] = input("Digite o seu telefone:\n")
    contato["peso"] = float(input("Digite o seu peso:\n"))
    contato["idade"] = int(input("Digite a sua idade:\n"))
    return contato


executar = True
while executar == True:
    print("""-----------------------------\n
            MENU
    (C)adastrar
    (L)istar
    (P)esquisar
    (B)ackup em um arquivo
    (R)estaurar de um arquivo
    (S)air
    """)
    resposta = input().upper()[0]
        

    if resposta == "C":
        contatos = cadastrar()
        lista.append(contatos)
    elif resposta == "L":
        print(lista)

    elif resposta == "P":
        pesquisar_email = input("Digite o Email que voce deseja procurar==>\n")
        for i in range[len(lista)]:
            if pesquisar_email == lista[contato["email"]]:
                print(lista[contato["email"]])

            else:
                print("Não existe esse email cadastrado")
            
    elif resposta == "S":
        print("Até breve")
        executar = False

    else:
        resposta == True