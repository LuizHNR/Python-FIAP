lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def filtro_3_4 ( numero ):
    
    # if numero % 3 == 0 or numero % 4 == 0:
    #     return True
    # else:
    #     return False
    # -------------OU----------
    return numero % 3 == 0 or numero % 4 == 0
        
nova_lista = filter( filtro_3_4, lista )

print("lista: \n", lista)

print("filtrando 3 ou 4:\n ", list(nova_lista))