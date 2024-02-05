from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMainWindow
from searchPage import Ui_Search_page

class searchPageDriver(QtWidgets.QWidget, Ui_Search_page):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        text = self.lineEdit.text()
        print("Searching the data base for %s." % (text))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = searchPageDriver()
    ui.show()
    sys.exit(app.exec())