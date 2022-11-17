from PyQt5.QtWidgets import QWidget
from ui.base_ui.mainWindow import Ui_main_window
from ui.AddFolderDialog import AddFolderDialog
from ui.FolderBtnWidget import FolderBtnWidget
from ui.AddGraphDialog import AddGraphDialog
from db.db_handlers import DataBase


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.ui.graph_frame.close()
        self.ui.my_graphs_frame.close()
        self.ui.generation_frame.close()
        self.ui.my_folders_frame.close()

        self.db = DataBase()

        self.folders = self.get_all_folders()
        print(self.folders)

        self.set_frame_folders()

        self.ui.my_folders_btn.clicked.connect(self.set_frame_folders)
        self.ui.generation_btn.clicked.connect(self.set_frame_generation)

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


    def set_frame_generation(self):
        print("Фрейм с формой для генерации графа")
        self.ui.my_folders_frame.close()
        self.ui.graph_frame.close()
        self.ui.my_graphs_frame.close()
        self.ui.generation_frame.show()

    def set_frame_folders(self):
        print("Фрейм с папками")
        self.ui.generation_frame.close()
        self.ui.graph_frame.close()
        self.ui.my_graphs_frame.close()
        self.ui.my_folders_frame.show()

        self.ui.create_folder_btn.clicked.connect(self.set_add_folder_dialog)

        row, column = 0, 0
        for folder in self.folders:
            folder_btn = FolderBtnWidget(folder[0], folder[1])
            self.ui.gridLayoutFolderBtns.addWidget(folder_btn, row, column)
            folder_btn.clicked_folder.connect(self.set_frame_my_graphs)
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
        self.set_frame_folders()

    def get_all_folders(self) -> list:
        print("Get all folders")
        with self.db:
            return self.db.get_folders()

