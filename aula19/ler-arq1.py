arq1 = open("D:/1TDSPM//COMPUTATIONAL THINKING USING PYTHON/aula19/nomes-idades.txt", "r")

#texto = arq1.read()
#print(texto)

# linha1 = arq1.readline()
# print(linha1)

# linha2 = arq1.readline()
# print(linha2)

# linha3 = arq1.readline()
# print(linha3)

lista = []
linha = "-"
while linha != "":
    #readline é para ler a linha
    linha = arq1.readline()
    linha = linha.replace("\n", "")
    if linha != "":
        dados = linha.split(";")
        print("Dados: ", dados)
        d = {
            "nome": dados[0],
            "idade": int(dados[1])
        }

        #append é para adicionar na lista
        lista.append(d)

print(lista)

arq1.close()