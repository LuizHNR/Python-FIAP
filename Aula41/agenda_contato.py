import os


def menuPrincipa():
    while True:
      os.system("cls")
      print('''
            ----------Menu----------
                  (C)adastrar
                  (L)er Registro
                  (S)air\n
            ''')
    
      opcao = input("escolha a opção que desejar: ")[0].upper()
      if opcao in ['C', 'L', 'S']:
            return opcao
      
      input("opção invalida, tecle <ENTER> para tentar novamente")


def cadastrar(escolha):
      nome = input("Digite o nome: ")
      telefone = input("Digite o telefone: ")
      email = input("Digite o email: ")
      nascimento = input("Digite a data de nascimento: ")


if __name__ == '__main__':
      escolha = menuPrincipa()
      print(f"Usuario escolheu {escolha}")
      if escolha == 'C':
           cadastrar(escolha)
           print("Cadastrado com sucesso, Bem vindo")