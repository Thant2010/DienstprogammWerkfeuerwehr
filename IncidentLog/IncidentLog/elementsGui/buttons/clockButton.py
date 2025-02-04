from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton

from utilityClasses.signalManager import signalManager

class ClockButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setFixedSize(30, 30)
        self.setIcon(QIcon('icons/clock.svg'))
        self.setIconSize(QSize(20, 20))
        self.setProperty("buttonType", "clock")
        self.setToolTip("Aktuelle Zeit setzen")

        self.clicked.connect(lambda: signalManager.on_set_time_click.emit())