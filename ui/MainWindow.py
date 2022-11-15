from PyQt5.QtWidgets import QWidget
from ui.base_ui.mainWindow import Ui_main_window
from ui.AddFolderDialog import AddFolderDialog
from ui.FolderBtnWidget import FolderBtnWidget
from ui.AddGraphDialog import AddGraphDialog

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.set_frame_folders()

        self.ui.create_folder_btn.clicked.connect(self.set_add_folder_dialog)
        self.ui.my_folders_btn.clicked.connect(self.set_frame_folders)
        self.ui.generation_btn.clicked.connect(self.set_frame_generation)
        self.ui.generate_graph_btn.clicked.connect(self.generate_graph)

    def set_add_folder_dialog(self):
        print("Окно для добавления папки")
        dialog = AddFolderDialog()
        dialog.show()
        new_folder_name = dialog.exec_()
        print(new_folder_name)

    def set_frame_generation(self):
        print("Фрейм с формой для генерации графа")
        self.ui.my_folders_frame.hide()
        self.ui.graph_frame.hide()
        self.ui.generation_frame.show()

    def set_frame_folders(self):
        print("Фрейм с папками")
        self.ui.graph_frame.hide()
        self.ui.my_graphs_frame.hide()
        self.ui.generation_frame.hide()
        self.ui.my_folders_frame.show()

        folders = ["folder", "folder", "folder", "folder", "folder", "folder", "folder",
                   "folder", "folder", "folder", "folder", "folder", "folder", "folder",
                   "folder", "folder", "folder", "folder", "folder"]
        row = 0
        column = 0
        count = 0
        for folder in folders:
            folder_btn = FolderBtnWidget(count, folder)
            self.ui.gridLayoutFolderBtns.addWidget(folder_btn, row, column)
            folder_btn.clicked_folder.connect(self.set_frame_my_graphs)
            count += 1
            column += 1
            if column == 4:
                row += 1
                column = 0

    def set_frame_my_graphs(self, folder_id):
        print(f"Frame with graphs from folder {folder_id}")

    def generate_graph(self):
        self.ui.generation_frame.hide()
        self.ui.graph_frame.show()
        self.ui.close_graph_frame_btn.clicked.connect(self.set_frame_generation)
        self.ui.add_graph_btn.clicked.connect(self.set_add_graph_dialog)

    def set_add_graph_dialog(self):
        dialog = AddGraphDialog()
        dialog.show()
        new_graph_name, folder_name = dialog.exec_()
        print(new_graph_name, folder_name)

        # nodes_num = int(self.ui.nodes_num.text())
        # min_troughput = int(self.ui.min_troughput.text())
        # max_troughput = int(self.ui.max_troughput.text())
        # graph_num = int(self.ui.graph_num.text())
        # print(nodes_num, min_troughput, max_troughput, graph_num)
