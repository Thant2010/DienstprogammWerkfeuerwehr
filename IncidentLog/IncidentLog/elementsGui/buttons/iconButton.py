from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton

from utilityClasses.shadowEffect import ShadowEffect
from globals import iconButtons

class IconButton(QPushButton):
    def __init__(self, key: str, size: int):
        super().__init__()
        self.setFixedSize(size, size)
        self.setIconSize(QSize(int(size * 0.75), int(size * 0.75)))
        self.setGraphicsEffect(ShadowEffect().shadow)
        self.setIcon(QIcon(iconButtons[key][0]))
        self.setToolTip(iconButtons[key][1])

        self.setProperty("buttonType", "icon")
