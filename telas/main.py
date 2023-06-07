import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import sys


from tela_login import Tela_Login
from tela_cadastro import Tela_Cadastro
from operacoes import Operacoes
from pessoa import Pessoa


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 480) 

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Login()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)


class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.tela_inicial.button_login.clicked.connect(self.verificar_login)
        self.tela_inicial.button_register.clicked.connect(self.abrir_tela_cadastro)
        self.tela_inicial.pushButton.clicked.connect(self.close)

        self.tela_cadastro.botao_cadastrar.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar_tela)


    def verificar_login(self):
        username_login = self.tela_inicial.txt_user.text()
        password_login = self.tela_inicial.txt_password.text()
        self.login = Operacoes()
        self.login.verificar_login(username_login, password_login)
        if self.login:
            QMessageBox.information(
                self, 'Login', 'Login realizado com sucesso!')
 
    def botaoCadastrar(self):
        nome = self.tela_cadastro.txt_nome.text()
        email = self.tela_cadastro.txt_email.text()
        endereco = self.tela_cadastro.txt_endereco.text()
        nascimento = self.tela_cadastro.txt_nascimento.text()
        usuario = self.tela_cadastro.txt_usuario.text()
        senha = self.tela_cadastro.txt_senha.text()
        senha_confirmacao = self.tela_cadastro.txt_senhaconf.text()
        plano_assinatura = self.tela_cadastro.planos_assinatura.currentIndex()
        self.p = Pessoa(nome, email, endereco, nascimento, usuario, senha, senha_confirmacao, plano_assinatura)
        self.cadastro = Operacoes()
        self.cadastro.cadastramento(self.p)
        if self.cadastro:
            QMessageBox.information(
                self, 'Cadastro', 'Cadastro realizado com sucesso!')
        else:
            QMessageBox.information(
                self, 'Cadastro', 'Cadastro não realizado!')


    def voltar_tela(self):
        self.QtStack.setCurrentIndex(0)
    def abrir_tela_cadastro(self):
        self.QtStack.setCurrentIndex(1)
    def close (self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())