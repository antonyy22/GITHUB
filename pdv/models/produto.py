
from database.db import conectar

class Produto:
    @staticmethod
    def cadastrar(codigo, nome, preco, estoque):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO produtos (codigo, nome, preco, estoque)
            VALUES (?, ?, ?, ?)
        """, (codigo, nome, preco, estoque))
        con.commit()
        con.close()

    @staticmethod
    def buscar_por_codigo(codigo):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM produtos WHERE codigo = ?", (codigo,))
        p = cur.fetchone()
        con.close()
        return p

    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM produtos")
        dados = cur.fetchall()
        con.close()
        return dados
