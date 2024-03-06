import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload

class UnloadSuccess(QWidget):
    def __init__(self, fileN):
        super(UnloadSuccess, self).__init__()
        self.filePicked = ''

        loadUi("source/features/ui/unloadpage_success.ui", self)
        self.label.setText(f'Successfully removed file {fileN}')
        self.cancel_button.clicked.connect(self.close_window)
        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')

    def close_window(self):
        self.window().close()
        
