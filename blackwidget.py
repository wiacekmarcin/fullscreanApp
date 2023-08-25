from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from enum import Enum
class Communicate(QObject):
    notification = pyqtSignal()
    value = {}

class BlackWidget(QFrame):
    
    def __init__(self, parent=None):
        super(BlackWidget, self).__init__(parent)
        self.mainWindow = None
        self.cntSec = 0
        #self.setLineWidth(2)
        #self.setFrameStyle(QFrame.Box | QFrame.Plain)
        

   
    def getColor(self, value=100):
        return QColor((int)(value*2.55), (int)(value*2.55), (int)(value*2.55))

    def getStyleColor(self, value=100):
        return "color: rgb(%d, %d, %d);" % ((int)(value*2.55), (int)(value*2.55), (int)(value*2.55))

    
    def setMainWindow(self, mw):
        self.mainWindow = mw


    def receiveNotfication(self, dictValue):
        pass

    def sendNotification(self, dictValue):
        if self.mainWindow:
            self.mainWindow.sendNotification(dictValue)

        

    
  