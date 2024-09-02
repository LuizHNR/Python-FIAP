#MANEIRAS DE IMPORTAR

from arquivo_funcoes import somar, dividir
print(f"Soma: {somar(10,20)}")
print(f"Dividir: {dividir(20,10)}")

import arquivo_funcoes
print(f"Soma: {arquivo_funcoes.somar(10,20)}")