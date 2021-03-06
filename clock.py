# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Clock(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 506)
        MainWindow.setMinimumSize(QtCore.QSize(733, 506))
        MainWindow.setMaximumSize(QtCore.QSize(733, 506))
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(50, 80, 641, 171))
        font = QtGui.QFont()
        font.setPointSize(90)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setStyleSheet("color: rgb(211, 215, 207);")
        self.TimeLabel.setObjectName("TimeLabel")
        self.DateLabel = QtWidgets.QLabel(self.centralwidget)
        self.DateLabel.setGeometry(QtCore.QRect(210, 310, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DateLabel.setFont(font)
        self.DateLabel.setStyleSheet("color: rgb(211, 215, 207);")
        self.DateLabel.setObjectName("DateLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Translate(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        timer = QtCore.QTimer(MainWindow)
        timer.timeout.connect(self.display_time)
        timer.start(1000)

    def display_time(self):
        currentTime = QtCore.QTime.currentTime()
        display_text = currentTime.toString('hh:mm:ss')
        hour = display_text[0:2]
        minute = display_text[3:5]
        seconds = display_text[6:]
        pd = "am"
        if int(hour) > 12:
            hour = int(hour) - 12
            pd = "pm"
        d_time = f"{hour}:{minute}:{seconds} {pd}"
        self.TimeLabel.setText(d_time)
        self.TimeLabel.setAlignment(QtCore.Qt.AlignCenter)

        currentDate = QtCore.QDate.currentDate()
        d = currentDate.toString()
               
        self.DateLabel.setText(f"{d}")
        self.DateLabel.setAlignment(QtCore.Qt.AlignCenter)

    def Translate(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Clock()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
