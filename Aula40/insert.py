import os
import oracledb

if __name__ == "__main__":

    usuario = os.environ.get("PYTHON_ORACLE_USER")
    senha = os.environ.get("PYTHON_ORACLE_PASS")
    db_path = "oracle.fiap.com.br:1521/orcl"
    print(f"Usuario: {usuario} e {senha}")

    con = oracledb.connect(user=usuario, password = senha, dsn=db_path)

    # sql = '''
    #     INSERT INTO time_futebol(id, nome, jogadores, vitorias, derrotas, empates, animo)
    #     VALUES (1, 'Corinthians', 26, 2, 8, 2, 10)
    # '''

    sql = '''
        INSERT INTO time_futebol(id, nome, jogadores, vitorias, derrotas, empates, animo)
        VALUES (3, 'Vasco da Gama', 25, 0, 6, 2, 30)
    '''

    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    con.close()