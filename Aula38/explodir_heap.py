

class No:
    lista = [x for x in range(1000)]
    proximo = None

if __name__ == "__main__":

    raiz = No()
    temp = raiz
    while True:
        outro = No()
        temp.proximo = outro

