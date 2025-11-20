
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
