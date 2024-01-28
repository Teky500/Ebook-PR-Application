import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QPushButton
import sqlite3 as sq
import pandas as pd
from helpers.add_to_database import setDatabaseUni

class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DropDown")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.combo_box = QComboBox(self)
        self.combo_box.addItem("")
        self.combo_box.addItem("Univ. of Prince Edward Island")
        self.combo_box.addItem("Acadia Univ.")
        self.combo_box.addItem("Algoma Univ.")

        layout.addWidget(self.combo_box)

        confirm_button = QPushButton("Confirm", self)
        confirm_button.clicked.connect(self.on_confirm_clicked)

        layout.addWidget(confirm_button)

    def on_combobox_changed(self):
        selected_text = self.sender().currentText()
        print(f"Selected option: {selected_text}")
        setDatabaseUni(selected_text)

    def on_confirm_clicked(self):
        selected_text = self.combo_box.currentText()
        print(f"Confirmed option: {selected_text}")
        setDatabaseUni(selected_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

