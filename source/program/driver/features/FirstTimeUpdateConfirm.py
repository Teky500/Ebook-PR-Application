import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from .HomePage import SetHomePage


class SetFirstTimeUpdateConfirm(QWidget):
    def __init__(self):
        super(SetFirstTimeUpdateConfirm, self).__init__()

        loadUi("source/program/driver/features/ui/confirmfirst-timepage.ui", self)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.confirm_update_first_time.clicked.connect(self.show_home_page)

    def run(self):
        self.window().show()

    def show_home_page(self):
        global m
        new_window = SetHomePage()
        m = new_window
        self.window().hide()
        new_window.run()