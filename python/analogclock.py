from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import blackwidget
import resources

class AnalogClock(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)
        self.setWschodZachod = 0
        self.startArcWschod = 0
        self.startArcZachod = 0
        self.m_h = 0
        self.m_m = 0
        self.m_s = 0
        self.wschod = "0:01"
        self.zachod = "23:59"
        self.resize(500, 500)

    def getRect(self):
        return QRect(580, 0, self.width(), self.height())
    
    def receiveNotfication(self, dictValue):
        if "sunrise" in dictValue:
            self.setWschod(dictValue["sunrise"].hour(), dictValue["sunrise"].minute())
        
        if "sunset" in dictValue:
            self.setZachod(dictValue["sunset"].hour(), dictValue["sunset"].minute())

    def setWschod(self, hour, min):
        print (hour, min)
        self.wschod = "%d:" % hour
        if min < 10:
            self.wschod += "0"
        self.wschod += "%d" % min

   
    def setZachod(self, hour, min):
        print (hour, min)
        self.zachod = "%d:" % hour
        if min < 10:
            self.zachod += "0"
        self.zachod += "%d" % min
    
    def timeout(self, dt):
        self.m_h = dt.time().hour()
        self.m_m = dt.time().minute()
        self.m_s = dt.time().second()
        self.update()
        
    def setNotfication(self, skey, value):
        if skey == "wschod-slonca":
            self.setWchod(value['hour'], value['min'])
        if skey == "zaschod-slonca":
            self.setWchod(value['hour'], value['min'])

    def paintEvent(self, a0):
        
        hourHand = QPolygon([QPoint(14, 16), QPoint(-14, 16), QPoint(0, -150)])
        minuteHand = QPolygon([QPoint(14, 16), QPoint(-14, 16), QPoint(0, -200)])
        secondHand = QPolygon([QPoint(8, 8), QPoint(-8, 8), QPoint(0, -200)])
    
        hourColor = QColor(225, 225, 225)
        minuteColor = QColor(255, 255, 255, 191)
        secondColor = QColor(200, 200, 200, 90)
        color = QColor(120, 255, 100)

        side = min(self.width(), self.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing);
        path = QPainterPath()
        path.addRoundedRect(QRectF(0, 0, self.width(), self.height()), 5, 5)
        pen = QPen(Qt.white, 2)
        painter.setPen(pen)
        painter.fillPath(path, Qt.black)
        painter.drawPath(path)

        soonPx = QPixmap(":/new/prefix1/sun.png")
        moonPx = QPixmap(":/new/prefix1/moon.png")
        painter.drawPixmap(1,1, soonPx)
        
        font = painter.font()
        font.setPixelSize(32)
        painter.setFont(font)
        painter.drawText(70,50, self.wschod)

        fm = QFontMetrics (font);
        pixelsWide = fm.width(self.zachod);
        #pixelsHigh = fm.height();
        painter.drawPixmap(500-pixelsWide-moonPx.width()-5,1, moonPx)
        painter.drawText(500-pixelsWide,50, self.zachod)

        painter.setRenderHint(painter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 500.0, side / 500.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(hourColor)

        painter.save()
        painter.rotate(30.0 * ((self.m_h + self.m_m / 60.0)))
        painter.drawConvexPolygon(hourHand)
        painter.restore()

        painter.setPen(hourColor)
        p = painter.pen()
        p.setWidth(5)
        painter.setPen(p)

        for i in range(12):
            painter.drawLine(176, 0, 192, 0)
            painter.rotate(30.0)
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(minuteColor)

        painter.save()
        painter.rotate(6.0 * (self.m_m + self.m_s / 60.0))
        painter.drawConvexPolygon(minuteHand)
        painter.restore()

        painter.setPen(minuteColor)

        for j in range(60):
            if i % 5:
                painter.drawLine(184, 0, 192, 0)
                painter.rotate(6.0)
        painter.setPen(Qt.NoPen)
        painter.setBrush(secondColor)

        painter.save()
        painter.rotate(360.0 * (1.0 * self.m_s / 60.0))
        painter.drawConvexPolygon(secondHand)
        painter.restore()


   