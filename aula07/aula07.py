n = 1
while n <= 10:
    res = 7 * n
    print("7 x", n, "=", res)
    n = n + 1
    
print("\n")

n = 0
while n <= 20:
  print(n)
  n = n + 2    

print("\n")

executar_novamente = True
while executar_novamente == True:
    print("Por favor digite o seu nome: ")
    nome = input()
    print("Bom dia ", nome)
    print("\nVoce deseja executar novamente? (S/N)")
    resposta = input()
    if resposta == "S":
        executar_novamente = True
    else:
        executar_novamente = False
print("\nValeu por hoje ", nome, "OwO")