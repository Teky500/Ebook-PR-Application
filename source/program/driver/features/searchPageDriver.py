from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMainWindow
from searchPage import Ui_Search_page
from helpers.search import search_title_substring, search_ISBN, search_OCN

class searchPageDriver(QtWidgets.QWidget, Ui_Search_page):
    def __init__(self, parent = None):
        super().__init__(parent)
        print('test')
        self.setupUi(self)
       
        #search button
        self.pushButton.clicked.connect(self.search)

        #Title button
        self.radioButton.clicked.connect(self.byTitle)

        #Keyword button
        self.radioButton_2.clicked.connect(self.byKeyword)

        #OCN button
        self.radioButton_3.clicked.connect(self.byOCN)

        #eISBN button
        self.radioButton_4.clicked.connect(self.by_eISBN)

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

        match self.radio:
            case 0:
                print("Please select a search criteria")
            case 1:
                search_title_substring(text, 'source/storage/database/proj.db')
            case 2:
                print("Searching the data base for %s by Keyword" % (text))
            case 3: 
                search_OCN(text, 'source/storage/database/proj.db')
            case 4:
                search_ISBN(text, 'source/storage/database/proj.db')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = searchPageDriver()
    ui.show()
    sys.exit(app.exec())