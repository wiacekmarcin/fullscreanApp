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
        self.parse = False
        
    
    def timeout(self, dt):
        #monthname = self.monts[dt.date().month()];
        #dayname = self.days[dt.date().dayOfWeek()];

        #self.ZegarUi.ldate.setText("%s, %d %s %d" % (dayname, dt.date().day(), monthname, dt.date().year()))

        hour = dt.time().hour()
        min = dt.time().minute()
        sec = dt.time().second()

        if self.parse:
            return
        
        self.parse = True
        
        http = urllib3.PoolManager()
        r = http.request('GET', 'https://www.kalbi.pl/')
        if r.status != 200:
            pass
        html = r.data
        parsed_html = BeautifulSoup(html, features='html.parser')
        self.CalendarDayUi.rok.setText(parsed_html.body.find('div', attrs={'class':'calCard-year'}).text.strip())
        self.CalendarDayUi.dzienRoku.setText(parsed_html.body.find('div', attrs={'class':'calCard-dayyear'}).text.strip().replace("roku", ""))
        self.CalendarDayUi.tydzienRoku.setText(parsed_html.body.find('div', attrs={'class':'calCard-week'}).text.strip().replace("roku", ""))
        self.CalendarDayUi.month.setText(parsed_html.body.find('div', attrs={'class':'calCard-month'}).text.strip())
        self.CalendarDayUi.dzien.setText(parsed_html.body.find('div', attrs={'class':'calCard-day'}).text.strip())
        
        swieto = parsed_html.body.find('div', attrs={'class':'calCard-fete'})
        if swieto is None:
            self.CalendarDayUi.swieto.setVisible(False)
        else:
            self.CalendarDayUi.swieto.setVisible(True)
            self.CalendarDayUi.swieto.setText(swieto.text.strip())

                
        self.CalendarDayUi.imieniny.setText(parsed_html.body.find('section', attrs={'class':'calCard-name-day'}).text.strip())
        #self.CalendarDayUi.przyslowia.setText(parsed_html.body.find('div', attrs={'class':'calCard_proverb-content'}).text.strip())
        #self.CalendarDayUi.inne_swieta.setText(parsed_html.body.find('section', attrs={'class':'calCard-ententa'}).text.strip())

    def getRect(self):
        return QRect(400, 0, 280, 500)

    
    def setupUi(self, CalendarDay):
        self.CalendarDayUi.setupUi(CalendarDay)
        pass
        