# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zegar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Zegar(object):
    def setupUi(self, Zegar):
        Zegar.setObjectName("Zegar")
        Zegar.resize(680, 90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Zegar.sizePolicy().hasHeightForWidth())
        Zegar.setSizePolicy(sizePolicy)
        Zegar.setMinimumSize(QtCore.QSize(680, 90))
        Zegar.setMaximumSize(QtCore.QSize(680, 114))
        Zegar.setBaseSize(QtCore.QSize(680, 90))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Zegar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.czas_h_m = QtWidgets.QLabel(Zegar)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.czas_h_m.setFont(font)
        self.czas_h_m.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.czas_h_m.setObjectName("czas_h_m")
        self.horizontalLayout.addWidget(self.czas_h_m)
        self.czas_sec = QtWidgets.QLabel(Zegar)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.czas_sec.setFont(font)
        self.czas_sec.setStyleSheet("color: rgb(85, 87, 83);\n"
"background-color: rgb(0, 0, 0);")
        self.czas_sec.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.czas_sec.setObjectName("czas_sec")
        self.horizontalLayout.addWidget(self.czas_sec)
        spacerItem = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(Zegar)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.miesiac_rok = QtWidgets.QLabel(self.frame)
        self.miesiac_rok.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(36)
        self.miesiac_rok.setFont(font)
        self.miesiac_rok.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(0, 0, 0);")
        self.miesiac_rok.setAlignment(QtCore.Qt.AlignCenter)
        self.miesiac_rok.setObjectName("miesiac_rok")
        self.verticalLayout.addWidget(self.miesiac_rok)
        self.info = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(18)
        font.setItalic(True)
        self.info.setFont(font)
        self.info.setStyleSheet("color: rgb(150, 150, 150);\n"
"background-color: rgb(0, 0, 0);")
        self.info.setLineWidth(0)
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Zegar)
        QtCore.QMetaObject.connectSlotsByName(Zegar)

    def retranslateUi(self, Zegar):
        _translate = QtCore.QCoreApplication.translate
        Zegar.setWindowTitle(_translate("Zegar", "Form"))
        self.czas_h_m.setText(_translate("Zegar", "88:88"))
        self.czas_sec.setText(_translate("Zegar", "88"))
        self.miesiac_rok.setText(_translate("Zegar", "październik, 2023"))
        self.info.setText(_translate("Zegar", "336 dzień, 52 tydzień, 11 miesiąc"))

