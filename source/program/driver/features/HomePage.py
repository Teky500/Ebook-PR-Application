import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget

class SetHomePage(QWidget):
    def __init__(self):
        super(SetHomePage, self).__init__()
        # self.window_width, self.window_height = 960, 750
        # self.setMinimumSize(self.window_width, self.window_height)

        loadUi("source/program/driver/features/homepage.ui", self)

        self.window().resize(963, 800)

    def run(self):

        self.setStyleSheet ("""
            QWidget {
                background-color: #333333;
                color: #ffffff;
                border: none;
            }
                        
        """)

        self.window().show()


  