from PyQt5 import QtCore, QtGui, QtWidgets
from clock import Clock
from stopWatch import stopWatch
from timer import timer

class Ui_MainWindow(object):
    def Tmer(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = timer()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def sWatch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = stopWatch()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def clock(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Clock()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(733, 506)
        MainWindow.setMinimumSize(QtCore.QSize(733, 506))
        MainWindow.setMaximumSize(QtCore.QSize(733, 506))
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 90, 331, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(211, 215, 207);\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: rgb(211, 215, 207);\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: rgb(211, 215, 207);\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clock"))
        self.pushButton.setText(_translate("MainWindow", "Clock"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop Watch"))
        self.pushButton_3.setText(_translate("MainWindow", "Timer"))

        self.pushButton.clicked.connect(self.clock)
        self.pushButton_2.clicked.connect(self.sWatch)
        self.pushButton_3.clicked.connect(self.Tmer)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
