from modelo import Contato
from repositorio import Repositorio

class Controle:
    
    def __init__(self) -> None:
        self.lista_contatos = []
        self.repositorio = Repositorio()
        
    def salvar(self, contato : Contato ):
        self.repositorio.adicionar_contato(contato)
    
    def pesquisar(self, nome_pesquisa: str) -> list:
        self.lista_contatos.clear()
        temp_lista = self.repositorio.pesquisar_contato(nome_pesquisa)
        self.lista_contatos.extend( temp_lista )
        return self.lista_contatos
    
    def atualizar(self, conato_id : int, contato : Contato):
        self.repositorio.atualizar_contato(conato_id, contato)
    
    def apagar(self, contato_id: int):
        self.repositorio.remover_contato(contato_id)