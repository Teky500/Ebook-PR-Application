import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
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


class NetworkPage(QWidget):
    def __init__(self, msg):
        super(NetworkPage, self).__init__()

        loadUi(img_resource_path("source/features/ui/internetConnectionPage.ui"), self)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")

        # Evan - insert langauge here

        self.optional_label.setText(msg)
        self.confirm_error.clicked.connect(self.on_confirm_clicked)

    def on_confirm_clicked(self):
        self.window().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NetworkPage(msg = "Could not download initial CRKN spreadsheets due to network error. Please try again")
    widget.show()
    sys.exit(app.exec())