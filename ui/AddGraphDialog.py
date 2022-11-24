from PyQt5.QtWidgets import QDialog
from ui.base_ui.AddGraphDialog import Ui_add_graph_dialog


class AddGraphDialog(QDialog):
    def __init__(self, folders_info):
        super(AddGraphDialog, self).__init__()
        self.ui = Ui_add_graph_dialog()
        self.ui.setupUi(self)

        self.folders = folders_info
        folder_names = [folder[1] for folder in folders_info]

        self.new_graph_name = None
        self.folder_id = None

        self.ui.folders_box.addItems(folder_names)

        self.ui.buttonBox.accepted.connect(self.accept_data)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept_data(self):
        if self.ui.name_graph.text().strip():
            print("Приемлемо")
            self.new_graph_name = self.ui.name_graph.text().strip()
            folder_name = self.ui.folders_box.currentText()
            self.folder_id = list(filter(lambda x: x[1] == folder_name, self.folders))[0][0]
            print('FOLDER_ID', self.folder_id)
            self.accept()
        else:
            return
