import sys
import socket
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from cod_tela_principal import Ui_TelaPrincipal
from cod_tela_login import Ui_Login
from cod_tela_cadastro import Ui_Cadastro
# from backend.sistema import SistemaEducacional, Professor, Aluno


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(500, 450)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Login()
        self.tela_login.setupUi(self.stack0)
        self.tela_cadastro = Ui_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        self.tela_principal = Ui_TelaPrincipal()
        self.tela_principal.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        '''Modificadores'''
        # self.sistema = SistemaEducacional()
        ip = 'localhost'
        port = 5000
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)
        self.tela_login.botao_login.clicked.connect(self.botao_login)
        self.tela_login.botao_cadastro.clicked.connect(self.botao_cadastrar)
        self.tela_cadastro.alunos_botao_voltar.clicked.connect(self.botao_voltar_cadastro)
        self.tela_cadastro.professores_botao_voltar.clicked.connect(self.botao_voltar_cadastro)
        self.tela_cadastro.alunos_botao_cadastrar.clicked.connect(self.botao_cadastrar_aluno)
        self.tela_cadastro.professores_botao_cadastrar.clicked.connect(self.botao_cadastrar_professor)
        self.tela_principal.botao_logoff.clicked.connect(self.botao_logoff)
        self.tela_principal.botao_sair.clicked.connect(self.botao_sair)

    def enviar_cadastro(self, mensagem):
        if mensagem.split(',')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta == '1':
                return True
        return False
    
    def enviar_login(self, mensagem):
        if mensagem.split(',')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta == '1':
                return True
        return False

    def botao_login(self):
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        mensagem = f'1,{email},{senha}'

        if email and senha:
            if self.enviar_login(mensagem):
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, "Erro", "E-mail ou senha incorretos")
        else:
            QMessageBox.about(self, "Erro", "E-mail ou senha não preenchidos")

    def botao_logoff(self):
        mensagem = '0'
        self.client_socket.send(mensagem.encode())
        self.QtStack.setCurrentIndex(0)
    
    def botao_sair(self):
        mensagem = '-1'
        self.client_socket.send(mensagem.encode())
        self.client_socket.close()
        exit()
        
    def botao_cadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def botao_voltar_cadastro(self):
        self.QtStack.setCurrentIndex(0)

    def botao_cadastrar_aluno(self):
        email = self.tela_cadastro.alunos_caixa_email.text()
        senha1 = self.tela_cadastro.alunos_caixa_senha1.text()
        senha2 = self.tela_cadastro.alunos_caixa_senha2.text()
        nome = self.tela_cadastro.alunos_caixa_nome.text()
        sobrenome = self.tela_cadastro.alunos_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.alunos_caixa_nascimento.text()
        mensagem = f'2,{email},{senha1},{nome},{sobrenome},{nascimento},a'
        if email and senha1 and senha2 and nome and sobrenome and nascimento:
            if senha1 == senha2:
                if self.enviar_cadastro(mensagem):
                    QMessageBox.about(self, "Sucesso", "Aluno cadastrado com sucesso")
                    self.limpar_campos()
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.about(self, "Erro", "E-mail de usuário já cadastrado")
            else:
                QMessageBox.about(self, "Erro", "Senhas não coincidem")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")
    
    def botao_cadastrar_professor(self):
        email = self.tela_cadastro.professores_caixa_email.text()
        senha1 = self.tela_cadastro.professores_caixa_senha1.text()
        senha2 = self.tela_cadastro.professores_caixa_senha2.text()
        nome = self.tela_cadastro.professores_caixa_nome.text()
        sobrenome = self.tela_cadastro.professores_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.professores_caixa_nascimento.text()
        mensagem = f'2,{email},{senha1},{nome},{sobrenome},{nascimento},p'
        if email and senha1 and senha2 and nome and sobrenome and nascimento:
            if senha1 == senha2:
                if self.enviar_cadastro(mensagem):
                    QMessageBox.about(self, "Sucesso", "Professor cadastrado com sucesso")
                    self.limpar_campos()
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.about(self, "Erro", "E-mail de usuário já cadastrado")
            else:
                QMessageBox.about(self, "Erro", "Senhas não coincidem")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")
    
    def limpar_campos(self):
        self.tela_cadastro.alunos_caixa_email.clear()
        self.tela_cadastro.alunos_caixa_senha1.clear()
        self.tela_cadastro.alunos_caixa_senha2.clear()
        self.tela_cadastro.alunos_caixa_nome.clear()
        self.tela_cadastro.alunos_caixa_sobrenome.clear()
        self.tela_cadastro.alunos_caixa_nascimento.setDate(QtCore.QDate(2000, 1, 1))
        self.tela_cadastro.professores_caixa_email.clear()
        self.tela_cadastro.professores_caixa_senha1.clear()
        self.tela_cadastro.professores_caixa_senha2.clear()
        self.tela_cadastro.professores_caixa_nome.clear()
        self.tela_cadastro.professores_caixa_sobrenome.clear()
        self.tela_cadastro.professores_caixa_nascimento.setDate(QtCore.QDate(2000, 1, 1))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    sys.exit(app.exec_())