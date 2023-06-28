import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 640)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1251, 551))
        self.frame.setStyleSheet("background-color: rgb(10, 11, 70);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 550, 1251, 91))
        self.frame_2.setStyleSheet("background-color: black;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 31, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-image: url(play.svg);\n"
"background-repeat: no-repeat;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(-20, 40, 1291, 20))
        self.label.setStyleSheet("border-bottom: 1px solid white;")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 10, 31, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-image: url(pause.svg);\n"
"background-repeat: no-repeat;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 20, 1131, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))


class MediaPlayer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar os sinais aos slots
        self.ui.pushButton.clicked.connect(self.play)
        self.ui.pushButton_2.clicked.connect(self.pause)
        self.ui.horizontalSlider.valueChanged.connect(self.seek)

    def play(self):
        print("Play button clicked")

    def pause(self):
        print("Pause button clicked")

    def seek(self, position):
        print("Slider value changed:", position)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MediaPlayer()
    MainWindow.show()
    sys.exit(app.exec_())


    
