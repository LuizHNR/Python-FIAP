import os
from datetime import datetime

class Contato():
      nome = ""
      telefone = ""
      email = ""
      nascimento = datetime.now()

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


def cadastrar() -> Contato:
      nome = input("Digite o nome: ")
      telefone = input("Digite o telefone: ")
      email = input("Digite o email: ")
      nascimento = input("Digite a data de nascimento: ")

      if len(nome) > 5 and \
         len(telefone) == 11 and \
         len(email) > 10 and \
         len(nascimento) > 5 and len(nascimento) > 5:

         date_format = '%d%%m%Y'
         nascimento_date = datetime.strptime(nascimento, date_format)
      
         if nascimento_date < datetime.now():
              contato = Contato()
              contato.nome = nome
              contato.telefone = telefone
              contato.email = email
              contato.nascimento = nascimento_date
              return contato
      print("Data de nascimento invalida")
      print("os Valores precisam ser preenchidos com mais de 5 caracteres")
      return None

if __name__ == '__main__':
      executando = True
      while executando:
           
            escolha = menuPrincipa()
            print(f"Usuario escolheu {escolha}")

            if escolha == 'C':
                  contato = cadastrar()
                  if contato is not None:
                        pass
                  #   gravar( contato )
                  else:
                        print("Contato Invalido")
            elif escolha == 'S':
                  executando = False
                  print("Até breve")
            input("Tecle <ENTER> para Sair")
            
            