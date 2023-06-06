import sys
import os
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication


from tela_inicial import Tela_Inicial
from tela_cadastro import Tela_Cadastro
from tela_buscar import Tela_buscar
from pessoa import Pessoa
from cadastro import Cadastro

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_buscar = Tela_buscar()
        self.tela_buscar.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.cadastro = Cadastro()
        self.tela_inicial.pushButton.clicked.connect(self.abrir_tela_cadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrir_tela_buscar)
        self.tela_inicial.pushButton_3.clicked.connect(self.close)

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar_tela)

        self.tela_buscar.pushButton.clicked.connect(self.botaoBuscar)
        self.tela_buscar.pushButton_2.clicked.connect(self.voltar_tela)

        self.tela_inicial.pushButton_3.clicked.connect(self.close)
    
    def botaoCadastrar (self):
        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()

        if not nome or not endereco or not cpf or not nascimento == '':
            p = Pessoa(nome,endereco,cpf,nascimento)
            if (self.cadastro.add_pessoa(p)):
                QMessageBox.information(None,'POOII','Cadastro realizado com sucesso')
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,'POOII','Cadastro não realizado')
        else:
            QMessageBox.information(None,'POOII','Preencha todos os campos')
        self.QtStack.setCurrentIndex(0)
    def botaoBuscar(self):
        cpf = self.tela_buscar.lineEdit.text()
        pessoa = self.cadastro.busca(cpf)
        if (pessoa!=None):
            self.tela_buscar.lineEdit_2.setText(pessoa.nome)
            self.tela_buscar.lineEdit_3.setText(pessoa.endereco)
            self.tela_buscar.lineEdit_4.setText(pessoa.cpf)
        else:
            QMessageBox.information(None,'POOII','Pessoa não encontrada')
    def abrir_tela_cadastro(self):
        self.QtStack.setCurrentIndex(1)
    def abrir_tela_buscar(self):
        self.QtStack.setCurrentIndex(2)
    def voltar_tela(self):
        self.QtStack.setCurrentIndex(0)
    def close (self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())


