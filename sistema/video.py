import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Player")
        self.setGeometry(100, 100, 800, 600)

        # Criar o layout e o widget de vídeo
        layout = QVBoxLayout()
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        # Criar o botão para iniciar a reprodução
        play_button = QPushButton("Play")
        play_button.clicked.connect(self.play_video)
        layout.addWidget(play_button)

        # Criar o widget central
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Criar o player de mídia
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

    def play_video(self,caminho):
        video_url = QUrl.fromLocalFile(f"{caminho}")  # Caminho do vídeo local
        media_content = QMediaContent(video_url)
        self.media_player.setMedia(media_content)
        self.media_player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaPlayer()
    window.show()
    sys.exit(app.exec_())
