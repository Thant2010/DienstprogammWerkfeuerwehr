from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.buttons.iconButton import IconButton
from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager


class IncidentLogButtonRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.__addEntryButton = IconButton("add", 60)
        self.__addEntryButton.clicked.connect(signalManager.on_add_new_entry_click.emit)
        self.__editEntryButton = IconButton("edit", 60)
        self.__editEntryButton.clicked.connect(signalManager.on_change_entry_click.emit)
        self.__removeEntryButton = IconButton("remove", 60)
        self.__closeButton = IconButton("close", 60)
        self.__closeButton.clicked.connect(signalManager.on_incident_log_window_close.emit)

        self.addWidget(self.__addEntryButton)
        self.addWidget(self.__editEntryButton)
        self.addWidget(self.__removeEntryButton)
        self.addWidget(self.__closeButton)
        self.addItem(LayoutSpacer.horizontalExpandingSpacer())
