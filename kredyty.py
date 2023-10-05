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
        return QRect(0, 1750, 600, 250)
    
    def setupUi(self, Kredyty):
        self.kred.setupUi(Kredyty)
    
    def timeout(self, dt):
        ddate = dt.date()

        y = ddate.year()
        mm = ddate.month()

        fstr = 'kredyty_%d_' % y
        if mm < 10: fstr += '0'
        fstr += '%d' % mm
        


        fpath = os.path.join("/tmp", fstr) + ".png"
        if os.path.exists(fpath):
            if not self.isImage:
                self.isImage = True
                pixmap = QPixmap (fpath)
                self.kred.label.setPixmap(pixmap);
                self.kred.label.setMask(pixmap.mask());
        else:
            self.isImage = False


        


    
    