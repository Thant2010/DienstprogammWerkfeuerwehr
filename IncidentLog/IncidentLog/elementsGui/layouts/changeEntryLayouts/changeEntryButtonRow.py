from PyQt6.QtWidgets import QVBoxLayout

from elementsGui.buttons.iconButton import IconButton
from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager


class ChangeEntryButtonRow(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.__saveButton = IconButton("save", 40)
        self.__saveButton.clicked.connect(signalManager.on_save_changes_click.emit)

        self.__closeButton = IconButton("close", 40)
        self.__closeButton.clicked.connect(signalManager.on_change_entry_window_close.emit)

        self.addWidget(self.__saveButton)
        self.addWidget(self.__closeButton)
        self.addItem(LayoutSpacer.verticalExpandingSpacer())
