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
        self.firstTime = True

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


        if self.firstTime:
            self.CalendarDayUi.dzien.setText(self.days[dt.date().dayOfWeek()])
            self.CalendarDayUi.day.setText("%d" % dt.date().day())
            self.getData()    
            self.firstTime = False
            return
        if hour == 0 and min == 0 and sec == 0:
            self.CalendarDayUi.dzien.setText(self.days[dt.date().dayOfWeek()])
            self.CalendarDayUi.day.setText("%d" % dt.date().day())
            self.getData()    
        
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

        cytat = parsed_html.body.find('div', attrs={'class':'calCard_proverb-content'}).text.strip()
        self.CalendarDayUi.imieniny.setText(parsed_html.body.find('section', attrs={'class':'calCard-name-day'}).text.strip())
        #self.CalendarDayUi.przyslowia.setText(parsed_html.body.find('div', attrs={'class':'calCard_proverb-content'}).text.strip())
        self.CalendarDayUi.inneSwieta.setText(parsed_html.body.find('section', attrs={'class':'calCard-ententa'}).text.strip())

    
    def getRect(self):
        return QRect(300, 115, 380, 400)
    
    def setupUi(self, CalendarDay):
        self.CalendarDayUi.setupUi(CalendarDay)
        
        