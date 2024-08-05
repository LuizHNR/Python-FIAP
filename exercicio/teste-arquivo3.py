arq1 = open("./nomes.txt", "r", encoding="utf-8")

arq2 = open("./teste.txt", "w", encoding="utf-8")

texto = " "
while texto != "":
    texto = arq1.readline()
    arq2.write(texto)

arq1.close()
arq2.close()