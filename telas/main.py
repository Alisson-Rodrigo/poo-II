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
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        hostname = socket.gethostname()
        ip_Adress = socket.gethostbyname(hostname)
        ip = '10.180.46.76'
        port = 10010
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
        self.tela_primaria.pushButton_2s.clicked.connect(self.abrir_menu)
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
 
    def operacao_log(self, mensagem):
        if mensagem.split(',')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta and resposta == '1':
                return True
        return False

    def buscar_video(self,caminho):
        msg = f'4,{caminho}'
        self.client_socket.send(msg.encode())
        tamanho_arquivo = int(self.client_socket.recv(1024).decode())
        if tamanho_arquivo == 0:
            QMessageBox.about(self, "Erro", "Video não encontrado")
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
        msg = f'3,{self.username_login}'
        self.client_socket.send(msg.encode())
        self.resposta2 = self.client_socket.recv(1024).decode().split(',')
        return self.resposta2
    
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
        self.QtStack.setCurrentIndex(6)

    def visualizar_usuarios(self):
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
        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page_3)

    def deletar_usuario(self):
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
        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page_4)

        
    def adicionar_midia(self):
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
            else:
                QMessageBox.about(self, "Erro", "Mídia não cadastrada")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def criar_botao_açao(self, tela, nome_filme, caminho, genero):
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
        if genero == 'Comédia':
            botao = QPushButton(tela.scrollAreaWidgetContents_3)
            botao.setObjectName(nome_filme)
            botao.setText(nome_filme)
            botao.setStyleSheet("font-size: 18px; color: white; border:none; border: 1px solid yellow; border-radius: 10px;")
            botao.setFixedSize(400, 30)
            botao.clicked.connect(lambda: self.abrir_tela_midia(self.buscar_video(caminho)))
            tela.verticalLayout_3.addWidget(botao)
            return botao

    
    def buscar_todos_filmes(self):
        msg = '6,exibir_todos_filmes'
        self.client_socket.send(msg.encode())
        resposta = self.client_socket.recv(1024).decode()
        resposta2 = ast.literal_eval(resposta)
        for nome_filme, caminho, genero in resposta2:
            if genero == 'Ação':
                self.criar_botao_açao(self.tela_categoria, nome_filme, caminho, genero)
            elif genero == 'Comédia':
                self.criar_botao_comedia(self.tela_categoria, nome_filme, caminho, genero)

    def tela_deletar_midia(self):
        self.tela_admin.stackedWidget.setCurrentWidget(self.tela_admin.page_5)
    
    def botao_deletar_midia(self):
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
        self.QtStack.setCurrentIndex(0)
    def voltar_tela2(self):
        self.QtStack.setCurrentIndex(2)
    def abrir_tela_cadastro(self):
        self.QtStack.setCurrentIndex(1)
    def abrir_tela_categoria(self):
        self.QtStack.setCurrentIndex(3)
        self.showInicial()
    def abrir_menu(self):
        self.QtStack.setCurrentIndex(5)
        self.showInicial_menu()

    def showInicial(self):
        self.tela_categoria.stackedWidget_2.setCurrentWidget(self.tela_categoria.page_1)
        nome = self.exibir_dados()[5].replace("'", "")
        self.tela_categoria.lineEdit.setText(f'ESCOLHA UMA CATEGORIA, {nome.upper()}')
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

    def showInicial_menu(self):
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page)
        nome = self.exibir_dados()[5].replace("'", "")
        self.tela_menu.label.setText(f'SEJA BEM-VINDO, {nome.upper()}')
    def showPerfil(self):
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_2)
        nome = self.exibir_dados()[1].replace("'", "")
        email = self.exibir_dados()[2].replace("'", "")
        endereco = self.exibir_dados()[3].replace("'", "")
        nascimento = self.exibir_dados()[4].replace("'", "")
        self.tela_menu.lineEdit.setText(f'{nome.upper()}')
        self.tela_menu.lineEdit_2.setText(f'{email.upper()}')
        self.tela_menu.lineEdit_3.setText(f'{endereco.upper()}')
        self.tela_menu.lineEdit_4.setText(f'{nascimento.upper()}')

    def showSobre(self):
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_3)

    def showContato(self):
        self.tela_menu.stackedWidget.setCurrentWidget(self.tela_menu.page_4)
        mensagem = f'5,exibir_contato'
        self.client_socket.send(mensagem.encode())
        resposta = self.client_socket.recv(1024).decode()
        if resposta == 'liberado':
            self.exibir_contato()
    
    def exibir_contato(self):
        url = "https://wa.me/5589981186169"
        webbrowser.open(url)
                
    def close (self):
        self.client_socket.close()
        sys.exit(app.exec_())

    def abrir_tela_midia(self, caminho):
        self.player = VideoPlayer(caminho)


class VideoPlayer(QWidget):
    def __init__(self, video_path):
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
        self.media_player.stop()
        event.accept()
                  
    def toggle_play_pause(self):
        if self.is_playing:
            self.media_player.pause()
        else:
            self.media_player.play()

    def update_position(self, position):
        self.slider.setValue(position)

    def update_duration(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def set_video_path(self, video_path):
        video_url = QUrl.fromLocalFile(video_path)
        video_content = QMediaContent(video_url)
        self.media_player.setMedia(video_content)
        self.is_playing = False
        self.media_player.pause()

    def video_state_changed(self, state):
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