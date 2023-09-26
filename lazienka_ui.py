# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/lazienka.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Lazienka(object):
    def setupUi(self, Lazienka):
        Lazienka.setObjectName("Lazienka")
        Lazienka.resize(309, 88)
        self.gridLayout = QtWidgets.QGridLayout(Lazienka)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Lazienka)
        self.line.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 6)
        self.temperature = QtWidgets.QLabel(Lazienka)
        font = QtGui.QFont()
        font.setFamily("Weather Icons")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(0, 0, 0);")
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 2, 2, 1, 1)
        self.etT = QtWidgets.QLabel(Lazienka)
        font = QtGui.QFont()
        font.setFamily("Weather Icons")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.etT.setFont(font)
        self.etT.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(0, 0, 0);")
        self.etT.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.etT.setObjectName("etT")
        self.gridLayout.addWidget(self.etT, 2, 1, 1, 1)
        self.wilgotnosc = QtWidgets.QLabel(Lazienka)
        font = QtGui.QFont()
        font.setFamily("Weather Icons")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.wilgotnosc.setFont(font)
        self.wilgotnosc.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(0, 0, 0);")
        self.wilgotnosc.setObjectName("wilgotnosc")
        self.gridLayout.addWidget(self.wilgotnosc, 2, 4, 1, 1)
        self.etW = QtWidgets.QLabel(Lazienka)
        font = QtGui.QFont()
        font.setFamily("Weather Icons")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.etW.setFont(font)
        self.etW.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(0, 0, 0);")
        self.etW.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.etW.setObjectName("etW")
        self.gridLayout.addWidget(self.etW, 2, 3, 1, 1)
        self.etLazienka = QtWidgets.QLabel(Lazienka)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etLazienka.setFont(font)
        self.etLazienka.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(0, 0, 0);")
        self.etLazienka.setObjectName("etLazienka")
        self.gridLayout.addWidget(self.etLazienka, 2, 0, 1, 1)
        self.etTemp = QtWidgets.QLabel(Lazienka)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(14)
        self.etTemp.setFont(font)
        self.etTemp.setObjectName("etTemp")
        self.gridLayout.addWidget(self.etTemp, 0, 1, 1, 2)
        self.etWilgotnosc = QtWidgets.QLabel(Lazienka)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(14)
        self.etWilgotnosc.setFont(font)
        self.etWilgotnosc.setObjectName("etWilgotnosc")
        self.gridLayout.addWidget(self.etWilgotnosc, 0, 3, 1, 2)

        self.retranslateUi(Lazienka)
        QtCore.QMetaObject.connectSlotsByName(Lazienka)

    def retranslateUi(self, Lazienka):
        _translate = QtCore.QCoreApplication.translate
        Lazienka.setWindowTitle(_translate("Lazienka", "Form"))
        self.temperature.setText(_translate("Lazienka", "0.0"))
        self.etT.setText(_translate("Lazienka", "T"))
        self.wilgotnosc.setText(_translate("Lazienka", "0.0"))
        self.etW.setText(_translate("Lazienka", "W"))
        self.etLazienka.setText(_translate("Lazienka", "Łazienka"))
        self.etTemp.setText(_translate("Lazienka", "Temperatura"))
        self.etWilgotnosc.setText(_translate("Lazienka", "Wilgotność"))

