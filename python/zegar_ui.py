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
        Zegar.resize(680, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Zegar.sizePolicy().hasHeightForWidth())
        Zegar.setSizePolicy(sizePolicy)
        Zegar.setAutoFillBackground(False)
        Zegar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ldate = QtWidgets.QLabel(Zegar)
        self.ldate.setGeometry(QtCore.QRect(0, 0, 680, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ldate.sizePolicy().hasHeightForWidth())
        self.ldate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(28)
        self.ldate.setFont(font)
        self.ldate.setObjectName("ldate")
        self.ltime = QtWidgets.QLabel(Zegar)
        self.ltime.setGeometry(QtCore.QRect(0, 60, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(72)
        font.setBold(True)
        self.ltime.setFont(font)
        self.ltime.setTextFormat(QtCore.Qt.RichText)
        self.ltime.setIndent(0)
        self.ltime.setObjectName("ltime")
        self.lsec = QtWidgets.QLabel(Zegar)
        self.lsec.setGeometry(QtCore.QRect(320, 60, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(36)
        self.lsec.setFont(font)
        self.lsec.setObjectName("lsec")
        self.label = QtWidgets.QLabel(Zegar)
        self.label.setGeometry(QtCore.QRect(10, 150, 48, 48))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/new/prefix1/sun.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Zegar)
        self.label_2.setGeometry(QtCore.QRect(190, 150, 48, 48))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/new/prefix1/moon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.wschod = QtWidgets.QLabel(Zegar)
        self.wschod.setGeometry(QtCore.QRect(60, 160, 100, 32))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(18)
        self.wschod.setFont(font)
        self.wschod.setObjectName("wschod")
        self.zachod = QtWidgets.QLabel(Zegar)
        self.zachod.setGeometry(QtCore.QRect(240, 160, 100, 32))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(18)
        self.zachod.setFont(font)
        self.zachod.setObjectName("zachod")

        self.retranslateUi(Zegar)
        QtCore.QMetaObject.connectSlotsByName(Zegar)

    def retranslateUi(self, Zegar):
        _translate = QtCore.QCoreApplication.translate
        Zegar.setWindowTitle(_translate("Zegar", "Form"))
        self.ltime.setText(_translate("Zegar", "<html><head/><body><p>88:88</p></body></html>"))
        self.lsec.setText(_translate("Zegar", "00"))
        self.wschod.setText(_translate("Zegar", "--"))
        self.zachod.setText(_translate("Zegar", "--"))

import ikony_rc
