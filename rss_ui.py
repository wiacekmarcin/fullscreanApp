# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rss.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RSS(object):
    def setupUi(self, RSS):
        RSS.setObjectName("RSS")
        RSS.resize(1024, 114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RSS.sizePolicy().hasHeightForWidth())
        RSS.setSizePolicy(sizePolicy)
        RSS.setMinimumSize(QtCore.QSize(1024, 90))
        RSS.setMaximumSize(QtCore.QSize(1024, 600))
        RSS.setBaseSize(QtCore.QSize(680, 90))
        self.horizontalLayout = QtWidgets.QHBoxLayout(RSS)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(RSS)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(0, 0, 0);")
        self.title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.info = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(18)
        font.setItalic(True)
        self.info.setFont(font)
        self.info.setStyleSheet("color: rgb(150, 150, 150);\n"
"background-color: rgb(0, 0, 0);")
        self.info.setLineWidth(0)
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.info.setWordWrap(True)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(RSS)
        QtCore.QMetaObject.connectSlotsByName(RSS)

    def retranslateUi(self, RSS):
        _translate = QtCore.QCoreApplication.translate
        RSS.setWindowTitle(_translate("RSS", "Form"))
        self.title.setText(_translate("RSS", "-"))
