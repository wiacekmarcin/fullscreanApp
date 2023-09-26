# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pogoda5_1day.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pogoda5_1Day(object):
    def setupUi(self, Pogoda5_1Day):
        Pogoda5_1Day.setObjectName("Pogoda5_1Day")
        Pogoda5_1Day.resize(326, 152)
        self.verticalLayout = QtWidgets.QVBoxLayout(Pogoda5_1Day)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Pogoda5_1Day)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(Pogoda5_1Day)
        QtCore.QMetaObject.connectSlotsByName(Pogoda5_1Day)

    def retranslateUi(self, Pogoda5_1Day):
        _translate = QtCore.QCoreApplication.translate
        Pogoda5_1Day.setWindowTitle(_translate("Pogoda5_1Day", "Form"))

