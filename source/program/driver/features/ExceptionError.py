import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload
from .helpers.getLanguage import getLanguage

class ExceptionErrorPage(QWidget):
    def __init__(self):
        super(ExceptionErrorPage, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/exception_error.ui", self)

        if getLanguage(self) == 1:
            self.unload.setText("Échec!")
            self.label.setText("Quelque chose s'est mal passé, une réinitialisation de l'application est recommandée")

        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')


    def close_window(self):
        self.window().close()
