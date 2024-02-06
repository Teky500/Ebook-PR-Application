from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMainWindow
from searchPage import Ui_Search_page

class searchPageDriver(QtWidgets.QWidget, Ui_Search_page):
    def __init__(self, parent = None):
        super().__init__(parent)
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
            raise ValueError("Search field can not be empty")
        #print("Searching the data base for %s." % (text))
        match self.radio:
            case 0:
                print("Please select a search criteria")
            case 1:
                print("Searching the data base for %s by Title." % (text))
            case 2:
                print("Searching the data base for %s by Keyword" % (text))
            case 3:
                print("Searching the data base for %s by OCN" % (text))
            case 4:
                print("Searching the data base for %s by eISBN" % (text))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = searchPageDriver()
    ui.show()
    sys.exit(app.exec())