import sys, os
import json
from PySide6.QtCore import Qt, QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QDialog
from registro_produtos_ui import Ui_janelaPrincipal
from tkinter import filedialog
import pyodbc as bd

global conexao, cursor

class FormPrincipal(QMainWindow, Ui_janelaPrincipal):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.show()
        self.situacao = "navegando"

        self.registrarProduto.clicked.connect(self.registrar_produto)
        self.selecionarImagem.clicked.connect(self.selecionar_imagem)

    def selecionar_imagem(self):
        global imagem
        tipos_de_arq = ( ('Arquivos jpg', '*.jpg'),
                         ('Arquivos webp', '*.webp'),
                         ('Arquivos png', '*.png'),
                         ('Arquivos gif', '*.gif'),
                         ('Arquivos jfif', '*.jfif'),
                         ('Qualquer arquivo', '*.*') )
        nome_arq = filedialog.askopenfilename(
            title='Selecione a imagem',
            initialdir=r'Z:\1º ano - Cotuca\Pratica Profissional\DaRoça\DaRoca\imagens',
            filetypes=tipos_de_arq
        )
        
        dir_list = nome_arq.split("/")
        caminho = f"../../{dir_list[-2]}/{dir_list[-1]}"
        
        imagem = f"'{caminho}'"

    def registrar_produto(self):
        nome = f"'{self.nomeProduto.text()}'"
        categoria = f"'{self.categoriaProduto.currentText()}'"
        preco = f"'{self.precoProduto.value()}'"
        quantidade = f"'{self.quantidadeProduto.text()}'"

        if nome == "" or categoria == "" or preco == 0 or quantidade == "":
            self.statusBar.showMessage("Preencha todos os campos", 5000)
            return

        comando = f"INSERT INTO daroca.produtos (nome, categoria, valor, descricao, imagem) VALUES ({nome}, {categoria}, {preco}, {quantidade}, {imagem})"

        try:
            cursor.execute(comando)
            conexao.commit()
            self.statusBar.showMessage("Produto registrado com sucesso", 5000)
        except Exception as e:
            if hasattr(e, 'message'):
                mensagem = e.message
            else:
                mensagem = e.args[1]
            self.statusBar.showMessage(mensagem)

application = QApplication(sys.argv)
try:
    conexao = bd.connect(driver="SQL Server",
                        server="regulus.cotuca.unicamp.br",
                        database="BD24159",
                        uid="BD24159",
                        pwd="BD24159")
    print("Conexão bem sucedida!")
    cursor = conexao.cursor()  # cursor: objeto de acesso ao BD
    janela = FormPrincipal()
    application.exec()
except:
    print("Não foi possível conectar ao banco de dados")
