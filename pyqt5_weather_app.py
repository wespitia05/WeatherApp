# python pyqt5 weather app

# provides modules used and maintained by the python interpreter
import sys
# used to make requests to an api
import requests
# provides gui components
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
# provides functionality
from PyQt5.QtCore import Qt

# this class inherits from base class QWidget
class WeatherApp(QWidget):
    # initializer for our class, runs after python creates the weather app
    # sets up everything the app needs to work
    def __init__(self):
        # calls the parent class initializer
        super().__init__()

# when running python file directly
if __name__ == "__main__":
    # creates the Qt application and handles any arguments
    app = QApplication(sys.argv)
    # construct our weather app 
    weather_app = WeatherApp()
    # show our weather app 
    weather_app.show()
    # weather app remains visible until exited
    sys.exit(app.exec_())