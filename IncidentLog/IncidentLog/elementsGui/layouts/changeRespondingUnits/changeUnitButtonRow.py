from PyQt6.QtWidgets import QVBoxLayout

from elementsGui.buttons.iconButton import IconButton
from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager


class ChangeUnitButtonRow(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.__saveButton = IconButton("save", 40)
        self.__saveButton.clicked.connect(signalManager.on_save_unit_changes_click)
        self.__clearButton = IconButton("clear", 40)
        self.__closeButton = IconButton("close", 40)

        self.addWidget(self.__saveButton)
        self.addWidget(self.__clearButton)
        self.addWidget(self.__closeButton)
        self.addItem(LayoutSpacer.verticalExpandingSpacer())
