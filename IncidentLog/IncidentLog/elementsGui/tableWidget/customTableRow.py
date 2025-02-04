from PyQt6.QtWidgets import QTableWidget

from elementsGui.tableWidget.customTableWidgetItem import CustomTableWidgetItem


class CustomTableRow:

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
        for i in range(len(self.__rowItems)):
            tableWidget.setItem(row, i, self.__rowItems[i])

