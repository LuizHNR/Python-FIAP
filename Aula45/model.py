from datetime import datetime

class Contato:
    """
        Classe que descreve os objetos do Tipo Contato
    """
    id = ""
    nome = ""
    telefone = ""
    email = ""
    nascimento = datetime.now
    
    def __str__(self):
        return f"""()
        """
    
    
    def __init__(self, contato_id="", nome="", telefone="", email="", nascimento=datetime.now):
        self.id = contato_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nascimento = nascimento
    
if __name__ == "__main__":
    date_time_str = "01/04/2003"
    nascimento = datetime.strptime(date_time_str, '%d/%m/%Y')
    
    c1 = Contato("0001", "João Silva", "(11) 99999-9999", "joao@teste.com.br", nascimento)
    
    
    print(f"Contato: {c1}")