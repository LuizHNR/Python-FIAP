import os
import oracledb

usuario = os.environ.get("PYTHON_ORACLE_USER")
senha = os.environ.get("PYTHON_ORACLE_PASS")
db_path = "oracle.fiap.com.br:1521/orcl"
print(f"Usuario: {usuario} e {senha}")

con = oracledb.connect(
    user=usuario,
    password = senha,
    dsn=db_path
)

def CriarTabela():
    ddl_tabela_pet = '''

    CREAT TABLE tabela_pet (
    id NUMBER(10),
    nome VARCHAR2(60),
    raca VARCHAR2(20),
    nome_tutor VARCHAR2(100),
     CONSTRAINT tabela_pet_pk PRIMARY KEY (id)
    )
    '''
    if ddl_tabela_pet == True:
        print("Essa tabela ja existe")
    else:
        print("Tabela Criada com sucesso")


def InserirNaTabela():
    id_pet = int(input("Digite o id: "))
    nome = int(input("Digite o nome do cachorro: "))
    raca = int(input("Digite a raça do cachorro: "))
    nome_tt = int(input("Digite o nome do Tutor: "))


    sql = f'''
        INSERT INTO tabela_pet(id, nome, raca, nome_tutor)
        VALUES ({id_pet}, {nome}, {raca}, {nome_tt})
    '''

def ler_tabela():
    sql = 'SELECT * FROM tabela_pet'
    times = cursor.execute(sql)

    for time in times:
        print(time)

cursor = con.cursor()
con.commit()

executar = True
while executar:
    print('''
    -----------MENU-------------\n
          (1)-Criar tabela\n
          (2)-Inserir na tabela\n
          (3)-Ler Tabela\n
          (4)-Sair\n
''')
    op = int(input("Digite a opção que vc quer: "))

    if op == 4:
        executar = False
    elif op == 1:
        CriarTabela()
    elif op == 2:
        InserirNaTabela()
    elif op == 3:
        ler_tabela()
