from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.labels.outlineTitleLabel import OutlineTitleLabel
from elementsGui.layouts.addEntryLayouts.inputTimeRow import InputTimeRow
from elementsGui.layouts.changeRespondingUnits.changeUnitButtonRow import ChangeUnitButtonRow
from elementsGui.layouts.changeRespondingUnits.unitCountRow import UnitCountsRow
from elementsGui.layouts.changeRespondingUnits.unitNameRow import UnitNameRow
from utilityClasses.signalManager import signalManager


class ChangeRespondingUnitsWindow(QWidget):

    def __init__(self, unitDict: dict, selectedRow: int):
        super().__init__()
        self.__unitRowIndex = selectedRow
        signalManager.on_save_unit_changes_click.connect(self.__saveChanges)
        self.setWindowTitle("Einheit bearbeiten")
        self.setWindowIcon(QIcon("icons/windowIcons/incidentLog.ico"))

        titleLabel = OutlineTitleLabel("Eintrag bearbeiten")
        layout = QGridLayout()
        buttons = ChangeUnitButtonRow()
        self.__unitNameRow = UnitNameRow()
        self.__inputAlarmTime = InputTimeRow("Alarmierung", clearTimeWidget=True)
        self.__inputArrivalSceneTime = InputTimeRow("EST an", clearTimeWidget=True)
        self.__inputDepartureSceneTime = InputTimeRow("EST ab", clearTimeWidget=True)
        self.__inputUnitsCount = UnitCountsRow()

        layout.addWidget(titleLabel, 0, 0, 1, -1, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttons, 1, 2, 5, 1)
        layout.addLayout(self.__unitNameRow, 1, 0, 1, 1)
        layout.addLayout(self.__inputAlarmTime, 2, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(self.__inputArrivalSceneTime, 3, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(self.__inputDepartureSceneTime, 4, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(self.__inputUnitsCount, 5, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

        self.__setUnitValues(unitDict)

        self.show()

    def __setUnitValues(self, unitDict: dict):
        self.__unitNameRow.setUnitName(unitDict["unit"])
        self.__inputAlarmTime.setTimeValue(unitDict["alarmTime"])
        self.__inputArrivalSceneTime.setTimeValue(unitDict["arivalSceneTime"])
        self.__inputDepartureSceneTime.setTimeValue(unitDict["departureSceneTime"])

        count = self.__tryToParseInt(unitDict["unitCount"])
        self.__inputUnitsCount.setUnitsCount(count)

    def __tryToParseInt(self, count: str):
        try:
            intCount = int(count)
        except ValueError:
            intCount = 0

        return intCount

    def __saveChanges(self) -> (int, dict):
        unitDict = {
            "unit": self.__unitNameRow.getUnitName(),
            "alarmTime": self.__inputAlarmTime.getValue(),
            "arivalSceneTime": self.__inputArrivalSceneTime.getValue(),
            "departureSceneTime": self.__inputDepartureSceneTime.getValue(),
            "unitCount": self.__inputUnitsCount.getUnitsCount()
        }

        signalManager.on_insert_unit_changes.emit(self.__unitRowIndex, unitDict)
