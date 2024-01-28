import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget

class SetInstitution(QWidget):
    def __init__(self):
        super(SetInstitution, self).__init__()
        loadUi("source/program/driver/features/dropdown.ui", self)

        self.submit_button_1.clicked.connect(self.clicked_function())
    def clicked_function():
        selected_text = self.institutions.currentText()
        print(selected_text)

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

