#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import blackwidget
import resources

from urllib.request import urlopen
import json

import pogodav2_ui

class Pogodav2(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Pogodav2, self).__init__(parent)
        self.PogodaUi = pogodav2_ui.Ui_Pogoda()
        self.setupUi(self)
        self.firstTime = True

        self.resize(self.getRect().width(), self.getRect().height())
        self.m_h = 0
        self.m_m = 0
        #QNetworkAccessManager netMng
        self.url = "https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
        self.sunrise = None
        self.sunset = None
        self.citiname = ""
        self.pog_h = 0
        self.pog_m = 0
        
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


        self.PogodaUi.tempIcon.setText("\uf055")
        self.PogodaUi.ikonaCisnienia.setText("\uf079")
        self.PogodaUi.ikonaWilgotnosci.setText("\uf07a")
        self.PogodaUi.ikonaWidocznosci.setText("\uf075")
        


        

    def getRect(self):
        return QRect(0,115,300,400)
    
    def timeout(self, dt):
        hour = dt.time().hour()
        min = dt.time().minute()
        sec = dt.time().second()
        if self.firstTime == False and min % 10 != 0 and sec != 0:
            return

        self.firstTime = False

        self.PogodaUi.nazwamiasta.setText(self.citiname)
        self.PogodaUi.czasAktualnoscidanych.setText(self.__getTimeRemaing(hour-self.pog_h, min-self.pog_m))
        
        self.m_h = hour
        self.m_m = min
        #try :
        if 1:
            response = urlopen(self.url)
            data_json = json.loads(response.read().decode('utf-8'))

            self.citiname = data_json["name"]
            utc = data_json["dt"]
            dtw = QDateTime.fromMSecsSinceEpoch(utc*1000).time()
            
            self.pog_h = dtw.hour()
            self.pog_m = dtw.minute()
            self.PogodaUi.czasAktualnoscidanych.setText("Dane aktualne")

            self.sunrise = QDateTime.fromMSecsSinceEpoch(data_json["sys"]["sunrise"]*1000)
            self.sunset = QDateTime.fromMSecsSinceEpoch(data_json["sys"]["sunset"]*1000)
        
            value = { "sunrise" : self.sunrise.time(), "sunset" : self.sunset.time() }
            self.sendNotification(value)

            #emit setSunrise(sunrise.time().hour(), sunrise.time().minute());
            #emit setSunset(sunset.time().hour(), sunset.time().minute());

            wind_speed = data_json["wind"]["speed"]
            wind_deg = data_json["wind"]["deg"]
            self.PogodaUi.ikonawiatru.setText(self._toBeaufortChar(self._ms2Beaufort(wind_speed)))
            self.PogodaUi.kierunekWiatru.setText(self._deg2Cardinal(wind_deg))
            self.PogodaUi.opiswiatru.setText(self._toDescrSilaWiatru(wind_speed))


            temp = data_json["main"]["temp"]
            feels_like = data_json["main"]["feels_like"]

            self.PogodaUi.temperatura.setText("%.1f\u00B0C" % temp)
            self.PogodaUi.temperaturaOdczuwalna.setText("%.1f\u00B0C" % feels_like)



            pressure = data_json["main"]["pressure"]
            huminidity = data_json["main"]["humidity"]
            
            self.PogodaUi.wilgotnosc.setText("%.0f%%" % huminidity)
            self.PogodaUi.cisnienie.setText("%.0f hPa" % pressure)

            #weather_main = data_json["weather"][0]["main"]
            weather_descr = data_json["weather"][0]["description"]
            weather_icon = data_json["weather"][0]["icon"]
            self.PogodaUi.ikonapogody.setText(self.iconMap[weather_icon])
            self.PogodaUi.opisPogody.setText(weather_descr)
            
            self.PogodaUi.widocznosc.setText("%d m" % data_json["visibility"])
            #self.clouds.setText("%d%%" % data_json["clouds"]["all"])

            if "snow" in data_json:
                if "1h" in data_json["snow"]:
                    self.PogodaUi.deszczsnieg.setText("%s" % data_json["snow"]["1h"])
                    self.PogodaUi.etdeszczsnieg.setText("mm/h")
                elif "3h" in data_json["snow"]:
                    self.PogodaUi.deszczsnieg.setText("%s" % data_json["snow"]["3h"])
                    self.PogodaUi.etdeszczsnieg.setText("mm/3h")
            elif "rain" in data_json:
                if "1h" in data_json["rain"]:
                    self.PogodaUi.deszczsnieg.setText("%s" % data_json["rain"]["1h"])
                    self.PogodaUi.etdeszczsnieg.setText("mm/h")
                elif "3h" in data_json["rain"]:
                    self.PogodaUi.deszczsnieg.setText("%s" % data_json["rain"]["3h"])
                    self.PogodaUi.etdeszczsnieg.setText("mm/3h")
            elif "clouds" in data_json:
                self.PogodaUi.deszczsnieg.setText("%s%%" % data_json["clouds"]["all"])
                self.PogodaUi.etdeszczsnieg.setText("")
            else:
                self.PogodaUi.deszczsnieg.setText("")
                self.PogodaUi.etdeszczsnieg.setText("")
        #except:
        else:
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

    def setupUi(self, Pogoda):
        self.PogodaUi.setupUi(Pogoda)
    