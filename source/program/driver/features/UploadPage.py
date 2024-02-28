import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload
from .upload_success import UploadSuccess
from .upload_failure import UploadFailure

class UploadSpreadsheet(QWidget):
    def __init__(self):
        super(UploadSpreadsheet, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/upload.ui", self)

        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == "default":
            pass
        else:
            self.setStyleSheet(f'background-color: {themeColour};')

        # Add upload button
        self.upload_button_1.clicked.connect(self.uploadFile)

        # Cancel process
        self.cancel_process.clicked.connect(self.close_window)
        self.upload_local_file.clicked.connect(self.submitFile)


    def uploadFile(self):
        # Open file dialog to select a file
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Spreadsheet Files (*.xls *.xlsx)")
        if fileName:
            print(f"File selected: {fileName}")
            # Update the label to show the selected file path
            self.filePicked = fileName
            self.file_label_1.setText(f"Selected File: {fileName}")
    def submitFile(self):
        global m
        if self.filePicked == "":
            print('NO FILE SELECTED')
        else:
            result = man_upload(self.filePicked)
            if result == []:
                m = UploadSuccess()
                m.window().show()
            else:
                r = str(result)
                m = UploadFailure(r)
                m.window().show()

    def close_window(self):
        self.window().close()

