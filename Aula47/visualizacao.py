import os
from modelo import Contato
from controle import Controle

class Visualizacao:
    
    def __init__(self) -> None:
        self.controle = Controle()
    
    def criar_contato() -> Contato:
        c = Contato()
        print("")
        c.nome = input("Digite o nome completo do contato: ")
        c.telefone = input("Digite o telefone do contato: ")
        c.email = input("Digite o email do contato: ")
        
        return c
    
    def mostrar_contatos(self, lista_contatos: list) -> None:
        for contatos in lista_contatos:
            print("-"*40)
            print(contatos)
            
    def ler_id_contato(self) -> int:
        numero = -1
        while numero == -1:
            str_contato_id = input("Digite o id do contato que deseja remover: ")
            if len(str_contato_id) > 0 and str_contato_id.isnumeric():
                numero = int(str_contato_id)
            else:
                input("Id inválido, tecle ENTER para tentar novamente: ")
        return numero
    
    def menu_principal(self) -> None:
        os.system("cls")
        print("""
            ----------------AGENDA DE CONTATOS----------------\n
            (C)adastrar um contato\n
            (P)esquisar um contato\n
            (R)emover um contato\n
            (A)tualizar um contato\n
            (S)air\n
              """)
        entrada = input("Escolha uma opção: ")
        if (len(entrada) > 0):
            opcao = entrada.upper()[0]
            match (opcao):
                case "C":
                    c1 = self.criar_contato()
                    self.controle.salvar(c1)
                    
                case "P":
                    nome = input("Digite o nome do contato que deseja pesquisar: ")
                    lista_contatos = self.controle.pesquisar(nome)
                    self.mostrar_contatos(lista_contatos)
                    
                case "R":
                    contato_id = self.ler_id_contato()
                    self.controle.remover_contato( contato_id)
                    
                case "U":
                    self.atualizar_contato()
                case "S":
                    print("Saindo...")
                    print("Ate mais!")
                    exit()
                case _:
                    print("Opção inválida!")
                    self.menu_principal()