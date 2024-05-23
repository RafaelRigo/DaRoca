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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        if not janelaPrincipal.objectName():
            janelaPrincipal.setObjectName(u"janelaPrincipal")
        janelaPrincipal.resize(291, 285)
        self.centralwidget = QWidget(janelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 248, 158))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.nomeProduto = QLineEdit(self.widget)
        self.nomeProduto.setObjectName(u"nomeProduto")

        self.gridLayout.addWidget(self.nomeProduto, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.categoriaProduto = QComboBox(self.widget)
        self.categoriaProduto.addItem("")
        self.categoriaProduto.addItem("")
        self.categoriaProduto.addItem("")
        self.categoriaProduto.setObjectName(u"categoriaProduto")

        self.gridLayout.addWidget(self.categoriaProduto, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.precoProduto = QDoubleSpinBox(self.widget)
        self.precoProduto.setObjectName(u"precoProduto")

        self.gridLayout.addWidget(self.precoProduto, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.quantidadeProduto = QLineEdit(self.widget)
        self.quantidadeProduto.setObjectName(u"quantidadeProduto")

        self.gridLayout.addWidget(self.quantidadeProduto, 3, 1, 1, 1)

        self.selecionarImagem = QPushButton(self.widget)
        self.selecionarImagem.setObjectName(u"selecionarImagem")

        self.gridLayout.addWidget(self.selecionarImagem, 4, 1, 1, 1)

        self.registrarProduto = QPushButton(self.widget)
        self.registrarProduto.setObjectName(u"registrarProduto")

        self.gridLayout.addWidget(self.registrarProduto, 5, 0, 1, 2)

        janelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(janelaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 291, 21))
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
        self.label_2.setText(QCoreApplication.translate("janelaPrincipal", u"Categoria do produto:", None))
        self.categoriaProduto.setItemText(0, QCoreApplication.translate("janelaPrincipal", u"fruta", None))
        self.categoriaProduto.setItemText(1, QCoreApplication.translate("janelaPrincipal", u"legume", None))
        self.categoriaProduto.setItemText(2, QCoreApplication.translate("janelaPrincipal", u"verdura", None))

        self.label_3.setText(QCoreApplication.translate("janelaPrincipal", u"Pre\u00e7o:", None))
        self.label_4.setText(QCoreApplication.translate("janelaPrincipal", u"Quantidade:", None))
        self.selecionarImagem.setText(QCoreApplication.translate("janelaPrincipal", u"selecionar imagem", None))
        self.registrarProduto.setText(QCoreApplication.translate("janelaPrincipal", u"Registrar produto", None))
    # retranslateUi

