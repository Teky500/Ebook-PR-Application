import sys
from source.features.StartingPage import WelcomePage

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QStackedWidget
import os
import yaml
if __name__ == "__main__":
    pathes = ['source/storage/spreadsheets', 'source/storage/database', 'source/storage/excel', 'source/config']
    for newpath in pathes:
        if not os.path.exists(newpath):
            os.makedirs(newpath)
    x = {'Language': 0, 'Status': 0, 'Universities': ['Acadia Univ.', 'Algoma Univ.', 'Athabasca Univ.', "Bishop's Univ.", 'Brandon Univ.', 'Brock Univ.', 'Cape Breton Univ.', 'Capilano Univ.', 'Carleton Univ.', 'Concordia Univ.', 'Concordia Univ. of Edmonton', 'Dalhousie Univ.', "École nationale d'administration publique", 'École de technologie supérieure', 'HEC Montréal', 'Institut national de la recherche scientifique', 'Kwantlen Polytechnic Univ.', 'Lakehead Univ.', 'Laurentian Univ.', 'MacEwan Univ', 'McGill Univ.', 'McMaster Univ.', 'Memorial Univ. of Newfoundland', 'Mount Allison Univ.', 'Mount Royal Univ.', 'Mount Saint Vincent Univ.', 'Nipissing Univ.', 'NSCAD Univ.', 'OCAD Univ.', 'Polytechnique Montréal', "Queen's University", 'Royal Military College', 'Royal Roads Univ.', 'Ryerson Univ.', "Saint Mary's Univ.", 'Simon Fraser Univ.', 'St. Francis Xavier Univ.', 'TÉLUQ', "The King's Univ.", 'Thompson Rivers Univ.', 'Trent Univ.', 'Trinity Western Univ.', 'Univ. de Moncton', 'Univ. de Montréal', 'Univ. de Sherbrooke', 'Univ. du Québec à Chicoutimi', 'Univ. du Québec à Montréal', 'Univ. du Québec à Rimouski', 'Univ. du Québec à Trois-Rivières', 'Univ. du Québec en Abitibi-Témiscamingue', 'Univ. du Québec en Outaouais', 'Univ. Laval', 'Univ. Sainte-Anne', 'Univ. of Alberta', 'Univ. of British Columbia', 'Univ. of Calgary', 'Univ. of Guelph', 'Univ. of Lethbridge', 'Univ. of Manitoba', 'Univ. of New Brunswick', 'Univ. of Northern British Columbia', 'Univ. of Ontario Institute of Technology', 'Univ. of Ottawa', 'Univ. of Prince Edward Island', 'Univ. of Regina', 'Univ. of Saskatchewan', 'Univ. of the Fraser Valley', 'Univ. of Toronto', 'Univ. of Victoria', 'Univ. of Waterloo', 'Univ. of Windsor', 'Univ. of Wininpeg', 'Vancouver Island Univ.', 'Western Univ.', 'Wilfrid Laurier Univ.', 'York Univ.'], 'University': 'Acadia Univ.', 'excel_links': ['https://library.upei.ca/sites/default/files/CRKN_EbookPARightsTracking_TaylorFrancis_2024_02_06_2.xlsx', 'https://library.upei.ca/sites/default/files/CRKN_EbookPARightsTracking_Proquest_2024_02_06_3.xlsx'], 'link': 'https://library.upei.ca/test-page-ebooks-perpetual-access-project'}
    if not os.path.isfile('source/config/config.yaml'):
        with open("source/config/config.yaml", 'w') as yF:
            yaml.dump(x, yF, default_flow_style=False)
    

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

    main_window = QWidget()
    main_layout = QVBoxLayout(main_window)

    stacked_widget = QStackedWidget(main_window)
    welcome_page = WelcomePage(stacked_widget)
  
    stacked_widget.addWidget(welcome_page)
    main_layout.addWidget(stacked_widget)

    
    main_window.show()

    sys.exit(app.exec())