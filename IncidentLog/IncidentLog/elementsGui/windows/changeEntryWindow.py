from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.labels.outlineTitleLabel import OutlineTitleLabel
from elementsGui.layouts.addEntryLayouts.inputReportCategoryRow import InputCategoryRow
from elementsGui.layouts.addEntryLayouts.inputReportSenderRow import InputReportSenderRow
from elementsGui.layouts.addEntryLayouts.inputReportTextRow import InputReportTextRow
from elementsGui.layouts.addEntryLayouts.inputTimeRow import InputTimeRow
from elementsGui.layouts.changeEntryLayouts.changeEntryButtonRow import ChangeEntryButtonRow
from elementsGui.layouts.changeEntryLayouts.inputChangesRow import InputChangesRow
from utilityClasses.getTimeStamp import GetTimeStamp
from utilityClasses.layoutSpacer import LayoutSpacer
from utilityClasses.signalManager import signalManager



class ChangeEntryWindow(QWidget):

    def __init__(self, currentRowData: dict):
        super().__init__()
        self.setWindowTitle("Nachtrag einfügen")
        self.setWindowIcon(QIcon("icons/windowIcons/incidentLog.ico"))
        self.__rowId = currentRowData["sequenzNumber"]

        signalManager.on_change_entry_window_close.connect(self.close)
        signalManager.on_save_changes_click.connect(self.__saveChanges)

        layout = QGridLayout()

        titleLabel = OutlineTitleLabel("Nachtrag einfügen")
        buttonRow = ChangeEntryButtonRow()

        self.__inputTime = InputTimeRow(buttonIsVisible=False)
        self.__inputCategory = InputCategoryRow()
        self.__inputReportSender = InputReportSenderRow()
        self.__inputReportTextRow = InputReportTextRow()
        self.__inputChangesRow = InputChangesRow()

        layout.addWidget(titleLabel, 0, 0, 1, -1, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttonRow, 1, 0, 4, 1)

        layout.addLayout(self.__inputTime, 1, 2)
        layout.addLayout(self.__inputCategory, 2, 2)
        layout.addLayout(self.__inputReportSender, 3, 2)
        layout.addLayout(self.__inputReportTextRow, 1, 3, 3, 1)

        layout.addLayout(self.__inputChangesRow, 4, 2, 1, 2)

        layout.addItem(LayoutSpacer.horizontalFixedSpacer(20), 1, 2)
        layout.addItem(LayoutSpacer.verticalExpandingSpacer(), 10, 1, 1, -1)

        self.__setEntryValues(currentRowData)
        self.__disableWidgets()

        self.setLayout(layout)
        self.show()

    def __disableWidgets(self):
        self.__inputTime.setDisabled()
        self.__inputCategory.setDisabled()
        self.__inputReportTextRow.setDiabled()
        self.__inputReportSender.setDisabled()

    def __setEntryValues(self, entryValues: dict):
        self.__inputTime.setTimeValue(entryValues['time'])
        self.__inputCategory.setCategoryValue(entryValues['category'])
        self.__inputReportSender.setReportSender(entryValues['reportSender'])
        self.__inputReportTextRow.setReportText(entryValues['reportText'])

    def __saveChanges(self):
        changes = self.__inputChangesRow.getInputValue()
        if changes is not None:
            timeStamp = GetTimeStamp.getTimeStamp()
            signalManager.on_get_change.emit(changes, timeStamp)
            changedEntry = self.__getValues()
            signalManager.on_insert_changes.emit(changedEntry)
            self.close()

    def __getValues(self):
        changedEntry = {
            "sequenzNumber": self.__rowId,
            "time": self.__inputTime.getValue(),
            "category": self.__inputCategory.getValue(),
            "reportSender": self.__inputReportSender.getValue(),
            "reportText": self.__inputReportTextRow.getValue()
        }
        return changedEntry
