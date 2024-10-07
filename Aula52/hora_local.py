import requests
import json

requests.get("https://api.weatherapi.com/v1/timezone.json?key=8eda3e30011b43f58e5120023240710&q=Sao Paulo")

def Menu():
    executar = True
    while executar:
        print("""
              \n-----------Menu---------
[1] pesquisar
[2] sair
-------------------------
            \n""")
        op = int(input())
        
        match(op):
            case 1:
                pesquisar()
            case 2:
                print("Até Logo :)")
                executar = False
            
def pesquisar():
    zonas = {}
    cidade = input("Digite a cidade que vc deseja pesquisar: ")
    response = requests.get(f"https://api.weatherapi.com/v1/timezone.json?key=8eda3e30011b43f58e5120023240710&q={cidade}")
    print(f"\n{response.content}")
    dicionario = json.loads(response.content)
    print(f"O horario atudal da {cidade} é {dicionario["location"]["localtime"]}")
    
Menu()