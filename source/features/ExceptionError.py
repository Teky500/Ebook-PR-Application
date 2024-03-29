import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload

class ExceptionErrorPage(QWidget):
    def __init__(self, message):
        super(ExceptionErrorPage, self).__init__()
        self.filePicked = ''

        loadUi("source/features/ui/exception_error.ui", self)
        self.label.setText(message)
        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')


    def close_window(self):
        self.window().close()
