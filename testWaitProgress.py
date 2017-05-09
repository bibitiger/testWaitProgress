from MyWaitProgressDialog import *
import sys

def setWindowCenter(window):
    '''setWindowCenter(QWidget)'''
    cp = window.frameGeometry()
    lo = QDesktopWidget().availableGeometry().center()
    cp.moveCenter(lo)
    window.move(cp.topLeft())

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        backGround = QWidget(self)
        button = QPushButton('begin wait')
        button.clicked.connect(self.showProgress)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(button)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)

        backGround.setLayout(hbox)

        self.setGeometry(100,100,500,500)
        self.setCentralWidget(backGround)
        self.setWindowTitle('testWaitProgress')

        setWindowCenter(self)
        self.show()

    def showProgress(self, isTrue):
        print('showProgress:{}'.format(isTrue))
        self.timer = QTimer()
        self.timer.timeout.connect(self.timesUp)
        self.timer.start(10*1000)

        self.progress = MyWaitProgressDialog('begin...',self)
        self.progress.RotateStyle = MyRotateProgress.MyRotateProgress.PenStyleNormal
        self.progress.exec()

    def timesUp(self):
        self.progress.close()
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())