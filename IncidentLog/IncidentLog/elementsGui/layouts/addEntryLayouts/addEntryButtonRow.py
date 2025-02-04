from PyQt6.QtWidgets import QVBoxLayout

from elementsGui.buttons.iconButton import IconButton
from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager


class AddEntryButtonRow(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.__closeButton = IconButton("close", 40)
        self.__closeButton.clicked.connect(lambda: signalManager.on_entry_window_close.emit())
        self.__clearButton = IconButton("clear", 40)
        self.__clearButton.clicked.connect(lambda: signalManager.on_set_default_values.emit())
        self.__saveButton = IconButton("save", 40)
        self.__saveButton.clicked.connect(lambda: signalManager.on_save_entry_click.emit())

        self.addWidget(self.__saveButton)
        self.addWidget(self.__clearButton)
        self.addWidget(self.__closeButton)
        self.addItem(LayoutSpacer.verticalExpandingSpacer())
