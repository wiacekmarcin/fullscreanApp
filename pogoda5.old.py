#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import datetime
import time

import blackwidget
import resources

from urllib.request import urlopen
import json
import pogoda5_ui

import numpy as np
from scipy.interpolate import splrep, splev




citiStyle = "font-size:30px;line-height:35px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;"
windBStyle = "font-size:45px;line-height:45px;color:#aaa;text-align:left;background:#000;font-weight:400;"
windDStyle = "font-size:25px;line-height:30px;color:#999;text-align:left;background:#000;font-weight:500;"
windSStyle = "font-size:16px;line-height:18px;color:#666;text-align:left;background:#000;font-weight:300;"
iconWiStyle = "font-size:65px;line-height:65px;color:#aaa;text-align:right;background:#000;font-weight:400;"
feelTempStyle = "font-size:30px;line-height:35px;color:#999;text-align:right;background:#000;font-weight:400;"
conditionalStyle = "font-size:22px;line-height:20px;color:#ccc;text-align:right;background:#000;font-weight:600;"

class Pogoda5(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Pogoda5, self).__init__(parent)
        self.oneday_ui = pogoda5_ui.Ui_Pogoda5_1Day()
        self.setupUi(self)
        self.url = "https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
        self.prevday = None
        self.delaySec = 0
        self.nodata = False
        self.minTemp = [None, None, None, None, None, None, None]
        self.maxTemp = [None, None, None, None, None, None, None]

        self.font = QFont()
        self.font.setFamily("Roboto Condensed Light")
        self.font.setPointSize(12)
        self.font.setBold(False)
        self.font.setWeight(50)
        self.w3h = 25
        self.h1deg = 10
        self.maxRange = 30
        self.minRange = 10
        self.height = 300
        self.margin = int((1080-(8*5*self.w3h)) / 2)
        self.dweek = 0

        self.daysName = [u'Niedziela',u'Poniedziałek',u'Wtorek',u'Środa',u'Czwartek',u'Piatek',u'Sobota']

    def getRect(self):
        return QRect(0, 550,(5*8+1)*self.w3h+2*self.margin, 300)
    
    def setupUi(self, Pogoda5_1Day):
        self.oneday_ui.setupUi(Pogoda5_1Day)
    
    def timeout(self, dt):
        if not self.prevday is None or self.prevday == dt.date().day():
            self.delaySec = 600
            return
        
        
        if self.delaySec > 0:
            self.delaySec -= 1
            return

        self.prevday = dt.date().day()
        #month = dt.date().month()
        #year = dt.date().year()
        #date_time = datetime.datetime(year, month, self.prevday, 0, 0, 0)
        #tdt = time.mktime(date_time.timetuple())
        #offset = dt.offsetFromUtc()
        
        response = urlopen(self.url)
        data_json = json.loads(response.read().decode('utf-8'))

        cnt_items = int(data_json["cnt"]) or 0
        if cnt_items == 0:
            print("Brak danych")
            self.delaySec = 60
            self.show(False)
            return

        items = data_json["list"]
        if items is None:
            print("Brak danych")
            self.delaySec = 60
            self.show(False)
            return
        
        self.clear(dt.date().dayOfWeek() - 1, cnt_items + 8)
    
        self.nodata = True
        minTempL = None
        maxTempL = None
        for i in items:
            dt_txt = i["dt_txt"]
            if i["dt_txt"] is None:
                continue
            fd,ft = dt_txt.split(' ')
            year,month,day = fd.split('-')
            hour,minute,second = ft.split(':')
            day = int(day)
            #idt = int(i['dt'])
            #ih = (idt - tdt - offset)/3600
            #idx = ih/3
            idx = (day-self.prevday)*8+int(int(hour)/3)

            m = i['main']
            w = i['weather'][0]
            rainsnow = 0
            if 'rain' in i:
                rainsnow = i['rain']['3h']
            if 'snow' in i:
                rainsnow = i['snow']['3h']                
            self.add(idx, day-self.prevday, m['temp'],m['feels_like'],m['temp_min'],m['temp_max'],m['pressure'],m['humidity'], w['description'], w['icon'],
                     rainsnow)

            if int(day) == int(self.prevday):
                if minTempL is None:
                    minTempL = float(m['temp_min'])
                elif minTempL > float(m['temp_min']):
                    minTempL = float(m['temp_min'])

                if maxTempL is None:
                    maxTempL = float(m['temp_max'])
                elif maxTempL < float(m['temp_max']):
                    maxTempL = float(m['temp_max'])

        if not minTempL is None and not maxTempL is None:
            value = { "minimum-temperature" : minTempL, "maximum-temperature" : maxTempL }
            self.sendNotification(value)
            print("Send", str(value))

        self.show(True)

    def clear(self, dweek, cnt):
        self.dweek = dweek
        self.temp = []
        self.feelstemp = []
        self.huminidity = []
        self.description = []
        self.icon = []
        self.rain = []
        for i in range(cnt):
            self.temp.append(None)
            self.feelstemp.append(None)
            self.huminidity.append(None)
            self.description.append(None)
            self.icon.append(None)
            self.rain.append(None)
        self.minTemp = [None, None, None, None, None, None]
        self.maxTemp = [None, None, None, None, None, None]
        self.minIdxTemp = [None, None, None, None, None, None]
        self.maxIdxTemp = [None, None, None, None, None, None]


    def add(self, idx, day, temp, feelstemp, temp_min, temp_max, pressure, humidity, description, icon, rainsnow):
        self.temp[int(idx)] = temp
        self.feelstemp[int(idx)] = feelstemp
        self.description[int(idx)] = description
        self.icon[int(idx)] = icon
        self.rain[int(idx)] = rainsnow
        if self.minTemp[day] is None or self.minTemp[day] > temp_min:
            self.minTemp[day] = temp_min
            self.minIdxTemp[day] = idx
        if self.maxTemp[day] is None or self.maxTemp[day] < temp_max:
            self.maxTemp[day] = temp_max
            self.maxIdxTemp[day] = idx
        

    def show(self, data):
        scene = QGraphicsScene()
        #scene.setForegroundBrush(QColor(0, 0, 0))
        #scene.setBackgroundBrush(QColor(255, 255, 255))
        scene.setBackgroundBrush(QColor(0, 0, 0))

        if not data:        
            scene.setFont(self.font)
            t = scene.addText("Brak danych", self.font)
            t.setPos(50,50)
            t.setDefaultTextColor(QColor(255, 255, 255))
            self.oneday_ui.graphicsView.setScene(scene)
            self.oneday_ui.graphicsView.show()
            return

        pen = QPen(QColor(255, 255, 255))
        pen.setWidth(3)

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
                t = scene.addText(self.daysName[int(self.dweek + i/8) % 7], self.font)
                pos = QPointF(self.margin + self.w3h*i, self.height+32)
                t.setDefaultTextColor(QColor(255, 255, 255))
                t.setPos(pos)
        self.oneday_ui.graphicsView.setScene(scene)
        self.oneday_ui.graphicsView.show()
        return
        prev2 = None
        prev = None
        points = []    
        for x in range(len(self.temp)):
            if self.temp[x] is None:
                continue
            pos = QRectF(self.margin + self.w3h*x -1 , (30-self.temp[x]) * self.h1deg +1, 6, 6)  
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




    def _ms2Beaufort(self, ms):
        kmh = ms * 60 * 60 / 1000
        speeds = [1, 7, 12, 20, 30, 40, 51, 63, 76, 88, 103, 117]
        if kmh > 117:
            return 12

        if kmh < speeds[0]:
            return 0

        index = 0
        while kmh > speeds[index]:
            index += 1
        return index-1

    def _deg2Cardinal(self, deg):
        if deg>11.25 and deg<=33.75 : 
            return "NNE"
        elif deg > 33.75 and deg <= 56.25: 
            return "NE"
        elif deg > 56.25 and deg <= 78.75 :
            return "ENE"
        elif deg > 78.75 and deg <= 101.25 :
            return "E"
        elif deg > 101.25 and deg <= 123.75 :
            return "ESE"
        elif deg > 123.75 and deg <= 146.25 :
            return "SE"
        elif deg > 146.25 and deg <= 168.75 :
            return "SSE"
        elif deg > 168.75 and deg <= 191.25 :
            return "S"
        elif deg > 191.25 and deg <= 213.75 :
            return "SSW"
        elif deg > 213.75 and deg <= 236.25 :
            return "SW"
        elif deg > 236.25 and deg <= 258.75 :
            return "WSW"
        elif deg > 258.75 and deg <= 281.25 :
            return "W"
        elif deg > 281.25 and deg <= 303.75 :
            return "WNW"
        elif deg > 303.75 and deg <= 326.25 :
            return "NW"
        elif deg > 326.25 and deg <= 348.75 :
            return "NNW"
        else :
            return "N"

    def _toBeaufortChar(self, b):
        if b == 0: return "\uF0B7"
        elif b == 1: return "\uF0B8"
        elif b == 2: return "\uF0B9"
        elif b == 3: return "\uF0BA"
        elif b == 4: return "\uF0BB"
        elif b == 5: return "\uF0BC"
        elif b == 6: return "\uF0BD"
        elif b == 7: return "\uF0BE"
        elif b == 8: return "\uF0BF"
        elif b == 9: return "\uF0C0"
        elif b == 10: return "\uF0C1"
        elif b == 11: return "\uF0C2"
        elif b == 12: return "\uF0C3"
        else: return "\uF050"
    
    def B2Description(self, b):
        if b == 0: return "Cisza"
        elif b == 1: return "Powiew"
        elif b == 2: return "Słaby wiatr"
        elif b == 3: return "Łagodny wiatr"
        elif b == 4: return "Umiarkowany wiatr"
        elif b == 5: return "Dość silny wiatr"
        elif b == 6: return "Silny wiatr"
        elif b == 7: return "Bardzo silny wiatr"
        elif b == 8: return "Wicher"
        elif b == 9: return "Silny sztorm"
        elif b == 10: return "Bardzo silny sztorm"
        elif b == 11: return "Gwałtowny sztorm"
        elif b == 12: return "Huragan"
        return ""

    def _toDescrSilaWiatru(self, ms):
        b = self._ms2Beaufort(ms)
        ret = "%.1f" % ms
        ret += "m/s (%s)" % self.B2Description(b)
        return ret

    def _isDayTime(self, h, m):
        act = QTime(h, m, 0)
        if act > self.sunrise and act < self.sunset:
            return True
        return False
    

    
    