#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import feedparser
import rss_ui
import blackwidget
import random


class RSS(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(RSS, self).__init__(parent)
        self.RSSUi = rss_ui.Ui_RSS()
        self.setupUi(self)
        self.prevH = None
        self.prevM = None
        self.rssSource = ["https://www.polsatnews.pl/rss/wszystkie.xml"]
        self.entries = []

        
    
    def timeout(self, dt):

        hour = dt.time().hour()
        minute = dt.time().minute()
        
        if self.prevH != hour:
            self.prevH = hour
            self.entries = []
            for source in self.rssSource:
                nf = feedparser.parse(source)
                for e in nf.entries:
                    self.entries.append(e)
        
        if self.prevM != minute:
            self.prevM = minute
            cntId = random.randrange(len(self.entries))
            self.RSSUi.title.setText(self.entries[cntId].title)
            self.RSSUi.info.setText(self.entries[cntId].summary)
    

    def getRect(self):
        return QRect(0, 800, 1024, 600)

    
    def setupUi(self, RSS):
        self.RSSUi.setupUi(RSS)
        