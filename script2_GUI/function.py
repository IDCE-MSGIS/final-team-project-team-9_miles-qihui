"""
The GUI and its functions need to be runin Python 3.4 or higher as there is no support in Python2 
for PyQT 5 and the packages that we need.
"""

import json
import os
import sys
import requests
from PyQt5 import QtWidgets
from weather_test import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # create an instance for lineEdit
        self.lineEdit = QLineEdit(self)
        # create button push event
        self.pushButton.clicked.connect(self.update_weather)

        #show the window
        self.show()



    #update label text depending on user input
    def  update_weather(self):
        test = self.lineEdit.text()
        # give a test value to test the whether or not the lineEdit can get user input
        # when lineEdit get the user input value
        if test==1:
            weather = {
                "wind": {"speed": 1.5, "deg": 350},
                "main": {
                    "temp": 296.71,
                    "pressure": 1013,
                    "humidity": 53,
                    "temp_min": 294.82,
                    "temp_max": 298.71
                },
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
            }
        # when lineEdit doesn't get the answer
        else:
            weather = {
                "wind": {"speed": 0, "deg": 0},
                "main": {
                    "temp": 0,
                    "pressure": 0,
                    "humidity": 0,
                    "temp_min": 0,
                    "temp_max": 0
                },
                "weather": [
                    {
                        "id": 0,
                        "main": "0",
                        "description": "0",
                        "icon": "01d"
                    }
                ],
            }
        self.label_6.setText("%.2f m/s" % weather['wind']['speed'])
        #choose whether the temperature dispaly in °F or in °C
        if self.radioButton_2.ischecked():
            n= "%.1f °F"
        else:
            n= "%.1f °C"
        self.label_7.setText(n % weather['main']['temp'])
        self.label_3.setText("%d" % weather['main']['humidity'])
        self.weatherLabel.setText("%s (%s)" % (
            weather['weather'][0]['main'],
            weather['weather'][0]['description']
        )
                                  )

# call the class
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
