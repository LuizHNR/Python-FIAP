produtos = [ {"nome": "Camisa", "preco": 50, "em_estoque": True}, 
            {"nome": "Calça", "preco": 80, "em_estoque": False}, 
            {"nome": "Chapéu", "preco": 30, "em_estoque": True}, ] 

def estoque_verdadeiro(produtos):
    if produtos ["em_estoque"] == True:
        return True
    
nova_lista = filter(estoque_verdadeiro, produtos)

print("Produtos em estoque:\n ", list(nova_lista))