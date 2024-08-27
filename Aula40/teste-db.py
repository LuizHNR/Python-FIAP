import os
import oracledb

if __name__ == "__main__":

    usuario = os.environ.get("PYTHON_ORACLE_USER")
    senha = os.environ.get("PYTHON_ORACLE_PASS")
    db_path = "oracle.fiap.com.br:1521/orcl"
    print(f"Usuario: {usuario} e {senha}")

    con = oracledb.connect(
        user=usuario,
        password = senha,
        dsn=db_path
    )
        
    ddl_times_futebol="""
        CREATE TABLE time_futebol (
        id NUMBER(10),
        nome VARCHAR2(60),
        jogadores NUMBER(5),
        vitorias NUMBER(5),
        derrotas NUMBER(5),
        empates NUMBER(5),
        animo NUMBER(5),
        CONSTRAINT times_futebol_pk PRIMARY KEY (id)
        )
    """

    print(f"Database version: {con.version}")

    cursor = con.cursor()
    cursor.execute(ddl_times_futebol)
    con.commit()
    # Para desfazer o commit/alterações
    # con.rollback()
    print("Tabela foi criada")

    con.close()