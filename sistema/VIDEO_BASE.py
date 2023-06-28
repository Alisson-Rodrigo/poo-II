import sys
import vlc
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication

class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Player")
        self.setGeometry(100, 100, 800, 600)

        # Criar o layout e o widget de vídeo
        layout = QVBoxLayout()
        self.video_widget = QtWidgets.QFrame()
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
        self.media_player = vlc.MediaPlayer()

        # Configurar a janela de reprodução do VLC
        self.media_player.set_hwnd(self.video_widget.winId())

    def play_video(self):
        video_path = "MC-CJ-Apaixonou-eu-_Funk-Explode_-_720p_.avi"  # Caminho do vídeo local
        media = vlc.Media(video_path)
        self.media_player.set_media(media)
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Configurar o estilo escuro
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QColor(250, 250, 250))
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(250, 250, 250))
    dark_palette.setColor(QPalette.ToolTipText, QColor(250, 250, 250))
    dark_palette.setColor(QPalette.Text, QColor(250, 250, 250))
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, QColor(250, 250, 250))
    dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(dark_palette)

    window = MediaPlayer()
    window.show()

    sys.exit(app.exec_())
