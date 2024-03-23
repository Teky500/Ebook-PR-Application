from PyQt6 import QtWidgets, QtGui
import yaml
from PyQt6.uic import loadUi
from .helpers.search import search_title_substring, search_ISBN, search_OCN
from .helpers.getLanguage import getLanguage
from .SearchPageResults import MainWindow
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import os
import sys
import logging
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

    except Exception:
    
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class searchPageDriver(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi(img_resource_path("source/features/ui/SearchPageModified.ui"), self)

        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)
        self.setWindowIcon(QIcon(transparent_pixmap))
        self.window().setWindowTitle("     ")
       
        #search button
        self.search_ebook.clicked.connect(self.search)

        #Title button
        self.radio_button_2.clicked.connect(self.byTitle)
        self.radio_button_2.setChecked(True)
        self.radio = 1 

        #OCN button
        self.radio_button_1.clicked.connect(self.byOCN)

        #eISBN button
        self.radio_button_3.clicked.connect(self.by_eISBN)

        #Cancel button
        self.cancel_search.clicked.connect(self.close)

        if getLanguage() == 1:
            self.label.setText("<font size='2'>Recherche de Livre Électronique</font>")
            self.search_ebook.setText("Recherche")
            self.cancel_search.setText("Annuler")
            self.radio_button_2.setText("Titre")

    
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
            if getLanguage() == 1:
                msg.setText("Le champ de recherche ne peut pas être vide!")
            else:
                msg.setText("Search field can not be empty!")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.window().setWindowTitle("     ")
            transparent_pixmap = QtGui.QPixmap(1, 1)
            transparent_pixmap.fill(Qt.GlobalColor.transparent)
            msg.setWindowIcon(QIcon(transparent_pixmap))
            msg.resize(400, 200)
            msg.setStyleSheet("""
                                QPushButton {
                                    font-weight: bold;
                                    min-width: 60px;
                                    }                                      
                            """)

            font = QtGui.QFont()
            font.setPointSize(14) 
            font.setBold(True) 
            msg.setFont(font)
            msg.exec()
            return
        
        match self.radio:

            case 0:
                #Case where no radio button selected (We have a default button so should never happen)
                pass
            case 1:
                s_result = search_title_substring(text, 'source/storage/database/proj.db')
                if s_result == []:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("messageBox")
                    if getLanguage() == 1:
                        msg.setText("Aucun correspondance trouvée")
                    else:
                        msg.setText("No matches found!")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

                    msg.window().setWindowTitle("     ")
                    transparent_pixmap = QtGui.QPixmap(1, 1)
                    transparent_pixmap.fill(Qt.GlobalColor.transparent)
                    msg.setWindowIcon(QIcon(transparent_pixmap))

                    msg.resize(400, 200)

                    msg.setStyleSheet("""
                                        QPushButton {
                                            font-weight: bold;
                                            min-width: 60px;
                                        }         
                                      
                                      """)

                    font = QtGui.QFont()
                    font.setPointSize(14) 
                    font.setBold(True) 
                    msg.setFont(font)

                    msg.exec()
                    logging.info('No Search found!')
                    return
                self.main_window = MainWindow(s_result, 1)
                logging.info(self.main_window)
                self.main_window.window().show()

            case 2:
                pass
            case 3: 
                s_result = search_OCN(text, 'source/storage/database/proj.db')
                if s_result == []:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("messageBox")
                    if getLanguage() == 1:
                        msg.setText("Aucun correspondance trouvée")
                    else:
                        msg.setText("No matches found!")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

                    msg.window().setWindowTitle("     ")
                    transparent_pixmap = QtGui.QPixmap(1, 1)
                    transparent_pixmap.fill(Qt.GlobalColor.transparent)
                    msg.setWindowIcon(QIcon(transparent_pixmap))

                    msg.resize(400, 200)

                    msg.setStyleSheet("""
                                        QPushButton {
                                            font-weight: bold;
                                            min-width: 60px;
                                        }         
                                      
                                      """)

                    font = QtGui.QFont()
                    font.setPointSize(14) 
                    font.setBold(True) 
                    msg.setFont(font)

                    msg.exec()
                    logging.info('No Search found!')
                    return
                self.main_window = MainWindow(s_result, 3)
                logging.info(self.main_window)
                self.main_window.window().show()

            case 4:
                s_result = search_ISBN(text, 'source/storage/database/proj.db')
                if s_result == []:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("messageBox")
                    if getLanguage() == 1:
                        msg.setText("Aucun correspondance trouvée")
                    else:
                        msg.setText("No matches found!")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

                    msg.window().setWindowTitle("     ")
                    transparent_pixmap = QtGui.QPixmap(1, 1)
                    transparent_pixmap.fill(Qt.GlobalColor.transparent)
                    msg.setWindowIcon(QIcon(transparent_pixmap))

                    msg.resize(400, 200)

                    msg.setStyleSheet("""
                                        QPushButton {
                                            font-weight: bold;
                                            min-width: 60px;
                                        }         
                                      
                                      """)

                    font = QtGui.QFont()
                    font.setPointSize(14) 
                    font.setBold(True) 
                    msg.setFont(font)
                    msg.exec()
                    logging.info('No Search found!')
                    return
                self.main_window = MainWindow(s_result, 0)
                logging.info(self.main_window)
                self.main_window.window().show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = searchPageDriver()
    ui.show()
    sys.exit(app.exec())