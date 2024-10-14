class Pizza:

    def __init__(self, sabor="", preco = 0, tamanho = ""):
        self.sabor = sabor
        self.preco = preco
        self.tamanho = tamanho
    
    def to_dict(self) -> dict:
        dici = {"sabor": self.sabor, "preco": self.preco, "tamanho": self.tamanho}

        return dici

    def from_dict( dicionario : dict):
        dicionario = {"sabor": frango, "preco": 100, "tamanho": "grande"}

    def __str__(self):
        return print(f"""\n
        **************Pizza***************
        sabor: {self.sabor}
        possui o preço: {self.preco}
        tem o tamanho: {self.tamanho}\n""")


class apresentacao:

        def menu_principal():
            executar = True
            while executar:
                print("""\n
                -------------Menu------------------
                (C) -> Cadastrar
                (L) -> Ler Todos
                (S) -> Sair
                \n""")
                op = input("Digite a opção que desejar: ")[0].upper

                if len(op) > 0 and len(op) != "":
                    if op == "C":
                        cadastrar()
                    elif op == "L":
                        ler_todos()
                    elif op = "S":
                        print("Até logo!")
                        executar = False
                    else:
                        print(f"{op} invalida, digite uma opção valida")

        
        def cadastrar():
            pizza = Pizza() 
            executar = True

            while executar:
                pizza.sabor = input("Digite o sabor de pizza que você desejar cadastrar: ")
                pizza.preco = int(input("Digite o preço do sabor da pizza: "))
                pizza.tamanho = input("Digite o tamanho da pizza que vc deseja cadastrar: ")

                if pizza.sabor != "" and pizza.preco != 0 and pizza.tamanho != "":
                    print("Cadastrado com sucesso!")
                    return pizza
                    executar = False
                else:
                    print("Dados não preenchidos corretamente, prencher todos os dados")
                    return False

        def ler_todos():
            repositorio = Repositorio()
            repositorio.ler_todos()

class Repositorio:

    def __init__(self):
        self.URL_BASE = "https://checkpoint-rtdb.firebaseio.com"
        self.lista = []

    def gravar( pizza : Pizza):

        result = request.post(url=f"{self.URL_BASE}/pizzas.json",json=pizza.to_dict(),timeout= 200)

        return result.status_code == 200

    def ler_todos():
        result = request.get(url=f"{self.URL_BASE}/pizzas.json",timeout=200)
        dicionario = json.loads("/pizzas.json")

        for item in dicionario:
            lista = []

            c1 = (sabor: ""), 
            (preco: 0), 
            (tamanho: "")

            lista.append(c1)
        return lista


                