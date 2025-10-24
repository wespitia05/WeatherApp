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
        # label prompts user to enter name of city
        self.city_label = QLabel("Enter city name: ", self)
        # input box that allows user to type name of city
        self.city_input = QLineEdit(self)
        # button to retrieve weather info
        self.get_weather_button = QPushButton("Get Weather", self)
        # temperature lable will display temperature of city
        self.temp_label = QLabel("40°F, self")
        # emoji label will show type of weather
        self.emoji_label = QLabel("🌤️", self)
        # brief description of type of weather
        self.description_label = QLabel("Partly Sunny", self)
        self.initUI()
    
    # this is where we will be designing the user interface
    def initUI(self):
        # changes name of window title
        self.setWindowTitle("Weather App")

        # declares vbox will have a vertical box layout
        vbox = QVBoxLayout()

        # adds our widgets to the vbox 
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        # passes in our vertical layout manager to set as the layout
        self.setLayout(vbox)

        # aligns all widgets to be in center of the window
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

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