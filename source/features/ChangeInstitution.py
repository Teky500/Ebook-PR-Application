import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget
from PyQt6.QtCore import Qt
import yaml

# from SetInstitutionPage import SetInstitution
# from .helpers.download_excel import downloadFiles

class ChangeInstitution(QWidget):
    def __init__(self):
        super(ChangeInstitution, self).__init__()

        loadUi("source/features/ui/changeOfInstitution.ui", self)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self.confirm_change.clicked.connect(self.reset)
        self.cancel_change.clicked.connect(self.load_home_page)
        self.confirm_change.clicked.connect(self.start_again)

    # # reset function here
    # def reset(self):
    #     if self.getStatus() == 0:
    #         print('Status 0')
    #         downloadFiles()
    #         global m
    #         new_window = SetInstitution()
    #         m = new_window
    #         new_window.run()
 

    def load_home_page(self):
        from .HomePage import SetHomePage
        global m
        new_window = SetHomePage()
        m = new_window
        self.window().hide()
        new_window.show()
    def start_again(self):
        from .StartingPage import WelcomePage
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            yaml_file['Status'] = 0
        with open('source/config/config.yaml', 'w') as config_file:
            yaml.dump(yaml_file, config_file)        

        global m
        m = WelcomePage()
        m.show()
        self.window().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ChangeInstitution()
    widget.show()
    sys.exit(app.exec())