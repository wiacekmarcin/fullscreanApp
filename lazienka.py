#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import blackwidget
import lazienka_ui


class Lazienka(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Lazienka, self).__init__(parent)
        self.lazienkaUi = lazienka_ui.Ui_Lazienka()
        self.setupUi(self)
        self.firstTime = True
        self.vals = {}
        self.lazienkaUi.etLazienka.setText("")

    def getRect(self):
        return QRect(0, 515, 250, 100)
    
    def setupUi(self, Lazienka):
        self.lazienkaUi.setupUi(Lazienka)

    def receiveNotfication(self, dictValue):
        if "lazienka_temp" in dictValue:
            self.lazienkaUi.temperature.setText(dictValue["lazienka_temp"])
        if "lazienka_humi" in dictValue:
            self.lazienkaUi.wilgotnosc.setText(dictValue["lazienka_humi"])

    def timeout(self, dt):
        hour = dt.time().hour()
        min = dt.time().minute()
        sec = dt.time().second()
        
        


