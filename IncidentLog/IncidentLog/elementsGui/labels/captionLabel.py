from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel


class CaptionLabel(QLabel):

    def __init__(self, caption):
        super().__init__()
        self.setText(caption)
        self.setProperty("fontsize", "medium")
        self.setProperty("weight", "bold")
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)