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
        
        idf = QFontDatabase.addApplicationFont(":/font/fonts/weathericons-regular-webfont.ttf")
        family = QFontDatabase.applicationFontFamilies(idf)[0]
        self._weatherFont = QFont(family)

        idf = QFontDatabase.addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-Light.ttf")
        family = QFontDatabase.applicationFontFamilies(idf)[0]
        self._robotoCondensedFont = QFont(family)

        idf = QFontDatabase.addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-Regular.ttf")
        family = QFontDatabase.applicationFontFamilies(idf)[0]
        self._robotoRegularFont = QFont(family)
        
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
    
    def setMainWindow(self, mw):
        self.mainWindow = mw


    def receiveNotfication(self, dictValue):
        pass

    def sendNotification(self, dictValue):
        if self.mainWindow:
            self.mainWindow.sendNotification(dictValue)

        

    
  