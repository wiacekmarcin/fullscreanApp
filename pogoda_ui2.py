# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../pogoda.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pogoda(object):
    def setupUi(self, Pogoda):
        Pogoda.setObjectName("Pogoda")
        Pogoda.resize(400, 300)
        self.wind = QtWidgets.QLabel(Pogoda)
        self.wind.setGeometry(QtCore.QRect(50, 150, 58, 18))
        self.wind.setObjectName("wind")
        self.citydate = QtWidgets.QLabel(Pogoda)
        self.citydate.setGeometry(QtCore.QRect(0, 0, 250, 40))
        self.citydate.setText("")
        self.citydate.setObjectName("citydate")
        self.line = QtWidgets.QFrame(Pogoda)
        self.line.setGeometry(QtCore.QRect(0, 42, 250, 16))
        self.line.setStyleSheet("color:rgb(145, 148, 148); size:5pt\n"
"")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Pogoda)
        QtCore.QMetaObject.connectSlotsByName(Pogoda)

    def retranslateUi(self, Pogoda):
        _translate = QtCore.QCoreApplication.translate
        Pogoda.setWindowTitle(_translate("Pogoda", "Form"))
        self.wind.setText(_translate("Pogoda", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pogoda = QtWidgets.QWidget()
    ui = Ui_Pogoda()
    ui.setupUi(Pogoda)
    Pogoda.show()
    sys.exit(app.exec_())

