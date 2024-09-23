from Livro import modelo
from Repositorio import repositorio

class Apresentação:

    def __init__(self):
        pass

    def menu_principal():
        continuar = True

        while continuar:
            print("""\n
            (C) - Cadastrar
            (P) - Pesquisar
            (S) - Sair
            \n
            """)
            op = input("Digite a sua opção: ").Upper[0]

            if op == "C":
                cadastrar()   
            elif op == "P":
                pesquisar()                
            elif op == "S":
                exit()
                continuar = False
            else:
                print("Opção invalida, tecle <ENTER> para tentar novamente:\n")

    def cadastrar():
        rep = Repositorio()
        auto = Livro()
        voltar = True

        while voltar:

            auto.titulo = input("Digite o titulo do livro: ")
            auto.autor = input("Digite o nome do autor do livro: ")
            auto.ano = int(input("Digite o ano da publicação do Livro: "))

            if len(auto.titulo and auto.autor and auto.ano) > 0:
                voltar = False
                 return rep.gravar(auto)
                 
            else{
                print("Dados não preenchidos corretamente, tecle <ENTER> para tentar novamente:\n")
            }

    def pesquisar():
        rep = Repositorio
        voltar = True

        while voltar: 
            titulo = input("Digite o titulo que você deseja pesquisar: ")

            if len(titulo) > 0:
                voltar = False
                return rep.pesquisar(titulo)
            else:
                print("Você não preencheu corretamente, tecle <ENTER> para tentar novamente:\n")

    def exit():
        print("Volte Sempre :)")

menu_principal()