class Contato:
    
    def __init__(self, contato_id: int = 0, nome: str = "", telefone: str = "", email: str = ""):
        self.id = contato_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return f"""{self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"""
        
if __name__ == "__main__":
    c1 = Contato(1, "João Silva", "11 99999-9999", "uq9pJ@example.com")
    print(c1)