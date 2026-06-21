import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00:00",self)
        self.time = QTime(0, 0, 0, 0)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setStyleSheet("""
                    QWidget{
                        background-color: black;
                        color: white;
                    }
                    QPushButton{
                        font-weight: bold;
                        font-size: 50px;
                        padding: 20px;
                    }
                    QLabel{
                        font-weight: bold;
                        font-size: 120px;
                        background-color: black;
                        color: white;
                        border-radius: 20px;
                        padding: 20px;
                    }
                """)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

        
        font = QFontDatabase.addApplicationFont("Stopwatch/DS-DIGIT.TTF")
        families = QFontDatabase.applicationFontFamilies(font)
        if families:
               my_font = QFont(families[0], 120)
               self.time_label.setFont(my_font)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())