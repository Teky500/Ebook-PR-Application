import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from .helpers.getLanguage import getLanguage
import os
# from .helpers.getLanguage import getLanguage (helpers import)

def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class NetworkUpdateFailurePage(QWidget):
    def __init__(self):
        super(NetworkUpdateFailurePage, self).__init__()

        loadUi(img_resource_path("source/features/ui/update_network_failure.ui"), self)

        if getLanguage() == 1:
            self.continue_button.setText("Continuer")
            self.exit_button.setText("Sortir")
            self.label.setText("Impossible de vérifier les mises à jour CRKN en raison d'une erreur réseau")

        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        # Evan - insert langauge here

        #self.continue_button.clicked.connect(self.on_continue_clicked)
        self.exit_button.clicked.connect(self.on_exit_clicked)
        self.continue_button.clicked.connect(self.on_continue_clicked)

    def on_exit_clicked(self):
        sys.exit()
    def on_continue_clicked(self):
        from .HomePage import SetHomePage
        self.home_page = SetHomePage()
        self.home_page.show()
        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NetworkUpdateFailurePage()
    widget.show()
    sys.exit(app.exec())