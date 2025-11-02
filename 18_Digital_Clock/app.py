# Python Digital Clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timeLabel = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        self.setLayout(vbox)

        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.timeLabel.setStyleSheet("font-size: 100px;"
                                     "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.timeLabel.setFont(my_font)

        self.timer.timeout.connect(slot=self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss A")
        self.timeLabel.setText(current_time)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())