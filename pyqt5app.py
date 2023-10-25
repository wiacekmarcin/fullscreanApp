#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import analogclock 
import zegar
import pogodav2
import calendar_day
import pogoda5
import read_serial
import stats
import rss
import kredyty

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
        
        


        self.widget.setMouseTracking(False)
        self.widget.setAutoFillBackground(True)
        self.widget.setCursor(Qt.BlankCursor)
            
        self.setBackground()

    def setPlugins(self, plg):
        print(self.geometry())
        self.plgs = plg
        for p in plg:
            p.setMainWindow(self)
            r = p.getRect()
            print(r)
            p.setGeometry(r)
            p.update()
        self.repaint()    

    def update1Sec(self):
        dt = QDateTime.currentDateTime()
        #print("--")
        try:
            for p in self.plgs:
                #print(p)
                try:
                    p.timeout(dt)
                except :
                    pass
            self.update()
        except KeyboardInterrupt:
            print("ctrl-c")
            sys.exit(0)

    def sendNotification(self, valueDict):
        for p in self.plgs:
            p.receiveNotfication(valueDict)
    
    def setBackground(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        pal = self.palette()
        pal.setColor(QPalette.Background, Qt.black)
        pal.setColor(QPalette.Window, Qt.black)

        pal.setColor(QPalette.WindowText, Qt.white)
        pal.setColor(QPalette.Text, Qt.white)
        pal.setColor(QPalette.BrightText, Qt.white)

        #self.setAutoFillBackground(True)
        self.setPalette(pal)

        
        pal = self.palette()
        pal.setColor(pal.Window, Qt.black)
        pal.setColor(pal.WindowText, Qt.white)
        pal.setColor(pal.Text, Qt.white)
        pal.setColor(pal.BrightText, Qt.white)
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
        self.setPalette(palette)

    def paintEvent(self, ev):
        print("paintEvent")
        #QMainWindow.repaint()
        m_GridDistance = 10
        p = QPainter(self)
        p.setPen(QPen(Qt.green,1))
        i = 0
        while i < self.width(): 
            p.drawLine(i,0,i,self.height())
            i += m_GridDistance
        i = 0
        while i < self.height(): 
            p.drawLine(0,i,self.width(),i);
            i += m_GridDistance


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    mainWin = MainWindow()
    pluggins = [
                analogclock.AnalogClock(mainWin.widget),
                zegar.Zegar(mainWin.widget),
                pogodav2.Pogodav2(mainWin.widget),
                calendar_day.CalendarDay(mainWin.widget),
                pogoda5.Pogoda5(mainWin.widget),
                read_serial.SerialReader(mainWin.widget),
                stats.StatsWidget(mainWin.widget),
                rss.RSS(mainWin.widget),
                kredyty.Kredyty(mainWin.widget),
                ]
    #mainWin.setWindowState(mainWin.WindowFullScreen)
    mainWin.setGeometry(0,0,1080,1920)
    mainWin.setPlugins(pluggins)
    mainWin.showFullScreen()
    mainWin.show()
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        sys.exit(-1)

    #pip3 install BeautifulSoup4
    #pip3 install pyserial
    #pip3 install feedparser
    #pip3 install scipy