from PyQt5.Qt import *

class MyRotateProgress(QWidget):
    PenStyleNormal = 0
    PenStyleGradient = 1
    PenstylePerGradient = 2

    def __init__(self, width, height, parent = None):
        super(MyRotateProgress, self).__init__(parent)
        self.setMinimumSize(width, height)
        self.now = 0;
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.onTime)
        self._timer.start(150)
        self._PenStyle = MyRotateProgress.PenStyleNormal

    def onTime(self):
        self.now += 1
        self.now = 0 if self.now >= 10 else self.now
        self.update()

    def paintEvent(self, QPaintEvent):
        super(MyRotateProgress, self).paintEvent(QPaintEvent)
        painter = QPainter(self)
        # 反走样，边缘平滑
        painter.setRenderHint(QPainter.Antialiasing, True)
        #radius取最小边长
        radius = self.width() if self.width() < self.height() else self.height()
        if radius <= 0:
            return
        radius = radius/6
        # 将圆等分为10份，分别画出10条线
        per = 360/10;
        painter.translate(self.width()/2, self.height()/2)
        for i in range(10):
            painter.save()
            painter.setPen(self.getPenStyle(self._PenStyle, i))
            painter.rotate(per*i)
            painter.drawLine(QPoint(0, 0 + radius), QPoint(0, 0 + radius*2))
            painter.restore()

    def getPenStyle(self, PenStyle, PenPoint):
        radius = self.width() if self.width() < self.height() else self.height()
        if radius <= 0:
            return
        radius = radius / 6

        if PenStyle == MyRotateProgress.PenStyleNormal:
            if PenPoint == self.now:
                return QPen(Qt.white, 3)
            else:
                return QPen(Qt.black, 3)
        elif PenStyle == MyRotateProgress.PenStyleGradient:
            point = PenPoint-self.now if PenPoint-self.now >= 0 else 10+PenPoint-self.now
            return QPen(QColor(255*point/10, 255*point/10,255*point/10), 3)
        elif PenStyle == MyRotateProgress.PenstylePerGradient:
            if PenPoint == self.now:
                gradient = QRadialGradient(0,radius, radius, 0, radius)
                gradient.setColorAt(0.2,Qt.white)
                gradient.setColorAt(0.6,Qt.gray)
                return QPen(gradient, 3)
            else:
                gradient = QRadialGradient(0,radius, radius, 0, radius)
                gradient.setColorAt(0.2,Qt.gray)
                gradient.setColorAt(0.6,Qt.black)
                return QPen(gradient, 3)

    def closeEvent(self, QCloseEvent):
        if self._timer.isActive():
            self._timer.stop()

    def hideEvent(self, QHideEvent):
        if self._timer.isActive():
            self._timer.stop()

    def showEvent(self, QShowEvent):
        if self._timer.isActive() != True:
            self._timer.start()

    @property
    def PenStyle(self):
        return self._PenStyle

    @PenStyle.setter
    def PenStyle(self, Value):
        self._PenStyle = Value
        self.update()