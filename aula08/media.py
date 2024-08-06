print("Média final de alunos(as)\n")

repetir = True
while repetir == True:
    aluno = input("Digite o nome do aluno(a)\n")
    n1 = float(input("digite a primeira nota do aluno(a)\n"))
    n2 = float(input("digite a primeira nota do aluno(a)\n"))
    n3 = float(input("digite a primeira nota do aluno(a)\n"))

    media = (n1 + n2 + n3)/3
    print("Nome         nota 1           nota 2         nota 3       média final")
    print(f"{aluno:<14}{n1:<18.1f}{n2:<18.1f}{n3:<14.1f}{media:>3.1f}")

    print("Voce deseja repetir o programa novamente?: (S/N)")
    novamente = input().lower()
    if novamente[0] == "s":
        repetir = True 
    else:
        break

print("\nFim do programa")

