import os
from controller import Controller
from model import Contato
from datetime import datetime

class View:
    
    rodando = True
    
    def __init__(self):
        self.control = Controller()
        
    def ler_dados_contato(self):
        print("Digite o nome do conbtato")
        contato = Contato()
        contato.nome = input("Nome: ")
        contato.telefone = input("Telefone: ")
        contato.email = input("Email: ")
        str_nascimento = input("Nascimento: ")
        contato.nascimento = datetime.strptime(str_nascimento, '%d/%m/%Y')
        return contato
        
    
    def menu_principal(self):
        os.system("CLS")
        print("Agenda de contato no Firebase")
        print("""Menu Principal
              (C)adastrar
              (P)rocurar contato existente
              (R)emover Contato especifico
              (A)tualizar contato especifico
              (S)air do sistema""")
        opcao = input("Escolha sua opção e tecle <ENTER> ==>")
        if len( opcao ) > 0:
            opcao = opcao.upper()[0]
            match opcao:
                case 'C':
                    contato = self.ler_dados_contato()
                    self.control.cadastrar( contato )
                case 'P':
                    self.control.pesquisar()
                case 'R':
                    self.control.remover()
                case 'A':
                    self.control.atualizar()
                case 'S':
                    print("Até breve :) Obrigado por usar o sistema")
                    self.rodando = False
                case _:
                    print("Opção invalida\n")
        else:
            print("Voce precisa selecionar uma opção")
            
    def executar(self):
        while self.rodando:
            self.menu_principal()
            input("Tecle <ENTER> para continuar")
            
if __name__ == "__main__":
    view = View()
    view.executar()
    
        