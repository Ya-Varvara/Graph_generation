from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHeaderView
from ui.base_ui.mainWindow import Ui_main_window
from ui.AddFolderDialog import AddFolderDialog
from ui.FolderBtnWidget import FolderBtnWidget
from ui.AddGraphDialog import AddGraphDialog
from db.db_handlers import DataBase
from generation.net_generation import generate_graph


class MainWindow(QWidget):
    current_widgets = []
    generated_graphs = []

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.ui.graph_widget.close()
        self.ui.my_graphs_widget.close()
        self.ui.generation_widget.close()
        self.ui.my_folders_widget.close()

        self.db = DataBase()

        self.folders = self.get_all_folders()
        print(self.folders)

        self.set_frame_folders()

        self.ui.my_folders_btn.clicked.connect(self.set_frame_folders)
        self.ui.generation_btn.clicked.connect(self.set_frame_generation)
        self.ui.create_folder_btn.clicked.connect(self.set_add_folder_dialog)
        self.ui.generate_graph_btn.clicked.connect(self.check_generation_input)
        self.ui.close_graph_frame_btn.clicked.connect(self.set_previous_widget)
        self.ui.add_graph_btn.clicked.connect(self.set_add_graph_dialog)
        self.ui.back_to_folders_btn.clicked.connect(self.set_previous_widget)
        self.ui.show_graph_btn.clicked.connect(self.set_frame_graph)
    # end def __init__

    def set_add_folder_dialog(self):
        print("Окно для добавления папки")
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
        self.current_widgets.pop().close()
        self.current_widgets[-1].show()
    # end def set_previous_widget

    def set_frame_generation(self):
        print("Фрейм с формой для генерации графа")
        while self.current_widgets:
            self.current_widgets.pop().close()
        self.current_widgets.append(self.ui.generation_widget)

        self.ui.generation_widget.show()

        self.ui.nodes_num.cleanText()
        self.ui.graph_num.cleanText()
        self.ui.min_troughput.clear()
        self.ui.max_troughput.clear()
    # end def set_frame_generation

    def check_generation_input(self):
        nodes_num = int(self.ui.nodes_num.text())
        graph_num = int(self.ui.graph_num.text())
        if self.ui.min_troughput.text() and self.ui.max_troughput.text():
            min_th = int(self.ui.min_troughput.text())
            max_th = int(self.ui.max_troughput.text())
            if max_th - min_th >= 10:
                if self.generated_graphs:
                    self.generated_graphs.clear()
                print(nodes_num, graph_num, min_th, max_th)
                graph_data = generate_graph(nodes_num, min_th, max_th)
                while not graph_data[0]:
                    graph_data = generate_graph(nodes_num, min_th, max_th)
                self.generated_graphs.append(graph_data)
                self.ui.nodes_num.cleanText()
                self.ui.graph_num.cleanText()
                self.ui.min_troughput.clear()
                self.ui.max_troughput.clear()
                self.set_frame_graph(graph_data)
            else:
                print("max <= min")
        else:
            print("No input")
        return
    # end def check_generation_input

    def set_frame_folders(self):
        print("Фрейм с папками")
        while self.current_widgets:
            self.current_widgets.pop().close()
        self.current_widgets.append(self.ui.my_folders_widget)
        self.ui.my_folders_widget.show()

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

    def set_frame_graph(self, graph_data=None):
        self.current_widgets[-1].close()
        self.current_widgets.append(self.ui.graph_widget)
        self.ui.graph_widget.show()

        check, net, nodes, cutA, cutB, cut, r_cut, max_flow = graph_data

        info = [f"Кол-во вершин: {nodes}",
                f"Максимальный поток: {max_flow}",
                f"Вершины, входящие в подмножество А: {cutA}",
                f"Вершины, входящие в подмножество В: {cutB}",
                f"Ребра разреза: {cut}",
                f"Обратные ребра разреза: {r_cut}"]

        self.ui.graph_info.clear()
        self.ui.graph_info.setText('\n'.join(info))

        self.ui.weights_table.clear()
        self.ui.weights_table.setRowCount(nodes)
        self.ui.weights_table.setColumnCount(nodes)
        labels = [f'x{node+1}' for node in range(nodes)]
        # print(lables)
        self.ui.weights_table.setHorizontalHeaderLabels(labels)
        self.ui.weights_table.setVerticalHeaderLabels(labels)
        header_hor = self.ui.weights_table.horizontalHeader()
        header_ver = self.ui.weights_table.verticalHeader()
        for i in range(nodes):
            header_ver.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            header_hor.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        # print(net)
        for node in net:
            for x in net[node]:
                self.ui.weights_table.setItem(node, x, QtWidgets.QTableWidgetItem(str(net[node][x])))
                # print(node, x)


        item_size = self.ui.weights_table.size()

        print(self.current_widgets)
        print("Graph info")
    # end def set_frame_graph

    def set_frame_table_graph(self, folser_id=None):
        self.current_widgets[-1].close()
        self.current_widgets.append(self.ui.my_graphs_widget)
        self.ui.my_graphs_widget.show()
    # end def set_frame_table_graph

    def set_add_graph_dialog(self):
        dialog = AddGraphDialog(self.folders)
        dialog.show()
        if dialog.exec_():
            graph_name = dialog.new_graph_name
            folder_id = dialog.folder_id
            if graph_name:
                print(self.generated_graphs)
                check, net, nodes, cutA, cutB, cut, r_cut, max_flow = self.generated_graphs.pop()
                print(check, net, nodes, cutA, cutB, cut, r_cut, max_flow)
                print(graph_name)
                with self.db:
                    print("In db")
                    self.db.add_graph(graph_name, folder_id, net, nodes, cutA, cutB, cut, r_cut, max_flow)
                self.set_frame_generation()
    # end def set_add_graph_dialog

    def get_all_folders(self) -> list:
        print("Get all folders")
        with self.db:
            return self.db.get_folders()
    # end def get_all_folders

