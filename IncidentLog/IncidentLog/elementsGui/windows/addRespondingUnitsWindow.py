from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.labels.outlineTitleLabel import OutlineTitleLabel
from elementsGui.layouts.addEntryLayouts.addEntryButtonRow import AddEntryButtonRow
from elementsGui.layouts.addEntryLayouts.inputTimeRow import InputTimeRow
from elementsGui.layouts.adddRespondingUnits.inputUnitsComboboxRow import InputRespondingUnitsRow
from utilityClasses.customMessageBox import CustomMessageBox

from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager


class AddRespondingUnitWindow(QWidget):

    def __init__(self):
        super().__init__()
        signalManager.on_new_entry_window_close.connect(self.close)
        signalManager.on_save_entry_click.connect(self.__getEntryValues)

        self.setWindowTitle("Einheiten hinzufügen")
        self.setWindowIcon(QIcon("icons/windowIcons/incidentLog.ico"))

        titleLabel = OutlineTitleLabel("Alamierte Einheiten:")
        layout = QGridLayout()
        buttons = AddEntryButtonRow()
        self.__inputUnitsRow = InputRespondingUnitsRow()
        self.__inputAlarmTime = InputTimeRow("Alarmierung", clearTimeWidget=True)
        self.__inputArrivalSceneTime = InputTimeRow("EST an", clearTimeWidget=True)
        self.__inputDepartureSceneTime = InputTimeRow("EST ab", clearTimeWidget=True)

        layout.addWidget(titleLabel, 0, 0, 1, -1, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttons, 1, 2, 4, 1)
        layout.addLayout(self.__inputUnitsRow, 1, 0, 1, 2)
        layout.addLayout(self.__inputAlarmTime, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(self.__inputArrivalSceneTime, 3, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(self.__inputDepartureSceneTime, 4, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addItem(LayoutSpacer.horizontalFixedSpacer(20), 1, 2)
        layout.addItem(LayoutSpacer.verticalExpandingSpacer(), 10, 1, 1, -1)

        self.setLayout(layout)

        self.show()

    def __getEntryValues(self):
        internalUnits, externalUnits = self.__inputUnitsRow.getValue()
        alarmTime = self.__inputAlarmTime.getValue()
        arivalSceneTime = self.__inputArrivalSceneTime.getValue()
        departureSceneTime = self.__inputDepartureSceneTime.getValue()

        values = {
            "internalUnits": internalUnits,
            "externalUnits": externalUnits,
            "alarmTime": alarmTime,
            "arivalSceneTime": arivalSceneTime,
            "departureSceneTime": departureSceneTime,
        }
        if internalUnits is None or externalUnits is None:
            return
        elif alarmTime is None:
            CustomMessageBox().showInfoMessage("Achtung", "Bitte Alarmierungszeit wählen!")
        else:
            signalManager.on_unit_data_is_valid.emit(values)