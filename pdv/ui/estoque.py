
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
