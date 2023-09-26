import blackwidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import serial
import re



# Step 1: Create a worker class
class Worker(QObject):
    #finished = pyqtSignal()
    #progress = pyqtSignal(int)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.regexp = re.compile(r'^DHT=(?P<lhum>\d+\.{0,1}\d*);(?P<ltemp>\d+\.{0,1}\d*):(?P<key1>[0-9a-f]{16})=(?P<value1>\d+\.{0,1}\d*):(?P<key2>[0-9a-f]{16})=(?P<value2>\d+\.{0,1}\d*)$')
        #DHT=62.5;24.3:286cf90f0b0000ae=34.9:28fff708640400a3=30.7
    
    def setWidget(self, blackwidget):
        self.blackwidget = blackwidget


    def run(self):
        """Long-running task."""
        self.isRun = True
        self.ser = serial.Serial(
            port='/dev/ttyACM0',\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0)
        while self.isRun:
            bline = self.ser.readline()
            if len(bline) == 0:
                #sleep()
                continue
            line = bline.decode('ascii').strip()
            obj = self.regexp.match(line)
            if obj is not None:
                valg = obj.groupdict()
                vals = {}
                vals['lazienka_temp'] = valg['ltemp']
                vals['lazienka_humi'] = valg['lhum']
                vals[valg['key1']] = valg['value1']
                vals[valg['key2']] = valg['value2']
                self.blackwidget.sendNotification(vals)
        self.ser.close()


class SerialReader(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = QThread()
        self.worker = Worker()
        self.worker.setWidget(self)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        #self.worker.finished.connect(self.thread.quit)
        #self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        #self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

    def getRect(self):
        return QRect(1080,1920,0,0)
    
    def timeout(self, dt):
        pass