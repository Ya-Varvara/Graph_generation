from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ui.base_ui.FolderBtnWidget import Ui_folder_btn_widget


class FolderBtnWidget(QWidget):
    clicked_folder = pyqtSignal(int)

    def __init__(self, folder_id: int, folder_name: str, parent=None):
        super(FolderBtnWidget, self).__init__(parent)
        self.ui = Ui_folder_btn_widget()
        self.ui.setupUi(self)

        self.id = folder_id

        self.ui.folder_btn.setText(folder_name)
        self.ui.folder_btn.clicked.connect(self.btn_click)

    def btn_click(self):
        self.clicked_folder.emit(self.id)
