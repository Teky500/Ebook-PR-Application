import sys
from source.features.StartingPage import WelcomePage

from source.features.LanguageChoice import LanguageChoice
from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QHBoxLayout


import os
import yaml
import logging
from datetime import datetime
import traceback
import os
if __name__ == "__main__":

    # Configure logger to write to a file...

    def my_handler(type, value, tb):
        for line in traceback.TracebackException(type, value, tb).format(chain=True):
            logging.exception(line)
        logging.exception(value)
        sys.exit()
    if getattr(sys, 'frozen', False):
        cwd = os.path.dirname(sys.executable)
    elif __file__:
        cwd = os.path.dirname(__file__)
        # Install exception handler
    sys.excepthook = my_handler
    os.chdir(cwd)
    sys.path.append(cwd)
    print(os.getcwd())
    print(sys.path)
    pathes = ['source/storage/spreadsheets', 'source/storage/database', 'source/storage/excel', 'source/config', 'source/logs']
    abs_pathes = []
    for p in pathes:
        new_path = os.path.join(cwd, p)
        abs_pathes.append(new_path)
    for newpath in abs_pathes:
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        today = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    filename = "log_" + today + '.txt'
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s %(filename)s %(funcName)s %(lineno)d', handlers=[ logging.FileHandler((f'source/logs/{filename}')), logging.StreamHandler() ] )

    logging.info('Starting app')
    logger = logging.getLogger('mylogger.app')
    x = {'Language': 0, 'Status': 0, 'Universities': ['Acadia Univ.', 'Algoma Univ.', 'Athabasca Univ.', "Bishop's Univ.", 'Brandon Univ.', 'Brock Univ.', 'Cape Breton Univ.', 'Capilano Univ.', 'Carleton Univ.', 'Concordia Univ.', 'Concordia Univ. of Edmonton', 'Dalhousie Univ.', "École nationale d'administration publique", 'École de technologie supérieure', 'HEC Montréal', 'Institut national de la recherche scientifique', 'Kwantlen Polytechnic Univ.', 'Lakehead Univ.', 'Laurentian Univ.', 'MacEwan Univ', 'McGill Univ.', 'McMaster Univ.', 'Memorial Univ. of Newfoundland', 'Mount Allison Univ.', 'Mount Royal Univ.', 'Mount Saint Vincent Univ.', 'Nipissing Univ.', 'NSCAD Univ.', 'OCAD Univ.', 'Polytechnique Montréal', "Queen's University", 'Royal Military College', 'Royal Roads Univ.', 'Ryerson Univ.', "Saint Mary's Univ.", 'Simon Fraser Univ.', 'St. Francis Xavier Univ.', 'TÉLUQ', "The King's Univ.", 'Thompson Rivers Univ.', 'Trent Univ.', 'Trinity Western Univ.', 'Univ. de Moncton', 'Univ. de Montréal', 'Univ. de Sherbrooke', 'Univ. du Québec à Chicoutimi', 'Univ. du Québec à Montréal', 'Univ. du Québec à Rimouski', 'Univ. du Québec à Trois-Rivières', 'Univ. du Québec en Abitibi-Témiscamingue', 'Univ. du Québec en Outaouais', 'Univ. Laval', 'Univ. Sainte-Anne', 'Univ. of Alberta', 'Univ. of British Columbia', 'Univ. of Calgary', 'Univ. of Guelph', 'Univ. of Lethbridge', 'Univ. of Manitoba', 'Univ. of New Brunswick', 'Univ. of Northern British Columbia', 'Univ. of Ontario Institute of Technology', 'Univ. of Ottawa', 'Univ. of Prince Edward Island', 'Univ. of Regina', 'Univ. of Saskatchewan', 'Univ. of the Fraser Valley', 'Univ. of Toronto', 'Univ. of Victoria', 'Univ. of Waterloo', 'Univ. of Windsor', 'Univ. of Wininpeg', 'Vancouver Island Univ.', 'Western Univ.', 'Wilfrid Laurier Univ.', 'York Univ.'], 'University': 'Acadia Univ.', 'excel_links': ['https://library.upei.ca/sites/default/files/CRKN_EbookPARightsTracking_TaylorFrancis_2024_02_06_2.xlsx', 'https://library.upei.ca/sites/default/files/CRKN_EbookPARightsTracking_Proquest_2024_02_06_3.xlsx'], 'link': 'https://library.upei.ca/test-page-ebooks-perpetual-access-project'}
    if not os.path.isfile(('source/config/config.yaml')):
        with open(("source/config/config.yaml"), 'w') as yF:
            yaml.dump(x, yF, default_flow_style=False)
    
    def getStatus():
        with open(os.path.join(cwd, 'source/config/config.yaml'), 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            status = yaml_file['Status']
        return status

            
    
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
            
            # QScrollBar:vertical {
            #     border: 1px solid #444444;
            #     background-color: #3a3a3a;
            #     width: 15px;
            #     height: 25px;
            #     margin: 16px 0 16px 0;

            # }
            # QScrollBar::handle:vertical {
            #     background-color: #444444;
            #     border-radius: 5px;
            # }
                      
            # QScrollBar:horizontal {
            #     border: 1px solid #444444;
            #     background-color: #3a3a3a;
            #     height: 15px;
            #     margin: 0px 16px 0 16px;
            # }
                      
            # QScrollBar::handle:horizontal {
            #     background-color: #444444;
            #     border-radius: 5px;
            # }
                                                   
            # QTabBar::tab:selected, QTabBar::tab:hover {
            #     background-color: #3a3a3a;
            #     color: white;
            # }
                      
            # QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            #     background: none;
            # }
     
            # QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	        #     background: none;
            # }   

            # QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	        #     background: none;
            # }  

            """)

    # main_window = QWidget()
    # main_layout = QVBoxLayout(main_window)
    # stacked_widget = QStackedWidget(main_window)
    
    # if getStatus() == 0:
    #     page = LanguageChoice(stacked_widget)
    # else:
    #     page = WelcomePage(stacked_widget)
    
    # stacked_widget.addWidget(page)
    # main_layout.addWidget(stacked_widget)

    # main_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    # main_window.show()

    main_window = QWidget()
    main_layout = QHBoxLayout(main_window)

    if getStatus() == 0:
        page = LanguageChoice(main_window)
    else:
        page = WelcomePage(main_window)

    main_layout.addWidget(page)

    main_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    main_window.show()

    screen_geometry = app.primaryScreen().geometry()
    center_point = screen_geometry.center()
    main_window.move(center_point - main_window.rect().center())

    sys.exit(app.exec())