from PyQt6.QtWidgets import QTableWidget

from elementsGui.tableWidget.customTableWidgetItem import CustomTableWidgetItem


class IncidentLogTableRow:

    def __init__(self, rowId: int, newEntryDict: dict):
        self.__rowIdItem = CustomTableWidgetItem(str(rowId), "sequenzNumber")
        self.__rowItems = [self.__rowIdItem]
        self.__createRowItems(newEntryDict)

    def __createRowItems(self, newEntryDict: dict):
        for key in newEntryDict.keys():
            align = "center"
            if key == "reportText":
                align = "left"
            self.__rowItems.append(CustomTableWidgetItem(newEntryDict[key], key, align))

    def getRowItems(self, tableWidget: QTableWidget):
        row = tableWidget.rowCount() - 1
        for i, item in enumerate(self.__rowItems):
            tableWidget.setItem(row, i, item)
