import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QHBoxLayout, QVBoxLayout, QFrame, QLabel
from PyQt6.QtCore import Qt, QTimer
import yaml
from .HomePage import SetHomePage

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Splash Screen')
        self.setFixedSize(500, 280)
        self.window().setWindowFlags(Qt.WindowType.FramelessWindowHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300  # total instance

        self.initUI()
        self.setStyleSheet('''

        #LabelTitle {
            font-size: 28px;
            color: white;             
        }
                      
        QFrame {
            background-color: #333333;
            color: white;
        }

        QProgressBar {
            background-color: white;
            color: black;
            border-style: none;
            text-align: center;  
            font-size: 15px;    
            font-weight: bold;
        }
                      
        QProgressBar::chunk {
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #4d4d4d, stop:1 #4d4d4d);      
        }  
        
        ''')

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')
 
        #center labels
        self.labelTitle.resize(self.width() - 20, 150)
        self.labelTitle.move(0, 10) # x,y
        if self.getLanguage() == 1:
            self.labelTitle.setText('<strong>Charger L\'information D\'institution</strong>')
        else:
            self.labelTitle.setText('<strong>Loading Institution Information</strong>')
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.labelDescription = QLabel(self.frame)
        self.labelDescription.move(0, self.labelTitle.height()) 

        # progress bar 
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 130 , 32)
        self.progressBar.move(55, self.labelTitle.y() + 140)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)


    def getLanguage(self):
        with open('source/config/config.yaml', 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            language = yaml_file['Language']
        return language
    
    def loading(self):
        self.progressBar.setValue(self.counter)

        
        if self.counter >= self.n:
            self.timer.stop()
            self.timer.singleShot(1000, self.show_home_page)
            self.window().hide()

        self.counter += 1


    def show_home_page(self):
        global m
        new_window = SetHomePage()
        m = new_window
        new_window.run()
        self.window().close()
