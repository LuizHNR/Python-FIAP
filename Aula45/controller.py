from servico import Servico

class Controller:
    
    def __init__(self):
        self.servico = Servico()
    
    def cadastrar(self, contato):
        print("Cadastrando o contato")
        self.servico.cadastrar_firebase(contato)
    
    def pesquisar(self):
        print("Pesquisar contato")
    
    def remover(self):
        print("Remover contato")
    
    def atualizar(self):
        print("Atualizar contato")
    
    def sair(self):
        pass