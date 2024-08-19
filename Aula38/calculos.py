def somar( n1, n2 ):
    soma = n1 + n2
    print("Soma realizada,")
    return soma

def subtrair( n1, n2 ):
    subtracao = n1 - n2
    print("Subtração realizada")
    return subtracao

if __name__ == "__main__":
    num1 = float(input("Digite o numero 1:"))
    num2 = float(input("Digite o numero 2:"))

    s = somar(num1, num2)
    print(f"O resultado da soma é: {s}")