# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Admin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 640)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 640))
        MainWindow.setStyleSheet("background-color: rgb(10, 3, 34);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(0, 0, 1261, 101))
        self.frame_10.setStyleSheet("background-color: black;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setGeometry(QtCore.QRect(580, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white;\n"
"border-bottom: 1px solid yellow;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_22.setGeometry(QtCore.QRect(1220, 60, 31, 31))
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet("background-image: url(log-out.svg);\n"
"background-repeat: no-repeat;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 100, 351, 541))
        self.frame.setStyleSheet("border: 1px solid rgb(255, 249, 255);\n"
"border-radius:2px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 20, 121, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: white;\n"
"border: none;\n"
"border-bottom:1px solid yellow;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 180, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 220, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(340, 100, 911, 541))
        self.stackedWidget.setStyleSheet("border: 1px solid white;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label = QtWidgets.QLabel(self.page_6)
        self.label.setGeometry(QtCore.QRect(70, 200, 781, 101))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"border: none;\n"
"border-bottom: 1px solid yellow;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_6)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(210, 50, 491, 461))
        self.scrollArea.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 472, 459))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 10, 201, 26))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: white;\n"
"border: none;\n"
"border-bottom:1px solid yellow;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "CAST"))
        self.pushButton_22.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "VISUALIZAR USUÁRIOS"))
        self.pushButton_2.setText(_translate("MainWindow", "MENU ADMIN"))
        self.pushButton_3.setText(_translate("MainWindow", "DELETAR USUÁRIOS"))
        self.pushButton_4.setText(_translate("MainWindow", "CADASTRAR FILMES"))
        self.pushButton_5.setText(_translate("MainWindow", "DELETAR FILMES"))
        self.label.setText(_translate("MainWindow", "PAINEL DE CONTROLE DA PLATAFORMA \"CAST\""))
        self.pushButton_6.setText(_translate("MainWindow", "USUÁRIOS"))
