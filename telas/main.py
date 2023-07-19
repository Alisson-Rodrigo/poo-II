import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QPushButton
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtPrintSupport import *

import sys
import socket
import webbrowser
import threading
import time
import ast
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


from tela_login import Tela_Login
from tela_inicial import Tela_Inicial
from tela_cadastro import Tela_Cadastro
from tela_categoria import Tela_Categoria
from tela_favoritos import Tela_Favoritos
from tela_menu import Tela_Menu
from tela_admin import Tela_Admin


class Ui_Main(object):
    '''
    Criando a tela principal, onde será exibido o menu principal, a tela de login e a tela de cadastro, além de todas as outras telas.

    Attribtues
    ------
    QtStack: QStackedLayout
        Layout que permite a troca de telas
    stack0: QMainWindow
        Tela de login
    stack1: QMainWindow
        Tela de cadastro
    stack2: QMainWindow
        Tela principal
    stack3: QMainWindow
        Tela de categorias
    stack4: QMainWindow
        Tela de favoritos
    stack5: QMainWindow
        Tela de menu
    stack6: QMainWindow
        Tela de admin
    
    Methods
    ------
    setupUi(self, Main)
        Define o tamanho da tela principal e adiciona as telas de login, cadastro, principal, categorias, favoritos, menu e admin ao QtStack

    '''

    def setupUi(self, Main):
        '''
        Esse metodo define o tamanho da tela principal e adiciona as telas de login, cadastro, principal, categorias, favoritos, menu e admin ao QtStack

        Attributes
        ------
        Main: QMainWindow
            Tela principal
        '''
        Main.setObjectName("Main")
        Main.resize(600, 400) 

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()


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

        self.tela_admin = Tela_Admin()
        self.tela_admin.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QtWidgets.QMainWindow, Ui_Main):
    '''
    Essa classe é responsável por controlar todas as telas do programa, além de realizar a comunicação com o servidor.

    Attributes
    ------
    client_socket: socket
        Socket que realiza a comunicação com o servidor
    username_login: str
        Nome do usuário que está logado no momento
    resposta2: list
        Lista com os dados do usuário que está logado no momento
    
    Methods
    ------
    operacao_log(self, mensagem)
        Envia uma mensagem para o servidor e recebe uma resposta
    buscar_video(self,caminho)
        Envia uma mensagem para o servidor e recebe um vídeo
    verificacao_login(self)
        Verifica se o usuário e senha digitados estão corretos
    exibir_dados(self)
        Envia uma mensagem para o servidor e recebe os dados do usuário logado
    enviar_cadastro(self, mensagem)
        Envia uma mensagem para o servidor e recebe uma resposta
    botaoCadastrar(self)
        Verifica se os campos do cadastro estão preenchidos corretamente
    pagina_admin (self)
        Abre a página do admin
    visualizar_usuarios(self)
        Envia uma mensagem para o servidor e recebe uma lista com os usuários cadastrados
    tela_deletar_usuario(self)
        Abre a tela de deletar usuário
    deletar_usuario(self)
        Envia uma mensagem para o servidor e recebe uma resposta
    tela_cadastrar_midia(self)
        Abre a tela de cadastrar mídia
    adicionar_midia(self)
        Envia uma mensagem para o servidor e recebe uma resposta
    criar_botao_açao(self, tela, nome_filme, caminho, genero)
        Cria um botão na tela de categorias
    criar_botao_comedia(self, tela, nome_filme, caminho, genero)
        Cria um botão na tela de categorias
    buscar_todos_filmes(self)
        Envia uma mensagem para o servidor e recebe uma lista com todas as mídias cadastradas
    tela_deletar_midia(self)
        Abre a tela de deletar mídia
    botao_deletar_midia(self)
        Envia uma mensagem para o servidor e recebe uma resposta
    voltar_tela(self)
        Volta para a tela inicial
    voltar_tela2(self)
        Volta para a tela principal
    abrir_tela_cadastro(self)   
        Abre a tela de cadastro
    abrir_tela_categoria(self)
        Abre a tela de categorias
    abrir_menu(self)
        Abre a tela de menu
    showInicial(self)
        Abre a tela inicial
    showAcao(self)
        Abre a tela de ação
    showComedia(self)
        Abre a tela de comédia
    showDrama(self)
        Abre a tela de drama
    showTerror(self)    
        Abre a tela de terror
    showInfantil(self) 
        Abre a tela de infantil
    showAnime(self)
        Abre a tela de anime
    showInicial_menu(self)
        Abre a tela inicial do menu
    showPerfil(self)
        Abre a tela de perfil
    showSobre(self)
        Abre a tela de sobre
    showContato(self)
        Abre a tela de contato
    exibir_contato(self)
        Abre o whatsapp
    close (self)
        Fecha o programa
    abrir_tela_midia(self, caminho)
        Abre a tela de vídeo
    
    Exceptions
    ------
    Erro ao abrir o vídeo

    
    '''

    def __init__(self,parent=None):
        '''
        Nesse metodo de inicialização, é criado o socket que realiza a comunicação com o servidor, além de conectar os botões das telas com suas respectivas funções.
        
        Attributes
        ------
        hostname: str
            Nome do host
        ip_Adress: str
            Endereço ip do host
        ip: str
            Endereço ip do host
        port: int
            Porta de comunicação
        addr: tuple
            Tupla com o endereço ip e a porta de comunicação

        Parameters
        ------
        parent: None
            Tela principal

        Methods
        ------
        setupUi(self, Main)

        return
        ------
        None
            
        ''' 
        super(Main,self).__init__(parent)
        self.setupUi(self)
        hostname = socket.gethostname()
        ip_Adress = socket.gethostbyname(hostname)
        ip = ip_Adress
        port = 10012
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)

        self.buscar_todos_filmes()

        self.tela_inicial.button_login.clicked.connect(self.verificacao_login)
        self.tela_inicial.button_register.clicked.connect(self.abrir_tela_cadastro)
        self.tela_inicial.pushButton.clicked.connect(self.close)

        self.tela_cadastro.botao_cadastrar.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar_tela)

        self.tela_primaria.pushButton_4.clicked.connect(self.abrir_tela_categoria)
        self.tela_primaria.pushButton_2.clicked.connect(self.abrir_menu)
        self.tela_primaria.pushButton_10.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video("ShaunOCarneiro-ClipedeEstreia-TVMarcelito2-FaixaInfantil.mp4")))
        self.tela_primaria.pushButton_6.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video("Landscapes_Volume4K(UHD)(1).mp4")))
        self.tela_primaria.pushButton_14.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video("AberturaOShowDeTomeJerryBomDiaeCiaSbt.mp4")))
        self.tela_primaria.pushButton.clicked.connect(self.voltar_tela)

        self.tela_categoria.pushButton_2.clicked.connect(self.abrir_menu)
        self.tela_categoria.pushButton_34.clicked.connect(self.voltar_tela2)

        self.tela_categoria.pushButton.clicked.connect(self.showAcao)
        self.tela_categoria.pushButton_5.clicked.connect(self.showComedia)
        self.tela_categoria.pushButton_6.clicked.connect(self.showDrama)
        self.tela_categoria.pushButton_7.clicked.connect(self.showTerror)
        self.tela_categoria.pushButton_8.clicked.connect(self.showInfantil)
        self.tela_categoria.pushButton_9.clicked.connect(self.showAnime)

        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page)
        self.tela_menu.pushButton_2.clicked.connect(self.showPerfil)
        self.tela_menu.pushButton_3.clicked.connect(self.showSobre)
        self.tela_menu.pushButton_5.clicked.connect(self.showContato)
        self.tela_menu.pushButton_4.clicked.connect(self.voltar_tela2)

        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page_6)
        self.tela_admin.pushButton_22.clicked.connect(self.voltar_tela)
        self.tela_admin.pushButton.clicked.connect(self.visualizar_usuarios)
        self.tela_admin.pushButton_3.clicked.connect(self.tela_deletar_usuario)
        self.tela_admin.pushButton_7.clicked.connect(self.deletar_usuario)
        self.tela_admin.pushButton_4.clicked.connect(self.tela_cadastrar_midia)
        self.tela_admin.pushButton_5.clicked.connect(self.tela_deletar_midia)
        self.tela_admin.pushButton_8.clicked.connect(self.adicionar_midia)
        self.tela_admin.pushButton_9.clicked.connect(self.botao_deletar_midia)
        self.tela_admin.pushButton_10.clicked.connect(self.enviar_midia_servidor)
 
    def operacao_log(self, mensagem):
        '''
        Esse metodo envia uma mensagem para o servidor e recebe uma resposta.
        Essa reposta será utilizada para o login e cadastro do usuário.

        Parameters
        ------
        mensagem: str
            Mensagem que será enviada para o servidor

        Attributes
        ------
        resposta: str
            Resposta que será recebida do servidor
        
        Returns
        ------
        True: bool
            Se a resposta for igual a 1, retorna True
        False: bool
            Se a resposta for diferente de 1, retorna False
        
        
        '''
        if mensagem.split(',')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta and resposta == '1':
                return True
        return False

    def buscar_video(self,caminho):
        '''
        Esse metodo envia uma mensagem para o servidor e recebe um vídeo.
        Esse vídeo será utilizado para a exibição do vídeo na tela de categorias e na tela principal ao clicar nas imagens.

        Attributes
        ------
        msg: str
            Mensagem que será enviada para o servidor
        tamanho_arquivo: int
            Tamanho do arquivo que será recebido
        bytes_recebidos: int
            Bytes recebidos
        data: bytes
            Bytes recebidos
        video_file: file
            Arquivo de vídeo

        Parameters
        ------
        caminho: str

        Returns
        ------
        caminho: str
            Caminho do vídeo que será exibido na tela de categorias e na tela principal ao clicar nas imagens
        
        '''
        msg = f'4,{caminho}'
        self.client_socket.send(msg.encode())
        tamanho_arquivo = int(self.client_socket.recv(1024).decode())
        if tamanho_arquivo == 0:
            return False
        with open(caminho, 'wb') as video_file:
            bytes_recebidos = 0
            while bytes_recebidos < tamanho_arquivo:
                data = self.client_socket.recv(4096)
                bytes_recebidos += len(data)
                video_file.write(data)
            print('Vídeo recebido e salvo com sucesso!')
        return caminho


    def verificacao_login(self):
        '''
        Esse metodo verifica se o usuário e senha digitados estão corretos.
        Se estiverem corretos, o usuário será redirecionado para a tela principal.
        Se não estiverem corretos, será exibida uma mensagem de erro.
        Se os campos não estiverem preenchidos, será exibida uma mensagem de erro.
        Se o usuário for o admin, será redirecionado para a tela de admin.
        Esse metodo também limpa os campos de usuário e senha.
        E por fim, se estiver tudo correto, a tela de login será fechada. E a tela principal será aberta.

        Attributes
        ------
        username_login: str
            Nome do usuário que está logado no momento
        password_login: str
            Senha do usuário que está logado no momento
        mensagem: str
            Mensagem que será enviada para o servidor
        
        Methods
        ------
        exibir_dados(self)
            Envia uma mensagem para o servidor e recebe os dados do usuário logado
        pagina_admin (self)
            Abre a página do admin
        
        return
        ------
        None
        '''
        self.username_login = self.tela_inicial.txt_user.text()
        password_login = self.tela_inicial.txt_password.text()
        mensagem = f'1,{self.username_login},{password_login}'

        if self.username_login and password_login:
            if self.username_login == 'admin' and password_login == 'admin':
                self.pagina_admin()
                self.tela_inicial.txt_user.clear()
                self.tela_inicial.txt_password.clear()
            elif self.operacao_log(mensagem):
                self.QtStack.setCurrentIndex(2)
                self.tela_inicial.txt_user.clear()
                self.tela_inicial.txt_password.clear()               
            else:
                QMessageBox.about(self, "Erro", "Usuário ou senha incorretos")
        else: 
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def exibir_dados(self):
        '''
        Essa função envia uma mensagem para o servidor e recebe os dados do usuário logado.

        Attributes
        ------
        msg: str
            Mensagem que será enviada para o servidor
        resposta2: list
            Lista com os dados do usuário que está logado no momento
        
        Returns
        ------
        resposta2: list
            Lista com os dados do usuário que está logado no momento
        '''
        msg = f'3,{self.username_login}'
        self.client_socket.send(msg.encode())
        self.resposta2 = self.client_socket.recv(1024).decode().split(',')
        return self.resposta2
    
    def enviar_cadastro(self, mensagem):
        '''
        Essa função envia uma mensagem para o servidor e recebe uma resposta.
        Essa resposta será utilizada para o cadastro do usuário.

        Parameters
        ------
        mensagem: str
            Mensagem que será enviada para o servidor
        
        Attributes
        ------
        resposta: str
            Resposta que será recebida do servidor

        Returns
        ------
        True: bool
            Se a resposta for igual a 1, retorna True
        False: bool
            Se a resposta for diferente de 1, retorna False

        '''
        if mensagem.split(',')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta and resposta == '1':
                return True
        return False

    def botaoCadastrar(self):
        '''
        Esses metodo verifica se os campos do cadastro estão preenchidos corretamente.
        Se estiverem corretos, o usuário será cadastrado.
        Se não estiverem corretos, será exibida uma mensagem de erro.
        Se os campos não estiverem preenchidos, será exibida uma mensagem de erro.
        

        Parameters
        ------
        None

        Attributes
        ------
        nome: str
            Nome do usuário que está sendo cadastrado
        email: str
            Email do usuário que está sendo cadastrado
        endereco: str
            Endereço do usuário que está sendo cadastrado
        nascimento: str
            Data de nascimento do usuário que está sendo cadastrado
        usuario: str
            Nome de usuário do usuário que está sendo cadastrado
        senha: str
            Senha do usuário que está sendo cadastrado
        senha_confirmacao: str
            Confirmação da senha do usuário que está sendo cadastrado
        mensagem: str
            Mensagem que será enviada para o servidor

        Methods
        ------
        enviar_cadastro(self, mensagem)
            Envia uma mensagem para o servidor e recebe uma resposta
        
        return
        ------
        None
        '''
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


    #admin
    def pagina_admin (self):
        '''
        Essa função abre a página do admin.

        Attributes
        ------
        None

        Returns
        ------
        None
        '''
        self.QtStack.setCurrentIndex(6)

    def visualizar_usuarios(self):
        '''
        Essa função envia uma mensagem para o servidor e recebe uma lista com os usuários cadastrados.
        Essa lista será utilizada para exibir os usuários cadastrados na tela de admin.

        Attributes
        ------
        msg: str
            Mensagem que será enviada para o servidor
        resposta: str
            Resposta que será recebida do servidor
        lista_dados: list
            Lista com os usuários cadastrados
        
        Methods
        ------
        None

        return
        ------
        None        
        '''

        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page)
        msg = '6,exibir_usuarios'
        self.client_socket.send(msg.encode())
        resposta = self.client_socket.recv(1024).decode()
        lista_dados = ast.literal_eval(resposta)

        existing_layout = self.tela_admin.scrollAreaWidgetContents_3.layout()
        if existing_layout is not None:
            QWidget().setLayout(existing_layout)
        
        layout = QVBoxLayout(self.tela_admin.scrollAreaWidgetContents_3)
        layout.setObjectName("layout")

        for usuario in lista_dados:
            nomes = usuario.upper()
            label = QLabel(nomes, self.tela_admin.scrollAreaWidgetContents_3)
            layout.addWidget(label)
            label.setStyleSheet("font-size: 18px; color: white; border:none; border-bottom: 1px solid yellow;")  
            label.setAlignment(Qt.AlignCenter)  
            label.setFixedSize(140, 30)

        self.tela_admin.scrollArea.setWidget(self.tela_admin.scrollAreaWidgetContents_3)

    def tela_deletar_usuario(self):
        '''
        Essa função abre a tela de deletar usuário.

        Attributes
        ------
        None

        Returns
        ------
        None
        '''
        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page_3)

    def deletar_usuario(self):
        '''
        Essa função envia uma mensagem para o servidor e recebe uma resposta.
        Essa resposta será a informação se o usuário foi deletado ou não.

        Attributes
        ------
        usuario: str
            Nome do usuário que será deletado
        msg: str
            Mensagem que será enviada para o servidor
        resposta: str
            Resposta que será recebida do servidor  

        Methods
        ------
        None

        return
        ------
        None

        '''
        usuario = self.tela_admin.lineEdit.text()
        if usuario:
            msg = f'6,deletar_usuario,{usuario}'
            self.client_socket.send(msg.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta == '1':
                QMessageBox.about(self, "Sucesso", "Usuário deletado com sucesso")
                self.tela_admin.lineEdit.clear()
            else:
                QMessageBox.about(self, "Erro", "Usuário não encontrado")
        else:
            QMessageBox.about(self, 'Erro', 'Preencha o campo')

    def tela_cadastrar_midia(self):
        '''
        Essa função abre a tela de cadastrar mídia.

        Attributes
        ------
        None

        Returns
        ------
        None
        '''
        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page_4)

        
    def adicionar_midia(self):
        '''
        Essa função envia uma mensagem para o servidor e recebe uma resposta.
        Essa resposta será a informação se a mídia foi cadastrada ou não.

        Parameters
        ------
        None

        Attributes
        ------
        nome_filme: str
            Nome do filme que será cadastrado
        genero: str
            Gênero do filme que será cadastrado
        diretor: str
            Diretor do filme que será cadastrado
        caminho: str
            Caminho do filme que será cadastrado
        msg: str
            Mensagem que será enviada para o servidor
        resposta: str
            Resposta que será recebida do servidor

        Methods
        ------
        criar_botao_açao(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de ação.
        criar_botao_comedia(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de comédia.

        return
        ------
        None

        '''
        nome_filme = self.tela_admin.lineEdit_2.text()
        genero = self.tela_admin.lineEdit_3.text().capitalize()
        diretor = self.tela_admin.lineEdit_4.text()
        caminho = self.tela_admin.lineEdit_5.text()
        if nome_filme and genero and diretor and caminho:
            msg = f'6,adicionar_midia,{nome_filme},{genero},{diretor},{caminho}'
            self.client_socket.send(msg.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta == '1':
                QMessageBox.about(self, "Sucesso", "Mídia cadastrada com sucesso")
                self.tela_admin.lineEdit_2.clear()
                self.tela_admin.lineEdit_3.clear()
                self.tela_admin.lineEdit_4.clear()
                self.tela_admin.lineEdit_5.clear()
                if genero == 'Ação':
                    self.criar_botao_açao(self.tela_categoria, nome_filme, caminho, genero)
                elif genero == 'Comédia':
                    self.criar_botao_comedia(self.tela_categoria, nome_filme, caminho, genero)
                elif genero == 'Drama':
                    self.criar_botao_drama(self.tela_categoria, nome_filme, caminho, genero)
                elif genero == 'Terror':
                    self.criar_botao_terror(self.tela_categoria, nome_filme, caminho, genero)
                elif genero == 'Infantil':
                    self.criar_botao_infantil(self.tela_categoria, nome_filme, caminho, genero)
                elif genero == 'Anime':
                    self.criar_botao_anime(self.tela_categoria, nome_filme, caminho, genero)
            else:
                QMessageBox.about(self, "Erro", "Mídia não cadastrada")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def criar_botao_drama(self, tela, nome_filme, caminho, genero):
        '''
        Esses metodo cria um botão na tela de categorias, na seção de drama.

        Parameters
        ------
        tela: QMainWindow
            Tela de categorias
        nome_filme: str
            Nome do filme que será cadastrado
        caminho: str
            Caminho do filme que será cadastrado
        genero: str
            Gênero do filme que será cadastrado
        
        Attributes
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        
        Methods
        ------
        buscar_video(self,caminho)
            Envia uma mensagem para o servidor e recebe um vídeo
        abrir_tela_midia(self, caminho)
            Abre a tela de vídeo
        
        return
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        '''
        if genero == 'Drama':
            botao = QPushButton(tela.scrollAreaWidgetContents_4)
            botao.setObjectName(nome_filme)
            botao.setText(nome_filme)
            botao.setStyleSheet("font-size: 18px; color: white; border:none; border: 1px solid yellow; border-radius: 10px;")
            botao.setFixedSize(400, 30)
            botao.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video(caminho)))
            tela.verticalLayout_4.addWidget(botao)
            return botao
    def criar_botao_terror(self, tela, nome_filme, caminho, genero):
        '''
        Esses metodo cria um botão na tela de categorias, na seção de terror.

        Parameters
        ------
        tela: QMainWindow
            Tela de categorias
        nome_filme: str
            Nome do filme que será cadastrado
        caminho: str
            Caminho do filme que será cadastrado
        genero: str
            Gênero do filme que será cadastrado
        
        Attributes
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        
        Methods
        ------
        buscar_video(self,caminho)
            Envia uma mensagem para o servidor e recebe um vídeo
        abrir_tela_midia(self, caminho)
            Abre a tela de vídeo
        
        return
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        '''
        if genero == 'Terror':
            botao = QPushButton(tela.scrollAreaWidgetContents_5)
            botao.setObjectName(nome_filme)
            botao.setText(nome_filme)
            botao.setStyleSheet("font-size: 18px; color: white; border:none; border: 1px solid yellow; border-radius: 10px;")
            botao.setFixedSize(400, 30)
            botao.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video(caminho)))
            tela.verticalLayout_5.addWidget(botao)
            return botao
    def criar_botao_infantil(self, tela, nome_filme, caminho, genero):
        '''
        Esses metodo cria um botão na tela de categorias, na seção infantil.

        Parameters
        ------
        tela: QMainWindow
            Tela de categorias
        nome_filme: str
            Nome do filme que será cadastrado
        caminho: str
            Caminho do filme que será cadastrado
        genero: str
            Gênero do filme que será cadastrado
        
        Attributes
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        
        Methods
        ------
        buscar_video(self,caminho)
            Envia uma mensagem para o servidor e recebe um vídeo
        abrir_tela_midia(self, caminho)
            Abre a tela de vídeo
        
        return
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        '''
        if genero == 'Infantil':
            botao = QPushButton(tela.scrollAreaWidgetContents_6)
            botao.setObjectName(nome_filme)
            botao.setText(nome_filme)
            botao.setStyleSheet("font-size: 18px; color: white; border:none; border: 1px solid yellow; border-radius: 10px;")
            botao.setFixedSize(400, 30)
            botao.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video(caminho)))
            tela.verticalLayout_6.addWidget(botao)
            return botao
    def criar_botao_anime(self, tela, nome_filme, caminho, genero):
        '''
        Esses metodo cria um botão na tela de categorias, na seção de anime.

        Parameters
        ------
        tela: QMainWindow
            Tela de categorias
        nome_filme: str
            Nome do filme que será cadastrado
        caminho: str
            Caminho do filme que será cadastrado
        genero: str
            Gênero do filme que será cadastrado
        
        Attributes
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        
        Methods
        ------
        buscar_video(self,caminho)
            Envia uma mensagem para o servidor e recebe um vídeo
        abrir_tela_midia(self, caminho)
            Abre a tela de vídeo
        
        return
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        '''
        if genero == 'Anime':
            botao = QPushButton(tela.scrollAreaWidgetContents_8)
            botao.setObjectName(nome_filme)
            botao.setText(nome_filme)
            botao.setStyleSheet("font-size: 18px; color: white; border:none; border: 1px solid yellow; border-radius: 10px;")
            botao.setFixedSize(400, 30)
            botao.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video(caminho)))
            tela.verticalLayout_8.addWidget(botao)
            return botao


    def criar_botao_açao(self, tela, nome_filme, caminho, genero):
        '''
        Esse metodo cria um botão na tela de categorias, na seção de ação.

        Parameters
        ------
        tela: QMainWindow
            Tela de categorias
        nome_filme: str
            Nome do filme que será cadastrado
        caminho: str
            Caminho do filme que será cadastrado
        genero: str
            Gênero do filme que será cadastrado

        Attributes
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        
        Methods
        ------
        buscar_video(self,caminho)
            Envia uma mensagem para o servidor e recebe um vídeo
        abrir_tela_midia(self, caminho)
            Abre a tela de vídeo
        
        return
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        '''
        if genero == 'Ação':
            botao = QPushButton(tela.scrollAreaWidgetContents)
            botao.setObjectName(nome_filme)
            botao.setText(nome_filme)
            botao.setStyleSheet("font-size: 18px; color: white; border:none; border: 1px solid yellow; border-radius: 10px;")
            botao.setFixedSize(400, 30)
            botao.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video(caminho)))
            tela.verticalLayout.addWidget(botao)
            return botao
    
    def criar_botao_comedia(self, tela, nome_filme, caminho, genero):
        '''
        Esse metodo cria um botão na tela de categorias, na seção de comédia.

        Parameters
        ------
        tela: QMainWindow
            Tela de categorias
        nome_filme: str
            Nome do filme que será cadastrado
        caminho: str
            Caminho do filme que será cadastrado
        genero: str
            Gênero do filme que será cadastrado
        
        Attributes
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        
        Methods
        ------
        buscar_video(self,caminho)
            Envia uma mensagem para o servidor e recebe um vídeo
        abrir_tela_midia(self, caminho)
            Abre a tela de vídeo

        return
        ------
        botao: QPushButton
            Botão que será criado na tela de categorias
        '''
        if genero == 'Comédia':
            botao = QPushButton(tela.scrollAreaWidgetContents_3)
            botao.setObjectName(nome_filme)
            botao.setText(nome_filme)
            botao.setStyleSheet("font-size: 18px; color: white; border:none; border: 1px solid yellow; border-radius: 10px;")
            botao.setFixedSize(400, 30)
            botao.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video(caminho)))
            tela.verticalLayout_3.addWidget(botao)
            return botao
        
    def enviar_midia_servidor (self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if fileName != '':
            url = QUrl.fromLocalFile(fileName)
            video = QMediaContent(url)

        buffer_size = 4096
        if os.path.exists(fileName):
            video_file_size = os.path.getsize(fileName)       
            with open(fileName, 'rb') as video_file:
                msg = f'6,tamanho_video,{video_file_size}'
                self.client_socket.send(str(msg).encode())
                while True:
                    data = video_file.read(buffer_size)
                    if not data:
                        break
                    msg = f'6,video,{data}'
                    self.client_socket.send(msg.encode())
            video_file.close()
            print('Arquivo enviado com sucesso.')
        else:
            QMessageBox.about('Erro', 'Arquivo não encontrado.')
    
    def buscar_todos_filmes(self):
        '''
        Essa função envia uma mensagem para o servidor e recebe uma lista com todas as mídias cadastradas.
        Essa lista será utilizada para exibir as mídias cadastradas na tela de categorias.

        Attributes
        ------
        msg: str
            Mensagem que será enviada para o servidor
        resposta: str
            Resposta que será recebida do servidor
        resposta2: list
            Lista com todas as mídias cadastradas

        Methods
        ------
        criar_botao_açao(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de ação.
        criar_botao_comedia(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de comédia.
        criar_botao_drama(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de drama.
        criar_botao_terror(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de terror.
        criar_botao_infantil(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de infantil.
        criar_botao_anime(self, tela, nome_filme, caminho, genero)
            Cria um botão na tela de categorias, na seção de anime.


        return
        ------
        None
        '''
        msg = '6,exibir_todos_filmes'
        self.client_socket.send(msg.encode())
        resposta = self.client_socket.recv(1024).decode()
        resposta2 = ast.literal_eval(resposta)
        for nome_filme, caminho, genero in resposta2:
            if genero == 'Ação':
                self.criar_botao_açao(self.tela_categoria, nome_filme, caminho, genero)
            elif genero == 'Comédia':
                self.criar_botao_comedia(self.tela_categoria, nome_filme, caminho, genero)
            elif genero == 'Drama':
                self.criar_botao_drama(self.tela_categoria, nome_filme, caminho, genero)
            elif genero == 'Terror':
                self.criar_botao_terror(self.tela_categoria, nome_filme, caminho, genero)
            elif genero == 'Infantil':
                self.criar_botao_infantil(self.tela_categoria, nome_filme, caminho, genero)
            elif genero == 'Anime':
                self.criar_botao_anime(self.tela_categoria, nome_filme, caminho, genero)

    def tela_deletar_midia(self):
        '''
        Essa função abre a tela de deletar mídia.
        '''
        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page_5)
    
    def botao_deletar_midia(self):
        '''
        Essa função envia uma mensagem para o servidor e recebe uma resposta.
        Essa resposta será a informação se a mídia foi deletada ou não.

        Attributes
        ------
        nome: str
            Nome da mídia que será deletada
        msg: str
            Mensagem que será enviada para o servidor

        Methods
        ------
        None

        return
        ------
        None
        '''
        nome = self.tela_admin.lineEdit_6.text()
        msg = f'6,deletar_midia,{nome}'
        self.client_socket.send(msg.encode())
        resposta = self.client_socket.recv(1024).decode()
        if resposta == '1':
            QMessageBox.about(self, "Sucesso", "Midia deletada com sucesso")
            self.tela_admin.lineEdit_6.clear()
        else:
            QMessageBox.about(self, "Erro", "Midia não encontrada")
    def voltar_tela(self):
        '''
        Essa função volta para a tela de login.
        '''
        self.QtStack.setCurrentIndex(0)
    def voltar_tela2(self):
        '''
        Essa função volta para a tela principal.
        '''
        self.QtStack.setCurrentIndex(2)
    def abrir_tela_cadastro(self):
        '''
        Essa função abre a tela de cadastro.
        '''
        self.QtStack.setCurrentIndex(1)
    def abrir_tela_categoria(self):
        '''
        Essa função abre a tela de categorias.

        Attributes
        ------
        None
        
        Methods
        ------
        showInicial(self)  
        '''
        self.QtStack.setCurrentIndex(3)
        self.showInicial()
    def abrir_menu(self):
        '''
        Essa função abre o menu.
        '''
        self.QtStack.setCurrentIndex(5)
        self.showInicial_menu()

    def showInicial(self):
        '''
        Essa função mostra a tela inicial.

        Attributes
        ------
        nome: str
            Nome do usuário que está logado no momento
        
        Methods
        ------
        exibir_dados(self)
            Envia uma mensagem para o servidor e recebe os dados do usuário logado

        return
        ------
        None
        '''
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_1)
        nome = self.exibir_dados()[5].replace("'", "")
        self.tela_categoria.lineEdit.setText(f'ESCOLHA UMA CATEGORIA, {nome.upper()}')
    def showAcao(self):
        '''
        Essa função mostra a tela de ação. que está na tela de categorias.
        '''
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page1_2)
    def showComedia(self):
        '''
        Essa função mostra a tela de comédia. que está na tela de categorias.
        '''
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_3)
    def showDrama(self):
        '''
        Essa função mostra a tela de drama. que está na tela de categorias.
        '''
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page)
    def showTerror(self):
        '''
        Essa função mostra a tela de terror. que está na tela de categorias.
        '''
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_2)
    def showInfantil(self):
        '''
        Essa função mostra a tela de infantil. que está na tela de categorias.
        '''
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_4)
    def showAnime(self):
        '''
        Essa função mostra a tela de anime. que está na tela de categorias.
        '''
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_5)
    def showInicial_menu(self):
        '''
        Essa função mostra a tela inicial do menu.

        Attributes
        ------
        nome: str
            Nome do usuário que está logado no momento
        
        Methods
        ------
        exibir_dados(self)
            Envia uma mensagem para o servidor e recebe os dados do usuário logado

        return
        ------
        None
        '''
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page)
        nome = self.exibir_dados()[5].replace("'", "")
        self.tela_menu.label.setText(f'SEJA BEM-VINDO, {nome.upper()}')
    def showPerfil(self):
        '''
        Essa função mostra a tela de perfil.

        Attributes
        ------
        nome: str
            Nome do usuário que está logado no momento
        email: str
            Email do usuário que está logado no momento
        usuario: str
            Nome de usuário do usuário que está logado no momento
        nascimento: str
            Data de nascimento do usuário que está logado no momento
        
        Methods
        ------
        exibir_dados(self)

        return
        ------
        None
        '''

        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_2)
        print (self.exibir_dados())
        nome = self.exibir_dados()[1].replace("'", "")
        email = self.exibir_dados()[2].replace("'", "")
        usuario = self.exibir_dados()[5].replace("'", "")
        nascimento = self.exibir_dados()[4].replace("'", "")
        self.tela_menu.lineEdit.setText(f'{nome.upper()}')
        self.tela_menu.lineEdit_2.setText(f'{email.upper()}')
        self.tela_menu.lineEdit_3.setText(f'{usuario.upper()}')
        self.tela_menu.lineEdit_4.setText(f'{nascimento.upper()}')

    def showSobre(self):
        '''
        Essa função mostra a tela de sobre. Que contém as informações do projeto.
        '''
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_3)

    def showContato(self):
        '''
        Essa função mostra a tela de contato. Que contém as informações para entrar em contato com o desenvolvedor.
        
        Attributes
        ------
        mensagem: str
            Mensagem que será enviada para o servidor
        resposta: str
            Resposta que será recebida do servidor
        
        Methods
        ------
        exibir_dados(self)
            Envia uma mensagem para o servidor e recebe os dados do usuário logado
        exibir_contato(self)
            Abre a tela de contato
        
        return
        ------
        None
        '''
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_4)
        mensagem = f'5,exibir_contato'
        self.client_socket.send(mensagem.encode())
        resposta = self.client_socket.recv(1024).decode()
        if resposta == 'liberado':
            self.exibir_contato()
    
    def exibir_contato(self):
        '''
        Essa função abre a tela de contato. Que seria a conversa do usuário com o desenvolvedor.
        
        Attributes
        ------
        url: str
            URL que será aberta no navegador
        
        Methods
        ------
        None

        return
        ------
        None
        '''
        url = "https://wa.me/5589981186169"
        webbrowser.open(url)
                
    def close (self):
        '''
        Essa função fecha o programa.
        E fecha o socket do cliente.

        Attributes
        ------
        None

        Methods
        ------
        None

        return
        ------
        None
        '''
        self.client_socket.close()
        sys.exit(app.exec_())

    def abrir_tela_midia(self, caminho):
        '''
        Essa função chama a classe VideoPlayer, que é responsável por exibir o vídeo na tela.

        Parameters
        ------
        caminho: str

        Attributes
        ------
        player: VideoPlayer
            Classe responsável por exibir o vídeo na tela
        
        Methods
        ------

        return
        ------
        None
        '''
        if caminho:
            self.player = VideoPlayer(caminho)
        else:
            QMessageBox.about(self, "Erro", "Vídeo não encontrado")


