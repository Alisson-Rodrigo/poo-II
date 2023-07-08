import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowTitle("Video Player")
        self.resize(800, 600)

        self.video_path = video_path
        
        # Definindo o background na cor preta
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor(0, 0, 0))
        self.setPalette(palette)

        # Criando o layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Criando o widget de vídeo
        self.video_widget = QVideoWidget()
        self.layout.addWidget(self.video_widget)

        # Criando o layout para as opções
        self.options_layout = QHBoxLayout()
        self.layout.addLayout(self.options_layout)

        # Criando o botão para reproduzir/pausar o vídeo
        self.play_pause_button = QPushButton()
        self.play_pause_button.setFixedSize(32, 32)
        self.play_pause_button.setStyleSheet("background-color: black")
        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        self.options_layout.addWidget(self.play_pause_button)

        # Criando a barra de reprodução
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)
        self.options_layout.addWidget(self.slider)

        # Carregando as imagens dos botões de reprodução e pausa
        self.play_image = QIcon(QPixmap("play.svg"))
        self.pause_image = QIcon(QPixmap("pause.svg"))

        # Criando o player de mídia
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.stateChanged.connect(self.video_state_changed)
        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)

        # Flag para controlar a reprodução do vídeo
        self.is_playing = False

        self.set_video_path(self.video_path)
        self.show()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_path = "videoplayback.avi"
    video_player = VideoPlayer(video_path)
    sys.exit(app.exec_())
