import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from Themes import Theme, getTheme
from helpers.manual_upload import man_upload

class UploadSpreadsheet(QWidget):
    def __init__(self):
        super(UploadSpreadsheet, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/exception_error.ui", self)

        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')


    def close_window(self):
        self.window().close()

app = QApplication(sys.argv)
window = UploadSpreadsheet()
window.show()
sys.exit(app.exec())