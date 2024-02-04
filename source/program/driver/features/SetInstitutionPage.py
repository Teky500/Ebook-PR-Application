import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget
from helpers.add_to_database import setDatabaseUni
import pandas as pd
from Themes import Theme, getTheme

class SetInstitution(QWidget):
    def __init__(self):
        super(SetInstitution, self).__init__()

        loadUi("source/program/driver/features/dropdown.ui", self)

        theme = Theme(getTheme())
        themeColour = theme.getColor()
        if themeColour == {}:
            pass
        else:
            bg_col = themeColour['background_color']
            txt_col = themeColour['text_color']
            self.setStyleSheet(f'background-color: {bg_col}; color: {txt_col};')
        spreadsheet_csv = pd.read_csv('source/storage/spreadsheets/CRKN_EbookPARightsTracking_TaylorFrancis_2024_01_19_01.csv', skiprows=[0,1])
        df = pd.DataFrame(spreadsheet_csv)
        Universities = df.columns[9:]
        for i in Universities:
            # should be changed to show a pop up on the front-end telling them to select an institution.
            self.institutions.addItem(i)
        self.submit_button_1.clicked.connect(self.clicked_function)

    def clicked_function(self):
        selected_text = self.institutions.currentText()
        if selected_text == '':
            print('You need to select an institution')
        else:
            setDatabaseUni(selected_text)

app = QApplication(sys.argv) 
app.setStyleSheet (
        """
        QWidget {
        background-color: #333333;
        color: #ffffff;
        border: none;
    }"""
)


mainwindow = SetInstitution()
widget = QStackedWidget()
widget.addWidget(mainwindow)

