import requests

class Servico:
    
     url = "https://tdspm-luiz-default-rtdb.firebaseio.com/contatos.json"
    
    def __init__(self):
        pass
    
    def cadastrar_firebase(self, contato):
        contato_dic = {
            "nome": contato.nome,
            "id": contato.id,
            "telefone": contato.telefone,
            "email": contato.email, 
            "nascimento": contato.nascimento.strftime('%d/%m/%Y'),
        }
       
        response = requests.post( self.url, json=contato, timeout=100 )
        return response