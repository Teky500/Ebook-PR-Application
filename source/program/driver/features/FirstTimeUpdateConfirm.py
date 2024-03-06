import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from .helpers.getLanguage import getLanguage



class SetFirstTimeUpdateConfirm(QWidget):
    def __init__(self):
        super(SetFirstTimeUpdateConfirm, self).__init__()

        loadUi("source/program/driver/features/ui/confirmfirst-timepage.ui", self)

        if getLanguage() == 1:
            self.label.setText("Vos données CRKN sont désormais à jour!")
            #Make text smaller
            self.label.setStyleSheet("""
    QLabel {
        font: 700 18pt "Segoe UI";
        color: #ffffff;
        background-color: #333333; /* Change color */
        border: 1px solid #333333;
        padding: 5px;
    }
""")

        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.confirm_update_first_time.clicked.connect(self.show_home_page)

    def run(self):
        self.window().show()

    def show_home_page(self):
        from .HomePage import SetHomePage
        global m
        new_window = SetHomePage()
        m = new_window
        self.window().hide()
        new_window.run()