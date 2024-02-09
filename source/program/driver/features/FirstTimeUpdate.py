import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget
from PyQt6.QtCore import Qt
from FirstTimeUpdateConfirm import SetFirstTimeUpdateConfirm
from HomePage import SetHomePage
from helpers.download_excel import downloadFiles

class SetFirstTimeUpdate(QWidget):
    def __init__(self, check):
        super(SetFirstTimeUpdate, self).__init__()

        loadUi("source/program/driver/features/ui/updatefirst-timepage.ui", self)
        self.checker = check
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.confirm_update_1.clicked.connect(self.load_confirm_page)
        self.cancel_update_1.clicked.connect(self.load_home_page)

 
    def load_confirm_page(self):
        self.checker.update_config()
        downloadFiles()
        global m
        new_window = SetFirstTimeUpdateConfirm()
        m = new_window
        self.window().hide()
        new_window.run()

    def load_home_page(self):
        global m
        new_window = SetHomePage()
        m = new_window
        self.window().hide()
        new_window.run()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = SetFirstTimeUpdate()
    widget.show()
    sys.exit(app.exec())