import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload

class UploadFailure(QWidget):
    def __init__(self, errorM):
        super(UploadFailure, self).__init__()
        self.filePicked = ''

        loadUi("source/features/ui/uploadpage_failure.ui", self)
        self.label.setText(errorM)
        self.cancel_button.clicked.connect(self.close_window)
        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')


    def close_window(self):
        self.window().close()
