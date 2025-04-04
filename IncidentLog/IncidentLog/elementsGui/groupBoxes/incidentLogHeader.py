from PyQt6.QtWidgets import QGroupBox, QGridLayout

from elementsGui.layouts.incidentLogLayouts.inputAlarmAreaRow import InputAlarmAreaRow
from elementsGui.layouts.incidentLogLayouts.inputAlarmCategoryRow import InputAlarmCategoryRow
from elementsGui.layouts.incidentLogLayouts.inputAlarmEventRow import InputAlarmEventRow


class IncidentLogHeaderBox(QGroupBox):

    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        self.__inputAlarmCategoryRow = InputAlarmCategoryRow()
        self.__inputAlarmAreaRow = InputAlarmAreaRow()
        self.__inputAlarmEventRow = InputAlarmEventRow()

        layout.addLayout(self.__inputAlarmCategoryRow, 0, 0, 1, 2)
        layout.addLayout(self.__inputAlarmAreaRow, 0, 2, 1, 2)
        layout.addLayout(self.__inputAlarmEventRow, 1, 0, 1, 4)

        self.setLayout(layout)