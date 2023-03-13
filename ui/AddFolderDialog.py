from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog
from ui.base_ui.AddFolderDialog import Ui_add_folder_dialog


class AddFolderDialog(QDialog):
    def __init__(self):
        super(AddFolderDialog, self).__init__()
        self.ui = Ui_add_folder_dialog()
        self.ui.setupUi(self)

        # self.ui.buttonBox.StandardButton.Save.

        text_validator = QRegExpValidator(QRegExp(r'^[\w]+$'))
        self.ui.name_folder.setValidator(text_validator)

        self.new_folder_name = None

        self.ui.buttonBox.accepted.connect(self.accept_data)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept_data(self):
        if self.ui.name_folder.text().strip():
            print("Приемлемо")
            self.new_folder_name = self.ui.name_folder.text().strip()
            self.accept()
        else:
            return
