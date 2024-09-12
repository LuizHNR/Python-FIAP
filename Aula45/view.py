import os

class View:
    
    rodando = True
    
    def __init__(self):
        pass
    
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
                    pass
                case 'P':
                    pass
                case 'R':
                    pass
                case 'A':
                    pass
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
    
        