class VideoPlayer(QWidget):
    '''
    Essa classe é responsável por exibir o vídeo na tela. 

    Attributes
    ------
    video_path: str
        Caminho do vídeo que será exibido na tela
    
    Methods
    ------
    closeEvent(self, event)
        Fecha o vídeo
    toggle_play_pause(self)
        Pausa ou dá play no vídeo
    update_position(self, position)
        Atualiza a posição do vídeo
    update_duration(self, duration)
        Atualiza a duração do vídeo
    set_position(self, position)
        Define a posição do vídeo
    set_video_path(self, video_path)
        Define o caminho do vídeo
    video_state_changed(self, state)
        Define o estado do vídeo

    '''
    def __init__(self, video_path):
        '''
        Nessa função é definido o layout da tela de vídeo.
        E é definido o caminho do vídeo que será exibido na tela.

        Parameters
        ------
        video_path: str
            Caminho do vídeo que será exibido na tela
        
        Attributes
        ------
        video_path: str
            Caminho do vídeo que será exibido na tela
        palette: QPalette
            Paleta de cores da tela
        layout: QVBoxLayout
            Layout da tela
        video_widget: QVideoWidget
            Widget do vídeo
        options_layout: QHBoxLayout
            Layout dos botões
        play_pause_button: QPushButton
            Botão de play e pause
        slider: QSlide
            Slider do vídeo
        play_image: QIcon
            Ícone do botão de play
        pause_image: QIcon
            Ícone do botão de pause
        media_player: QMediaPlayer
            Reprodutor de vídeo
        is_playing: bool
            Estado do vídeo
        
        Methods
        ------
        closeEvent(self, event)
            Fecha o vídeo
        toggle_play_pause(self)
            Pausa ou dá play no vídeo
        update_position(self, position)
            Atualiza a posição do vídeo
        update_duration(self, duration)
            Atualiza a duração do vídeo
        set_position(self, position)
            Define a posição do vídeo
        set_video_path(self, video_path)
            Define o caminho do vídeo
        video_state_changed(self, state)
            Define o estado do vídeo
        
        return
        ------
        None
        '''
        super().__init__()
        self.setWindowTitle("Video Player")
        self.resize(800, 600)

        self.video_path = video_path
        
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor(0, 0, 0))
        self.setPalette(palette)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.video_widget = QVideoWidget()
        self.layout.addWidget(self.video_widget)

        self.options_layout = QHBoxLayout()
        self.layout.addLayout(self.options_layout)

        self.play_pause_button = QPushButton()
        self.play_pause_button.setFixedSize(32, 32)
        self.play_pause_button.setStyleSheet("background-color: black")
        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        self.options_layout.addWidget(self.play_pause_button)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)
        self.options_layout.addWidget(self.slider)

        self.play_image = QIcon(QPixmap("play.svg"))
        self.pause_image = QIcon(QPixmap("pause.svg"))

        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.stateChanged.connect(self.video_state_changed)
        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)

        self.is_playing = False

        self.set_video_path(self.video_path)
        self.show()

    def closeEvent(self, event):
        '''
        Essa função fecha o vídeo. E para o vídeo.
        '''
        self.media_player.stop()
        event.accept()
                  
    def toggle_play_pause(self):
        '''
        Essa função pausa ou dá play no vídeo.

        Attributes
        ------
        None

        Methods
        ------
        None

        return
        ------
        None
        '''
        if self.is_playing:
            self.media_player.pause()
        else:
            self.media_player.play()

    def update_position(self, position):
        '''
        Essa função atualiza a posição do vídeo.

        Parameters
        ------
        position: int
            Posição do vídeo

        '''
        self.slider.setValue(position)

    def update_duration(self, duration):
        '''
        Essa função atualiza a duração do vídeo.

        Parameters
        ------
        duration: int
            Duração do vídeo
        '''
        self.slider.setRange(0, duration)

    def set_position(self, position):
        '''
        Essa função define a posição do vídeo.

        Parameters
        ------
        position: int
            Posição do vídeo
        '''
        self.media_player.setPosition(position)

    def set_video_path(self, video_path):
        '''
        Essa função define o caminho do vídeo.

        Parameters
        ------
        video_path: str
            Caminho do vídeo que será exibido na tela
        
        Attributes
        ------
        video_url: QUrl
            URL do vídeo
        
        Methods
        ------
        video_state_changed(self, state)
            Define o estado do vídeo
        
        return
        ------
        None
        '''
        video_url = QUrl.fromLocalFile(video_path)
        video_content = QMediaContent(video_url)
        self.media_player.setMedia(video_content)
        self.is_playing = False
        self.media_player.pause()

    def video_state_changed(self, state):
        '''
        Essa função define o estado do vídeo.

        Parameters
        ------
        state: QMediaPlayer.PlayingState
            Estado do vídeo

        Attributes
        ------
        state: QMediaPlayer.PlayingState
            Estado do vídeo
        
        Methods
        ------
        None

        return
        ------
        None
        '''
        if state == QMediaPlayer.PlayingState:
            self.is_playing = True
            self.play_pause_button.setIcon(self.pause_image)
        else:
            self.is_playing = False
            self.play_pause_button.setIcon(self.play_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)    
    show_main = Main()
    sys.exit(app.exec_())

    