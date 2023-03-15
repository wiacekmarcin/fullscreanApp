from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Communicate(QObject):
    notification = pyqtSignal()
    value = {}

class BlackWidget(QFrame):
    
    def __init__(self, parent=None):
        super(BlackWidget, self).__init__(parent)
        self.mainWindow = None
        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Box | QFrame.Plain)
        #self.setStyleSheet("QFrame {background-color: white); border-color: blue;}")
        self.c = Communicate(self)
        if 0:
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

            self.setAutoFillBackground(True)
            self.setPalette(pal)
    def setMainWindow(self, mw):
        self.mainWindow = mw


    def receiveNotfication(self, dictValue):
        pass

    def sendNotification(self, dictValue):
        if self.mainWindow:
            self.mainWindow.sendNotification(dictValue)

    def paintEvent(self, ev):
        QFrame.paintEvent(event)

        p = QPainter(self)
        p.setPen(QPen(Qt.white,3))
        
        for i in range (int i(0); i < width(); i += m_GridDistance){
        p.drawLine(i,0,i,height());
    }

    for(int i(0); i < height(); i += m_GridDistance){
        p.drawLine(0,i,width(),i);
    }
  