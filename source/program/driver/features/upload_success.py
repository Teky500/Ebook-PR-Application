import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload
from .helpers.getLanguage import getLanguage

class UploadSuccess(QWidget):
    def __init__(self):
        super(UploadSuccess, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/uploadpage_success.ui", self)

        if getLanguage() == 1:
            self.unload.setText("Succès!")
            self.label.setText("Fichier téléchargé avec succès")
            self.cancel_button.setText("OK")

        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')


    def close_window(self):
        self.window().close()

