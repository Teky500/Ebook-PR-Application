import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload
from .helpers.getLanguage import getLanguage

class UploadFailure(QWidget):
    def __init__(self, errorM):
        super(UploadFailure, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/uploadpage_failure.ui", self)

        if getLanguage() == 1:
            self.unload.setText("Échec!")
            self.label.setText("Tell them what went wrong, but in french, Oui! Oui!")
            self.submit_button.setText("Réessayez")
            self.cancel_button.setText("Annuler")

        self.cancel_button.clicked.connect(self.close_window)
        self.label.setText(errorM)
        #Added style sheet to reduce font size
        self.label.setStyleSheet("""
    QLabel {
        font: 700 10pt "Segoe UI";
        color: #ffffff;
        background-color: #333333; /* Change color */
        border: 1px solid #333333;
        padding: 5px;
    }
""")
        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')


    def close_window(self):
        self.window().close()