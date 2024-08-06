lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
            # inicio : termino : passo
sub_lista = lista[4:      8:      1]
sub_lista2 = lista[0: 10: 2]
# inverter a lista
sub_lista3 = lista[9: : -1] # ou sub_lista3 = lista[ : : -1]

print(lista)
print(sub_lista)
print(sub_lista2)
print(sub_lista3)