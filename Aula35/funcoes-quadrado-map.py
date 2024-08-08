lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def trasformar_quadrado( numero ):
    return numero * numero

lista_trasformada = map( trasformar_quadrado, lista )

print("Lista:\n", lista)
print("Lista transformada:\n", list(lista_trasformada) )