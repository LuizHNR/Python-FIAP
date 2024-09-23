def Repositorio:
    def __init__():
        pass

    def database():
        usuario = os.environ.get("FIAP_ORACLE_USER")
        senha = os.environ.get("FIAP_ORACLE_PASS")
        url = os.environ.get("oracle.fiap.com.br:1521/orcl")

        conexao = oracledb.connect(
            user = usuario,
            password = senha,
            dns = url
        )

    def gravar(livro : Livro):
        cursor = conexao.cursor()
        cursor.execute("""INSERT INTO livros VALUES( 1=?, 2=?, 3=?);""", Livro.titulo, Livro.auto, Livro.ano)
        conexao.commit()

    def pesquisar(titulo : str) -> list:
        cursor = conexao.cursor()
        list = []
        cursor.execute(f"""SELECT * FROM livros WHERE {titulo}""")
        
        for dados in cursor:
            dados.titulo = {1}
            dados.autor = {2}
            dados.ano = {3}
            
            list.append(dados)
        
        return list
            
