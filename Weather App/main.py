import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Search Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
                    QLabel, QPushButton{
                        font-family: calibri;
                    }
                    QLabel#city_label{
                        font-weight: bold;
                        font-size: 40px;
                        font-style: italic;
                        background-color: hsl(195.7, 91.4%, 59%);
                    }
                    QLineEdit#city_input{
                        font-size: 40px;
                    }
                    QPushButton#get_weather_button{
                        font-size: 30px;
                        font-weight: bold;
                        background-color: yellow;
                    }
                    QLabel#temperature_label{
                        font-size: 70px;
                        background-color: hsl(195.7, 91.4%, 59%);
                    }
                    QLabel#emoji_label{
                        font-size: 100px;
                        background-color: white;
                    }
                    QLabel#description_label{
                        font-size: 35px;
                        background-color: hsl(195.7, 91.4%, 59%);
                    }
                """)
        
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        API_key = "f58d810d5606201efb9eea5bf6bfa5ea"
        city = self.city_input.text()
        url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_Error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request: \nPlease check your input")
                case 401:
                    self.display_error("Unauthorized: \nInvalid API key")
                case 403:
                    self.display_error("Forbidden: \nAccess is denied")
                case 404:
                    self.display_error("Not found: \nCity not found")
                case 500:
                    self.display_error("Internal Server Error: \nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway: \nInvalid response from server")
                case 503:
                    self.display_error("Server Unavailable: \nServer is down")
                case 504:
                    self.display_error("Gateway timeout: \nNo resposne from server")
                case _:
                    self.display_error(f"HTTP error occured: \n{http_Error}")\
                    
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nRequest timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\n Check your URL")
        except requests.exceptions.RequestException as reg_error:
            self.display_error(f"Request Error:\n{reg_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 25px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 70px;")
        temp = data["main"]["temp"]
        temp_c = temp - 273.15
        weather = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temp_c:.1f}°C")
        self.emoji_label.setText(self.get_emoji(weather_id))
        self.description_label.setText(f"{weather.capitalize()}")

    @staticmethod
    def get_emoji(weather_id):
        match weather_id:
            case x if 200 <= x <= 232:
                return "⛈️"
            case x if 300 <= x <= 321:
                return "🌦️"
            case x if 500 <= x <= 531:
                return "🌧️"
            case x if 600 <= x <= 622:
                return "❄️"
            case x if 701 <= x <= 781:
                return "🌫️"
            case 800:
                return "☀️"
            case 801:
                return "🌤️"
            case 802:
                return "⛅"
            case 803 | 804:
                return "☁️"
            case _:
                return "🌍"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())