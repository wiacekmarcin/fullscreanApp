#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import zegar_ui
import blackwidget
dateStyle = "font-size:30px;line-height:35px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";
timeStyle = "font-size:65px;line-height:65px;color:#fff;text-align:left;background:#000;font-family:\"Roboto Condensed\",sans-serif;font-weight:300;";
secsStyle = "font-size:50%;line-height:50%;color:#666;vertical-align:super;text-align:left;background:#000;font-family:\"Roboto Condensed\",sans-serif;font-weight:300;";
minStyle  = "font-size:24px;line-height:25px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";

class Zegar(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Zegar, self).__init__(parent)
        self.ZegarUi = zegar_ui.Ui_Zegar()
        self.setupUi(self)
        self.ltime = self.ZegarUi.ltime
        self.days = []
        self.monts = []

        self.ZegarUi.ltime.setFont(self.getFont("Roboto-Slab", 96, "Bold"))

        self.days = ["", ("Poniedziałek"),
                      ("Wtorek"),
                      ("Środa"),
                      ("Czwartek"),
                      ("Piątek"),
                      ("Sobota"),
                      ("Niedziela")]
        self.monts = ["", ("styczeń"),
                   ("luty"),
                   ("marzec"),
                   ("kwiecień"),
                   ("maj"),
                   ("czerwiec"),
                   ("lipiec"),
                   ("sierpień"),
                   ("wrzesień"),
                   ("październik"),
                   ("listopad"),
                   ("grudzień")]
    
    def timeout(self, dt):


        hour = dt.time().hour();
        min = dt.time().minute();
        sec = dt.time().second();
        hs = '%d' % hour
        if hour < 10:
            hs = " " + hs
        ms = '%d' % min
        if min < 10:
            ms = "0" + ms

        ss = '%d' % sec
        if sec < 10:
            ss = "0" + ss
        self.ltime.setText("<span>%s:%s<sup style=\"%s\">%s</sup><span>" % 
                      (hs, ms, secsStyle, ss))


    def getRect(self):
        return QRect(0, 0, 400, 115)

    #def setWschod(self, h, m):
    #    ms = '%d' % m
    #    if m < 10:
    #        ms = "0"+ms
    #    hs = '%d' % h
    #    self.wschod.setText("%1:%2" % (hs,ms))

    #def setZachod(self, h, m):
    #    ms = '%d' % m
    #    if m < 10:
    #        ms = "0"+ms
    #    hs = '%d' % h
    #    self.zachod.setText("%1:%2" % (hs,ms))


    def setupUi(self, Zegar):
        self.ZegarUi.setupUi(Zegar)
        