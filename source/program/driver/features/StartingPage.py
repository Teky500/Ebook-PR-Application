import sys
from .Themes import Theme, getTheme
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QStackedWidget
from .SetInstitutionPage import SetInstitution
import yaml
from .helpers.crknScrapper import CrknExcelExtractor
from .helpers.download_excel import downloadExcel, parseExcel, downloadFiles
from .helpers.crknUpdater import UpdateChecker
from .HomePage import SetHomePage
from .FirstTimeUpdate import SetFirstTimeUpdate
import os
theme = Theme(getTheme())
themeColour = theme.getColor()
class WelcomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
       
        self.setup_ui()


    def setup_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel(f"Starting", self)

        font = label.font()
        font.setPointSize(35) 
        font.setBold(True)
        label.setFont(font)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate_text)
        self.animation_counter = 0

        self.page_timer = QTimer(self)
        self.page_timer.timeout.connect(self.show_next_page)

        self.animation_timer.start(600)
        self.page_timer.start(5000)

        self.window().setFixedSize(500, 280)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint) 

    def getStatus(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            status = yaml_file['Status']
        return status
    def animate_text(self):
        dots = '.' * (self.animation_counter % 4)
        label = self.findChild(QLabel)
        label.setText(f"Starting{dots}")
        self.animation_counter += 1

    def show_next_page(self):
        self.page_timer.stop()
        self.window().close()
        self.openNewWindow()
  
    def setFixedSize(self, width, height):
        super().setFixedSize(width, height)

    def openNewWindow(self):
        if self.getStatus() == 0:
            print('Status 0')
            downloadFiles()
            global m
            new_window = SetInstitution()
            m = new_window
            new_window.run()
        else:
            checker = UpdateChecker()
            url = checker.config.get('link')
            new_excel_files = checker.get_website_excel_files(url)
            (added, removed) = checker.compare(new_excel_files)
            if (len(added) + len(removed)) == 0:
                print('Status 1, found no updates')
                new_window = SetHomePage()
                m = new_window
                new_window.window().show()
                self.window().close()
            else:
                print('Status 1, found update')
                print(added, removed)
                update = SetFirstTimeUpdate(checker)
                m = update
                m.window().show()
                self.window().close()
                # checker.update_config()
                # downloadFiles()
                # new_window = SetHomePage()
                # m = new_window
                # new_window.window().show()




      

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet("""
                           
            QWidget {
                background-color: #333333;
                color: #ffffff;
                border-color: #333333;
            }
            QPushButton {
                background-color: #4d4d4d;
                border: 1px solid #4d4d4d;
                border-radius: 4px;
                color: #ffffff;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
                border: 1px solid #5a5a5a;
            }
            
            QScrollBar:vertical {
                border: 1px solid #444444;
                background-color: #3a3a3a;
                width: 15px;
                height: 25px;
                margin: 16px 0 16px 0;

            }
            QScrollBar::handle:vertical {
                background-color: #444444;
                border-radius: 5px;
            }
                      
            QScrollBar:horizontal {
                border: 1px solid #444444;
                background-color: #3a3a3a;
                height: 15px;
                margin: 0px 16px 0 16px;
            }
                      
            QScrollBar::handle:horizontal {
                background-color: #444444;
                border-radius: 5px;
            }
                                                   
            QTabBar::tab:selected, QTabBar::tab:hover {
                background-color: #3a3a3a;
                color: white;
            }
                      
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
     
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	            background: none;
            }   

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	            background: none;
            }  

            """)

    main_window = QWidget()
    main_layout = QVBoxLayout(main_window)

    if themeColour == {}:
        pass
        
    else:
        bg_col = themeColour['background_color']
        txt_col = themeColour['text_color']
        main_window.setStyleSheet(f'background-color: {bg_col}; color: {txt_col}')

    stacked_widget = QStackedWidget(main_window)
    welcome_page = WelcomePage(stacked_widget)
  
    stacked_widget.addWidget(welcome_page)
    main_layout.addWidget(stacked_widget)

    
    main_window.show()

    sys.exit(app.exec())

