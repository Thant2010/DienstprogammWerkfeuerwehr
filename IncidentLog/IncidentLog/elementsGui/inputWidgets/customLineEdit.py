from PyQt6.QtWidgets import QLineEdit


class CustomLineEdit(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setProperty("fontsize", "medium")
