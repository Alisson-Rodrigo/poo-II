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
from tela_inicial import Tela_Inicial
from tela_cadastro import Tela_Cadastro
from operacoes import Operacoes
from pessoa import Pessoa


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(600, 400) 

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Login()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_primaria = Tela_Inicial()
        self.tela_primaria.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)


class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.tela_inicial.button_login.clicked.connect(self.verificacao_login)
        self.tela_inicial.button_register.clicked.connect(self.abrir_tela_cadastro)
        self.tela_inicial.pushButton.clicked.connect(self.close)

        self.tela_cadastro.botao_cadastrar.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar_tela)

        self.tela_primaria.pushButton.clicked.connect(self.voltar_tela)
        self.tela_primaria.pushButton_2.clicked.connect(self.close)


    def verificacao_login(self):
        username_login = self.tela_inicial.txt_user.text()
        password_login = self.tela_inicial.txt_password.text()
        self.login = Operacoes()
        resultado = self.login.verificar_login(username_login, password_login)
        if username_login == "" or password_login == "":
            QMessageBox.information(self, 'Erro', 'Preencha todos os campos!')
        elif resultado == False:
            QMessageBox.information(self, 'Erro', 'Usuário ou senha incorretos!')
        elif resultado == True:
            QMessageBox.information(
                self, 'Login', 'Login realizado com sucesso!')
            self.tela_inicial.txt_user.clear()
            self.tela_inicial.txt_password.clear()
            self.QtStack.setCurrentIndex(2)
    def botaoCadastrar(self):
        nome = self.tela_cadastro.txt_nome.text()
        email = self.tela_cadastro.txt_email.text()
        endereco = self.tela_cadastro.txt_endereco.text()
        nascimento = self.tela_cadastro.txt_nascimento.text()
        usuario = self.tela_cadastro.txt_usuario.text()
        senha = self.tela_cadastro.txt_senha.text()
        senha_confirmacao = self.tela_cadastro.txt_senhaconf.text()
        plano_assinatura = self.tela_cadastro.planos_assinatura.currentIndex()
        if nome == "" or email == "" or endereco == "" or nascimento == "" or usuario == "" or senha == "" or senha_confirmacao == "" or plano_assinatura == 0:
            QMessageBox.information(self, 'Erro', 'Preencha todos os campos!')
        elif senha != senha_confirmacao:
            QMessageBox.information(self, 'Erro', 'Senhas não coincidem!')
        else:
            self.p = Pessoa(nome, email, endereco, nascimento, usuario, senha, senha_confirmacao, plano_assinatura)
            self.cadastro = Operacoes()
            operacao = self.cadastro.cadastramento(self.p)
            if operacao:
                QMessageBox.information(
                    self, 'Cadastro', 'Cadastro realizado com sucesso!')
                self.tela_cadastro.txt_nome.clear()
                self.tela_cadastro.txt_email.clear()
                self.tela_cadastro.txt_endereco.clear()
                self.tela_cadastro.txt_nascimento.clear()
                self.tela_cadastro.txt_usuario.clear()
                self.tela_cadastro.txt_senha.clear()
                self.tela_cadastro.txt_senhaconf.clear()
                
            else:
                QMessageBox.information(
                    self, 'Cadastro', 'Usuario já existente!')

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