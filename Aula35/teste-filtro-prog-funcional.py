lista = [1,2,3,4,5,6,7,8,9,10]

def filtro_impar( numero):
    if numero % 2 == 0:
        return False
    else:
        return True
    
nova_lista = filter( filtro_impar, lista)

print("lista: \n", lista)
print("Numeros impares \n", list(nova_lista))