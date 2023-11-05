#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import blackwidget
import resources

from urllib.request import urlopen
import json





citiStyle = "font-size:30px;color:#999;text-align:left;background:#000"
windBStyle = "font-size:45px;color:#aaa;text-align:left;background:#000"
windDStyle = "font-size:25px;color:#999;text-align:left;background:#000"
windSStyle = "font-size:18px;color:#999;text-align:left;background:#000"
iconWiStyle = "font-size:65px;color:#aaa;text-align:right;background:#000"
humiTempStyle = "font-size:36px;color:#ccc;text-align:right;background:#000"
feelTempStyle = "font-size:32px;color:#aaa;text-align:right;background:#000"
conditionalStyle = "font-size:22px;color:#ccc;text-align:right;background:#000"
otherCondStyle = "font-size:22px;color:#666;text-align:right;background:#000"

class Pogoda(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Pogoda, self).__init__(parent)
        self.resize(self.getRect().width(), self.getRect().height())
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
        self.pressure = None
        self.visibility = None
        self.clouds = None

        self.citiname = ""
        self.pog_h = 0
        self.pog_m = 0

        self.weatherFont = None
        self.windDescr = None
        self.tempFont = None

        self.iconMap = None
        self.firstTime = True

        self.weatherFont = self.getFont("Weathericons", 32)
        self.windDescr = self.getFont("Roboto-Condensed", 32, "Light")
        self.tempFont = self.getFont("Roboto-Condensed", 32, "Regular")

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

        #self.citydate = QLabel(self)
        #self.citydate.setObjectName("citydate")
        #self.citydate.setGeometry(QRect(0, 0, self.width(), 40))
        #self.citydate.setStyleSheet(citiStyle)
        #self.citydate.setTextFormat(Qt.RichText)

        actHLevel = 40
        line = QFrame(self)
        line.setObjectName("line")
        line.setGeometry(QRect(0, actHLevel, self.width(), 15))
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Plain)
        line.setLineWidth(2)
        line.setStyleSheet("%s;background-color:rgb(0,0,0);" % self.getStyleColor(50))
        actHLevel += 15 

        self.windB = QLabel(self)
        self.windB.setObjectName("windB")
        self.windB.setGeometry(QRect(0, actHLevel, 60, 48))
        self.windB.setStyleSheet(windBStyle)
        self.windB.setFont(self.weatherFont)

        self.windD = QLabel(self)
        self.windD.setObjectName("windD")
        self.windD.setGeometry(QRect(self.windB.size().width(), actHLevel, 75, 48))
        self.windD.setStyleSheet(windDStyle)

        self.windS = QLabel(self)
        self.windS.setObjectName("windS")
        self.windS.setGeometry(QRect(self.windB.size().width()+self.windD.size().width(),
                                     actHLevel, 
                                     self.width()-self.windD.size().width()-self.windB.size().width(), 60))
        self.windS.setWordWrap(True)
        self.windS.setStyleSheet(windSStyle)
        self.windS.setFont(self.windDescr)
        actHLevel += 60

        self.wIcon = QLabel(self)
        self.wIcon.setObjectName("wIcon")
        self.wIcon.setStyleSheet(iconWiStyle)
        self.wIcon.setFont(self.weatherFont)
        self.wIcon.setGeometry(QRect(0, actHLevel, 100, 100))
        self.wIcon.setText(" ")

        self.wTemp = QLabel(self)
        self.wTemp.setObjectName("wTemp")
        self.wTemp.setGeometry(QRect(self.wIcon.geometry().right(), actHLevel, 320-self.wIcon.geometry().right(), 60))
        self.wTemp.setStyleSheet(iconWiStyle)
        self.wTemp.setFont(self.tempFont)

        tempActHLevel = self.wTemp.geometry().bottom()

        label_H = QLabel(self)
        label_H.setObjectName("lhumiTemp")
        label_H.setGeometry(QRect(self.wIcon.geometry().right(), tempActHLevel+5, 35, 35))
        label_H.setText("\uf07a")
        label_H.setStyleSheet(feelTempStyle)
        label_H.setFont(self.weatherFont)

        self.humiTemp = QLabel(self)
        self.humiTemp.setObjectName("humiTemp")
        self.humiTemp.setGeometry(QRect(label_H.geometry().right(), tempActHLevel+5, 60, 35))
        self.humiTemp.setStyleSheet(humiTempStyle)
        self.humiTemp.setFont(self.tempFont)
        actHLevel += self.wIcon.geometry().height()

        self.wCond = QLabel(self)
        self.wCond.setObjectName("lwcond")
        self.wCond.setGeometry(QRect(0, actHLevel, self.width(), 30))
        self.wCond.setStyleSheet(conditionalStyle)
        self.wCond.setFont(self.tempFont)
        actHLevel += self.wCond.geometry().height()
                
        #self.pressure = QLabel(self)
        #self.pressure.setObjectName("pressure")
        #self.pressure.setGeometry(QRect(200, tempActHLevel, 100, 50))
        #self.pressure.setStyleSheet(feelTempStyle)
        #self.pressure.setFont(self.tempFont)
        


        label_1 = QLabel(self)
        label_1.setObjectName("lfeelTemp")
        label_1.setGeometry(QRect(0, actHLevel, 165, 30))
        label_1.setText("Odczuwalna")
        label_1.setStyleSheet(feelTempStyle)
        label_1.setFont(self.tempFont)

        self.feelTemp = QLabel(self)
        self.feelTemp.setObjectName("feelTemp")
        self.feelTemp.setGeometry(QRect(label_1.geometry().right(), actHLevel, 165, 30))
        self.feelTemp.setStyleSheet(feelTempStyle)
        self.feelTemp.setFont(self.tempFont)
        actHLevel = self.feelTemp.geometry().bottom()

        label_P = QLabel(self)
        label_P.setObjectName("lpressure")
        label_P.setGeometry(QRect(0, actHLevel, 165, 30))
        label_P.setText("Ciśnienie")
        label_P.setStyleSheet(otherCondStyle)
        label_P.setFont(self.tempFont)

        self.pressure = QLabel(self)
        self.pressure.setObjectName("pressure")
        self.pressure.setGeometry(QRect(label_P.geometry().right(), actHLevel, 155, 30))
        self.pressure.setStyleSheet(otherCondStyle)
        self.pressure.setFont(self.tempFont)
        self.pressure.setTextFormat(Qt.RichText)
        actHLevel = self.pressure.geometry().bottom()

        label_V = QLabel(self)
        label_V.setObjectName("lvisibility")
        label_V.setGeometry(QRect(0, actHLevel, 165, 30))
        label_V.setText("Widoczność")
        label_V.setStyleSheet(otherCondStyle)
        label_V.setFont(self.tempFont)

        self.visibility = QLabel(self)
        self.visibility.setObjectName("visibility")
        self.visibility.setGeometry(QRect(label_V.geometry().right(), actHLevel, 155, 30))
        self.visibility.setStyleSheet(otherCondStyle)
        self.visibility.setFont(self.tempFont)
        actHLevel = self.visibility.geometry().bottom()

        label_C = QLabel(self)
        label_C.setObjectName("lzachmurzenie")
        label_C.setGeometry(QRect(0, actHLevel, 165, 30))
        label_C.setText("Zachmurzenie")
        label_C.setStyleSheet(otherCondStyle)
        label_C.setFont(self.tempFont)

        self.clouds = QLabel(self)
        self.clouds.setObjectName("clouds")
        self.clouds.setGeometry(QRect(label_C.geometry().right(), actHLevel, 155, 30))
        self.clouds.setStyleSheet(otherCondStyle)
        self.clouds.setFont(self.tempFont)




        

    def getRect(self):
        return QRect(0,115,300,400)
    
    def timeout(self, dt):
        #if not self.firstTime and dt.time().second() == 0:
            #self.citydate.setText("%s <span style=\"font-size:15px;color:#666\">Dane sprzed %s</span>" % (self.citiname, 
            #            self.__getTimeRemaing(dt.time().hour()-self.pog_h, dt.time().minute()-self.pog_m)))
        aMin = dt.time().hour()*60 + dt.time().minute()
        if not self.firstTime and aMin % 5 != 0:
            return;
        self.firstTime = False

        self.m_h = dt.time().hour()
        self.m_m = dt.time().minute()
        #try :
        if 1:
            response = urlopen(self.url)
            data_json = json.loads(response.read().decode('utf-8'))

            self.citiname = data_json["name"]
            utc = data_json["dt"]
            dtw = QDateTime.fromMSecsSinceEpoch(utc*1000).time()
            
            self.pog_h = dtw.hour()
            self.pog_m = dtw.minute()
            #self.citydate.setText("%s <span style=\"font-size:15px;color:#666\">Dane aktualne</span>" % (self.citiname))


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
            self.wTemp.setText("%.1f\u00B0C" % temp)
            self.feelTemp.setText("%.1f\u00B0C" % feels_like)

            pressure = data_json["main"]["pressure"]
            huminidity = data_json["main"]["humidity"]
            self.humiTemp.setText("%.0f%%" % huminidity)
            self.pressure.setText("%.0f hPa" % pressure)

            weather_main = data_json["weather"][0]["main"]
            weather_descr = data_json["weather"][0]["description"]
            weather_icon = data_json["weather"][0]["icon"]
            self.wIcon.setText(self.iconMap[weather_icon])
            self.wCond.setText(weather_descr)
            self.clouds.setText("%d%%" % data_json["clouds"]["all"])
            self.visibility.setText("%d m" % data_json["visibility"])
        #except:
        else:
            self.wIcon.setText(" ")
            #self.citiname = "Piastów"
            #self.citydate.setText("%s <span style=\"font-size:15px;color:#666\">Brak danych</span>" % (self.citiname))
            self.windB.setText("--")
            self.windD.setText("--")
            self.windS.setText("--")
            self.wCond.setText("--")
            self.wTemp.setText("--")
            self.feelTemp.setText("--")
            self.visibility.setText("--")
            self.clouds.setText("--")
            self.humiTemp.setText("--")
            self.pressure.setText("--")


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


    