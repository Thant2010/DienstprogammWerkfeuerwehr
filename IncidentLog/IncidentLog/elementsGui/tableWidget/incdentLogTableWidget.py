from PyQt6.QtWidgets import QHeaderView, QMessageBox

from elementsGui.tableWidget.IncidentLogTableRow import IncidentLogTableRow
from elementsGui.tableWidget.customTableWidget import CustomTableWidget
from elementsGui.tableWidget.customTableWidgetItem import CustomTableWidgetItem
from globals import logTableHeader
from utilityClasses.signalManager import signalManager
from utilityClasses.customMessageBox import CustomMessageBox


class IncidentLogTableWidget(CustomTableWidget):
    MAX_HEIGHT = 500

    def __init__(self):
        super().__init__(headerList=logTableHeader)
        signalManager.on_log_data_is_valid.connect(self.__addNewEntryRow)
        signalManager.on_change_entry_click.connect(self.__getRowValue)
        signalManager.on_insert_changes.connect(self.__insertChanges)
        signalManager.on_strike_out_row_click.connect(self.__checkRowStrike)

        self.itemDoubleClicked.connect(self.__getRowValue)

        self.__setColumnWidth()
        self.__updateHeight()

    def __setColumnWidth(self):
        self.setColumnWidth(0, 50)
        self.setColumnWidth(1, 80)
        self.setColumnWidth(2, 100)
        self.setColumnWidth(3, 100)

        self.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

    def __addNewEntryRow(self, newEntryDict: dict):
        self.insertRow(self.rowCount())
        newEntryRow = IncidentLogTableRow(self.rowCount(), newEntryDict)
        newEntryRow.getRowItems(self)
        self.resizeRowsToContents()
        self.__updateHeight()

    def __updateHeight(self):
        totalRowHeight = sum(self.rowHeight(row) for row in range(self.rowCount()))
        totalHeight = self.horizontalHeader().height() + totalRowHeight + 2
        newHeight = min(totalHeight, self.MAX_HEIGHT)
        self.setMinimumHeight(newHeight)

    def __getRowValue(self):
        if self.currentRow() >= 0:
            item: CustomTableWidgetItem
            rowdata = dict()
            selectedRow = self.currentRow()
            items = [self.item(selectedRow, column) for column in range(self.columnCount())]
            for item in items:
                key, value = item.getItemValue()
                rowdata[key] = value

            signalManager.on_get_row_data.emit(rowdata)

    def __rowStrikeOut(self):

        if self.currentRow() >= 0:
            selectedRow = self.currentRow()
            for column in range(self.columnCount()):
                item: CustomTableWidgetItem = self.item(selectedRow, column)
                if item:
                    font = item.font()
                    font.setStrikeOut(True)
                    item.setFont(font)

    def __checkRowStrike(self):
        result = CustomMessageBox().showYesNoMessage("Durchstreichen",
                                                   "Wollen sie die Aktuelle Reihe durchstreichen?")
        if result == QMessageBox.StandardButton.Yes:
            self.__rowStrikeOut()
        else:
            return

    def __checkStrikeOut(self, item: CustomTableWidgetItem):

        return "Durchgestrichen" if item.font().strikeOut() else "Nein"

    def __insertChanges(self, changedValue):
        rowId = int(changedValue['sequenzNumber']) - 1

        item: CustomTableWidgetItem = self.item(rowId, 4)
        item.setValue(changedValue['reportText'])
        self.resizeRowsToContents()