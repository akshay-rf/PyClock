# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopWatch.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os    
import time


class stopWatch(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 506)
        MainWindow.setMinimumSize(QtCore.QSize(733, 506))
        MainWindow.setMaximumSize(QtCore.QSize(733, 506))
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(116, 130, 511, 91))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(211, 215, 207);")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(115, 270, 521, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"     color: rgb(211, 215, 207);\n"
"    background-color: rgb(85, 87, 83)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color: rgb(37, 37, 37);\n" 
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"     color: rgb(211, 215, 207);\n"
"    background-color: rgb(85, 87, 83)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color: rgb(37, 37, 37);\n" 
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"     color: rgb(211, 215, 207);\n"
"    background-color: rgb(85, 87, 83)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color: rgb(37, 37, 37);\n"        
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 360, 511, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(211, 215, 207);")
        self.label_2.setObjectName("label_2")
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
        
        self.second = 1    
        self.minute = 0    
        self.hour = 0
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.start)

    def start_time(self):
        self.timer.start(1000)
        self.pushButton_2.setText(self._translate("MainWindow", "pause"))
        self.pushButton_2.clicked.connect(self.pause)

    def start(self):                     
        self.time = '%d : %d : %d '%(self.hour,self.minute,self.second)
        self.time = self.time.strip()
        self.label.setText(self._translate("MainWindow", f"{self.time}"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)      
        self.second+=1    
        if(self.second == 60):    
                self.second = 0    
                self.minute+=1    
        if(self.minute == 60):    
                self.minute = 0    
                self.hour+=1;

    def pause(self):
        self.timer.stop()
        self.pushButton_2.setText(self._translate("MainWindow", "start"))
        self.pushButton_2.clicked.connect(self.start_time)        

    def stop(self):
        self.second = 1    
        self.minute = 0    
        self.hour = 0
        self.time = "0 : 0 : 0" 
        self.label.setText(self._translate("MainWindow", f"0 : 0 : 0"))
        self.timer.stop()
        self.label_2.setText(self._translate("MainWindow", ""))
        self.pushButton_2.setText(self._translate("MainWindow", "start"))
        self.pushButton_2.clicked.connect(self.start_time)

    def flag(self):
        self.label_2.setText(self._translate("MainWindow", f"--> {self.time}"))        

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Stop Watch"))
        self.pushButton.setText(self._translate("MainWindow", "flag"))
        self.pushButton_2.setText(self._translate("MainWindow", "start"))
        self.pushButton_4.setText(self._translate("MainWindow", "stop"))
        self.label_2.setText(self._translate("MainWindow", ""))
        self.label.setText(self._translate("MainWindow", f"0 : 0 : 0"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton_2.clicked.connect(self.start_time)
        self.pushButton_4.clicked.connect(self.stop)
        self.pushButton.clicked.connect(self.flag)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = stopWatch()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
