# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QHeaderView, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator, QIcon
from PyQt5.QtCore import QRegExp

from ui.base_ui.mainWindow import Ui_main_window
from ui.AddFolderDialog import AddFolderDialog
from ui.FolderBtnWidget import FolderBtnWidget
from ui.AddGraphDialog import AddGraphDialog
from db.db_handlers import DataBase
from db.save_handlers import to_dataframe, save_to_file
from generation.net_generation import generate_graph


class MainWindow(QWidget):
    current_widgets = []
    generated_graphs = []
    current_graph_id = 0
    current_folder_id = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icon.ico'))

        self.db = DataBase()

        self.folders = self.get_all_folders()
        # print(self.folders)

        self.set_frame_folders()

        self.ui.my_folders_btn.clicked.connect(self.set_frame_folders)
        self.ui.generation_btn.clicked.connect(self.set_frame_generation)
        self.ui.create_folder_btn.clicked.connect(self.set_add_folder_dialog)
        self.ui.generate_graph_btn.clicked.connect(self.check_generation_input)
        self.ui.close_graph_frame_button.clicked.connect(self.set_previous_widget)
        self.ui.add_graph_button.clicked.connect(self.set_add_graph_dialog)
        self.ui.back_to_folders_btn.clicked.connect(self.set_previous_widget)
        self.ui.graphs_table.cellDoubleClicked.connect(self.show_graph_from_table)
        self.ui.graph_num.textChanged.connect(self.show_full_generation_form)
        self.ui.delete_graph_button.clicked.connect(self.delete_graph)
        self.ui.delete_folder_btn.clicked.connect(self.delete_folder)
        self.ui.download_graphs_btn.clicked.connect(self.save_graphs_to_file)
        self.ui.save_graph_button.clicked.connect(self.save_one_graph)

        int_validator = QRegExpValidator(QRegExp(r'[0-9]+'))
        text_validator = QRegExpValidator(QRegExp(r'^[\w]+$'))

        self.ui.min_troughput.setValidator(int_validator)
        self.ui.max_troughput.setValidator(int_validator)
        self.ui.folder_name.setValidator(text_validator)
    # end def __init__

    def set_add_folder_dialog(self):
        # print("Окно для добавления папки")
        dialog = AddFolderDialog()
        dialog.show()
        if dialog.exec_():
            new_folder_name = dialog.new_folder_name
            if new_folder_name:
                with self.db:
                    self.db.add_folder(new_folder_name)
                    self.folders = self.db.get_folders()
                self.set_frame_folders()
    # end def set_add_folder_dialog

    def set_previous_widget(self):
        self.current_widgets = self.current_widgets[:-1]
        self.ui.stackedWidget.setCurrentWidget(self.current_widgets[-1])
    # end def set_previous_widget

    def set_frame_generation(self):
        # print("Фрейм с формой для генерации графа")
        self.current_widgets.clear()
        self.current_widgets.append(self.ui.generation_widget)

        self.ui.stackedWidget.setCurrentWidget(self.ui.generation_widget)

        self.ui.folder_name.clear()
        self.ui.nodes_num.cleanText()
        self.ui.graph_num.cleanText()
        self.ui.min_troughput.clear()
        self.ui.max_troughput.clear()

        self.ui.folder_name.hide()
        self.ui.label_folder_name.hide()
    # end def set_frame_generation

    def show_full_generation_form(self, value):
        if int(value) > 1:
            self.ui.folder_name.show()
            self.ui.label_folder_name.show()
        else:
            self.ui.folder_name.hide()
            self.ui.label_folder_name.hide()
    # end def show_full_generation_form

    def show_info_messagebox(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Осторожно!")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def check_generation_input(self):
        nodes_num = int(self.ui.nodes_num.text())
        graph_num = int(self.ui.graph_num.text())

        if self.ui.min_troughput.text() and self.ui.max_troughput.text():
            min_th = int(self.ui.min_troughput.text())
            max_th = int(self.ui.max_troughput.text())

            if max_th - min_th >= 10 and min_th > 0:
                if self.generated_graphs:
                    self.generated_graphs.clear()

                graph_data = None

                for _ in range(graph_num):
                    graph_data = generate_graph(nodes_num, min_th, max_th)
                    while not graph_data[0]:
                        graph_data = generate_graph(nodes_num, min_th, max_th)
                    self.generated_graphs.append(graph_data)

                if graph_num == 1:
                    self.set_frame_graph(graph_data)
                else:
                    new_folder_name = self.ui.folder_name.text().strip()

                    if new_folder_name:
                        with self.db:
                            self.db.add_folder(new_folder_name)
                            self.folders = self.db.get_folders()

                        folder_id = list(filter(lambda x: x[1] == new_folder_name, self.folders))[0][0]

                        with self.db:
                            for i in range(len(self.generated_graphs)):
                                check, net, nodes, cutA, cutB, cut, r_cut, max_flow = self.generated_graphs.pop()
                                graph_name = f'graph_{i+1}'
                                self.db.add_graph(graph_name, folder_id, net, nodes, cutA, cutB, cut, r_cut, max_flow)

                        self.ui.graph_num.setValue(self.ui.graph_num.minimum())
                        self.ui.nodes_num.setValue(self.ui.nodes_num.minimum())
                        self.ui.min_troughput.clear()
                        self.ui.max_troughput.clear()
                        self.ui.folder_name.clear()
                        self.ui.folder_name.hide()
                        self.ui.label_folder_name.hide()

                        self.set_frame_table_graph(folder_id)
                    else:
                        self.show_info_messagebox("Введите название папки")
                        # print("Enter new folder name")

            else:
                self.show_info_messagebox(f"Минимальная пропускная способность должна быть меньше максимальной!\nДля лучшего распределения разница между максимальным и минимальным значением должна быть больше 30")
                # print("max <= min")
        else:
            self.show_info_messagebox("Вы ввели не все значения")
            # print("No input")
        return
    # end def check_generation_input

    def set_frame_folders(self):
        # print("Фрейм с папками")
        self.ui.stackedWidget.setCurrentWidget(self.ui.my_folders_widget)
        self.current_widgets.clear()
        self.current_widgets.append(self.ui.my_folders_widget)

        self.clear_area()

        row, column = 0, 0
        for folder in self.folders:
            folder_btn = FolderBtnWidget(folder[0], folder[1])
            self.ui.gridLayoutFolderBtns.addWidget(folder_btn, row, column)
            folder_btn.clicked_folder.connect(self.set_frame_table_graph)
            column += 1
            if column == 4:
                row += 1
                column = 0
    # end def set_frame_folders

    def clear_area(self):
        while self.ui.gridLayoutFolderBtns.count() > 0:
            item = self.ui.gridLayoutFolderBtns.takeAt(0)
            item.widget().deleteLater()
    # end def clear_area

    def set_frame_graph(self, graph_data=None):
        # print("In graph frame")
        self.current_widgets.append(self.ui.graph_widget)
        self.ui.stackedWidget.setCurrentWidget(self.ui.graph_widget)

        if len(graph_data) == 8:
            check, net, nodes, cutA, cutB, cut, r_cut, max_flow = graph_data
            self.ui.add_graph_button.show()
            self.ui.save_graph_button.hide()
            self.ui.delete_graph_button.hide()
        else:
            graph_id, name, folder, net, nodes, max_flow, cutA, cutB, cut, r_cut = graph_data
            self.ui.add_graph_button.hide()
            self.ui.save_graph_button.show()
            self.ui.delete_graph_button.show()

        info = [f"Кол-во вершин: {nodes}",
                f"Максимальный поток: {max_flow}",
                f"Вершины, входящие в подмножество А: {cutA}",
                f"Вершины, входящие в подмножество В: {cutB}",
                f"Ребра разреза: {cut}",
                f"Обратные ребра разреза: {r_cut}"]

        self.ui.graph_info_textedit.clear()
        self.ui.graph_info_textedit.setText('\n'.join(info))

        self.ui.weights_table_3.clear()
        self.ui.weights_table_3.setRowCount(nodes)
        self.ui.weights_table_3.setColumnCount(nodes)
        labels = [f'x{node+1}' for node in range(nodes)]
        self.ui.weights_table_3.setHorizontalHeaderLabels(labels)
        self.ui.weights_table_3.setVerticalHeaderLabels(labels)
        header_hor = self.ui.weights_table_3.horizontalHeader()
        header_ver = self.ui.weights_table_3.verticalHeader()
        for i in range(nodes):
            header_ver.setSectionResizeMode(i, QHeaderView.Stretch)
            header_hor.setSectionResizeMode(i, QHeaderView.Stretch)

        for node in net:
            for x in net[node]:
                self.ui.weights_table_3.setItem(int(node), int(x), QTableWidgetItem(str(net[node][x])))
    # end def set_frame_graph

    def set_frame_table_graph(self, folder_id):
        self.current_widgets.append(self.ui.my_graphs_widget)
        self.ui.stackedWidget.setCurrentWidget(self.ui.my_graphs_widget)

        # print(self.current_widgets)

        self.current_folder_id = folder_id

        if folder_id == 1:
            self.ui.delete_folder_btn.hide()
        else:
            self.ui.delete_folder_btn.show()

        graphs = self.get_graph_from_db(folder_id)

        self.ui.graphs_table.setRowCount(len(graphs))
        self.ui.graphs_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for i in range(3):
            self.ui.graphs_table.horizontalHeader().setSectionResizeMode(i+1, QHeaderView.Stretch)

        for i, graph in enumerate(graphs):
            self.ui.graphs_table.setItem(i, 0, QTableWidgetItem(str(graph[0])))
            self.ui.graphs_table.setItem(i, 1, QTableWidgetItem(graph[1]))
            self.ui.graphs_table.setItem(i, 2, QTableWidgetItem(str(graph[2])))
            self.ui.graphs_table.setItem(i, 3, QTableWidgetItem(str(graph[3])))
    # end def set_frame_table_graph

    def show_graph_from_table(self, row, column):
        # print(row)
        graph_id = str(self.ui.graphs_table.item(row, 0).text())
        self.current_graph_id = graph_id
        # print(graph_id)
        with self.db:
            graph_info = tuple(self.db.get_graph(graph_id))
        # print(graph_info)
        self.set_frame_graph(graph_info)
    # end def show_graph_from_table

    def set_add_graph_dialog(self):
        dialog = AddGraphDialog(self.folders)
        dialog.show()
        if dialog.exec_():
            graph_name = dialog.new_graph_name
            folder_id = dialog.folder_id
            if graph_name:
                # print(self.generated_graphs)
                check, net, nodes, cutA, cutB, cut, r_cut, max_flow = self.generated_graphs.pop()
                # print(check, net, nodes, cutA, cutB, cut, r_cut, max_flow)
                # print(graph_name)
                with self.db:
                    # print("In db")
                    self.db.add_graph(graph_name, folder_id, net, nodes, cutA, cutB, cut, r_cut, max_flow)
                self.set_frame_generation()
    # end def set_add_graph_dialog

    def get_all_folders(self) -> list:
        # print("Get all folders")
        with self.db:
            return self.db.get_folders()
    # end def get_all_folders

    def get_graph_from_db(self, folder_id) -> list:
        with self.db:
            return self.db.get_graphs(folder_id)
    # end def get_graph_from_db

    def delete_graph(self):
        msg = QMessageBox.question(self, 'Удаление графа', "Вы действительно хотите удалить граф?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            with self.db:
                self.db.delete_graph(self.current_graph_id)
            # print(self.current_widgets)
            # self.current_widgets.pop().close()
            # self.current_widgets.pop().close()
            self.current_widgets = self.current_widgets[:-2]
            # print(self.current_widgets)
            # print(self.current_folder_id)
            self.set_frame_table_graph(self.current_folder_id)
    # end def delete_graph

    def delete_folder(self, folder_id):
        msg = QMessageBox.question(self, 'Удаление папки', "Вы действительно хотите удалить папку?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            with self.db:
                self.db.delete_folder(self.current_folder_id)

            self.folders = self.get_all_folders()
            # print(self.folders)

            self.current_widgets = self.current_widgets[:-1]
            # print(self.current_widgets)

            self.set_frame_folders()
    # end def delete_folder

    def save_graphs_to_file(self):
        file_name = self.save_file_dialog()
        if file_name == 0:
            return
        with self.db:
            graphs = self.db.get_graph_net(self.current_folder_id)
        df_list = []
        for graph in graphs:
            df_list.append(to_dataframe(graph[0]))
        save_to_file(df_list, file_name)
    # end def save_graphs_to_file

    def save_one_graph(self):
        file_name = self.save_file_dialog()
        if file_name == 0:
            return
        with self.db:
            graph = self.db.get_graph(self.current_graph_id)
        # print(graph)
        df_list = [to_dataframe(graph[3])]
        save_to_file(df_list, file_name)
    # end def save_one_graph

    def save_file_dialog(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Сохранение графов',
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls)',
            directory='new_file.xlsx'
        )
        # print(response)
        if response[0]:
            return response[0]
        else:
            # print("Return")
            return 0
    # end def save_file_dialog