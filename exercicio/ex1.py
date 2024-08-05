texto = "Digite um numero:\n"

valido = False

while valido == False:
    digitado = input(texto)

    try:
         n = int(digitado)
         valido = True
    except:
         print("----------!numero invalido----------")