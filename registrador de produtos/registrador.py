import sys, os
import json
from PySide6.QtCore import Qt, QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QDialog
from registro_produtos_ui import Ui_janelaPrincipal
from tkinter import filedialog

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
        
        imagem = caminho

    def registrar_produto(self):
        with open("codigo/produtos/produtos.json", encoding='utf-8') as f:
            json_produtos = json.load(f)
        
        maior_id = 0
        for produto in json_produtos:
            if int(produto["id"]) > maior_id:
                maior_id = produto["id"]
        
        id = maior_id + 1
        nome = self.nomeProduto.text()
        categoria = self.categoriaProduto.currentText()
        preco = self.precoProduto.value()
        quantidade = self.quantidadeProduto.text()

        obj = {
            "id": id,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade,
            "imagem": imagem
        }

        json_produtos.append(obj)
        json_produtos = json.dumps( json_produtos, indent=4)

        with open("codigo/produtos/produtos.json", "w", encoding='utf-8') as f:
            f.write(json_produtos)

application = QApplication(sys.argv)
janela = FormPrincipal()
application.exec()