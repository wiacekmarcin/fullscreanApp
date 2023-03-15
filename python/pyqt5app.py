#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import analogclock 
import zegar
import pogoda

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.plgs = []
        self.timerOneSec = QTimer()
        self.timerOneSec.timeout.connect(self.update1Sec)
        self.timerOneSec.start(1000)
        self.setObjectName("MainWindow")
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.setCentralWidget(self.centralWidget)
        
        if 1:
            pal = self.palette()
            pal.setColor(pal.Window, Qt.black)
            pal.setColor(pal.WindowText, Qt.white)
            pal.setColor(pal.Text, Qt.white)
            pal.setColor(pal.BrightText, Qt.white)
            self.setAutoFillBackground(True)
            self.setPalette(pal)

            #sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            #sizePolicy.setHorizontalStretch(0)
            #sizePolicy.setVerticalStretch(0)
            #sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
            #self.widget.setSizePolicy(sizePolicy)
            palette = QPalette()
            brush = QBrush (QColor(255, 255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(palette.Active, palette.WindowText, brush)
            palette.setBrush(palette.Active, palette.Button, brush)
            brush1 = QBrush(QColor(0, 0, 0, 255))
            brush1.setStyle(Qt.SolidPattern)
            palette.setBrush(palette.Active, palette.Midlight, brush1)
            palette.setBrush(palette.Active, palette.Dark, brush1)
            palette.setBrush(palette.Active, palette.Mid, brush1)
            palette.setBrush(palette.Active, palette.Text, brush)
            palette.setBrush(palette.Active, palette.ButtonText, brush)
            palette.setBrush(palette.Active, palette.Base, brush1)
            palette.setBrush(palette.Active, palette.Window, brush1)
            palette.setBrush(palette.Active, palette.Shadow, brush1)
            palette.setBrush(palette.Active, palette.Highlight, brush1)
            palette.setBrush(palette.Active, palette.Link, brush1)
            palette.setBrush(palette.Active, palette.LinkVisited, brush1)
            palette.setBrush(palette.Active, palette.AlternateBase, brush1)
            palette.setBrush(palette.Active, palette.ToolTipBase, brush1)
            brush2 = QBrush(QColor(255, 255, 255, 128))
            brush2.setStyle(Qt.NoBrush)
            #palette.setBrush(palette.Active, palette.PlaceholderText, brush2)
            palette.setBrush(palette.Inactive, palette.WindowText, brush)
            palette.setBrush(palette.Inactive, palette.Button, brush)
            palette.setBrush(palette.Inactive, palette.Midlight, brush1)
            palette.setBrush(palette.Inactive, palette.Dark, brush1)
            palette.setBrush(palette.Inactive, palette.Mid, brush1)
            palette.setBrush(palette.Inactive, palette.Text, brush)
            palette.setBrush(palette.Inactive, palette.ButtonText, brush)
            palette.setBrush(palette.Inactive, palette.Base, brush1)
            palette.setBrush(palette.Inactive, palette.Window, brush1)
            palette.setBrush(palette.Inactive, palette.Shadow, brush1)
            palette.setBrush(palette.Inactive, palette.Highlight, brush1)
            palette.setBrush(palette.Inactive, palette.Link, brush1)
            palette.setBrush(palette.Inactive, palette.LinkVisited, brush1)
            palette.setBrush(palette.Inactive, palette.AlternateBase, brush1)
            palette.setBrush(palette.Inactive, palette.ToolTipBase, brush1)
            brush3 = QBrush(QColor(255, 255, 255, 128))
            brush3.setStyle(Qt.NoBrush)
            #palette.setBrush(palette.Inactive, palette.PlaceholderText, brush3)
            palette.setBrush(palette.Disabled, palette.WindowText, brush1)
            palette.setBrush(palette.Disabled, palette.Button, brush)
            palette.setBrush(palette.Disabled, palette.Midlight, brush1)
            palette.setBrush(palette.Disabled, palette.Dark, brush1)
            palette.setBrush(palette.Disabled, palette.Mid, brush1)
            palette.setBrush(palette.Disabled, palette.Text, brush1)
            palette.setBrush(palette.Disabled, palette.ButtonText, brush1)
            palette.setBrush(palette.Disabled, palette.Base, brush1)
            palette.setBrush(palette.Disabled, palette.Window, brush1)
            palette.setBrush(palette.Disabled, palette.Shadow, brush1)
            brush4 = QBrush(QColor(145, 141, 126, 255))
            brush4.setStyle(Qt.SolidPattern)
            palette.setBrush(palette.Disabled, palette.Highlight, brush4)
            palette.setBrush(palette.Disabled, palette.Link, brush1)
            palette.setBrush(palette.Disabled, palette.LinkVisited, brush1)
            palette.setBrush(palette.Disabled, palette.AlternateBase, brush1)
            palette.setBrush(palette.Disabled, palette.ToolTipBase, brush1)
            brush5 = QBrush(QColor(255, 255, 255, 128))
            brush5.setStyle(Qt.NoBrush)
            #palette.setBrush(palette.Disabled, palette.PlaceholderText, brush5)
            self.widget.setPalette(palette)

            self.widget.setMouseTracking(False)
            self.widget.setAutoFillBackground(False)
            self.widget.setCursor(Qt.BlankCursor)
            
        

    def setPlugins(self, plg):
        print(self.geometry())
        self.plgs = plg
        for p in plg:
            p.setMainWindow(self)
            r = p.getRect()
            print(r)
            p.setGeometry(r)
            p.update()
            

    def update1Sec(self):
        for p in self.plgs:
            p.timeout(QDateTime.currentDateTime())

    def sendNotification(self, valueDict):
        for p in self.plgs:
            p.receiveNotfication(valueDict)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    pluggins = [analogclock.AnalogClock(mainWin.widget),
                zegar.Zegar(mainWin.widget),
                pogoda.Pogoda(mainWin.widget)
                ]
    #mainWin.setWindowState(mainWin.WindowFullScreen)
    mainWin.setGeometry(0,0,1080,1920)
    mainWin.setPlugins(pluggins)
    mainWin.show()
    
    sys.exit(app.exec_())