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


class Pogoda5():
    def __init__(self):
        self.url = "https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
        self.prevday = None
        self.delaySec = 0
        self.nodata = False
        self.minTemp = [None, None, None, None, None, None, None]
        self.maxTemp = [None, None, None, None, None, None, None]
    
        self.w3h = 25
        self.h1deg = 10
        self.maxRange = 30
        self.minRange = 10
        self.height = 300
        self.margin = int((1080-(8*5*self.w3h)) / 2)

        dt = datetime.datetime.now()
        tdt = time.mktime(dt.timetuple())
        offset = 7200
        self.prevday = dt.date().day
        self.daysName = [u'Niedziela',u'Poniedziałek',u'Wtorek',u'Środa',u'Czwartek',u'Piatek',u'Sobota']


        response = urlopen(self.url)
        data_json = json.loads(response.read().decode('utf-8'))

        cnt_items = int(data_json["cnt"]) or 0
        if cnt_items == 0:
            print("Brak danych")
            self.delaySec = 60
            self.show()
            return

        items = data_json["list"]
        if items is None:
            print("Brak danych")
            self.delaySec = 60
            self.show()
            return
        
        self.clear(dt.date().weekday, cnt_items + 8)
    
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
            #print("idt", idt, "tdt", tdt, "idt - tdt",(idt - tdt), "idt - tdt - offset", (idt - tdt - offset),"ih", ih)
            #idx = ih/3
            idx = (day-self.prevday)*8+int(int(hour)/3)

            m = i['main']
            self.add(idx, day-self.prevday, m['temp'],m['feels_like'],m['temp_min'],m['temp_max'],m['pressure'],m['humidity'])

            print("d",day, "h",hour, m['temp_min'], m['temp_max'])
            if int(day) == int(self.prevday) or ((int(day)-1 == int(self.prevday)) and (int(hour) == 0)):
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
            print("Send", str(value))

        self.show()

    def clear(self, dweek, cnt):
        self.temp = []
        self.feelstemp = []
        for i in range(cnt):
            self.temp.append(None)
            self.feelstemp.append(None)
        self.minTemp = [None, None, None, None, None, None]
        self.maxTemp = [None, None, None, None, None, None]
        self.minIdxTemp = [None, None, None, None, None, None]
        self.maxIdxTemp = [None, None, None, None, None, None]


    def add(self, idx, day, temp, feelstemp, temp_min, temp_max, pressure, humidity):
        self.temp[int(idx)] = temp
        self.feelstemp[int(idx)] = feelstemp
        if self.minTemp[day] is None or self.minTemp[day] > temp_min:
            self.minTemp[day] = temp_min
            self.minIdxTemp[day] = idx
        if self.maxTemp[day] is None or self.maxTemp[day] < temp_max:
            self.maxTemp[day] = temp_max
            self.maxIdxTemp[day] = idx
        

    def show(self):
        print("minT", self.minTemp)
        print("minT[]", self.minIdxTemp)
        print("maxT", self.maxTemp)
        print("maxT[]", self.maxIdxTemp)
        print("temp",self.temp)
        

p = Pogoda5()