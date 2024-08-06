def menu_principal():
    print("SISTEMA DE GESTÃO PARA HORTIFRUTI")
    print("---------MENU PRINCIPAL------\n" +
        "(C)adastrar um produto\n" + 
        "(L)istar os produtos\n" +
        "(G)ravar em documento cvs\n" +
        "(S)air")
    
def solicita_opcao():
    print("Escolha sua opção:\n")
    return input().lower()[0]

def produto_cadastar( lista_produto ):
    produto = {}
    print("Digite o nome do produto: ")
    produto["nome"] = input()
    print("Digite a cor do produto: ")
    produto["cor"] = input()
    print("Digite o preço do produto: ")
    produto["preco"] = float(input())
    print("Digite a unidade de medida do produto: ")
    produto["unidade_medida"] = input()
    lista_produto.append( produto )

def produto_listar(lista_produto):
    for p in lista:
            print(f"Nome Produto: {p['nome']}\tCor: {p['cor']}")
            print(f"Preço: {p['preco']:.2f}\tUnidade de medida: {p['unidade_medida']}")

def gravar_arquivo( lista_produto ):
    arq1 = open("./hortfruti.csv", "w", encoding="utf-8")
    arq1.write("nome Produto, Cor, Preco, Unidade de Medida\n")
    for p in lista_produto:
        arq1.write(f"{p['nome']}, {p['cor']}, {p['preco']:.2f}, {p['unidade_medida']}\n")
    arq1.close()

lista = []
executando = True

while executando:
    menu_principal()
    opcao = solicita_opcao()

    if opcao == 'c':
       produto_cadastar( lista )

    elif opcao == 'l':
        produto_listar( lista )

    elif opcao == 'g':
        gravar_arquivo( lista )

    elif opcao == 's':
        print("Obrigado por usar o sistema, até breve")
        executando = False
print("Fim do programa")

