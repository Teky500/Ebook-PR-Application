# Form implementation generated from reading ui file 'c:\Users\hp\Desktop\VSC\Cloned\Ebook-PR-Application\source\program\driver\features\homepage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1092, 683)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        Form.setStyleSheet("  QWidget {\n"
"        background-color: #333333;\n"
"        color: #ffffff;\n"
"        border: none;\n"
"    }\n"
"    QPushButton {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        border-radius: 4px;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #5a5a5a;\n"
"        border: 1px solid #5a5a5a;\n"
"    }\n"
"    QCheckBox {\n"
"        color: #ffffff;\n"
"    }\n"
"    QLineEdit {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QTextEdit {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QProgressBar {\n"
"        border: 1px solid #444444;\n"
"        border-radius: 7px;\n"
"        background-color: #2e2e2e;\n"
"        text-align: center;\n"
"        font-size: 10pt;\n"
"        color: white;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #3a3a3a;\n"
"        width: 5px;\n"
"    }\n"
"    QScrollBar:vertical {\n"
"        border: none;\n"
"        background-color: #3a3a3a;\n"
"        width: 10px;\n"
"        margin: 16px 0 16px 0;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #444444;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QScrollBar:horizontal {\n"
"        border: none;\n"
"        background-color: #3a3a3a;\n"
"        height: 10px;\n"
"        margin: 0px 16px 0 16px;\n"
"    }\n"
"    QScrollBar::handle:horizontal {\n"
"        background-color: #444444;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QTabWidget {\n"
"        background-color: #2e2e2e;\n"
"        border: none;\n"
"    }\n"
"    QTabBar::tab {\n"
"        background-color: #2e2e2e;\n"
"        color: #b1b1b1;\n"
"        padding: 8px 20px;\n"
"        border-top-left-radius: 5px;\n"
"        border-top-right-radius: 5px;\n"
"        border: none;\n"
"    }\n"
" \n"
"    QTabBar::tab:selected, QTabBar::tab:hover {\n"
"        background-color: #3a3a3a;\n"
"        color: white;\n"
"    }")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 50, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(1000, 208))
        self.label.setStyleSheet("font: 700 110pt \"Segoe UI\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(5, 50, 5, 300)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search = QtWidgets.QPushButton(parent=Form)
        self.search.setMinimumSize(QtCore.QSize(100, 60))
        self.search.setMaximumSize(QtCore.QSize(550, 80))
        self.search.setSizeIncrement(QtCore.QSize(0, 0))
        self.search.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.search.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.change = QtWidgets.QPushButton(parent=Form)
        self.change.setMinimumSize(QtCore.QSize(100, 60))
        self.change.setMaximumSize(QtCore.QSize(550, 80))
        self.change.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.change.setObjectName("change")
        self.horizontalLayout_2.addWidget(self.change)
        self.update = QtWidgets.QPushButton(parent=Form)
        self.update.setMinimumSize(QtCore.QSize(100, 60))
        self.update.setMaximumSize(QtCore.QSize(550, 80))
        self.update.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.update.setObjectName("update")
        self.horizontalLayout_2.addWidget(self.update)
        self.upload = QtWidgets.QPushButton(parent=Form)
        self.upload.setMinimumSize(QtCore.QSize(100, 60))
        self.upload.setMaximumSize(QtCore.QSize(550, 80))
        self.upload.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.upload.setObjectName("upload")
        self.horizontalLayout_2.addWidget(self.upload)
        self.unload = QtWidgets.QPushButton(parent=Form)
        self.unload.setMinimumSize(QtCore.QSize(100, 60))
        self.unload.setMaximumSize(QtCore.QSize(550, 80))
        self.unload.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.unload.setObjectName("unload")
        self.horizontalLayout_2.addWidget(self.unload)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "HOME PAGE"))
        self.search.setText(_translate("Form", "Search"))
        self.change.setText(_translate("Form", "Change"))
        self.update.setText(_translate("Form", "Update"))
        self.upload.setText(_translate("Form", "Upload"))
        self.unload.setText(_translate("Form", "Unload"))
