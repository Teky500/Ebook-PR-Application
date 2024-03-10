from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMainWindow
import yaml
from .searchPage import Ui_Search_page
from .helpers.search import search_title_substring, search_ISBN, search_OCN
from .SearchPageResults import MainWindow
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt

class searchPageDriver(QtWidgets.QWidget, Ui_Search_page):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")
       
        #search button
        self.pushButton.clicked.connect(self.search)

        #Title button
        self.radioButton.clicked.connect(self.byTitle)
        self.radioButton.setChecked(True)
        self.radio = 1 
        #Keyword button
        self.radioButton_2.clicked.connect(self.byKeyword)

        #OCN button
        self.radioButton_3.clicked.connect(self.byOCN)

        #eISBN button
        self.radioButton_4.clicked.connect(self.by_eISBN)

        #Cancel button
        self.pushButton_2.clicked.connect(self.close)

        if self.getLanguage() == 1:
            self.label.setText("Recherche de Livre Électronique")
            self.pushButton.setText("Recherche")
            self.pushButton_2.setText("Annule la Recherche")
            self.radioButton.setText("Titre")
            self.radioButton_2.setText("Mot Clé")

    def getLanguage(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            language = yaml_file['Language']
        return language
    
    def close(self):
        super().close()
        #self.window().close()
        # 0 = no button selected
        self.radio = 0

    def byTitle(self):
        self.radio = 1
    def byKeyword(self):
        self.radio = 2
    def byOCN(self):
        self.radio = 3
    def by_eISBN(self):
        self.radio = 4
    def search(self):
        text = self.lineEdit.text()
        if (len(text) == 0):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("messageBox")
            msg.setText("Search field can not be empty!")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            msg.exec()
            return
        global m
        match self.radio:

            case 0:
                print("Please select a search criteria")
            case 1:
                s_result = search_title_substring(text, 'source/storage/database/proj.db')
                m = MainWindow(s_result, 1)
                print(m)
                m.window().show()

            case 2:
                pass
            case 3: 
                s_result = search_OCN(text, 'source/storage/database/proj.db')
                m = MainWindow(s_result, 3)
                print(m)
                m.window().show()
            case 4:
                s_result = search_ISBN(text, 'source/storage/database/proj.db')
                m = MainWindow(s_result, 0)
                print(m)
                m.window().show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = searchPageDriver()
    ui.show()
    sys.exit(app.exec())