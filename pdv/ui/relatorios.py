
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class TelaRelatorios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relatórios")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Relatórios ainda serão implementados."))
        self.setLayout(layout)
