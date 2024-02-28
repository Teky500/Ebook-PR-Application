import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QPushButton, QFileDialog, QLabel
import yaml
from .Themes import Theme, getTheme
from .helpers.manual_upload import man_upload

class UploadSpreadsheet(QWidget):
    def __init__(self):
        super(UploadSpreadsheet, self).__init__()
        self.filePicked = ''

        loadUi("source/program/driver/features/ui/upload.ui", self)

        if self.getLanguage() == 1:
            self.label.setText("Mettre en ligne la feuille de calcul locale")
                        #Change style sheet to reduce font size and fit text
            self.label.setStyleSheet("""
    QLabel {
        font: 700 38pt "Segoe UI";
        color: #ffffff;
        background-color: #333333; /* Change color */
        border: 1px solid #333333;
        padding: 5px;
    }
""")
            self.upload_button_1.setText("Mettre en ligne")
            self.upload_local_file.setText("Soumettre")
            self.cancel_process.setText("Annuler")
            self.file_label_1.setText("aucun fichier sélectionné")

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
        if self.filePicked == "":
            print('NO FILE SELECTED')
        else:
            man_upload(self.filePicked)

    def close_window(self):
        self.window().close()

    def getLanguage(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            language = yaml_file['Language']
        return language