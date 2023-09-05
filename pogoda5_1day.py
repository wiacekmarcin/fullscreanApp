#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import feedparser
import pogoda5_1day_ui
import blackwidget
import numpy as np
from scipy.interpolate import splrep, splev


class Pogoda5_1Day(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Pogoda5_1Day, self).__init__(parent)
        self.oneday_ui = pogoda5_1day_ui.Ui_Pogoda5_1Day()
        self.setupUi(self)
        self.prevM = None
        self.font = QFont()
        self.font.setFamily("Roboto Condensed Light")
        self.font.setPointSize(12)
        self.font.setBold(False)
        self.font.setWeight(50)
        self.w3h = 20
        self.h1deg = 10
        self.maxRange = 30
        self.minRange = 10
        self.height = 300
        self.margin = 10
        self.daysName = [u'Niedziela',u'Poniedziałek',u'Wtorek',u'Środa',u'Czwartek',u'Piatek',u'Sobota']
        self.temp =  [15.27, 13.76, 14.84, 19.40, 22.43, 22.87, 18.48, 16.75, 15.57, 14.46, 17.77, 23.04, 25.37, 25.24, 20.43, 18.59, 16.91, 15.71, 18.73, 24.52, 27.10, 25.56,
                      22.04, 19.79, 18.15, 17.20, 19.71, 25.96, 25.56, 28.48, 28.30, 22.88, 20.22, 18.44, 17.28, 20.01, 25.85, 28.58, 28.63, 23.09, 20.63 ]
        #self.ftemp = [14.84, ]
    
    def timeout(self, dt):

        hour = dt.time().hour()
        minute = dt.time().minute()
        
        if self.prevM != minute:
            self.prevM = minute
            self.draw()
    

    def getRect(self):
        return QRect(0, 300,(5*8+1)*self.w3h+2*self.margin, 500)

    
    def setupUi(self, Pogoda5_1Day):
        self.oneday_ui.setupUi(Pogoda5_1Day)
        
    def draw(self):

        scene = QGraphicsScene()
        #scene.setForegroundBrush(QColor(0, 0, 0))
        #scene.setBackgroundBrush(QColor(255, 255, 255))
        scene.setBackgroundBrush(QColor(0, 0, 0))
        #scene.setFont(self.font)

        #t = scene.addText("Hello, world!", self.font)
        #t.setPos(50,50)
        #t.setDefaultTextColor(QColor(255, 255, 255))
        pen = QPen(QColor(255, 255, 255))
        pen.setWidth(1)

        x = []
        for i in range(8*5+1) :
            #scene.addLine(QLineF(self.margin + self.w3h*i, 0, self.margin + self.w3h*i, self.height), pen)
            if i % 2 == 0:
                if i == 8*5:
                    t = scene.addText("24", self.font)
                else:
                    t = scene.addText("%d" % ((i*3) % 24), self.font)
                pos = QPointF(self.margin + self.w3h*i, self.height+16)                
                #item.setPos(pos - item.boundingRect().center())
                t.setPos(pos - t.boundingRect().center())
                t.setDefaultTextColor(QColor(255, 255, 255))
            if i % 8 == 0 and i < 5*8:
                if int(i/8) % 2 == 0:
                    b = QBrush(QColor(50, 50, 50))
                else:
                    b = QBrush(QColor(0, 0, 0, 0))
                r = scene.addRect(self.margin + self.w3h*i, 0, self.w3h*8, self.height, QPen(QColor(0, 0, 0)), b)
                t = scene.addText(self.daysName[int(i/8) % 7], self.font)
                pos = QPointF(self.margin + self.w3h*i, self.height+32)
                t.setDefaultTextColor(QColor(255, 255, 255))
                t.setPos(pos)
        prev2 = None
        prev = None
        points = []    
        for x in range(len(self.temp)):
            if self.temp[x] is None:
                continue
            pos = QRectF(self.margin + self.w3h*x -1 , (30-self.temp[x]) * self.h1deg +1, 3, 3)  
            e = scene.addEllipse(pos,  QPen(QColor(255, 255, 255)), QBrush(QColor(255,255,255)))
            points.append(pos)
            if prev is None:
                prev = pos.center()
                continue

            #pl = QLineF(prev, pos.center())
            #l = scene.addLine(pl, pen)

            if prev2 is None:
                prev2 = prev
                prev = pos.center()
                continue

            if prev2.y() < prev.y()  and prev.y() > pos.center().y():
                t = scene.addText("%2.1f" % self.temp[x-1], self.font)
                t.setDefaultTextColor(QColor(255, 255, 255))
                t.setPos(prev)

            if prev2.y() > prev.y()  and prev.y() < pos.center().y():
                t = scene.addText("%2.1f" % self.temp[x-1], self.font)
                t.setDefaultTextColor(QColor(255, 255, 255))
                t.setPos(prev - QPointF(0, 32))

            prev2 = prev
            prev = pos.center()

        x = np.array([p.x() for p in points])
        y = np.array([p.y() for p in points])

        spl = splrep(x, y)
        f = splev(x, spl)

# Estimate values
        x_new = np.linspace(points[0].x(), points[-1].x(), (5*8+1)*self.w3h)
        y_new = splev(x_new, spl)
        poly = []
        for i in range(len(x_new)):
            poly.append(QPointF(x_new[i], y_new[i]))
        polygon = QPolygonF(poly)
        #scene.addPolygon(polygon, pen)
        path = QPainterPath();
        path.addPolygon(polygon);
        contour = QGraphicsPathItem(path);
        contour.setPen(pen);
        scene.addItem(contour)



        self.oneday_ui.graphicsView.setScene(scene)
        self.oneday_ui.graphicsView.show()
        