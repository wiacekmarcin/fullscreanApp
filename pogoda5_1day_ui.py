# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pogoda5_1day.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.widget = QtWidgets.QWidget(Pogoda5_1Day)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.dayname = QtWidgets.QLabel(self.widget)
        self.dayname.setAlignment(QtCore.Qt.AlignCenter)
        self.dayname.setObjectName("dayname")
        self.gridLayout.addWidget(self.dayname, 1, 0, 1, 8)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Pogoda5_1Day)
        QtCore.QMetaObject.connectSlotsByName(Pogoda5_1Day)

    def retranslateUi(self, Pogoda5_1Day):
        _translate = QtCore.QCoreApplication.translate
        Pogoda5_1Day.setWindowTitle(_translate("Pogoda5_1Day", "Form"))
        self.label.setText(_translate("Pogoda5_1Day", "00:00"))
        self.label_4.setText(_translate("Pogoda5_1Day", "09:00"))
        self.label_5.setText(_translate("Pogoda5_1Day", "12:00"))
        self.label_7.setText(_translate("Pogoda5_1Day", "18:00"))
        self.label_3.setText(_translate("Pogoda5_1Day", "06:00"))
        self.label_8.setText(_translate("Pogoda5_1Day", "21:00"))
        self.label_2.setText(_translate("Pogoda5_1Day", "03:00"))
        self.label_6.setText(_translate("Pogoda5_1Day", "15:00"))
        self.dayname.setText(_translate("Pogoda5_1Day", "Poniedziałek"))
