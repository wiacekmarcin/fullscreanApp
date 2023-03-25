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
        Zegar.resize(395, 113)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Zegar.sizePolicy().hasHeightForWidth())
        Zegar.setSizePolicy(sizePolicy)
        Zegar.setAutoFillBackground(False)
        Zegar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Zegar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ltime = QtWidgets.QLabel(Zegar)
        self.ltime.setTextFormat(QtCore.Qt.RichText)
        self.ltime.setIndent(0)
        self.ltime.setObjectName("ltime")
        self.horizontalLayout.addWidget(self.ltime)

        self.retranslateUi(Zegar)
        QtCore.QMetaObject.connectSlotsByName(Zegar)

    def retranslateUi(self, Zegar):
        _translate = QtCore.QCoreApplication.translate
        Zegar.setWindowTitle(_translate("Zegar", "Form"))
        self.ltime.setText(_translate("Zegar", "<html><head/><body><p>88:88<span style=\" vertical-align:super;\">88</span></p></body></html>"))

import ikony_rc
