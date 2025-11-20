import os

def criar_arquivo(caminho, conteudo):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"[OK] Arquivo criado: {caminho}")

# ------------------------------
# Conteúdos dos arquivos
# ------------------------------

db_py = """
import sqlite3

DB_PATH = "pdv.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def inicializar_banco():
    con = conectar()
    cur = con.cursor()
    cur.execute(\"\"\"
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        nivel INTEGER NOT NULL
    )
    \"\"\")
    cur.execute(\"\"\"
    INSERT OR IGNORE INTO usuarios (usuario, senha, nivel)
    VALUES ('admin', '1234', 3)
    \"\"\")
    cur.execute(\"\"\"
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE NOT NULL,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque REAL NOT NULL
    )
    \"\"\")
    cur.execute(\"\"\"
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        total REAL NOT NULL,
        metodo_pagamento TEXT NOT NULL
    )
    \"\"\")
    cur.execute(\"\"\"
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
    \"\"\")
    con.commit()
    con.close()
"""

usuario_py = """
from database.db import conectar

class Usuario:
    @staticmethod
    def login(usuario, senha):
        con = conectar()
        cur = con.cursor()
        cur.execute(\"\"\"
            SELECT id, usuario, nivel FROM usuarios
            WHERE usuario = ? AND senha = ?
        \"\"\", (usuario, senha))
        u = cur.fetchone()
        con.close()
        return u
"""

produto_py = """
from database.db import conectar

class Produto:
    @staticmethod
    def cadastrar(codigo, nome, preco, estoque):
        con = conectar()
        cur = con.cursor()
        cur.execute(\"\"\"
            INSERT INTO produtos (codigo, nome, preco, estoque)
            VALUES (?, ?, ?, ?)
        \"\"\", (codigo, nome, preco, estoque))
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
"""

venda_py = """
from database.db import conectar
from datetime import datetime

class Venda:
    @staticmethod
    def criar_venda(total, metodo):
        con = conectar()
        cur = con.cursor()
        cur.execute(\"\"\"
            INSERT INTO vendas (data, total, metodo_pagamento)
            VALUES (?, ?, ?)
        \"\"\", (datetime.now().isoformat(), total, metodo))
        vid = cur.lastrowid
        con.commit()
        con.close()
        return vid

    @staticmethod
    def adicionar_item(venda_id, produto_id, qtd, preco):
        con = conectar()
        cur = con.cursor()
        subtotal = qtd * preco
        cur.execute(\"\"\"
            INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unit, subtotal)
            VALUES (?, ?, ?, ?, ?)
        \"\"\", (venda_id, produto_id, qtd, preco, subtotal))
        con.commit()
        con.close()
"""

helpers_py = """
def formatar_moeda(valor):
    return f"R$ {valor:.2f}"
"""

login_ui = """
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from models.usuario import Usuario

class TelaLogin(QWidget):
    def __init__(self, abrir_menu):
        super().__init__()
        self.abrir_menu = abrir_menu
        self.setWindowTitle("Login - PDV")

        layout = QVBoxLayout()
        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuário")
        self.senha = QLineEdit()
        self.senha.setPlaceholderText("Senha")
        self.senha.setEchoMode(QLineEdit.Password)

        btn = QPushButton("Entrar")
        btn.clicked.connect(self.fazer_login)

        layout.addWidget(QLabel("Acesso ao Sistema"))
        layout.addWidget(self.usuario)
        layout.addWidget(self.senha)
        layout.addWidget(btn)
        self.setLayout(layout)

    def fazer_login(self):
        try:
            u = Usuario.login(self.usuario.text(), self.senha.text())
            if u:
                self.abrir_menu()
                self.close()
            else:
                print("Login inválido!")
        except Exception as e:
            print("ERRO AO LOGAR:", e)
"""

venda_ui = """
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget
from models.produto import Produto
from models.venda import Venda
from utils.helpers import formatar_moeda

class TelaVenda(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venda - PDV")
        self.total = 0
        self.itens = []

        layout = QVBoxLayout()
        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código de barras")
        self.codigo.returnPressed.connect(self.adicionar_item)
        self.lista = QListWidget()
        btn_finalizar = QPushButton("Finalizar Venda")
        btn_finalizar.clicked.connect(self.finalizar_venda)
        self.lbl_total = QLabel("Total: R$ 0,00")

        layout.addWidget(self.codigo)
        layout.addWidget(self.lista)
        layout.addWidget(self.lbl_total)
        layout.addWidget(btn_finalizar)
        self.setLayout(layout)

    def adicionar_item(self):
        cod = self.codigo.text()
        p = Produto.buscar_por_codigo(cod)
        if not p:
            return
        _, _, nome, preco, estoque = p
        self.itens.append((p[0], nome, preco))
        self.lista.addItem(f"{nome} - {formatar_moeda(preco)}")
        self.total += preco
        self.lbl_total.setText(f"Total: {formatar_moeda(self.total)}")
        self.codigo.clear()

    def finalizar_venda(self):
        vid = Venda.criar_venda(self.total, "Dinheiro")
        for produto_id, nome, preco in self.itens:
            Venda.adicionar_item(vid, produto_id, 1, preco)
        self.lista.addItem("VENDA FINALIZADA!")
"""

