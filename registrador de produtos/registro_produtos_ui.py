# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_produtos.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        if not janelaPrincipal.objectName():
            janelaPrincipal.setObjectName(u"janelaPrincipal")
        janelaPrincipal.resize(264, 285)
        self.centralwidget = QWidget(janelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 121, 16))
        self.nomeProduto = QLineEdit(self.centralwidget)
        self.nomeProduto.setObjectName(u"nomeProduto")
        self.nomeProduto.setGeometry(QRect(130, 20, 113, 20))
        self.categoriaProduto = QComboBox(self.centralwidget)
        self.categoriaProduto.addItem("")
        self.categoriaProduto.addItem("")
        self.categoriaProduto.addItem("")
        self.categoriaProduto.setObjectName(u"categoriaProduto")
        self.categoriaProduto.setGeometry(QRect(130, 50, 111, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 121, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 111, 16))
        self.precoProduto = QDoubleSpinBox(self.centralwidget)
        self.precoProduto.setObjectName(u"precoProduto")
        self.precoProduto.setGeometry(QRect(130, 80, 111, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 110, 111, 16))
        self.quantidadeProduto = QLineEdit(self.centralwidget)
        self.quantidadeProduto.setObjectName(u"quantidadeProduto")
        self.quantidadeProduto.setGeometry(QRect(130, 110, 113, 20))
        self.selecionarImagem = QPushButton(self.centralwidget)
        self.selecionarImagem.setObjectName(u"selecionarImagem")
        self.selecionarImagem.setGeometry(QRect(130, 140, 111, 23))
        self.registrarProduto = QPushButton(self.centralwidget)
        self.registrarProduto.setObjectName(u"registrarProduto")
        self.registrarProduto.setGeometry(QRect(70, 180, 101, 41))
        janelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(janelaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 264, 21))
        janelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(janelaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        janelaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(janelaPrincipal)

        QMetaObject.connectSlotsByName(janelaPrincipal)
    # setupUi

    def retranslateUi(self, janelaPrincipal):
        janelaPrincipal.setWindowTitle(QCoreApplication.translate("janelaPrincipal", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("janelaPrincipal", u"Nome do produto:", None))
        self.categoriaProduto.setItemText(0, QCoreApplication.translate("janelaPrincipal", u"fruta", None))
        self.categoriaProduto.setItemText(1, QCoreApplication.translate("janelaPrincipal", u"legume", None))
        self.categoriaProduto.setItemText(2, QCoreApplication.translate("janelaPrincipal", u"verdura", None))

        self.label_2.setText(QCoreApplication.translate("janelaPrincipal", u"Categoria do produto:", None))
        self.label_3.setText(QCoreApplication.translate("janelaPrincipal", u"Pre\u00e7o:", None))
        self.label_4.setText(QCoreApplication.translate("janelaPrincipal", u"Quantidade:", None))
        self.selecionarImagem.setText(QCoreApplication.translate("janelaPrincipal", u"selecionar imagem", None))
        self.registrarProduto.setText(QCoreApplication.translate("janelaPrincipal", u"Registrar produto", None))
    # retranslateUi

