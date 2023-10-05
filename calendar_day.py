#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import urllib3
from bs4  import BeautifulSoup

import blackwidget
import calendar_day_ui

class CalendarDay(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(CalendarDay, self).__init__(parent)
        self.CalendarDayUi = calendar_day_ui.Ui_CalendarDay()
        self.setupUi(self)
        self.dayCalc = None

        self.days = ["", ("Poniedziałek"),
                ("Wtorek"),
                ("Środa"),
                ("Czwartek"),
                ("Piątek"),
                ("Sobota"),
                ("Niedziela")]        


    
    def timeout(self, dt):


        
        hour = dt.time().hour()
        min = dt.time().minute()
        sec = dt.time().second()
        day = dt.date().day()


        if self.dayCalc is None or self.dayCalc != day:
            if min == 0:
                return
            self.dayCalc = day
            self.CalendarDayUi.dzien.setText(self.days[dt.date().dayOfWeek()])
            self.CalendarDayUi.day.setText("%d" % dt.date().day())
            self.getData()    
        
        secs = int((24 * hour + 60 * min + sec) / 30) % 4
        self.CalendarDayUi.imieniny.setVisible(secs == 0)
        self.CalendarDayUi.przyslowia.setVisible(secs == 1)
        self.CalendarDayUi.cytat.setVisible(secs == 2)
        self.CalendarDayUi.inneSwieta.setVisible(secs == 3)
           
        
    def getData(self):

        http = urllib3.PoolManager()
        r = http.request('GET', 'https://www.kalbi.pl/')
        if r.status != 200:
            pass
        html = r.data
        parsed_html = BeautifulSoup(html, features='html.parser')
        
        swieto = parsed_html.body.find('div', attrs={'class':'calCard-fete'})
        if swieto is None:
            self.CalendarDayUi.swieto.setVisible(False)
        else:
            self.CalendarDayUi.swieto.setVisible(True)
            self.CalendarDayUi.swieto.setText(swieto.text.strip())

        divPrzyslowia = parsed_html.body.find('section', attrs={'class':'calCard_proverb'})
        divCytat = parsed_html.body.find('section', attrs={'class':'calCard-quotes'})
        self.CalendarDayUi.imieniny.setText(parsed_html.body.find('section', attrs={'class':'calCard-name-day'}).text.strip())
        self.CalendarDayUi.przyslowia.setText(divPrzyslowia.find('div', attrs={'class':'calCard_proverb-content'}).text.strip())
        self.CalendarDayUi.cytat.setText(divCytat.find('div', attrs={'class':'calCard_proverb-content'}).text.strip())
        self.CalendarDayUi.inneSwieta.setText(parsed_html.body.find('section', attrs={'class':'calCard-ententa'}).text.strip())

    
    def getRect(self):
        return QRect(300, 115, 380, 400)
    
    def setupUi(self, CalendarDay):
        self.CalendarDayUi.setupUi(CalendarDay)
        
        