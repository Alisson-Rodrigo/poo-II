import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import sys
import socket


from tela_login import Tela_Login
from tela_inicial import Tela_Inicial
from tela_cadastro import Tela_Cadastro

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

        ip = 'localhost'
        port = 8900
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)

        self.tela_inicial.button_login.clicked.connect(self.verificacao_login)
        self.tela_inicial.button_register.clicked.connect(self.abrir_tela_cadastro)
        self.tela_inicial.pushButton.clicked.connect(self.close)

        self.tela_cadastro.botao_cadastrar.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar_tela)

        self.tela_primaria.pushButton.clicked.connect(self.voltar_tela)
        self.tela_primaria.pushButton_2.clicked.connect(self.close)

    
    def operacao_log(self, mensagem):
        if mensagem.split(',')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta and resposta == '1':
                return True
        return False

    def verificacao_login(self):
        username_login = self.tela_inicial.txt_user.text()
        password_login = self.tela_inicial.txt_password.text()
        mensagem = f'1,{username_login},{password_login}'
        if username_login and password_login:
            if self.operacao_log(mensagem):
                QMessageBox.about(self, "Sucesso", "Login realizado com sucesso")
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, "Erro", "E-mail ou senha incorretos")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")


    def enviar_cadastro(self, mensagem):
        if mensagem.split(',')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta and resposta == '1':
                return True
        return False

    def botaoCadastrar(self):
        nome = self.tela_cadastro.txt_nome.text()
        email = self.tela_cadastro.txt_email.text()
        endereco = self.tela_cadastro.txt_endereco.text()
        nascimento = self.tela_cadastro.txt_nascimento.text()
        usuario = self.tela_cadastro.txt_usuario.text()
        senha = self.tela_cadastro.txt_senha.text()
        senha_confirmacao = self.tela_cadastro.txt_senhaconf.text()
        plano_assinatura = self.tela_cadastro.planos_assinatura.currentIndex()
        mensagem = f'2,{nome},{email},{endereco},{nascimento},{usuario},{senha},{senha_confirmacao},{plano_assinatura}'
        if nome and email and endereco and nascimento and usuario and senha and senha_confirmacao and plano_assinatura:
            if senha == senha_confirmacao:
                if self.enviar_cadastro(mensagem):
                    QMessageBox.about(self, "Sucesso", "Cadastro realizado com sucesso")
                    self.tela_cadastro.txt_nome.clear()
                    self.tela_cadastro.txt_email.clear()
                    self.tela_cadastro.txt_endereco.clear()
                    self.tela_cadastro.txt_nascimento.clear()
                    self.tela_cadastro.txt_usuario.clear()
                    self.tela_cadastro.txt_senha.clear()
                    self.tela_cadastro.txt_senhaconf.clear()
                else:
                    QMessageBox.about(self, "Erro", "Usuário já cadastrado")
            else:
                QMessageBox.about(self, "Erro", "Senhas não conferem")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

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