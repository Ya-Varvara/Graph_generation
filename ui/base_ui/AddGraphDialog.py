# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddGraphDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_graph_dialog(object):
    def setupUi(self, add_graph_dialog):
        add_graph_dialog.setObjectName("add_graph_dialog")
        add_graph_dialog.resize(400, 250)
        add_graph_dialog.setMinimumSize(QtCore.QSize(400, 250))
        add_graph_dialog.setMaximumSize(QtCore.QSize(400, 250))
        add_graph_dialog.setStatusTip("")
        add_graph_dialog.setWhatsThis("")
        add_graph_dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame{\n"
"    border-color: rgb(245, 242, 242);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    width: 70px;\n"
"    height: 23px;\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 8px;\n"
"    border-color: rgb(174, 171, 171);\n"
"    border-style: solid;\n"
"    background-color: rgb(255, 255, 255);\n"
"    margin: 1px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    width: 70px;\n"
"    height: 23px;\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 8px;\n"
"    border-color: rgb(174, 171, 171);\n"
"    border-style: solid;\n"
"    background-color: rgb(249, 247, 247);\n"
"    margin: 1px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: rgb(174, 171, 171);\n"
"    margin: 1px;\n"
"    padding: 2px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: rgb(174, 171, 171);\n"
"    margin: 1px;\n"
"    padding: 2px;\n"
"}\n"
"")
        add_graph_dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonBox = QtWidgets.QDialogButtonBox(add_graph_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 170, 400, 60))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(add_graph_dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 361, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.name_graph_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_graph_label.sizePolicy().hasHeightForWidth())
        self.name_graph_label.setSizePolicy(sizePolicy)
        self.name_graph_label.setMinimumSize(QtCore.QSize(100, 30))
        self.name_graph_label.setMaximumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.name_graph_label.setFont(font)
        self.name_graph_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_graph_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_graph_label.setWordWrap(True)
        self.name_graph_label.setObjectName("name_graph_label")
        self.gridLayout.addWidget(self.name_graph_label, 0, 0, 1, 1)
        self.name_folder_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_folder_label.sizePolicy().hasHeightForWidth())
        self.name_folder_label.setSizePolicy(sizePolicy)
        self.name_folder_label.setMinimumSize(QtCore.QSize(100, 30))
        self.name_folder_label.setMaximumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.name_folder_label.setFont(font)
        self.name_folder_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_folder_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_folder_label.setWordWrap(True)
        self.name_folder_label.setObjectName("name_folder_label")
        self.gridLayout.addWidget(self.name_folder_label, 1, 0, 1, 1)
        self.name_graph = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_graph.sizePolicy().hasHeightForWidth())
        self.name_graph.setSizePolicy(sizePolicy)
        self.name_graph.setMinimumSize(QtCore.QSize(200, 23))
        self.name_graph.setMaximumSize(QtCore.QSize(10000, 23))
        self.name_graph.setObjectName("name_graph")
        self.gridLayout.addWidget(self.name_graph, 0, 1, 1, 1)
        self.folders_box = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folders_box.sizePolicy().hasHeightForWidth())
        self.folders_box.setSizePolicy(sizePolicy)
        self.folders_box.setMinimumSize(QtCore.QSize(200, 23))
        self.folders_box.setMaximumSize(QtCore.QSize(16777215, 23))
        self.folders_box.setObjectName("folders_box")
        self.gridLayout.addWidget(self.folders_box, 1, 1, 1, 1)

        self.retranslateUi(add_graph_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_graph_dialog)

    def retranslateUi(self, add_graph_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_graph_dialog.setWindowTitle(_translate("add_graph_dialog", "Сохранение графа"))
        self.name_graph_label.setText(_translate("add_graph_dialog", "Название графа"))
        self.name_folder_label.setText(_translate("add_graph_dialog", "Папка"))
