
import sqlite3

DB_PATH = "pdv.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def inicializar_banco():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        nivel INTEGER NOT NULL
    )
    """)
    cur.execute("""
    INSERT OR IGNORE INTO usuarios (usuario, senha, nivel)
    VALUES ('admin', '1234', 3)
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE NOT NULL,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque REAL NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        total REAL NOT NULL,
        metodo_pagamento TEXT NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS itens_venda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        venda_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        quantidade REAL NOT NULL,
        preco_unit REAL NOT NULL,
        subtotal REAL NOT NULL,
        FOREIGN KEY (venda_id) REFERENCES vendas(id),
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    )
    """)
    con.commit()
    con.close()
