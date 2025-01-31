from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.buttons.iconButton import IconButton
from utilityClasses.SignalManager import signalManager

class ButtonLayoutRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.__closeButton = IconButton("close")
        self.__closeButton.clicked.connect(lambda: signalManager.on_entry_window_close.emit())
        self.__clearButton = IconButton("clear")
        self.__clearButton.clicked.connect(lambda: signalManager.on_set_default_values.emit())
        self.__saveButton = IconButton("save")
        self.__saveButton.clicked.connect(lambda: signalManager.on_save_entry_click.emit())

        self.addWidget(self.__saveButton)
        self.addWidget(self.__clearButton)
        self.addWidget(self.__closeButton)
