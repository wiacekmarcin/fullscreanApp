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
        self.lazienkaUi.etLazienka.setText("")

    def getRect(self):
        return QRect(0, 515, 250, 100)
    
    def setupUi(self, Lazienka):
        self.lazienkaUi.setupUi(Lazienka)

    def receiveNotfication(self, dictValue):
        vals['lazienka_temp'] = valg['ltemp']
                vals['lazienka_humi'] = valg['lhum']
        if "lazienka_temp" in dictValue:
            self.lazienkaUi. = dictValue["28fff708640400a3"]
        if "286cf90f0b0000ae" in dictValue:
            self.raspTemp = dictValue["286cf90f0b0000ae"]

    def timeout(self, dt):
        hour = dt.time().hour()
        min = dt.time().minute()
        sec = dt.time().second()
        self.statsUi.cpuSpeed.setText("%d MHz" % getCPUcurrentSpeed())
        self.statsUi.cpuUsage.setText("%d %%" % getCPUuse())
        
        if not self.firstTime and min % 5 != 0 or sec != 0:
            return

        if self.firstTime or (min == 0 and sec == 0):
            self.statsUi.localIp.setText("%s" % getIP())
            self.statsUi.zewnetrzneIp.setText("%s" % getIPOut())
        self.firstTime = False
        self.statsUi.tempGPU.setText("%2.1f\u00B0C" % getCPUtemperature())
        self.statsUi.tempMonitor.setText("%s\u00B0C" % self.monitorTemp)
        self.statsUi.tempRasp.setText("%s\u00B0C" % self.raspTemp)
