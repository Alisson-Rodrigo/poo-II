from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from video2 import tela_video


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reprodução de Vídeo")
        self.setGeometry(100, 100, 1250, 640)

        # Criar a tela de vídeo
        self.tela_video = tela_video()
        self.tela_video.setupUi(self)

        # Criar o layout e o widget de vídeo
        layout = QVBoxLayout()
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        # Criar o botão para iniciar a reprodução
        #play_button = QPushButton("Play")
        self.tela_video.pushButton.clicked.connect(self.play_video)

        # Definir o widget de vídeo como widget central
        self.tela_video.frame.setLayout(layout)

        # Criar o player de mídia
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

    def play_video(self):
        video_url = QUrl.fromLocalFile("MC-CJ-Apaixonou-eu-_Funk-Explode_-_720p_.mp4")  # Caminho do vídeo local
        media_content = QMediaContent(video_url)
        self.media_player.setMedia(media_content)
        self.media_player.play()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()