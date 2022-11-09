# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        main_window.setMinimumSize(QtCore.QSize(800, 600))
        main_window.setMaximumSize(QtCore.QSize(800, 600))
        main_window.setStyleSheet("QMainWindow{\n"
                                  "    background-color: rgb(245, 242, 242);\n"
                                  "}\n"
                                  "\n"
                                  "QWidget{\n"
                                  "    background-color: rgb(245, 242, 242)\n"
                                  "}\n"
                                  "\n"
                                  "QFrame{\n"
                                  "    border-color: rgb(245, 242, 242);\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QTableWidget{\n"
                                  "    border: none\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton{\n"
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
                                  "\n"
                                  "QTextEdit{\n"
                                  "    border-width: 1px;\n"
                                  "    border-radius: 4px;\n"
                                  "    border-style: solid;\n"
                                  "    border-color: rgb(174, 171, 171);\n"
                                  "    margin: 1px;\n"
                                  "    padding: 2px;\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "QSpinBox{\n"
                                  "    border-width: 1px;\n"
                                  "    border-radius: 4px;\n"
                                  "    border-style: solid;\n"
                                  "    border-color: rgb(174, 171, 171);\n"
                                  "    margin: 1px;\n"
                                  "    padding: 2px;\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QSpinBox::up-button, QSpinBox::down-button { \n"
                                  "    width: 16px; \n"
                                  "}\n"
                                  "\n"
                                  "")
        self.my_folders_btn = QtWidgets.QPushButton(main_window)
        self.my_folders_btn.setGeometry(QtCore.QRect(10, 0, 120, 50))
        self.my_folders_btn.setMinimumSize(QtCore.QSize(120, 50))
        self.my_folders_btn.setMaximumSize(QtCore.QSize(120, 50))
        self.my_folders_btn.setObjectName("my_folders_btn")
        self.generation_btn = QtWidgets.QPushButton(main_window)
        self.generation_btn.setGeometry(QtCore.QRect(130, 0, 180, 50))
        self.generation_btn.setMinimumSize(QtCore.QSize(180, 50))
        self.generation_btn.setMaximumSize(QtCore.QSize(180, 50))
        self.generation_btn.setObjectName("generation_btn")
        self.my_folders_frame = QtWidgets.QFrame(main_window)
        self.my_folders_frame.setGeometry(QtCore.QRect(0, 50, 800, 550))
        self.my_folders_frame.setStyleSheet("")
        self.my_folders_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.my_folders_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.my_folders_frame.setObjectName("my_folders_frame")
        self.create_folder_btn = QtWidgets.QPushButton(self.my_folders_frame)
        self.create_folder_btn.setGeometry(QtCore.QRect(600, 30, 140, 40))
        self.create_folder_btn.setStyleSheet("")
        self.create_folder_btn.setObjectName("create_folder_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.my_folders_frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 740, 430))
        self.tableWidget.setMinimumSize(QtCore.QSize(740, 420))
        self.tableWidget.setMaximumSize(QtCore.QSize(740, 450))
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(180)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(180)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(180)
        self.generation_frame = QtWidgets.QFrame(main_window)
        self.generation_frame.setGeometry(QtCore.QRect(0, 50, 800, 550))
        self.generation_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.generation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generation_frame.setObjectName("generation_frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.generation_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 140, 401, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nodes_num = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nodes_num.sizePolicy().hasHeightForWidth())
        self.label_nodes_num.setSizePolicy(sizePolicy)
        self.label_nodes_num.setMinimumSize(QtCore.QSize(220, 40))
        self.label_nodes_num.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_nodes_num.setFont(font)
        self.label_nodes_num.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_nodes_num.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_nodes_num.setWordWrap(True)
        self.label_nodes_num.setObjectName("label_nodes_num")
        self.gridLayout.addWidget(self.label_nodes_num, 0, 0, 1, 1)
        self.graph_num = QtWidgets.QSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_num.sizePolicy().hasHeightForWidth())
        self.graph_num.setSizePolicy(sizePolicy)
        self.graph_num.setMinimumSize(QtCore.QSize(70, 27))
        self.graph_num.setObjectName("graph_num")
        self.graph_num.setMinimum(1)
        self.graph_num.setMaximum(30)
        self.gridLayout.addWidget(self.graph_num, 3, 1, 1, 1)
        self.label_min_troughput = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_min_troughput.sizePolicy().hasHeightForWidth())
        self.label_min_troughput.setSizePolicy(sizePolicy)
        self.label_min_troughput.setMinimumSize(QtCore.QSize(220, 40))
        self.label_min_troughput.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_min_troughput.setFont(font)
        self.label_min_troughput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_min_troughput.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_min_troughput.setWordWrap(True)
        self.label_min_troughput.setObjectName("label_min_troughput")
        self.gridLayout.addWidget(self.label_min_troughput, 1, 0, 1, 1)
        self.label_graph_num = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_graph_num.sizePolicy().hasHeightForWidth())
        self.label_graph_num.setSizePolicy(sizePolicy)
        self.label_graph_num.setMinimumSize(QtCore.QSize(220, 40))
        self.label_graph_num.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_graph_num.setFont(font)
        self.label_graph_num.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_graph_num.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_graph_num.setWordWrap(True)
        self.label_graph_num.setObjectName("label_graph_num")
        self.gridLayout.addWidget(self.label_graph_num, 3, 0, 1, 1)
        self.nodes_num = QtWidgets.QSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodes_num.sizePolicy().hasHeightForWidth())
        self.nodes_num.setSizePolicy(sizePolicy)
        self.nodes_num.setMinimumSize(QtCore.QSize(70, 27))
        self.nodes_num.setObjectName("nodes_num")
        self.nodes_num.setMinimum(7)
        self.nodes_num.setMaximum(15)
        self.gridLayout.addWidget(self.nodes_num, 0, 1, 1, 1)
        self.label_max_throughput = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_max_throughput.sizePolicy().hasHeightForWidth())
        self.label_max_throughput.setSizePolicy(sizePolicy)
        self.label_max_throughput.setMinimumSize(QtCore.QSize(220, 40))
        self.label_max_throughput.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_max_throughput.setFont(font)
        self.label_max_throughput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_max_throughput.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_max_throughput.setWordWrap(True)
        self.label_max_throughput.setObjectName("label_max_throughput")
        self.gridLayout.addWidget(self.label_max_throughput, 2, 0, 1, 1)
        self.min_troughput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_troughput.sizePolicy().hasHeightForWidth())
        self.min_troughput.setSizePolicy(sizePolicy)
        self.min_troughput.setMinimumSize(QtCore.QSize(70, 27))
        self.min_troughput.setMaximumSize(QtCore.QSize(60, 23))
        self.min_troughput.setObjectName("min_troughput")
        self.gridLayout.addWidget(self.min_troughput, 1, 1, 1, 1)
        self.max_troughput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_troughput.sizePolicy().hasHeightForWidth())
        self.max_troughput.setSizePolicy(sizePolicy)
        self.max_troughput.setMinimumSize(QtCore.QSize(70, 27))
        self.max_troughput.setMaximumSize(QtCore.QSize(60, 23))
        self.max_troughput.setObjectName("max_troughput")
        self.gridLayout.addWidget(self.max_troughput, 2, 1, 1, 1)
        self.generate_graph_btn = QtWidgets.QPushButton(self.generation_frame)
        self.generate_graph_btn.setGeometry(QtCore.QRect(330, 400, 140, 40))
        self.generate_graph_btn.setMinimumSize(QtCore.QSize(100, 20))
        self.generate_graph_btn.setMaximumSize(QtCore.QSize(180, 50))
        self.generate_graph_btn.setObjectName("generate_graph_btn")
        self.graph_frame = QtWidgets.QFrame(main_window)
        self.graph_frame.setGeometry(QtCore.QRect(0, 50, 800, 550))
        self.graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_frame.setObjectName("graph_frame")
        self.textEdit = QtWidgets.QTextEdit(self.graph_frame)
        self.textEdit.setGeometry(QtCore.QRect(480, 50, 300, 300))
        self.textEdit.setObjectName("textEdit")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.graph_frame)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 50, 450, 450))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(450, 450))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setRowCount(13)
        self.tableWidget_2.setColumnCount(13)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(32)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setVisible(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(32)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.close_graph_frame_btn = QtWidgets.QPushButton(self.graph_frame)
        self.close_graph_frame_btn.setGeometry(QtCore.QRect(505, 435, 250, 35))
        self.close_graph_frame_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.close_graph_frame_btn.setMaximumSize(QtCore.QSize(300, 50))
        self.close_graph_frame_btn.setObjectName("close_graph_frame_btn")
        self.save_graph_btn = QtWidgets.QPushButton(self.graph_frame)
        self.save_graph_btn.setGeometry(QtCore.QRect(635, 390, 120, 35))
        self.save_graph_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.save_graph_btn.setMaximumSize(QtCore.QSize(300, 50))
        self.save_graph_btn.setObjectName("save_graph_btn")
        self.add_graph_btn = QtWidgets.QPushButton(self.graph_frame)
        self.add_graph_btn.setGeometry(QtCore.QRect(505, 390, 120, 35))
        self.add_graph_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.add_graph_btn.setMaximumSize(QtCore.QSize(120, 50))
        self.add_graph_btn.setObjectName("add_graph_btn")
        self.my_folders_btn.raise_()
        self.generation_btn.raise_()
        self.graph_frame.raise_()
        self.my_folders_frame.raise_()
        self.generation_frame.raise_()

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Генерация графов"))
        self.my_folders_btn.setText(_translate("main_window", "Мои графы"))
        self.generation_btn.setText(_translate("main_window", "Сгенерировать граф"))
        self.create_folder_btn.setText(_translate("main_window", "Создать папку"))
        self.label_nodes_num.setText(_translate("main_window", "Количество вершин"))
        self.label_min_troughput.setText(_translate("main_window", "Минимальная пропускная способность"))
        self.label_graph_num.setText(_translate("main_window", "Количество графов"))
        self.label_max_throughput.setText(_translate("main_window", "Максимальная пропускная способность"))
        self.generate_graph_btn.setText(_translate("main_window", "Сгенерировать"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.close_graph_frame_btn.setText(_translate("main_window", "Закрыть"))
        self.save_graph_btn.setText(_translate("main_window", "Скачать граф"))
        self.add_graph_btn.setText(_translate("main_window", "Сохранить граф"))
