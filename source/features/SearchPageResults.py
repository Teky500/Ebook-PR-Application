import csv
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog
import pandas as pd
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
        if itemData == []:
            print('Nothing Found')
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

            header_labels = ['eISBN', 'Title', 'Publisher', 'Year', 'OCN', 'PA Rights','File Path']
            self.model.setHeaderLabels(header_labels)


            self.table.resizeColumnsToContents()

            layout.addWidget(self.table)

            # Add a button for downloading
            self.download_button = QPushButton("Download")
            layout.addWidget(self.download_button)
            self.downloadType = 1
            self.download_button.clicked.connect(self.downloadTable) # backend function here 


    def downloadTable(self):
        # Get the file path using a file dialog
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV Files (*.csv);;TSV Files (*.tsv)')
        download_type = 0
        if file_path.endswith('.tsv'):
            download_type = 1
        if file_path:
            # Determine delimiter based on file extension
            if download_type == 0:
                df = pd.DataFrame(self.data)
                df[0] = df[0].astype(float).map(lambda x: '{:.0f}'.format(x))
                df[0] = df[0].astype(str)
                df.to_csv(file_path, header= ['eISBN', 'Title', 'Publisher', 'Year', 'OCN', 'PA Rights','File Path'], index=False)
            if download_type == 1:
                df = pd.DataFrame(self.data)
                df[0] = df[0].astype(float).map(lambda x: '{:.0f}'.format(x))
                df[0] = df[0].astype(str)
                df.to_csv(file_path, header= ['eISBN', 'Title', 'Publisher', 'Year', 'OCN', 'PA Rights','File Path'], index=False, sep='\t')