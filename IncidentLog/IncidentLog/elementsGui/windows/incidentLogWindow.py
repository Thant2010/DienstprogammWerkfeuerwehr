from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.groupBoxes.incidentLogHeader import IncidentLogHeaderBox
from elementsGui.labels.outlineTitleLabel import OutlineTitleLabel
from elementsGui.layouts.incidentLogLayouts.incidentLogButtonRow import IncidentLogButtonRow
from elementsGui.tableWidget.incdentLogTableWidget import IncidentLogTableWidget
from elementsGui.windows.addEntryWindow import AddEntryWindow
from elementsGui.windows.changeEntryWindow import ChangeEntryWindow
from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager


class IncidentLogWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Einsatztagebuch")
        self.setWindowIcon(QIcon("icons/windowIcons/incidentLog.ico"))
        self.setMinimumSize(1200, 750)

        signalManager.on_get_row_data.connect(self.__openChangeEntryWindow)
        signalManager.on_add_new_entry_click.connect(self.__openAddEntryWindow)
        signalManager.on_incident_log_window_close.connect(self.close)

        layout = QGridLayout()

        titleLabel = OutlineTitleLabel("Einsatztagebuch")
        buttonLayout = IncidentLogButtonRow()
        headerGroupBox = IncidentLogHeaderBox()
        self.__incidentLogTable = IncidentLogTableWidget()

        layout.addWidget(titleLabel, 0, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(headerGroupBox, 1, 1, 1, 1)
        layout.addLayout(buttonLayout, 2, 1, 1, 1)
        layout.addWidget(self.__incidentLogTable, 3, 1, 1, 1)

        layout.addItem(LayoutSpacer.verticalExpandingSpacer(), 10, 0, 1, -1)

        self.setLayout(layout)

        self.show()

    def __openAddEntryWindow(self):

        self.__addEntryWindow = AddEntryWindow()

    def __openChangeEntryWindow(self, currentRowData: dict):

        self.changeEntryWindow = ChangeEntryWindow(currentRowData)
