from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.labels.outlineTitleLabel import OutlineTitleLabel
from elementsGui.layouts.addEntryLayouts.addEntryButtonRow import AddEntryButtonRow
from elementsGui.layouts.addEntryLayouts.inputReportCategoryRow import InputCategoryRow
from elementsGui.layouts.addEntryLayouts.inputReportSenderRow import InputReportSenderRow
from elementsGui.layouts.addEntryLayouts.inputReportTextRow import InputReportTextRow
from elementsGui.layouts.addEntryLayouts.inputTimeRow import InputTimeRow
from utilityClasses.signalManager import signalManager
from utilityClasses.layoutSpacer import LayoutSpacer


class AddEntryWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neuer Eintrag")
        self.setWindowIcon(QIcon("icons/windowIcons/incidentLog.ico"))
        self.setFixedSize(950, 220)

        signalManager.on_save_entry_click.connect(self.__checkValues)
        signalManager.on_entry_window_close.connect(self.close)

        titleLabel = OutlineTitleLabel("Neuer Eintrag:")
        layout = QGridLayout()
        buttonLayoutRow = AddEntryButtonRow()

        self.__inputTimeRow = InputTimeRow()
        self.__inputCategoryRow = InputCategoryRow()
        self.__inputReportSender = InputReportSenderRow()
        self.__inputReportTextRow = InputReportTextRow()

        layout.addWidget(titleLabel, 0, 1, 1, -1, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttonLayoutRow, 1, 1, 3, 1)

        layout.addLayout(self.__inputTimeRow, 1, 3)
        layout.addLayout(self.__inputCategoryRow, 2, 3)
        layout.addLayout(self.__inputReportSender, 3, 3)
        layout.addLayout(self.__inputReportTextRow, 1, 4, 3, 1)

        layout.addItem(LayoutSpacer.horizontalFixedSpacer(20), 1, 2)
        layout.addItem(LayoutSpacer.verticalExpandingSpacer(), 10, 1, 1, -1)

        self.setLayout(layout)
        self.show()

    def __checkValues(self):
        time = self.__inputTimeRow.getValue()
        category = self.__inputCategoryRow.getValue()
        reportSender = self.__inputReportSender.getValue()
        reportText = self.__inputReportTextRow.getValue()
        newEntry = {
            "time": time,
            "category": category,
            "reportSender": reportSender,
            "reportText": reportText
        }

        for value in newEntry.values():
            if value is None:
                return

        signalManager.on_data_is_valid.emit(newEntry)
        signalManager.on_set_default_values.emit()



