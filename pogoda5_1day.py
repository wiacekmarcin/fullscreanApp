#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import feedparser
import pogoda5_1day_ui
import blackwidget



class Pogoda5_1Day(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Pogoda5_1Day, self).__init__(parent)
        self.oneday_ui = pogoda5_1day_ui.Ui_Pogoda5_1Day()
        self.setupUi(self)
        self.prevM = None

    
    def timeout(self, dt):

        hour = dt.time().hour()
        minute = dt.time().minute()
        
        if self.prevM != minute:
            self.prevM = minute
            self.draw()
    

    def getRect(self):
        return QRect(0, 700, 1024, 600)

    
    def setupUi(self, Pogoda5_1Day):
        self.oneday_ui.setupUi(Pogoda5_1Day)
        
    def draw(self):
        s = self.oneday_ui.dayname.setText("Wtorek")

        scene = QGraphicsScene()

        scene.addText("Hello, world!")

        self.oneday_ui.graphicsView.setScene(scene)
        self.oneday_ui.graphicsView.show()
        