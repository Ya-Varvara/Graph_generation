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
"    \n"
"QWidget{\n"
"    background-color: rgb(245, 242, 242)\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: rgba(255, 255, 255, 127);\n"
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
"\n"
"QScrollArea{\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
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
        self.my_folders_widget = QtWidgets.QWidget(main_window)
        self.my_folders_widget.setGeometry(QtCore.QRect(0, 50, 800, 550))
        self.my_folders_widget.setStyleSheet("")
        self.my_folders_widget.setObjectName("my_folders_widget")
        self.create_folder_btn = QtWidgets.QPushButton(self.my_folders_widget)
        self.create_folder_btn.setGeometry(QtCore.QRect(600, 30, 140, 40))
        self.create_folder_btn.setStyleSheet("")
        self.create_folder_btn.setObjectName("create_folder_btn")
        self.scrollArea = QtWidgets.QScrollArea(self.my_folders_widget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 90, 740, 430))
        self.scrollArea.setMinimumSize(QtCore.QSize(740, 430))
        self.scrollArea.setMaximumSize(QtCore.QSize(740, 430))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaFolderBtns = QtWidgets.QWidget()
        self.scrollAreaFolderBtns.setGeometry(QtCore.QRect(0, 0, 740, 430))
        self.scrollAreaFolderBtns.setObjectName("scrollAreaFolderBtns")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaFolderBtns)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayoutFolderBtns = QtWidgets.QGridLayout()
        self.gridLayoutFolderBtns.setObjectName("gridLayoutFolderBtns")
        self.gridLayout_3.addLayout(self.gridLayoutFolderBtns, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaFolderBtns)
        self.line_3 = QtWidgets.QFrame(self.my_folders_widget)
        self.line_3.setGeometry(QtCore.QRect(0, 0, 800, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.generation_widget = QtWidgets.QWidget(main_window)
        self.generation_widget.setGeometry(QtCore.QRect(0, 50, 800, 550))
        self.generation_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.generation_widget.setObjectName("generation_widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.generation_widget)
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
        self.label_nodes_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.graph_num.setMinimum(1)
        self.graph_num.setMaximum(30)
        self.graph_num.setObjectName("graph_num")
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
        self.label_min_troughput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.label_graph_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.nodes_num.setMinimum(7)
        self.nodes_num.setMaximum(15)
        self.nodes_num.setObjectName("nodes_num")
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
        self.label_max_throughput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.min_troughput.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.min_troughput.setInputMask("")
        self.min_troughput.setFrame(True)
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
        self.generate_graph_btn = QtWidgets.QPushButton(self.generation_widget)
        self.generate_graph_btn.setGeometry(QtCore.QRect(330, 400, 140, 40))
        self.generate_graph_btn.setMinimumSize(QtCore.QSize(100, 20))
        self.generate_graph_btn.setMaximumSize(QtCore.QSize(180, 50))
        self.generate_graph_btn.setObjectName("generate_graph_btn")
        self.line = QtWidgets.QFrame(self.generation_widget)
        self.line.setGeometry(QtCore.QRect(0, 0, 800, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.graph_widget = QtWidgets.QWidget(main_window)
        self.graph_widget.setGeometry(QtCore.QRect(0, 50, 800, 550))
        self.graph_widget.setObjectName("graph_widget")
        self.graph_info = QtWidgets.QTextEdit(self.graph_widget)
        self.graph_info.setGeometry(QtCore.QRect(480, 50, 300, 300))
        self.graph_info.setObjectName("graph_info")
        self.weights_table = QtWidgets.QTableWidget(self.graph_widget)
        self.weights_table.setEnabled(True)
        self.weights_table.setGeometry(QtCore.QRect(20, 50, 450, 450))
        self.weights_table.setMaximumSize(QtCore.QSize(450, 450))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.weights_table.setFont(font)
        self.weights_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.weights_table.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.weights_table.setFrameShape(QtWidgets.QFrame.HLine)
        self.weights_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weights_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.weights_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.weights_table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.weights_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.weights_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.weights_table.setGridStyle(QtCore.Qt.SolidLine)
        self.weights_table.setWordWrap(True)
        self.weights_table.setCornerButtonEnabled(True)
        self.weights_table.setRowCount(7)
        self.weights_table.setColumnCount(7)
        self.weights_table.setObjectName("weights_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.weights_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.weights_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.weights_table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.weights_table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.weights_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.weights_table.setItem(5, 2, item)
        self.weights_table.horizontalHeader().setVisible(True)
        self.weights_table.horizontalHeader().setCascadingSectionResizes(False)
        self.weights_table.horizontalHeader().setDefaultSectionSize(30)
        self.weights_table.horizontalHeader().setHighlightSections(False)
        self.weights_table.horizontalHeader().setMinimumSectionSize(0)
        self.weights_table.horizontalHeader().setSortIndicatorShown(False)
        self.weights_table.verticalHeader().setVisible(True)
        self.weights_table.verticalHeader().setCascadingSectionResizes(True)
        self.weights_table.verticalHeader().setDefaultSectionSize(30)
        self.weights_table.verticalHeader().setHighlightSections(False)
        self.weights_table.verticalHeader().setMinimumSectionSize(0)
        self.weights_table.verticalHeader().setSortIndicatorShown(False)
        self.weights_table.verticalHeader().setStretchLastSection(False)
        self.close_graph_frame_btn = QtWidgets.QPushButton(self.graph_widget)
        self.close_graph_frame_btn.setGeometry(QtCore.QRect(505, 435, 250, 35))
        self.close_graph_frame_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.close_graph_frame_btn.setMaximumSize(QtCore.QSize(300, 50))
        self.close_graph_frame_btn.setObjectName("close_graph_frame_btn")
        self.save_graph_btn = QtWidgets.QPushButton(self.graph_widget)
        self.save_graph_btn.setGeometry(QtCore.QRect(635, 390, 120, 35))
        self.save_graph_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.save_graph_btn.setMaximumSize(QtCore.QSize(300, 50))
        self.save_graph_btn.setObjectName("save_graph_btn")
        self.add_graph_btn = QtWidgets.QPushButton(self.graph_widget)
        self.add_graph_btn.setGeometry(QtCore.QRect(505, 390, 120, 35))
        self.add_graph_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.add_graph_btn.setMaximumSize(QtCore.QSize(120, 50))
        self.add_graph_btn.setObjectName("add_graph_btn")
        self.line_2 = QtWidgets.QFrame(self.graph_widget)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 800, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.my_graphs_widget = QtWidgets.QWidget(main_window)
        self.my_graphs_widget.setGeometry(QtCore.QRect(0, 50, 800, 550))
        self.my_graphs_widget.setStyleSheet("")
        self.my_graphs_widget.setObjectName("my_graphs_widget")
        self.download_graphs_btn = QtWidgets.QPushButton(self.my_graphs_widget)
        self.download_graphs_btn.setGeometry(QtCore.QRect(600, 30, 140, 40))
        self.download_graphs_btn.setStyleSheet("")
        self.download_graphs_btn.setObjectName("download_graphs_btn")
        self.line_4 = QtWidgets.QFrame(self.my_graphs_widget)
        self.line_4.setGeometry(QtCore.QRect(0, 0, 800, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.graphs_table = QtWidgets.QTableWidget(self.my_graphs_widget)
        self.graphs_table.setGeometry(QtCore.QRect(30, 90, 740, 420))
        self.graphs_table.setMinimumSize(QtCore.QSize(740, 420))
        self.graphs_table.setMaximumSize(QtCore.QSize(740, 420))
        self.graphs_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphs_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphs_table.setMidLineWidth(0)
        self.graphs_table.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.graphs_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.graphs_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.graphs_table.setObjectName("graphs_table")
        self.graphs_table.setColumnCount(4)
        self.graphs_table.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.graphs_table.setHorizontalHeaderItem(3, item)
        self.graphs_table.horizontalHeader().setCascadingSectionResizes(True)
        self.graphs_table.horizontalHeader().setDefaultSectionSize(144)
        self.graphs_table.horizontalHeader().setMinimumSectionSize(32)
        self.graphs_table.horizontalHeader().setSortIndicatorShown(False)
        self.graphs_table.horizontalHeader().setStretchLastSection(False)
        self.graphs_table.verticalHeader().setVisible(False)
        self.graphs_table.verticalHeader().setCascadingSectionResizes(False)
        self.graphs_table.verticalHeader().setDefaultSectionSize(30)
        self.graphs_table.verticalHeader().setHighlightSections(False)
        self.graphs_table.verticalHeader().setMinimumSectionSize(30)
        self.graphs_table.verticalHeader().setSortIndicatorShown(False)
        self.graphs_table.verticalHeader().setStretchLastSection(False)
        self.back_to_folders_btn = QtWidgets.QPushButton(self.my_graphs_widget)
        self.back_to_folders_btn.setGeometry(QtCore.QRect(40, 30, 40, 40))
        self.back_to_folders_btn.setStyleSheet("")
        self.back_to_folders_btn.setObjectName("back_to_folders_btn")

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
        __sortingEnabled = self.weights_table.isSortingEnabled()
        self.weights_table.setSortingEnabled(False)
        self.weights_table.setSortingEnabled(__sortingEnabled)
        self.close_graph_frame_btn.setText(_translate("main_window", "Закрыть"))
        self.save_graph_btn.setText(_translate("main_window", "Скачать граф"))
        self.add_graph_btn.setText(_translate("main_window", "Сохранить граф"))
        self.download_graphs_btn.setText(_translate("main_window", "Скачать графы"))
        item = self.graphs_table.verticalHeaderItem(0)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(1)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(2)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(3)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(4)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(5)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(6)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(7)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(8)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(9)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(10)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(11)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(12)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.verticalHeaderItem(13)
        item.setText(_translate("main_window", "New Row"))
        item = self.graphs_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "ID"))
        item = self.graphs_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Название"))
        item = self.graphs_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Количество вершин"))
        item = self.graphs_table.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "Максимальный поток"))
        self.back_to_folders_btn.setText(_translate("main_window", "<-"))
