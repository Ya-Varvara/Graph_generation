from PyQt5.QtWidgets import QDialog
from ui.base_ui.AddGraphDialog import Ui_add_graph_dialog


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
