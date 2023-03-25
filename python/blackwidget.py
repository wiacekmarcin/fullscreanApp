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
        self.fonts = {}
        #self.setLineWidth(2)
        #self.setFrameStyle(QFrame.Box | QFrame.Plain)

        
        idf = QFontDatabase.addApplicationFont(":/font/fonts/weathericons-regular-webfont.ttf")
        family = QFontDatabase.applicationFontFamilies(idf)[0]
        self.fonts["Weathericons"] = {}
        self.fonts["Weathericons"]["Regular"] = QFont(family)

        self.fonts["Roboto"] = {}
        for f in ["Black", "BlackItalic", "Bold", "BoldItalic", 
                  "Light", "LightItalic", "Medium", "MediumItalic",
                  "Regular", "RegularItalic", "Thin", "ThinItalic"]:
            idf = QFontDatabase.addApplicationFont(":/font/fonts/robotic/Roboto-%s.ttf" % f)
            family = QFontDatabase.applicationFontFamilies(idf)[0]
            self.fonts["Roboto"][f] = QFont(family)

        self.fonts["Roboto-Condensed"] = {}
        for f in ["Bold", "BoldItalic", "Light", "LightItalic", "Regular", "RegularItalic"]:
            idf = QFontDatabase.addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-%s.ttf" % f)
            family = QFontDatabase.applicationFontFamilies(idf)[0]
            self.fonts["Roboto-Condensed"] = QFont(family)
        
        self.fonts["Roboto-Slab"] = {}
        for f in ["Bold", "Light", "Regular", "Thin"]:
            idf = QFontDatabase.addApplicationFont(":/font/fonts/roboto-slab/Roboto-Slab-%s.ttf" % f)
            family = QFontDatabase.applicationFontFamilies(idf)[0]
            self.fonts["Roboto-Slab"][f] = QFont(family)
        
        
    def getFont(self, name, size, type="Regular", italic=False):
        if name not in ["Weathericons", "Roboto", "Roboto-Condensed", "Roboto-Slab"]:
            return None

        if italic:
            type = type + "Italic"
        
        if type not in self.fonts[name]:
            return None
        
        font = self.fonts[name][type]
        font.setPixelSize(size)

        return font
    
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

        

    
  