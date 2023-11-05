#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import datetime
import time

import blackwidget
import kredyty_ui



class Kredyty(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Kredyty, self).__init__(parent)
        self.kred = kredyty_ui.Ui_Kredyty()
        self.setupUi(self)
        self.isImage = False
        self.maxCnt = 0
        self.cntSec = self.maxCnt
        

    def getRect(self):
        return QRect(1080-710, 1920-125, 710, 125)
    
    def setupUi(self, Kredyty):
        self.kred.setupUi(Kredyty)
    
    def timeout(self, dt):
        print("kr-1")
        ddate = dt.date()

        y = ddate.year()
        mm = ddate.month()

        fstr = 'kredyty_%d_' % y
        if mm < 10: fstr += '0'
        fstr += '%d' % mm
        

        print("kr-2")
        fpath = os.path.join("/home/pi/tmp", fstr) + ".png"
        print(fpath)
        if os.path.exists(fpath):
            if not self.isImage:
                self.isImage = True
                pixmap = QPixmap (fpath)
                self.kred.label.setPixmap(pixmap);
                self.kred.label.setMask(pixmap.mask());
        else:
            self.isImage = False


        


    
    