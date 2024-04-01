import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
import os
from .helpers.getLanguage import getLanguage

def packagingPath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class SetFirstTimeUpdateConfirm(QWidget):
    def __init__(self, msg, stat):
        super(SetFirstTimeUpdateConfirm, self).__init__()

        loadUi(packagingPath("source/features/ui/confirmfirst-timepage.ui"), self)
        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        if getLanguage() == 1:
            self.label.setText("Vos données CRKN sont désormais à jour!")
            self.label.setStyleSheet('''font-size: 18pt;
                                           background-color: #333333;
                                            color: #ffffff;
                                           padding: 5px;
                                          border-color: #333333;''')

        self.confirm_update_first_time.clicked.connect(self.show_home_page)
        self.label.setText(msg)

    def run(self):
        self.window().show()

    def show_home_page(self):
        from .HomePage import SetHomePage
        self.home_page = SetHomePage()
        self.window().hide()
        self.home_page.run()