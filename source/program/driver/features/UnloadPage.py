import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from Themes import Theme, getTheme
from helpers.manual_upload import man_upload

class UnloadSpreadsheet(QWidget):
    def __init__(self):
        super(UnloadSpreadsheet, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/unloadpage.ui", self)

        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')

        # Add unload functionality here
        self.submit_button.clicked.connect(self.unloadSpreadsheets)

        # Cancel process here
        self.cancel_button.clicked.connect(self.close_window)

    def unloadSpreadsheets(self):
        pass


    def close_window(self):
        self.window().close()

