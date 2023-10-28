#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import zegar_ui
import blackwidget
secsStyle = "font-size:40%;color:#666;vertical-align:super;text-align:left;";



class Zegar(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Zegar, self).__init__(parent)
        self.ZegarUi = zegar_ui.Ui_Zegar()
        self.setupUi(self)
        self.days = []
        self.monts = []
        self.firstRun = True

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

        hour = dt.time().hour()
        min = dt.time().minute()
        sec = dt.time().second()

        if self.firstRun:
            self.updateDayLabels(dt.date())
            self.updateTimeLabels(hour, min, sec)
            self.firstRun = False
            return

        if hour == 0 and min == 0 and sec == 0:
            self.updateDayLabels(dt.date())

        self.updateTimeLabels(hour, min, sec)
        

    def updateDayLabels(self, date):
        year = date.year()
        month = date.month()
        dayofYear = date.dayOfYear()
        week = date.weekNumber()
        self.ZegarUi.miesiac_rok.setText("%s %d" % (self.monts[month], year))
        self.ZegarUi.info.setText("%d dzień, %d tydzień, %d miesiąc" % (dayofYear, week[0], month))

    def updateTimeLabels(self, hour, min, sec):
        hs = '%d' % hour
        if hour < 10:
            hs = " " + hs
        ms = '%d' % min
        if min < 10:
            ms = "0" + ms

        ss = '%d' % sec
        if sec < 10:
            ss = "0" + ss

        if sec % 2 == 0:    
            self.ZegarUi.czas_h_m.setText("<span>%s<span style=\"color:rgb(100,100,100)\">:</span>%s</span>" % 
                      (hs, ms))
        else:
            self.ZegarUi.czas_h_m.setText("<span>%s:%s</span>" % 
                      (hs, ms, ))
        self.ZegarUi.czas_sec.setText(ss)

    def getRect(self):
        return QRect(0, 0, 680, 115)

    
    def setupUi(self, Zegar):
        self.ZegarUi.setupUi(Zegar)
        