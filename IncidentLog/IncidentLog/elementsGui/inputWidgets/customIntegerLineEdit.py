from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QLineEdit


class CustomIntegerLineEdit(QLineEdit):

    def __init__(self):
        super().__init__()
        intValidator = QIntValidator(0, 999, self)
        self.setValidator(intValidator)
        self.setMaxLength(3)
        self.setFixedWidth(100)
        self.setProperty("fontsize", "medium")

