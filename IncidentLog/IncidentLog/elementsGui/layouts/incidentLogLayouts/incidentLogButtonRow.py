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
        self.__removeEntryButton.clicked.connect(signalManager.on_strike_out_row_click.emit)
        self.__respondingUnitsButton = IconButton("alarmBell", 60)
        self.__respondingUnitsButton.clicked.connect(signalManager.on_add_unit_click.emit)
        self.__closeButton = IconButton("close", 60)
        self.__closeButton.clicked.connect(signalManager.on_incident_log_window_close.emit)

        #self.addItem(LayoutSpacer.horizontalExpandingSpacer())
        self.addWidget(self.__addEntryButton)
        self.addWidget(self.__editEntryButton)
        self.addWidget(self.__removeEntryButton)
        self.addWidget(self.__respondingUnitsButton)
        self.addWidget(self.__closeButton)
       # self.addItem(LayoutSpacer.horizontalExpandingSpacer())
