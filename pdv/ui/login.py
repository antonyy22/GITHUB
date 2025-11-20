
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
