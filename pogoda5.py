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
        #QNetworkAccessManager netMng
        self.url = "https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
        self.prevday = None
        self.delaySec = 0
        self.nodata = False
        

    def getRect(self):
        return QRect(0,0,0,0)
    
    def timeout(self, dt):
        if not self.prevday is None or self.prevday == dt.date().day():
            return
        self.prevday = dt.date().day()
        month = dt.date().month()
        year = dt.date().year()
        
        date_time = datetime.datetime(year, month, self.prevday, 0, 0, 0)
        tdt = time.mktime(date_time.timetuple())

        print(tdt)
        offset = dt.offsetFromUtc()

        if self.delaySec > 0:
            self.delaySec -= 1
            return

        response = urlopen(self.url)
        data_json = json.loads(response.read().decode('utf-8'))

        cnt_items = int(data_json["cnt"]) or 0
        if cnt_items == 0:
            print("Brak danych")
            self.delaySec = 60
            show()
            return

        items = data_json["list"]
        if items is None:
            print("Brak danych")
            self.delaySec = 60
            show()
            return
        
        clear(dt.dayOfWeek() - 1, cnt_items + 8)
        self.minTemp = None
        self.maxTemp = None
        self.nodata = True
        for i in items:
            dt_txt = i["dt_txt"]
            if i["dt_txt"] is None:
                continue
            fd,ft = dt_txt.split(' ')
            year,month,day = fd.split('-')
            hour,minute,second = ft.split(':')
            day = int(day)
            idt = int(i['dt'])
            ih = (idt - tdt - offset)/3600
            idx = ih/3

            m = i['main']
            add(idx, day-self.prevday, m['temp'],m['feels_like'],m['temp_min'],m['temp_max'],m['pressure'],m['humidity'])

            if day == self.prevday:
                if self.minTemp is None:
                    self.minTemp = m['temp_min']
                elif self.minTemp > m['temp_min']:
                    self.minTemp = m['temp_min']

                if self.maxTemp is None:
                    self.maxTemp = m['temp_max']
                elif self.maxTemp > m['temp_max']:
                    self.minTemp = m['temp_max']

        if self.minTemp and self.maxTemp:
            value = { "minimum-temperature" : self.minTemp, "maximum-temperature" : self.maxTemp }
            self.sendNotification(value)

        show()

    def clear(self, dweek, cnt):
        self.temp = []
        self.feelstemp = []
        for i in range(cnt):
            self.temp.add(None)
            self.feelstemp.add(None)
        self.minTemp = [None, None, None, None, None, None]
        self.maxTemp = [None, None, None, None, None, None]
        self.minIdxTemp = [None, None, None, None, None, None]
        self.maxIdxTemp = [None, None, None, None, None, None]


    def add(self, idx, day, temp, feelstemp, temp_min, temp_max, pressure, humidity):
        self.temp[idx] = temp
        self.feelstemp[idx] = feelstemp
        if self.minTemp[day] is None or self.minTemp[day] > temp_min:
            self.minTemp[day] = temp_min
            self.minIdxTemp[day] = idx
        if self.minTemp[day] is None or self.minTemp[day] > temp_min:
            self.minTemp[day] = temp_min
            self.minIdxTemp[day] = idx
        

    def show(self):
        pass




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
    

    
    