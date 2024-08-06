import random

#Menu
def menu ():
    menu = ("\n----------------------------------------------------------\n                  B E M   V I N D O\n\n"
            "Esses são os serviços que temos disponiveis:\n"
            "\n[1] - Conversar com nossa IA para ajuda mecânica rápida\n"
            "[2] - Olá Usuario você deseja se cadastrar?\n"
            "[3] - Cadastrar a sua oficina de mecânica\n"
            "[4] - Cadastrar o seu serviço de guincho\n"
            "[5] - Finalizar o Programa\n"
            "----------------------------------------------------------")
    
    resposta_invalida_True = True
    mensagem_menu = "Qual serviço o senhor(a) deseja?\n==> "

    while resposta_invalida_True == True:
        print(menu)
        resposta = input(mensagem_menu)
        if resposta != "1" and resposta != "2" and resposta != "3" and resposta != "4" and resposta != "5":
            mensagem_menu = "Por favor digite algum valor correspondente com o Menu\n==> "
        else: 
            resposta_invalida_True = False
    return resposta



def conversa_IA ():
    menu_IA = ("\n\nOlá, sou uma Inteligência Artificial e irei lhe ajudar neste momento. (Caso meus serviços não lhe sirvam contate meus criadores)\n\n\n"  
                    '[1] - "Meu carro acabou de parar no meio da estrada"\n'
                    '[2] - "Desejo voltar ao menu"\n'
                    '[3] - "Não preciso de nada quero sair deste programa"')
    mensagem_IA = ("Quais dos meus serviços o senhor(a) precisa?\n==> ")


    resposta_invalida_IA = True
    while resposta_invalida_IA == True:
        print(menu_IA)
        resposta = (input(mensagem_IA))


        if resposta != "1" and resposta != "2" and resposta != "3":
            mensagem_IA = "Por favor digite algum valor correspondente com o Menu\n==> "
        else:
            resposta_invalida_IA = False

    if resposta == "1":
        posiveis_probl = ["aconteceu um arrefecimento","deu pane elétrico"," a embreagem esta desgastada", " tem deficiência de lubrificação do motor"]
        qnt_probl = len(posiveis_probl)

        lista_num = []
        for i in range(qnt_probl):
            lista_num.append(i)

        index = random.choice(lista_num)
        print(f'De acordo com os sensores do seu carro o problema em questão é que {posiveis_probl[index]}')
        guincho_escolha = input("Quer que eu já chame o Guincho mais em conta e eficiente para o senhor?(S/N)")

        if guincho_escolha == "S":
            print("O guincho esta a caminho senhor(a), agora va para nosso mapa de mecanicos e decida o mecanico que o senhor deseja ir")
        elif guincho_escolha == "N":
            print("Tudo bem, lembre-se de olhar nosso mapa para ter uma ideia sobre mecanicos proximos")
        return True

    elif resposta == "2":
        return True
    
    elif resposta == "3":
        return False



#cadastro do mecanico
def cadastro_mec():
    dic_mecanico = {}
    dic_mecanico["nome"] = input("Digite o seu nome:\n")
    dic_mecanico["contato"] = input("Digite o seu contato:(Ex erickaxs@gmail... , 11 975...)\n")
    dic_mecanico["preco"] = float(input("Digite a média do preço do seu serviço em reais:\nR$"))
    dic_mecanico["regiao"] = input("Digite a sua região:(Ex: SP/São Paulo)\n")
    return dic_mecanico




#cadastro do guincho
def cadastro_guin():    
    dic_guincho = {}
    dic_guincho["local_atual"] = input("Digite o seu local atual:(Rua Euclides Alves...)\n")
    dic_guincho["empresa"] = input("Digite o nome da sua empresa:\n")
    dic_guincho["contato"] = input("Digite o seu contato:(Ex erickaxs@gmail... , 11 975...)\n")
    return dic_guincho



#cadastro do usuario
def cadastro_user():
    lista_veiculo = []
    dic_cliente = {}

    dic_cliente["cpf"] = input("Digite o seu CPF:\n")
    dic_cliente["nome"] = input("Digite o seu nome:\n")
    dic_cliente["idade"] = int(input("Digite a sua idade:\n"))
    dic_cliente["local_real"] = input("Digite o seu local atual:\n")
    seguro_posse = input("Você possui seguro?(S/N)\n")

    if seguro_posse == "S":
        dic_cliente["seguradora"] = input("Digite a sua segurado:\n")

    dic_cliente["quantidade_veiculo"] = quantidade_Vec = int(input("Digite a sua quantidade de veiculos:\n"))

    for i in range(quantidade_Vec):
        dic_veiculo = {}
        dic_veiculo["placa"] = input(f"Digite a placa do seu {i + 1}º veiculo:\n")
        dic_veiculo["modelo"] = input(f"Digite o modelo do seu {i + 1}º veiculo:\n")
        dic_veiculo["cor"] = input(f"Digite a cor do seu {i + 1}º veiculo:\n")
        dic_veiculo["ano"] = input(f"Digite o ano do seu {i + 1}º veiculo:\n")

        lista_veiculo.append(dic_veiculo)

    dic_cliente["carros"] = lista_veiculo
    return dic_cliente


#Funcionalidade
repetir = True
while repetir == True:
    decisao = menu()

    if decisao == "1":
        repetir = conversa_IA()

    elif decisao == "2":
        d_cliente = cadastro_user()

    elif decisao == "3":
        d_mecanico = cadastro_mec()

    elif decisao == "4":
        d_guincho = cadastro_guin()
    elif decisao == "5":
        repetir = False
print("Fim do Programa")