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

    cursor = con.cursor()

    sql = 'SELECT * FROM time_futebol'
    times = cursor.execute(sql)

    for time in times:
        print(time)

    con.close()