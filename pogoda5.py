#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import datetime
import time

import blackwidget
import pogoda5_ui



class Pogoda5(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Pogoda5, self).__init__(parent)
        self.oneday_ui = pogoda5_ui.Ui_Pogoda5_1Day()
        self.setupUi(self)
        self.isImage = False
        self.maxCnt = 0
        self.cntSec = self.maxCnt
        

    def getRect(self):
        return QRect(0, 500, 1024, 300)
    
    def setupUi(self, Pogoda5_1Day):
        self.oneday_ui.setupUi(Pogoda5_1Day)
    
    def timeout(self, dt):
        print("PG-1")
        ddate = dt.date()
        ttime = dt.time()
        h = ttime.hour()
        m = ttime.minute()
        s = ttime.second()
        y = ddate.year()
        mm = ddate.month()
        d = ddate.day()
        fstr = '%d_' % y
        if mm < 10: fstr += '0'
        fstr += '%d_' % mm
        if d < 10: fstr += '0'
        fstr += '%d' % d

        print("PG-2")
        fpath = os.path.join("/home/pi/tmp", fstr) + ".png"
        if os.path.exists(fpath):
            if not self.isImage:
                self.isImage = True
                pixmap = QPixmap (fpath)
                self.oneday_ui.label.setPixmap(pixmap);
                self.oneday_ui.label.setMask(pixmap.mask());
        else:
            self.isImage = False


        


    
    