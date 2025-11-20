
from database.db import conectar

class Usuario:
    @staticmethod
    def login(usuario, senha):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT id, usuario, nivel FROM usuarios
            WHERE usuario = ? AND senha = ?
        """, (usuario, senha))
        u = cur.fetchone()
        con.close()
        return u
