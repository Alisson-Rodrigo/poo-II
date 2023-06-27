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
from tela_categoria import Tela_Categoria
from tela_favoritos import Tela_Favoritos
from tela_menu import Tela_Menu


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(600, 400) 

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()


        self.tela_inicial = Tela_Login()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_primaria = Tela_Inicial()
        self.tela_primaria.setupUi(self.stack2)

        self.tela_categoria = Tela_Categoria()
        self.tela_categoria.setupUi(self.stack3)

        self.tela_favoritos = Tela_Favoritos()
        self.tela_favoritos.setupUi(self.stack4)

        self.tela_menu = Tela_Menu()
        self.tela_menu.setupUi(self.stack5)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)


class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        ip = 'localhost'
        port = 8901
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)

        self.tela_inicial.button_login.clicked.connect(self.verificacao_login)
        self.tela_inicial.button_register.clicked.connect(self.abrir_tela_cadastro)
        self.tela_inicial.pushButton.clicked.connect(self.close)

        self.tela_cadastro.botao_cadastrar.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar_tela)

        self.tela_primaria.pushButton_4.clicked.connect(self.abrir_tela_categoria)
        self.tela_primaria.pushButton_3.clicked.connect(self.abrir_tela_favoritos)
        self.tela_primaria.pushButton_2.clicked.connect(self.abrir_menu)

        self.tela_categoria.pushButton_2.clicked.connect(self.abrir_menu)
        self.tela_categoria.pushButton_3.clicked.connect(self.abrir_tela_favoritos)
        self.tela_categoria.pushButton_34.clicked.connect(self.voltar_tela2)

        self.tela_categoria.pushButton.clicked.connect(self.showAcao)
        self.tela_categoria.pushButton_5.clicked.connect(self.showComedia)
        self.tela_categoria.pushButton_6.clicked.connect(self.showDrama)
        self.tela_categoria.pushButton_7.clicked.connect(self.showTerror)
        self.tela_categoria.pushButton_8.clicked.connect(self.showInfantil)
        self.tela_categoria.pushButton_9.clicked.connect(self.showAnime)

        self.tela_favoritos.pushButton_2.clicked.connect(self.abrir_menu)
        self.tela_favoritos.pushButton_4.clicked.connect(self.abrir_tela_categoria)
        self.tela_favoritos.pushButton_34.clicked.connect(self.voltar_tela2)

        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page)

        self.tela_menu.pushButton_2.clicked.connect(self.showPerfil)
        self.tela_menu.pushButton_3.clicked.connect(self.showSobre)
        self.tela_menu.pushButton_4.clicked.connect(self.voltar_tela2)

    
    def operacao_log(self, mensagem):
        if mensagem.split(',')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta and resposta == '1':
                return True
        return False


    def verificacao_login(self):
        self.username_login = self.tela_inicial.txt_user.text()
        password_login = self.tela_inicial.txt_password.text()
        mensagem = f'1,{self.username_login},{password_login}'

        if self.username_login and password_login:
            if self.operacao_log(mensagem):
                QMessageBox.about(self, "Sucesso", f"Login realizado com sucesso")
                self.QtStack.setCurrentIndex(2)
                
            else:
                QMessageBox.about(self, "Erro", "Usuário ou senha incorretos")
        else: 
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def exibir_dados(self):
        msg = f'3,{self.username_login}'
        self.client_socket.send(msg.encode())
        self.resposta2 = self.client_socket.recv(1024).decode().split(',')
        print (self.resposta2)
        return self.resposta2
    
    def enviar_cadastro(self, mensagem):
        if mensagem.split(',')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            #dados_usu = self.client_socket.recv(1024).decode()
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
        mensagem = f'2,{nome},{email},{endereco},{nascimento},{usuario},{senha},{senha_confirmacao}'
        if nome and email and endereco and nascimento and usuario and senha and senha_confirmacao:
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
    def voltar_tela2(self):
        self.QtStack.setCurrentIndex(2)
    def abrir_tela_cadastro(self):
        self.QtStack.setCurrentIndex(1)
    def abrir_tela_categoria(self):
        self.QtStack.setCurrentIndex(3)
        self.showInicial()
    def abrir_tela_favoritos(self):
        self.QtStack.setCurrentIndex(4)
    def abrir_menu(self):
        self.QtStack.setCurrentIndex(5)

    def showInicial(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_1)
        self.tela_categoria.lineEdit.setText(f'ESCOLHA UMA CATEGORIA, {self.exibir_dados()[5]}')
    def showAcao(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page1_2)
    def showComedia(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_3)
    def showDrama(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page)
    def showTerror(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_2)
    def showInfantil(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_4)
    def showAnime(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_5)

    def showPerfil(self):
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_2)
    def showSobre(self):
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_3)
    
    def close (self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    show_main = Main()
    sys.exit(app.exec_())