#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

class Pogoda(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Pogoda, self).__init__(parent)
        self.m_h = 0
        self.m_m = 0
        #QNetworkAccessManager netMng
        self.url = "https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
        self.sunrise = None
        self.sunset = None

        self.windB = None
        self.windD = None
        self.windS = None
        self.wIcon = None
        self.wTemp = None
        self.wTempMin = None
        self.wTempMax = None
        self.citydate = None
        self.feelTemp = None
        self.maxTemp = None
        self.minTemp = None
        self.wCond = None
        self.humiTemp = None
        self.presTemp = None

        self.citiname = ""
        self.pog_h = 0
        self.pog_m = 0

        self.weatherFont = None
        self.windDescr = None
        self.tempFont = None

        self.iconMap = None
        self.firstTime = True

        idf = QFontDatabase.addApplicationFont(":/font/fonts/weathericons-regular-webfont.ttf")
        family = QFontDatabase.applicationFontFamilies(idf)[0]
        self.weatherFont = QFont(family)
        self.weatherFont.setPointSize(32)

        idf = QFontDatabase.addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-Light.ttf")
        family = QFontDatabase.applicationFontFamilies(idf)[0]
        self.windDescr = QFont(family)

        idf = QFontDatabase.addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-Regular.ttf")
        family = QFontDatabase.applicationFontFamilies(idf)[0]
        self.tempFont = QFont(family)

        self.m_h = self.m_m = self.pog_h = self.pog_m = -1
        self.citiname = "Nieznane"
        #connect(&netMng, SIGNAL(finished(QNetworkReply*)), this, SLOT(parseMessage(QNetworkReply*)))

        self.iconMap = {}
        self.iconMap["01d"]="\uf00d" #"wi-day-sunny",
        self.iconMap["02d"]="\uf002" #"wi-day-cloudy",
        self.iconMap["03d"]="\uf013" #"wi-cloudy",
        self.iconMap["04d"]="\uf012" #"wi-cloudy-windy",
        self.iconMap["09d"]="\uf01a" #"wi-showers",
        self.iconMap["10d"]="\uf019" #"wi-rain",
        self.iconMap["11d"]="\uf01e" #"wi-thunderstorm",
        self.iconMap["13d"]="\uf01b" #"wi-snow",
        self.iconMap["50d"]="\uf014" #"wi-fog",
        self.iconMap["01n"]="\uf02e" #"wi-night-clear",
        self.iconMap["02n"]="\uf031" #"wi-night-cloudy",
        self.iconMap["03n"]="\uf031" #"wi-night-cloudy",
        self.iconMap["04n"]="\uf031" #"wi-night-cloudy",
        self.iconMap["09n"]="\uf037" #"wi-night-showers",
        self.iconMap["10n"]="\uf036" #"wi-night-rain",
        self.iconMap["11n"]="\uf03b" #"wi-night-thunderstorm",
        self.iconMap["13n"]="\uf038" #"wi-night-snow",
        self.iconMap["50n"]="\uf023" #"wi-night-alt-cloudy-windy"

        self.citydate = QLabel(self)
        self.citydate.setObjectName("citydate")
        self.citydate.setGeometry(QRect(0, 0, 300, 40))
        self.citydate.setStyleSheet(citiStyle)
        self.citydate.setTextFormat(Qt.RichText)

        line = QFrame(self)
        line.setObjectName("line")
        line.setGeometry(QRect(0, 42, 300, 15))
        line.setStyleSheet("color:rgb(145, 148, 148); size:5pt;")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        self.windB = QLabel(self)
        self.windB.setObjectName("windB")
        self.windB.setGeometry(QRect(0, 60, 60, 48))
        self.windB.setStyleSheet(windBStyle)
        self.windB.setFont(self.weatherFont)

        self.windD = QLabel(self)
        self.windD.setObjectName("windD")
        self.windD.setGeometry(QRect(60, 60, 75, 48))
        self.windD.setStyleSheet(windDStyle)

        self.windS = QLabel(self)
        self.windS.setObjectName("windS")
        self.windS.setGeometry(QRect(135, 50, 165, 60))
        self.windS.setWordWrap(True)
        self.windS.setStyleSheet(windSStyle)
        self.windS.setFont(self.windDescr)

        self.wIcon = QLabel(self)
        self.wIcon.setObjectName("wIcon")
        self.wIcon.setGeometry(QRect(0, 110, 115, 60))
        self.wIcon.setStyleSheet(iconWiStyle)
        self.wIcon.setFont(self.weatherFont)

        self.wTemp = QLabel(self)
        self.wTemp.setObjectName("wTemp")
        self.wTemp.setGeometry(QRect(120, 110, 165, 60))
        self.wTemp.setStyleSheet(iconWiStyle)
        self.wTemp.setFont(self.tempFont)

        self.wCond = QLabel(self)
        self.wCond.setObjectName("lwcond")
        self.wCond.setGeometry(QRect(0, 170, 300, 30))
        self.wCond.setStyleSheet(conditionalStyle)
        self.wCond.setFont(self.tempFont)

        label_1 = QLabel(self)
        label_1.setObjectName("lfeelTemp")
        label_1.setGeometry(QRect(0, 200, 165, 30))
        label_1.setText("Odczuwalna")
        label_1.setStyleSheet(feelTempStyle)
        label_1.setFont(self.tempFont)

        self.feelTemp = QLabel(self)
        self.feelTemp.setObjectName("feelTemp")
        self.feelTemp.setGeometry(QRect(170, 200, 165, 30))
        self.feelTemp.setStyleSheet(feelTempStyle)
        self.feelTemp.setFont(self.tempFont)

        label_2 = QLabel(self)
        label_2.setObjectName("lhumiTemp")
        label_2.setGeometry(QRect(250, 110, 65, 35))
        label_2.setText("\uf07a")
        label_2.setStyleSheet(feelTempStyle)
        label_2.setFont(self.weatherFont)

        self.humiTemp = QLabel(self)
        self.humiTemp.setObjectName("humiTemp")
        self.humiTemp.setGeometry(QRect(280, 110, 30, 30))
        self.humiTemp.setStyleSheet(feelTempStyle)
        self.humiTemp.setFont(self.tempFont)

        presLabel1 = QLabel(self)
        presLabel1.setObjectName("presL1")
        presLabel1.setGeometry(QRect(250, 150, 30, 30))
        presLabel1.setStyleSheet(feelTempStyle)
        presLabel1.setFont(self.weatherFont)
        presLabel1.setText("\uf079")

        self.presTemp = QLabel(self)
        self.presTemp.setObjectName("presTemp")
        self.presTemp.setGeometry(QRect(250, 180, 70, 30))
        self.presTemp.setStyleSheet(feelTempStyle)
        self.presTemp.setFont(self.tempFont)

        presLabel2 = QLabel(self)
        presLabel2.setObjectName("presL2")
        presLabel2.setGeometry(QRect(250, 210, 70, 30))
        presLabel2.setStyleSheet(windSStyle)
        presLabel2.setFont(self.weatherFont)
        presLabel2.setText("kPa")
        presLabel2.setAlignment(Qt.AlignRight)
        

    def getRect(self):
        return QRect(0,180,400,300)
    
    def timeout(self, dt):
        if not self.firstTime and dt.time().second() == 0:
            self.citydate.setText("%s <span style=\"font-size:15px;color:#666\">Dane sprzed %s</span>" % (self.citiname, 
                        self.__getTimeRemaing(dt.time().hour()-self.pog_h, dt.time().minute()-self.pog_m)))
        aMin = dt.time().hour()*60 + dt.time().minute()
        if not self.firstTime and aMin % 5 != 0:
            return;
        self.firstTime = False

        self.m_h = dt.time().hour()
        self.m_m = dt.time().minute()
        response = urlopen(self.url)
        data_json = json.loads(response.read().decode('utf-8'))

        self.citiname = data_json["name"]
        utc = data_json["dt"]
        dtw = QDateTime.fromMSecsSinceEpoch(utc*1000).time()
        
        self.pog_h = dtw.hour()
        self.pog_m = dtw.minute()
        self.citydate.setText("%s <span style=\"font-size:15px;color:#666\">Dane aktualne</span>" % (self.citiname))


        self.sunrise = QDateTime.fromMSecsSinceEpoch(data_json["sys"]["sunrise"]*1000)
        self.sunset = QDateTime.fromMSecsSinceEpoch(data_json["sys"]["sunset"]*1000)
    
        value = { "sunrise" : self.sunrise.time(), "sunset" : self.sunset.time() }
        self.sendNotification(value)

        #emit setSunrise(sunrise.time().hour(), sunrise.time().minute());
        #emit setSunset(sunset.time().hour(), sunset.time().minute());

        wind_speed = data_json["wind"]["speed"]
        wind_deg = data_json["wind"]["deg"]
        self.windB.setText(self._toBeaufortChar(self._ms2Beaufort(wind_speed)))
        self.windD.setText(self._deg2Cardinal(wind_deg))
        self.windS.setText(self._toDescrSilaWiatru(wind_speed))


        temp = data_json["main"]["temp"]
        feels_like = data_json["main"]["feels_like"]
        self.wTemp.setText("%.1f\u00B0" % temp)
        self.feelTemp.setText("%.1f\u00B0" % feels_like)

        pressure = data_json["main"]["pressure"]
        huminidity = data_json["main"]["humidity"]
        self.humiTemp.setText("%.0f" % huminidity)
        self.presTemp.setText("%.0f" % pressure)

        weather_main = data_json["weather"][0]["main"]
        weather_descr = data_json["weather"][0]["description"]
        weather_icon = data_json["weather"][0]["icon"]
        self.wIcon.setText(self.iconMap[weather_icon])
        self.wCond.setText(weather_descr);



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
    

    def __getTimeRemaing(self, h, m):
        if m < 0:
            h = h - 1
            m += 60
        
        if h < 0:
            h += 24

        if h == 0 and m < 30:
            return "%d min" % m
        else:
            hal = 1.0*h + m/60.0
            h10 = int(10*hal + 5)
            return "%d.%d godz" % (int(h10/10), int(h10) % 10)


    