cadastro_ui = """
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from models.produto import Produto

class TelaCadastro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Produto")
        layout = QVBoxLayout()
        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código de barras")
        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome do produto")
        self.preco = QLineEdit()
        self.preco.setPlaceholderText("Preço")
        self.estoque = QLineEdit()
        self.estoque.setPlaceholderText("Estoque")
        btn = QPushButton("Cadastrar")
        btn.clicked.connect(self.cadastrar)
        layout.addWidget(self.codigo)
        layout.addWidget(self.nome)
        layout.addWidget(self.preco)
        layout.addWidget(self.estoque)
        layout.addWidget(btn)
        self.setLayout(layout)

    def cadastrar(self):
        Produto.cadastrar(
            self.codigo.text(),
            self.nome.text(),
            float(self.preco.text()),
            float(self.estoque.text())
        )
        print("Produto cadastrado!")
"""

estoque_ui = """
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget
from models.produto import Produto

class TelaEstoque(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estoque")
        layout = QVBoxLayout()
        self.lista = QListWidget()
        for p in Produto.listar():
            self.lista.addItem(f"{p[2]} — Estoque: {p[4]}")
        layout.addWidget(self.lista)
        self.setLayout(layout)
"""

relatorios_ui = """
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class TelaRelatorios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relatórios")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Relatórios ainda serão implementados."))
        self.setLayout(layout)
"""

main_py = """
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from ui.login import TelaLogin
from ui.venda import TelaVenda
from ui.cadastro import TelaCadastro
from ui.estoque import TelaEstoque
from ui.relatorios import TelaRelatorios
from database.db import inicializar_banco
import sys

class MenuPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu PDV")
        layout = QVBoxLayout()
        btn_venda = QPushButton("Vendas")
        btn_venda.clicked.connect(self.abrir_vendas)
        btn_cadastro = QPushButton("Cadastro de Produtos")
        btn_cadastro.clicked.connect(self.abrir_cadastro)
        btn_estoque = QPushButton("Estoque")
        btn_estoque.clicked.connect(self.abrir_estoque)
        btn_relatorios = QPushButton("Relatórios")
        btn_relatorios.clicked.connect(self.abrir_relatorios)
        layout.addWidget(btn_venda)
        layout.addWidget(btn_cadastro)
        layout.addWidget(btn_estoque)
        layout.addWidget(btn_relatorios)
        self.setLayout(layout)

    def abrir_vendas(self):
        self.tela = TelaVenda()
        self.tela.show()
    def abrir_cadastro(self):
        self.tela = TelaCadastro()
        self.tela.show()
    def abrir_estoque(self):
        self.tela = TelaEstoque()
        self.tela.show()
    def abrir_relatorios(self):
        self.tela = TelaRelatorios()
        self.tela.show()

if __name__ == "__main__":
    try:
        inicializar_banco()
        app = QApplication(sys.argv)
        def abrir_menu():
            menu = MenuPrincipal()
            menu.show()
        login = TelaLogin(abrir_menu)
        login.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("ERRO NO APP:", e)
"""

# ------------------------------
# Criar todos os arquivos
# ------------------------------

arquivos = {
    "pdv/database/db.py": db_py,
    "pdv/models/usuario.py": usuario_py,
    "pdv/models/produto.py": produto_py,
    "pdv/models/venda.py": venda_py,
    "pdv/utils/helpers.py": helpers_py,
    "pdv/ui/login.py": login_ui,
    "pdv/ui/venda.py": venda_ui,
    "pdv/ui/cadastro.py": cadastro_ui,
    "pdv/ui/estoque.py": estoque_ui,
    "pdv/ui/relatorios.py": relatorios_ui,
    "pdv/main.py": main_py
}

for caminho, conteudo in arquivos.items():
    criar_arquivo(caminho, conteudo)

print("\n🎉 PDV FINAL CRIADO COM SUCESSO!")
print("➡ Rode: python pdv\\main.py")
print("Login padrão: admin / 1234")
