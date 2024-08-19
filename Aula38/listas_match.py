lista = ["Joao", "maria", "jose", "sara"]

match lista:
    case [*nomes]:
        for nome in nomes:
            print("Nome:", nome)