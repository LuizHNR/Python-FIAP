def area_retangulo(b, a):
    area = b * a
    return area

def area_triangulo(b, a):
    area = b * a / 2
    return area

print("PROGRAMA PARA CALCULAR AREAS")

base = float(input("Informa o valor da base:\n"))

altura = float(input("Informe o valor da altura:\n"))

menu = """
Infome o tipo do objeto
(T)riangulo
(R)etangulo
"""
opcao = input(menu + "\nResposta:").lower()[0]

if opcao == 't':
    resultado = area_triangulo(base, altura)
    print("A area do triangulo é: ", resultado)
elif opcao == 'r':
    resultado = area_retangulo(base, altura)
    print("A area do retangulo é: ", resultado)

