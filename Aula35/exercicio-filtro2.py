vendas = [120, 80, 150, 90, 200]

def minimo(vendas):
    if vendas >= 100:
        return True
    
lista_minimo = filter(minimo, vendas)

def desconto( venda ):
    venda -= (venda * 10) / 100
    return venda

nova_lista = map(desconto, lista_minimo)

print(list(nova_lista))