# Form implementation generated from reading ui file 'c:\Users\hp\Desktop\VSC\Cloned\Ebook-PR-Application\source\program\driver\features\dropdown.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1141, 685)
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 50, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.institution = QtWidgets.QLabel(parent=Form)
        self.institution.setStyleSheet("font: 700 65pt \"Segoe UI\";")
        self.institution.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.institution.setObjectName("institution")
        self.horizontalLayout_2.addWidget(self.institution)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(100, -1, 100, 320)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.institutions = QtWidgets.QComboBox(parent=Form)
        self.institutions.setMinimumSize(QtCore.QSize(500, 50))
        self.institutions.setMaximumSize(QtCore.QSize(850, 60))
        self.institutions.setStyleSheet("QComboBox {\n"
"    /* Main styling for the combo box */\n"
"    background-color: #f0f0f0; /* Background color */\n"
"    border: 1px solid #999; /* Border color */\n"
"    padding: 5px; /* Padding inside the combo box */\n"
"    color: #333333;\n"
"    font-size: 20px; /* Replace with your desired font size */\n"
"    font-weight: bold; /* Make the text bold */\n"
"\n"
"\n"
"\n"
"    /* Dropdown button styling */\n"
"    QComboBox::drop-down {\n"
"        background-color: #ddd; /* Dropdown button background color */\n"
"        border: 1px solid #999; /* Dropdown button border color */\n"
"    }\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down:open {\n"
"    /* Styling when the dropdown is open */\n"
"    border: 1px solid #666;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"    /* Styling for the selection indicator (the small arrow on the right) */\n"
"    border: none;\n"
"}\n"
"")
        self.institutions.setObjectName("institutions")
        self.institutions.addItem("")
        self.institutions.setItemText(0, "")
        self.horizontalLayout_4.addWidget(self.institutions)
        self.submit_button_1 = QtWidgets.QPushButton(parent=Form)
        self.submit_button_1.setMinimumSize(QtCore.QSize(100, 60))
        self.submit_button_1.setMaximumSize(QtCore.QSize(150, 80))
        self.submit_button_1.setStyleSheet("font: 700 15pt \"Segoe UI\";")
        self.submit_button_1.setObjectName("submit_button_1")
        self.horizontalLayout_4.addWidget(self.submit_button_1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.institution.setText(_translate("Form", "Set Your Institution Below"))
        self.submit_button_1.setText(_translate("Form", "Submit"))
