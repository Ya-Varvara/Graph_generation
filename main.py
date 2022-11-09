import sys

from PyQt5.QtWidgets import *
from ui.mainWindow import Ui_main_window
from ui.AddFolderDialog import Ui_add_folder_dialog
from ui.AddGraphDialog import Ui_add_graph_dialog


class AddGraphDialog(QDialog):
    def __init__(self):
        super(AddGraphDialog, self).__init__()
        self.ui = Ui_add_graph_dialog()
        self.ui.setupUi(self)

        folders = ["test1", "test2"]

        self.new_graph_name = None
        self.folder_name = None

        self.ui.folders_box.addItems(folders)

        self.ui.buttonBox.accepted.connect(self.accept_data)
        self.ui.buttonBox.rejected.connect(self.reject_data)

    def accept_data(self):
        if self.ui.name_graph.text().strip():
            print("Приемлемо")
            self.new_graph_name = self.ui.name_graph.text().strip()
            self.folder_name = self.ui.folders_box.currentText()
            self.accept()
    
    def reject_data(self):
        print("Галя, у нас отмена!")
        self.close()
        
    def exec_(self):
        super(AddGraphDialog, self).exec_()
        return self.new_graph_name, self.folder_name       
        

class AddFolderDialog(QDialog):
    def __init__(self):
        super(AddFolderDialog, self).__init__()
        self.ui = Ui_add_folder_dialog()
        self.ui.setupUi(self)

        self.new_folder_name = None

        self.ui.buttonBox.accepted.connect(self.accept_data)
        self.ui.buttonBox.rejected.connect(self.reject_data)

    def accept_data(self):
        if self.ui.name_folder.text().strip():
            print("Приемлемо")
            self.new_folder_name = self.ui.name_folder.text().strip()
            self.accept()

    def reject_data(self):
        print("Галя, у нас отмена!")
        self.close()

    def exec_(self):
        super(AddFolderDialog, self).exec_()
        return self.new_folder_name


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
        self.ui.generation_frame.show()

    def set_frame_folders(self):
        print("Фрейм с папками")
        self.ui.generation_frame.hide()
        self.ui.my_folders_frame.show()

        folders = ["folder1", "folder2", "folder3"]




    def generate_graph(self):
        dialog = AddGraphDialog()
        dialog.show()
        new_graph_name, folder_name = dialog.exec_()
        print(new_graph_name, folder_name)

        # nodes_num = int(self.ui.nodes_num.text())
        # min_troughput = int(self.ui.min_troughput.text())
        # max_troughput = int(self.ui.max_troughput.text())
        # graph_num = int(self.ui.graph_num.text())
        # print(nodes_num, min_troughput, max_troughput, graph_num)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
