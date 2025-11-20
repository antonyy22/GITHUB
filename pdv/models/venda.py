
from database.db import conectar
from datetime import datetime

class Venda:
    @staticmethod
    def criar_venda(total, metodo):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO vendas (data, total, metodo_pagamento)
            VALUES (?, ?, ?)
        """, (datetime.now().isoformat(), total, metodo))
        vid = cur.lastrowid
        con.commit()
        con.close()
        return vid

    @staticmethod
    def adicionar_item(venda_id, produto_id, qtd, preco):
        con = conectar()
        cur = con.cursor()
        subtotal = qtd * preco
        cur.execute("""
            INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unit, subtotal)
            VALUES (?, ?, ?, ?, ?)
        """, (venda_id, produto_id, qtd, preco, subtotal))
        con.commit()
        con.close()
