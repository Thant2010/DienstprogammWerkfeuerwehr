from PyQt6.QtWidgets import QHeaderView

from elementsGui.tableWidget.customTableWidget import CustomTableWidget
from elementsGui.tableWidget.customTableWidgetItem import CustomTableWidgetItem
from elementsGui.tableWidget.respondingUnitRow import RespondingUnitRow
from globals import unitsTableHeader
from utilityClasses.signalManager import signalManager


class RespondingUnitsTableWidget(CustomTableWidget):


    def __init__(self):
        super().__init__(headerList=unitsTableHeader)

        signalManager.on_unit_data_is_valid.connect(self.__addNewEntrys)
        signalManager.on_insert_unit_changes.connect(self.__updateUnitRowData)

        self.__setColumnWidth()

    def __setColumnWidth(self):
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.setColumnWidth(1, 80)
        self.setColumnWidth(2, 80)
        self.setColumnWidth(3, 80)
        self.setColumnWidth(4, 80)

    def __addNewEntrys(self, unitValues: dict):

        for value in unitValues["internalUnits"]:
            unitValue = {
                "unit": value,
                "alarmTime": unitValues["alarmTime"],
                "arivalSceneTime": unitValues["arivalSceneTime"] or "",
                "departureSceneTime": unitValues["departureSceneTime"] or "",
                "unitCount": "-"
            }
            self.__addNewRow(unitValue)

        for value in unitValues["externalUnits"]:
            unitValue = {
                "unit": value,
                "alarmTime": unitValues["alarmTime"],
                "arivalSceneTime": unitValues["arivalSceneTime"] or "",
                "departureSceneTime": unitValues["departureSceneTime"] or "",
                "unitCount": "-"
            }
            self.__addNewRow(unitValue)

    def __addNewRow(self, unitValue: dict):
        self.insertRow(self.rowCount())
        newEntryRow = RespondingUnitRow(unitValue)
        newEntryRow.getRowItems(self)
        self.resizeRowsToContents()
        self.__updateHeight()

    def __updateHeight(self):
        totalRowHeight = sum(self.rowHeight(row) for row in range(self.rowCount()))
        totalHeight = self.horizontalHeader().height() + totalRowHeight + 2
        newHeight = min(totalHeight, self.MAX_HEIGHT)
        self.setMinimumHeight(newHeight)

    def sendRowData(self, rowData: dict, selectedRow: int):
        signalManager.on_get_unit_data.emit(rowData, selectedRow)

    def __updateUnitRowData(self, columnIndex: int, unitData: dict):
        item: CustomTableWidgetItem
        items = [self.item(columnIndex, column) for column in range(self.columnCount())]
        for key in unitData.keys():
            for item in items:
                if item.checkKey(key):
                    item.setValue(unitData[key])
                    break
