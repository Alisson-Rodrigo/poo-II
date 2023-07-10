import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Abrir Página no Chrome")
        self.resize(300, 200)

        button = QPushButton("Abrir Página", self)
        button.clicked.connect(self.open_page)
        button.setGeometry(50, 50, 200, 100)

    def open_page(self):
        url = "https://www.example.com"  # Insira a URL da página desejada aqui
        webbrowser.get("chrome").open(url)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
