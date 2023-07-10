import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon

class MediaPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Player")
        self.setGeometry(100, 100, 800, 600)
        
        # Criação do widget de vídeo
        self.video_widget = QVideoWidget(self)
        
        # Criação dos botões de controle
        self.play_button = QPushButton()
        self.play_button.setIcon(QIcon("play.png"))
        self.pause_button = QPushButton()
        self.pause_button.setIcon(QIcon("pause.png"))
        self.stop_button = QPushButton()
        self.stop_button.setIcon(QIcon("stop.png"))
        
        # Criação da label para exibir o status
        self.status_label = QLabel()
        
        # Criação do layout horizontal para os botões
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addStretch()
        
        # Criação do layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addLayout(button_layout)
        layout.addWidget(self.status_label)
        
        # Definição do layout principal
        self.setLayout(layout)
        
        # Criação do objeto QMediaPlayer
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        # Conexão dos botões aos métodos correspondentes
        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)
        
        # Conexão dos sinais do media player aos métodos correspondentes
        self.media_player.stateChanged.connect(self.media_state_changed)
        
        # Configuração do player de vídeo
        self.media_player.setVideoOutput(self.video_widget)
        
    def play(self):
        self.media_player.play()
        
    def pause(self):
        self.media_player.pause()
        
    def stop(self):
        self.media_player.stop()
        
    def media_state_changed(self, state):
        if state == QMediaPlayer.StoppedState:
            self.status_label.setText("Stopped")
        elif state == QMediaPlayer.PlayingState:
            self.status_label.setText("Playing")
        elif state == QMediaPlayer.PausedState:
            self.status_label.setText("Paused")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MediaPlayer()
    player.show()
    sys.exit(app.exec_())
