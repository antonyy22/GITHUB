import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QGroupBox, QGridLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QPixmap, QColor
from PyQt5.QtCore import Qt

class PDV(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YZIDRO - PDV")
        self.setGeometry(200, 100, 900, 600)
        self.setStyleSheet("background-color: #1b365d; color: white;")
        self.produtos = []
        self.total_recebido = 0.0

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Top logo + title area
        top_layout = QHBoxLayout()
        logo = QLabel()
        logo.setFixedSize(150, 50)
        # Coloque aqui o caminho para seu logo se quiser
        # Exemplo: pix = QPixmap("logo.png")
        # logo.setPixmap(pix.scaled(150, 50, Qt.KeepAspectRatio))
        logo.setStyleSheet("background-color: white; border-radius: 5px;")
        top_layout.addWidget(logo)

        title = QLabel("CAIXA ABERTO")
        title.setFont(QFont("Arial", 22, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(title, stretch=1)

        main_layout.addLayout(top_layout)

        # Main area com painel esquerdo e direito
        middle_layout = QHBoxLayout()

        # Painel esquerdo: código + imagem + subtotal e valores
        left_panel = QVBoxLayout()

        # Campo código de barras
        self.input_codigo = QLineEdit()
        self.input_codigo.setPlaceholderText("Digite ou escaneie o código de barras")
        self.input_codigo.setFont(QFont("Arial", 14))
        self.input_codigo.returnPressed.connect(self.adicionar_produto)

        left_panel.addWidget(self.input_codigo)

        # Imagem carrinho (placeholder)
        img_carrinho = QLabel()
        img_carrinho.setFixedSize(150, 150)
        img_carrinho.setStyleSheet("background-color: white; border-radius: 10px;")
        left_panel.addWidget(img_carrinho, alignment=Qt.AlignCenter)

        # Valores do caixa
        self.lbl_subtotal = QLabel("SUBTOTAL: R$ 0,00")
        self.lbl_subtotal.setFont(QFont("Arial", 16, QFont.Bold))
        self.lbl_total_recebido = QLabel("TOTAL RECEBIDO: R$ 0,00")
        self.lbl_total_recebido.setFont(QFont("Arial", 16))
        self.lbl_troco = QLabel("TROCO: R$ 0,00")
        self.lbl_troco.setFont(QFont("Arial", 16))

        left_panel.addWidget(self.lbl_subtotal)
        left_panel.addWidget(self.lbl_total_recebido)
        left_panel.addWidget(self.lbl_troco)

        # Botões
        btn_abrir_caixa = QPushButton("Abrir Caixa")
        btn_abrir_caixa.setStyleSheet("background-color: #007bff; font-size: 16px; padding: 10px;")
        btn_abrir_caixa.clicked.connect(self.abrir_caixa)

        btn_finalizar = QPushButton("Finalizar Venda")
        btn_finalizar.setStyleSheet("background-color: #28a745; font-size: 16px; padding: 10px;")
        btn_finalizar.clicked.connect(self.finalizar_venda)

        left_panel.addWidget(btn_abrir_caixa)
        left_panel.addWidget(btn_finalizar)

        middle_layout.addLayout(left_panel, stretch=1)

        # Painel direito: tabela de produtos
        self.tabela = QTableWidget(0, 5)
        self.tabela.setHorizontalHeaderLabels(["Código", "Descrição", "Qtde", "Preço Unit.", "Total"])
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.setStyleSheet("background-color: white; color: black;")
        self.tabela.setSelectionBehavior(self.tabela.SelectRows)

        middle_layout.addWidget(self.tabela, stretch=2)

        main_layout.addLayout(middle_layout)

        self.setLayout(main_layout)

    def abrir_caixa(self):
        QMessageBox.information(self, "Caixa", "Caixa aberto com sucesso!")
        self.total_recebido = 0.0
        self.atualizar_valores()

    def adicionar_produto(self):
        codigo = self.input_codigo.text().strip()
        if not codigo:
            return

        # Simulação de busca produto - substitua por consulta ao banco ou lista real
        produtos_fake = {
            "123": ("Arroz 5kg", 15.90),
            "456": ("Feijão 1kg", 7.50),
            "789": ("Açúcar 2kg", 4.20),
            "101": ("Óleo de soja", 6.30),
        }

        if codigo in produtos_fake:
            nome, preco = produtos_fake[codigo]
            quantidade = 1
            self.produtos.append((codigo, nome, quantidade, preco))
            self.atualizar_tabela()
            self.input_codigo.clear()
        else:
            QMessageBox.warning(self, "Produto não encontrado", f"Código {codigo} não localizado.")

    def atualizar_tabela(self):
        self.tabela.setRowCount(len(self.produtos))
        subtotal = 0.0
        for row, (codigo, nome, qtd, preco) in enumerate(self.produtos):
            total = qtd * preco
            subtotal += total
            self.tabela.setItem(row, 0, QTableWidgetItem(codigo))
            self.tabela.setItem(row, 1, QTableWidgetItem(nome))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(qtd)))
            self.tabela.setItem(row, 3, QTableWidgetItem(f"R$ {preco:.2f}"))
            self.tabela.setItem(row, 4, QTableWidgetItem(f"R$ {total:.2f}"))

        self.lbl_subtotal.setText(f"SUBTOTAL: R$ {subtotal:.2f}")

        # Atualizar troco e total recebido - para simplificar, troco = total recebido - subtotal
        troco = self.total_recebido - subtotal
        self.lbl_total_recebido.setText(f"TOTAL RECEBIDO: R$ {self.total_recebido:.2f}")
        self.lbl_troco.setText(f"TROCO: R$ {troco:.2f}")

    def finalizar_venda(self):
        if not self.produtos:
            QMessageBox.warning(self, "Aviso", "Nenhum produto na venda.")
            return
        subtotal = sum(qtd * preco for _, _, qtd, preco in self.produtos)
        # Para simular pagamento, perguntar valor recebido
        valor, ok = QInputDialog.getDouble(self, "Pagamento", "Valor recebido:", decimals=2)
        if ok:
            self.total_recebido = valor
            if valor < subtotal:
                QMessageBox.warning(self, "Pagamento", "Valor recebido é menor que o subtotal.")
                return
            self.atualizar_tabela()
            QMessageBox.information(self, "Venda", "Venda finalizada com sucesso!")
            self.produtos.clear()
            self.atualizar_tabela()
        else:
            QMessageBox.information(self, "Venda", "Venda cancelada.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = PDV()
    janela.show()
    sys.exit(app.exec_())
