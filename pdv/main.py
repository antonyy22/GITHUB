
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
