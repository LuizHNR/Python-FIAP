contador = 1

class No:
    lista = [x for x in range(100000000)]
    proximo = None

if __name__ == "__main__":

    raiz = No()
    temp = raiz
    while True:
        contador = contador + 1
        print(f"Contador: {contador}")
        outro = No()
        temp.proximo = outro
        temp = outro

