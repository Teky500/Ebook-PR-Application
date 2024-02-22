import sys
from features.StartingPage import WelcomePage
from features.Themes import Theme, getTheme
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QStackedWidget

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
    theme = Theme(getTheme())
    themeColour = theme.getColor()
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