from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.groupBoxes.incidentLogButtonGroupBox import IncidentLogButtonGroupBox
from elementsGui.groupBoxes.incidentLogHeader import IncidentLogHeaderBox
from elementsGui.groupBoxes.incidentLogTableGroupBox import IncidentLogTableGroupBox
from elementsGui.groupBoxes.respondingUnitsTableGroupBox import RespondingUnitsGroupBox
from elementsGui.labels.outlineTitleLabel import OutlineTitleLabel
from elementsGui.windows.addEntryWindow import AddEntryWindow
from elementsGui.windows.addRespondingUnitsWindow import AddRespondingUnitWindow
from elementsGui.windows.changeEntryWindow import ChangeEntryWindow
from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager


class IncidentLogWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Einsatztagebuch")
        self.setWindowIcon(QIcon("icons/windowIcons/incidentLog.ico"))
        self.setMinimumSize(1250, 750)

        signalManager.on_get_row_data.connect(self.__openChangeEntryWindow)
        signalManager.on_add_new_entry_click.connect(self.__openAddEntryWindow)
        signalManager.on_add_unit_click.connect(self.__openAddUnitsWindow)
        signalManager.on_incident_log_window_close.connect(self.close)

        layout = QGridLayout()

        titleLabel = OutlineTitleLabel("Einsatztagebuch")
        buttonGroupBox = IncidentLogButtonGroupBox()
        headerGroupBox = IncidentLogHeaderBox()
        incidentLogTableGroup = IncidentLogTableGroupBox()
        respondingUnitsTableGroup = RespondingUnitsGroupBox()

        layout.addWidget(titleLabel, 0, 0, 1, 6, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(headerGroupBox, 1, 0, 1, 3)
        layout.addWidget(buttonGroupBox, 2, 0, 1, 1)
        layout.addWidget(incidentLogTableGroup, 3, 0, 1, 4)
        layout.addWidget(respondingUnitsTableGroup, 3, 4, 1, 1)

        layout.addItem(LayoutSpacer.verticalExpandingSpacer(), 10, 0, 1, -1)

        self.setLayout(layout)

        self.show()

    def __openAddEntryWindow(self):

        self.__addEntryWindow = AddEntryWindow()

    def __openAddUnitsWindow(self):

        self.__addUnitsWindow = AddRespondingUnitWindow()

    def __openChangeEntryWindow(self, currentRowData: dict):

        self.changeEntryWindow = ChangeEntryWindow(currentRowData)
