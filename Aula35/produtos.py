produtos = [ {"nome": "Camisa", "preço": 50, "em_estoque": True}, 
            {"nome": "Calça", "preço": 80, "em_estoque": False}, 
            {"nome": "Chapéu", "preço": 30, "em_estoque": True}, ] 

def estoque_verdadeiro(estoque):
    for estoque in produtos:
        if estoque["em_estoque"] != True:
            return False
        else:
            return True
    
nova_lista = filter(estoque_verdadeiro, produtos)

print("Produtos em estoque:\n ", list(nova_lista))