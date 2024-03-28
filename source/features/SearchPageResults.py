from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QFileDialog, QHBoxLayout

from .helpers.getLanguage import getLanguage
import pandas as pd
import logging
class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self._header_labels = []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]
        
        if role == Qt.ItemDataRole.ToolTipRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal and section < len(self._header_labels):
                return self._header_labels[section]
            elif orientation == Qt.Orientation.Vertical:
                return str(section + 1)

    def setHeaderLabels(self, labels):
        self._header_labels = labels
        self.headerDataChanged.emit(Qt.Orientation.Horizontal, 0, len(labels) - 1)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, itemData, sType):    
        super().__init__()

        # Create a transparent QPixmap
        transparent_pixmap = QPixmap(1, 1)
        transparent_pixmap.fill(Qt.GlobalColor.transparent)

        # Set the window icon with the transparent QPixmap
        self.setWindowIcon(QIcon(transparent_pixmap))
            
        # Remove title default name
        self.window().setWindowTitle("     ")
        if itemData == []:
            logging.info('Nothing Found')
            self.window().close()
            return None
        
        self.setStyleSheet("""
             
            QTableView {    
                background-color: #333333;
                alternate-background-color: white;
                selection-background-color: white;
            }

            QHeaderView::section {
                background-color: white; 
                color: #333333; 
                padding: 4px;
                font-weight: bold;
            }
                                       
            QTableView::corner {
            background-color: #333333; 
            }
                           
            QTableView::item {
            background-color: white;
            color: #333333; 
            font-weight: bold;
            }
                           
            """)

        if True:
            self.data = itemData
            main_widget = QWidget()
            self.setCentralWidget(main_widget)
            layout = QVBoxLayout()
            main_widget.setLayout(layout)
            self.table = QtWidgets.QTableView()

            self.model = TableModel(self.data)
            self.table.setModel(self.model)

            if getLanguage() == 1:
                header_labels = ['eISBN', 'Titre', 'Éditeur', 'Année', 'OCN', 'Droits PA', 'Nom du fichier', 'Plate-forme']
            else:
                header_labels = ['eISBN', 'Title', 'Publisher', 'Year', 'OCN', 'PA Rights','File Name', 'Platform']
            self.model.setHeaderLabels(header_labels)

            layout.addWidget(self.table)
            button_layout = QHBoxLayout()

            self.download_button = QPushButton('Export')
            self.cancel_button = QPushButton('Cancel')
            self.cancel_button.setText('Close')

            if getLanguage() == 1:
                self.download_button.setText("Exporter")
                self.cancel_button.setText("Annuler")


            button_style = "QPushButton { font-size: 18px; font-weight: bold; background-color: #4d4d4d; border: 1px solid #4d4d4d; border-radius: 4px; color: #ffffff; padding: 5px;}"
            self.download_button.setStyleSheet(button_style)
            self.cancel_button.setStyleSheet(button_style)

            button_layout.addWidget(self.download_button)
            button_layout.addWidget(self.cancel_button)


            self.downloadType = 1
            self.download_button.clicked.connect(self.downloadTable)
            self.cancel_button.clicked.connect(self.exitResultsPage)

            layout.addLayout(button_layout)

            self.table.resizeColumnsToContents()

            self.resize(1092, 683)



    def exitResultsPage(self):
        self.close()

    def downloadTable(self):
        # Get the file path using a file dialog
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'TSV Files (*.tsv);;CSV Files (*.csv)')
        download_type = 0

        if file_path:
            if file_path.endswith('.tsv'):
                download_type = 1
            # Determine delimiter based on file extension
            if download_type == 0:
                df = pd.DataFrame(self.data)
                df[0] = df[0].astype(float).map(lambda x: '{:.0f}'.format(x))
                df[0] = df[0].astype(str)
                df.to_csv(file_path, header= ['eISBN', 'Title', 'Publisher', 'Year', 'OCN', 'PA Rights','File Name', 'Platform'], index=False)
            if download_type == 1:
                df = pd.DataFrame(self.data)
                df[0] = df[0].astype(float).map(lambda x: '{:.0f}'.format(x))
                df[0] = df[0].astype(str)
                df.to_csv(file_path, header= ['eISBN', 'Title', 'Publisher', 'Year', 'OCN', 'PA Rights','File Name', 'Platform'], index=False, sep='\t')