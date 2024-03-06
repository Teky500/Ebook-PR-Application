import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload
from .helpers.getLanguage import getLanguage

class UnloadSuccess(QWidget):
    def __init__(self, fileN):
        super(UnloadSuccess, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/unloadpage_success.ui", self)
        self.label.setText(f'Successfully removed file {fileN}')

        if getLanguage() == 1:
            self.unload.setText("Succès!")
            self.label.setText(f'Fichier supprimé avec succès: {fileN}')

        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')

    def close_window(self):
        self.window().close()
        
