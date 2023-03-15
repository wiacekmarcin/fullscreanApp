#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import blackwidget
dateStyle = "font-size:30px;line-height:35px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";
timeStyle = "font-size:65px;line-height:65px;color:#fff;text-align:left;background:#000;font-family:\"Roboto Condensed\",sans-serif;font-weight:300;";
secsStyle = "font-size:50%;line-height:50%;color:#666;vertical-align:super;text-align:left;background:#000;font-family:\"Roboto Condensed\",sans-serif;font-weight:300;";
minStyle  = "font-size:24px;line-height:25px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";

class Zegar(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Zegar, self).__init__(parent)
        self.ldate = None
        self.ltime = None
        self.wschod = None
        self.zachod = None
        self.days = [];
        self.monts = [];

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
        self.setupUi(self)
    
    def timeout(self, dt):
        monthname = self.monts[dt.date().month()];
        dayname = self.days[dt.date().dayOfWeek()];

        self.ldate.setText("%s, %d %s %d" % (dayname, dt.date().day(), monthname, dt.date().year()))

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
        return QRect(0, 0, 580, 180)

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
        if Zegar.objectName() == '':
            Zegar.setObjectName("Zegar")
        Zegar.resize(self.getRect().width(), self.getRect().height())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        Zegar.setSizePolicy(sizePolicy)
        Zegar.setAutoFillBackground(False)
        Zegar.setStyleSheet("background-color:rgb(0,0,0);color:rgb(255,255,255);")
        self.ldate = QLabel(Zegar)
        self.ldate.setObjectName("ldate")
        self.ldate.setGeometry(QRect(0, 0, 680, 50))
        self.ldate.setStyleSheet(dateStyle)
        self.ltime = QLabel(Zegar)
        self.ltime.setObjectName("ltime")
        self.ltime.setGeometry(QRect(0, 60, 311, 81))
        self.ltime.setTextFormat(Qt.RichText)
        self.ltime.setStyleSheet(timeStyle)
        font = self.ltime.font()
        font.setPixelSize(65);
        self.ltime.setFont(font)
        