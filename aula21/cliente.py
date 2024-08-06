class Cliente:

    def __init__(self):
        self.nome = "Desconhecido"
        self.cpf = ""
        self.idade = 0

    def comprar(self):
        print(f"{self.nome} com {self.idade} anos está comprando um produto")
    
    def trocar(self):
        print(f"{self.nome} trouxe seu periferico para trocar")
    
    def reclamar(self):
        print(f"Vim reclamar de algo")