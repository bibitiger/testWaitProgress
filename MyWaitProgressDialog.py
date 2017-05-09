from PyQt5.Qt import *
import  MyRotateProgress

class MyWaitProgressDialog(QDialog):
    '''MyWaitProgressDialog(string,QWidget)'''

    def __init__(self, value, targetWindow):
        super(MyWaitProgressDialog, self).__init__()
        self.decTile = QLabel()
        self.decTile.setAlignment(Qt.AlignHCenter)
        self.Dec = value
        self._targetWindow = targetWindow
        self._rotate = MyRotateProgress.MyRotateProgress(80,80)
        self._rotate.PenStyle = MyRotateProgress.MyRotateProgress.PenStyleNormal
        self._rotate.setAutoFillBackground(True)
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignHCenter)
        vbox.addStretch(1)
        vbox.addWidget(self._rotate)
        vbox.addWidget(self.decTile)
        vbox.addStretch(1)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self._oldTargetFlags = self._targetWindow.windowFlags()

        self.setLayout(hbox)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setGeometry(targetWindow.geometry())
        self.setWindowOpacity(0.8)

    @property
    def Dec(self):
        return self._dec

    @Dec.setter
    def Dec(self, value):
        assert isinstance(value, str), "value %r not match %s" (value, QUrl)
        self._dec = value
        self.decTile.setText(value)

    @property
    def RotateStyle(self):
        return self._rotate.PenStyle

    @RotateStyle.setter
    def RotateStyle(self, value):
        self._rotate.PenStyle = value

    def closeEvent(self, QCloseEvent):
        self._targetWindow.setWindowFlags(self._oldTargetFlags)

    def paintEvent(self, QPaintEvent):
        print('paint Event')
