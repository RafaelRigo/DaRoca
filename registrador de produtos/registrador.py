import sys
from PySide6.QtCore import Qt, QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QDialog
from registro_produtos_ui import Ui_janelaPrincipal

class FormPrincipal(QMainWindow, Ui_janelaPrincipal):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.show()
        self.situacao = "navegando"
        self.registrarProduto.clicked.connect(self.registrar_produto)

    def registrar_produto():
        pass