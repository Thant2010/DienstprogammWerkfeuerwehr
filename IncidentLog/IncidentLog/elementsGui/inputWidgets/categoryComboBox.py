from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox

from globals import categorys

class CategoryComboBox(QComboBox):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 30)
        self.setProperty("selectable", True)
        self.setMaxVisibleItems(len(categorys) + 1)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.addItem("---")
        for category in categorys:
            self.addItem(category)