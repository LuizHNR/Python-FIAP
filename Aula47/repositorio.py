import oracledb
import os
from oracledb import Connection
from modelo import Contato
from controle import Controle


class Repositorio:
    
    def __init__(self):
        self.usuario = os.environ.get("FIAP_ORACLE_USER")
        self.senha = os.environ.get("FIAP_ORACLE_PASS")
        self.db_path = "oracle.fiap.com.br:1521/orcl"
        
    def gerar_conexao(self) -> Connection:
        con = oracledb.connect(
            user=self.usuario,
            password=self.senha,
            dsn=self.db_path
        )
        return con
    
    def adicionar_contato(self, contato: Contato) -> bool:
        conexao = self.gerar_conexao()  
        cursor = conexao.cursor()
        sql = """INSERT INTO contatos (nome, telefone, email) VALUES (:1, :2, :3)"""
        
        try:
            cursor.execute(sql, (contato.nome, contato.telefone, contato.email))
            conexao.commit()
            
        except Exception:
            conexao.rollback()
            return False
        
        conexao.close()
        return True
    
    def pesquisar_contato(self, nome: str) -> list:
        conexao = self.gerar_conexao()  
        cursor = conexao.cursor()
        sql = """SELECT * FROM contatos WHERE nome LIKE: :1"""
        
        cursor.execute(sql, (f"%{nome}%",))
        resultado = []
        
        for dados in cursor:
            resultado.append(dados)
        conexao.close()
        return resultado
        
    def remover_contato(self, contato_id: int) -> bool:
        conexao = self.gerar_conexao()  
        cursor = conexao.cursor()
        sql = """DELETE * FROM contatos WHERE id = :1"""
        
        try:
            cursor.execute(sql, (contato_id))
            conexao.commit()
            
        except Exception:
            conexao.rollback()
            return False
        
        conexao.close()
        return True
    
    def atualizar_contato(self, contato_id: int, contato: Contato) -> bool:
        conexao = self.gerar_conexao()  
        cursor = conexao.cursor()
        sql = """UPDATE INTO contatos SET nome = :1, telefone = :2, email = :3 WHERE id = :4"""
        
        try:
            cursor.execute(sql, (contato.nome, contato.telefone, contato.email, contato_id))
            conexao.commit()
            
        except Exception:
            conexao.rollback()
            return False
        
        conexao.close()
        return True