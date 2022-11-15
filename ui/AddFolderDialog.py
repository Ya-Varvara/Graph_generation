from PyQt5.QtWidgets import QDialog
from ui.base_ui.AddFolderDialog import Ui_add_folder_dialog


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
