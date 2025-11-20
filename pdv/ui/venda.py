
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
